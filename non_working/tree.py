import sys

# Requirements:
# Each node uses the gameboard as the key
# Each node holds the upper and lower bounds for the MTDf alg.
# Each node holds whether or not its a min or max node
# Can find the next sibling of a given node
# Can find the first child of a given node
# Tree can have 7 nodes
# Tree can add children on a node


# Parent is at index 1
# The nth child is always at (index of parent) * (n_nodes) + n

class Tree:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.tree_lst = []
        self.tree_dict = {}

    def get_node(self, key):
        return self.tree_dict(key, None)

    def get_nth_child_index(self, parent_i, n):
        return n_nodes * parent_i + n

    def get_nth_child(self, parent, n):
        i = get_nth_child_index(self, parent.index(), n)
        return self.tree_dict(self.tree_lst[i], None)

    def update_node(self, node):
        if self.tree_dict.get(node.board, None):
            self.tree_dict[node.board] = node

    def add_child(self, parent, child):
        parent_node = self.tree_dict.get(parent, None)
        if not parent_node:
            first_child_i = get_nth_child_index(parent_node.index(), 1)
            # Check to see if this is the first child
            if first_child_i > len(self.tree_lst):
                # Prep the list for possible children of this node
                # Add empty entries for parent's children and children's children I dont think i need to do this
                self.tree_lst.extend([None for c in range(self.n_nodes) for pc in range(self.n_nodes + 1)])

            # Able to update child
            # Need to find next available child to update
            for i in range(first_child_i, first_child_i  + self.n_nodes):
                if not self.tree_list[i]:
                    # Update the child and add its node to the dict
                    self.tree_list[i] = child
                    self.tree_dict[child.board] = child

    def next_sibling(self, child):
        child_node = self.tree_dict.get(child, None)
        if child_node:
            # Check if last child
            if not child_node.n < 7:
                # Look up the index in the list and get the node from the dict
                return self.tree_dict.get(self.tree_lst[child_node.index() + 1], None)
        return None

    def has_children(self, key):
        node = self.get_node(key)
        result = True
        try:
            for n in range(1, self.n_nodes + 1):
                result = result and self.tree_lst[node.index() + n]
        except:
            result = False

        return result


class Node:
    def __init__(self, parent_i, n, board, is_max_node):
        self.parent_i = parent_i
        self.n = n
        self.board = board
        self.is_max_node = is_max_node
        self.upper = sys.maxsize
        self.lower = -sys.maxsize

    def index(self):
        return self.parent_i + self.n
