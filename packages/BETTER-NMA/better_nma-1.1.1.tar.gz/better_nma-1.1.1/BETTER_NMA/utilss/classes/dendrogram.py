from scipy.cluster.hierarchy import to_tree
from ..wordnet_utils import process_hierarchy
import json
import numpy as np
import os
import pickle

class Dendrogram:
    def __init__(self, Z=None):
        self.Z = Z
        self.Z_tree_format = None
        self.dendrogram_filename = None

    def _build_tree_format(self, node, labels):
        if node.is_leaf():
            return {
                "id": node.id,
                "name": labels[node.id],
                }
        else:
            return {
                "id": node.id,
                "name": f"cluster_{node.id}",
                "children": [self._build_tree_format(node.get_left(), labels), self._build_tree_format(node.get_right(), labels)],
                "value": node.dist
            }

    def build_tree_hierarchy(self, linkage_matrix, labels):
        tree, nodes = to_tree(linkage_matrix, rd=True)
        self.Z_tree_format = self._build_tree_format(tree, labels)
        self.Z_tree_format = process_hierarchy(self.Z_tree_format)
        return self.Z_tree_format  
    
    def filter_dendrogram_by_labels(self, full_data, target_labels):
        def contains_target_label(node):
            if 'children' not in node:
                return node.get('name') in target_labels
            for child in node.get('children', []):
                if contains_target_label(child):
                    return True
            return False
        def filter_tree(node):
            if not contains_target_label(node):
                return None
            new_node = {
                'id': node.get('id'),
                'name': node.get('name')
            }
            if 'value' in node:
                new_node['value'] = node.get('value')
            if 'children' not in node:
                return new_node
            filtered_children = []
            for child in node.get('children', []):
                filtered_child = filter_tree(child)
                if filtered_child:
                    filtered_children.append(filtered_child)
            if filtered_children:
                new_node['children'] = filtered_children
            return new_node
        return filter_tree(full_data)

    def merge_clusters(self, node):
        if node is None:
            return None
        if "children" not in node:
            return node
        merged_children = []
        for child in node["children"]:
            merged_child = self.merge_clusters(child)
            if merged_child:
                merged_children.append(merged_child)
        if all(c.get("value", 0) == 100 for c in merged_children):
            node["children"] = [grandchild for child in merged_children for grandchild in child.get("children", [])]
        else:
            node["children"] = merged_children
        if len(node["children"]) == 1:
            return node["children"][0]
        return node
    
    def get_sub_dendrogram_formatted(self, selected_labels):
        filtered_tree = self.filter_dendrogram_by_labels(self.Z_tree_format, selected_labels)
        if filtered_tree is None:
            raise ValueError(f"No clusters found for the selected labels: {selected_labels}")
        filtered_tree = self.merge_clusters(filtered_tree)
        filtered_tree_json = json.dumps(filtered_tree, indent=2)
        return filtered_tree_json
    
    def find_name_hierarchy(self, node, target_name):
        if node.get('name') == target_name:
            return [target_name]
        if 'children' in node:
            for child in node['children']:
                result = self.find_name_hierarchy(child, target_name)
                if result is not None:
                    if node.get('name'):
                        result.append(node['name'])
                    return result
        return None
    
    def rename_cluster(self, cluster_id, new_name):
        print(f"Renaming cluster {cluster_id} to {new_name}")
        def collect_names(node, names):
            names.add(node.get('name'))
            for child in node.get('children', []):
                collect_names(child, names)
        existing_names = set()
        collect_names(self.Z_tree_format, existing_names)
        unique_name = new_name
        suffix = 1
        while unique_name in existing_names:
            unique_name = f"{new_name}_{suffix}"
            suffix += 1
            
        def rename_node(node):
            if node.get('id') == cluster_id:
                node['name'] = unique_name
            for child in node.get('children', []):
                rename_node(child)
        rename_node(self.Z_tree_format)
        return self.Z_tree_format
    
    def get_common_ancestor_subtree(self, selected_labels):
        if not selected_labels:
            raise ValueError("selected_labels must be non-empty")
        
        if self.Z_tree_format is None:
            raise ValueError("No tree format available. Build hierarchy first.")
        
        def contains_all_labels(node, target_labels):
            found_labels = set()
            
            def collect_labels(n):
                if 'children' not in n:
                    found_labels.add(n.get('name'))
                else:
                    for child in n.get('children', []):
                        collect_labels(child)
            
            collect_labels(node)
            return all(label in found_labels for label in target_labels)
        
        def find_smallest_ancestor(node):
            if contains_all_labels(node, selected_labels):
                if 'children' not in node:
                    return node
                
                for child in node.get('children', []):
                    child_result = find_smallest_ancestor(child)
                    if child_result is not None:
                        return child_result
                
                return node
            return None
        
        def get_all_labels_in_subtree(node):
            labels = set()
            
            def collect(n):
                if 'children' not in n:
                    labels.add(n.get('name'))
                else:
                    for child in n.get('children', []):
                        collect(child)
            
            collect(node)
            return list(labels)
        
        subtree = find_smallest_ancestor(self.Z_tree_format)
        if subtree is None:
            raise ValueError(f"No common ancestor found for labels: {selected_labels}")
        
        all_labels = get_all_labels_in_subtree(subtree)
        return subtree, all_labels
    
    def get_node_name(self, node_id):
        def find_name(node):
            if node.get('id') == node_id:
                return node.get('name')
            for child in node.get('children', []):
                result = find_name(child)
                if result is not None:
                    return result
            return None
        return find_name(self.Z_tree_format)

    def get_dendrogram_height(self, num_leaves):
        n = num_leaves
        children = {}
        for i, (left, right, _, _) in enumerate(self.Z):
            children[n + i] = (int(left), int(right))

        def node_depth(node):
            if node < n:
                return 0
            left, right = children[node]
            return 1 + max(node_depth(left), node_depth(right))

        root = n + self.Z.shape[0] - 1
        return node_depth(root)
    