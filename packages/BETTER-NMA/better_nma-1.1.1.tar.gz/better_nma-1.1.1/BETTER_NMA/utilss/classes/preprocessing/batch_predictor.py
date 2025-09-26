import numpy as np
import tensorflow as tf
from ...wordnet_utils import synset_to_readable


class BatchPredictor:
    def __init__(self, model, batch_size=32):
        self.model = model
        self.batch_size = batch_size
        self.buffer_images = []  # To store images
        self.buffer_labels = []  # To store corresponding labels
        self.buffer_results = []  # To store batch results

    def get_top_predictions(self, X, labels, top_k, graph_threshold):
        batch_preds = self.model.predict(np.array(X), verbose=0)
        batch_results = []
        for pred in batch_preds:
            top_indices = pred.argsort()[-top_k:][::-1]
            valid_indices = [i for i in top_indices if i < len(labels)]

            top_predictions = [
                # (i, labels[i], pred[i])
                (i, synset_to_readable(labels[i]), pred[i]) 
                for i in valid_indices
                if pred[i] >= graph_threshold
            ]

            batch_results.append(top_predictions)

        return batch_results
