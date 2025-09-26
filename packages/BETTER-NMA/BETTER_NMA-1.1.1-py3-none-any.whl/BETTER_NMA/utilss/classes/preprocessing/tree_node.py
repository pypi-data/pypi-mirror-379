from nltk.tree import Tree

class TreeNode(Tree):
    def __init__(self, node_id, label=None, children=None, weight=0, parent=None):
        self.node_name = label if label else f"cluster {node_id}"
        super().__init__(self.node_name, children if children else [])
        self.node_id = node_id
        self.weight = weight
        self.parent = parent
        if children:
            for child in children:
                if isinstance(child, TreeNode):
                    child.parent = self

    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return self.node_id == other.node_id

    def add_child(self, child):
        if isinstance(child, TreeNode):
            child.parent = self
        self.append(child)
        return self

    @classmethod
    def create_parent(cls, node_id, children, label=None, weight=0):
        parent = cls(node_id, label, weight=weight)
        for child in children:
            parent.add_child(child)
        return parent

    def get_root(self):
        current = self
        while current.parent is not None:
            current = current.parent
        return current

    def get_path_to_root(self):
        path = []
        current = self
        while current is not None:
            path.append(current)
            current = current.parent
        return path

    def find_lca(self, other_node):
        if not isinstance(other_node, TreeNode):
            raise TypeError("Expected TreeNode node")
        path1 = []
        current = self
        while current is not None:
            path1.append(current)
            current = current.parent
        path2 = []
        current = other_node
        while current is not None:
            path2.append(current)
            current = current.parent
        path1.reverse()
        path2.reverse()
        lca = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] is path2[i]:
                lca = path1[i]
            else:
                break
        return lca
