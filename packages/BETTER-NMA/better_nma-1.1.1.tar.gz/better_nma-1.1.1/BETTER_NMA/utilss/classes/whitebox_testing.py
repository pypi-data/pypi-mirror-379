import pandas as pd

class WhiteBoxTesting:
    def __init__(self, model_name, verbose=False):
        self.model_name = model_name
        self.problematic_img_ids = None
        self.problematic_img_preds = None
        self.verbose = verbose
        
        
    def find_problematic_images(self, source_labels, target_labels, edges_df, explanation_method=None):
        filtered_edges_df = edges_df[
            (edges_df['source'].isin(source_labels)) & 
            (edges_df['target'].isin(target_labels))
        ]

        filtered_edges_df_switched = edges_df[
            (edges_df['source'].isin(target_labels)) & 
            (edges_df['target'].isin(source_labels))
        ]
        
        if self.verbose:
            print(filtered_edges_df_switched.head())
        
        combined_filtered_edges_df = pd.concat([filtered_edges_df, filtered_edges_df_switched])
        
        if self.verbose:
            print("Combined filtered edges dataset:")
            print(combined_filtered_edges_df)
        
        unique_ids_list = combined_filtered_edges_df['image_id'].unique().tolist()
        
        matched_dict = {
            image_id: list(zip(group['source'], group['target'], group['target_probability']))
            for image_id, group in edges_df[edges_df['image_id'].isin(unique_ids_list)].groupby('image_id')
        }
        
        if self.verbose:
            print("Matched dictionary:")
            print(matched_dict)
        
        return matched_dict
