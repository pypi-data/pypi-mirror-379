from __future__ import annotations

import pickle
from collections.abc import Iterable
from typing import TYPE_CHECKING

from ..tree_approximation import TreeApproximationTemplate

if TYPE_CHECKING:
    from ..lineage_tree import LineageTree


def create_links_and_chains(
    lT: LineageTree,
    roots: int | Iterable | None = None,
    end_time: int | None = None,
) -> dict[str, dict]:
    """Generates a dictionary containing all the edges (from start of lifetime to end not the intermediate timepoints)
      of a subtree spawned by node/s and their duration


    Parameters
    ----------
    lT : LineageTree
        The LineageTree that the user is working on
    roots : int or Iterable, optional
        The root/s from which the tree/s will be generated, if 'None' all the roots will be selected.
    end_time : int, optional
        The last timepoint to be considered, if 'None' the last timepoint of the dataset (t_e) is considered, by default None.

    Returns
    -------
    dict mapping str to set or dict mapping int to list or int
        A dictionary that contains:
            - "links": The dictionary that contains the hierarchy of the nodes (only start and end of each chain)
            - "times": The time distance between the start and the end of a chain
            - "roots": The roots used
    """
    if roots is None:
        to_do = set(lT.roots)
    elif isinstance(roots, Iterable):
        to_do = set(roots)
    else:
        to_do = {int(roots)}
    if end_time is None:
        end_time = lT.t_e
    times = {}
    links = {}
    while to_do:
        curr = to_do.pop()
        cyc = lT.get_successors(curr, end_time=end_time)
        if cyc[-1] != curr or lT.time[cyc[-1]] <= end_time:
            last = cyc[-1]
            times[curr] = len(cyc)
            if last != curr:
                links[curr] = [last]
            else:
                links[curr] = []
            succ = lT._successor.get(last)
            if succ:
                times[cyc[-1]] = 0
                to_do.update(succ)
            links[last] = succ
    return {"links": links, "times": times, "root": roots}


def _find_leaves_and_depths_iterative(lnks_tms: dict, root: int) -> tuple[list[int], dict[int, int]]:
    """Find all leaves and calculate depths for all nodes using iterative approach.
    
    Parameters
    ----------
    lnks_tms : dict
        A dictionary created by create_links_and_chains.
    root : int
        The id of the root node.

    Returns
    -------
    leaves : list of int
        List of leaf node ids.
    depths : dict mapping int to int
        Dictionary mapping all node ids to their depth in the tree.
    """
    leaves = []
    depths = {}

    times = lnks_tms["times"]
    links = lnks_tms["links"]
    
    # Stack for DFS: (node, parent_depth)
    stack = [(root, 0)]
    
    while stack:
        parent_node, parent_depth = stack.pop()
        depths[parent_node] = parent_depth
        succ = links.get(parent_node, [])
         
        if not succ:  # This is a leaf
            leaves.append(parent_node)
        else:
            if len(succ) == 1: # in this case, times[parent_node] is equal to the length of the chain
                child_depth = parent_depth + times[parent_node] - 1
            else: # in this case, times[parent_node] is 0
                child_depth = parent_depth + 1
            # Add children to stack (reverse order to maintain left-to-right traversal)
            for child in reversed(succ):
                stack.append((child, child_depth))
    
    return leaves, depths


def _calculate_leaf_positions(leaves: list[int], width: int, xcenter: int) -> dict[int, float]:
    """Calculate uniform x-positions for leaves."""
    num_leaves = len(leaves)
    if num_leaves == 1:
        return {leaves[0]: xcenter}
    
    leaf_spacing = width / (num_leaves - 1)
    return {
        leaf: xcenter - width/2 + i * leaf_spacing 
        for i, leaf in enumerate(leaves)
    }


def _assign_positions_iterative(
    lnks_tms: dict, 
    root: int, 
    depths: dict[int, int], 
    leaf_x_positions: dict[int, float],
    vert_gap: int,
    ycenter: int
) -> dict[int, list[float]]:
    """Assign positions to nodes using iterative post-order traversal."""
    pos_node = {}
    
    # First pass: build parent-child relationships and find processing order
    children_map = lnks_tms["links"] 

    # Reverse-order traversal using two stacks
    stack1 = [root]
    stack2 = []
    
    # This while loop stores nodes in stack2 so that children are processed before parents
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        stack1.extend(children_map.get(node, []))
    
    # Process nodes in reverse-order (children before parents)
    while stack2:
        node = stack2.pop()
        succ = children_map.get(node, [])
        
        if not succ: # This is a leaf
            pos_node[node] = [
                leaf_x_positions[node], 
                ycenter - depths[node] * vert_gap
            ]
        elif len(succ) == 1:
            # Single child: place directly above
            pos_node[node] = [
                pos_node[succ[0]][0],
                ycenter - depths[node] * vert_gap
            ]
        else:
            # Multiple children: place at center of children
            child_x_positions = [pos_node[child][0] for child in succ]
            center_x = sum(child_x_positions) / len(child_x_positions)
            pos_node[node] = [
                center_x,
                ycenter - depths[node] * vert_gap
            ]
    
    return pos_node


def hierarchical_pos(
    lnks_tms: dict, root, width=1000, vert_gap=2, xcenter=0, ycenter=0
) -> dict[int, list[float]] | None:
    """Calculates the position of each node on the tree graph with uniform leaf spacing.

    Parameters
    ----------
    lnks_tms : dict
         a dictionary created by create_links_and_chains.
    root : _type_
        The id of the node, usually it exists inside lnks_tms dictionary, however you may use your own root.
    width : int, optional
        Max width, will not change the graph but interacting with the graph takes this distance into account, by default 1000
    vert_gap : int, optional
        How far downwards each timepoint will go, by default 2
    xcenter : int, optional
        Where the root will be placed on the x axis, by default 0
    ycenter : int, optional
        Where the root will be placed on the y axis, by default 0

    Returns
    -------
    dict mapping int to list of float
        Provides a dictionary that contains the id of each node as keys and its 2-d position on the
        tree graph as values. Leaves are uniformly spaced on the x-axis.
        If the root requested does not exists, None is then returned
    """
    if root not in lnks_tms["times"]:
        return None
    
    # Find all leaves and calculate depths
    leaves, depths = _find_leaves_and_depths_iterative(lnks_tms, root)
    
    # Calculate uniform x-positions for leaves
    leaf_x_positions = _calculate_leaf_positions(leaves, width, xcenter)
    
    # Assign positions using iterative approach
    pos_node = _assign_positions_iterative(
        lnks_tms, root, depths, leaf_x_positions, vert_gap, ycenter
    )
    
    return pos_node


def convert_style_to_number(
    style: str | TreeApproximationTemplate,
    downsample: int | None,
) -> int:
    """Converts tree_style and downsampling to a single number.

    Parameters
    ----------
    style : str
        the tree style
    downsample : int
        the downsampling factor

    Returns
    -------
    int
        A number which serves as ID if the tree style and downsampling used.
    """
    style_dict = {
        "full": 0,
        "simple": -1,
        "normalized_simple": -2,
        "mini": -1000,
    }
    if style == "downsampled" and downsample is not None:
        return downsample
    elif not isinstance(style, str) and issubclass(
        style, TreeApproximationTemplate
    ):
        return hash(style.__name__)
    else:
        return style_dict[style]


class CompatibleUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "LineageTree.lineageTree" and name == "lineageTree":
            from lineagetree import LineageTree

            return LineageTree
        return super().find_class(module, name)
