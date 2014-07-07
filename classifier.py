import numpy as np

import sklearn
import sklearn.ensemble


class LabelDistributingBinaryForest:

    def __init__(self, **kwargs):
        self.clf = sklearn.ensemble.RandomForestClassifier(**kwargs)

    def fit(self, feature_array_list, label_matrix):

        assert(len(label_matrix) == len(feature_array_list))

        label_array_list = []

        for i, feature_array in enumerate(feature_array_list):
            label_array = label_matrix[i]
            # Repeat the labels for each window of features
            expanded_label_array = np.repeat(np.atleast_2d(label_array), feature_array.shape[0], axis=0)
            label_array_list.append(expanded_label_array)

        feature_matrix = np.vstack(feature_array_list)
        distributed_labels = np.vstack(label_array_list)

        if len(label_matrix.shape) == 1:
            distributed_labels = distributed_labels.ravel()

        self.clf.fit(feature_matrix, distributed_labels)

    def transform(self, list_of_features):

        feature_matrix = np.vstack(list_of_features)
        splits = np.cumsum([w.shape[0] for w in list_of_features])[:-1]
        # If the random forest hasn't seen both a positive and negative case of a particular label,
        # it returns a column filled with [1] instead of [0.2 0.8].
        probs_weird_structure = self.clf.predict_proba(feature_matrix)
        # We pick out the probs for the label not being present because it is more common for a positive
        # case to be missing than a negative case
        # TODO: make this handle the case when the negative label is missing

        if self.clf.classes_.shape == (2,): # Handle binary case

            index_of_negative_case = np.where(self.clf.classes_ == 0)[0][0]
            splits = np.cumsum([w.shape[0] for w in list_of_features])[:-1]
            probs_of_positive_case = 1 - probs_weird_structure[:,index_of_negative_case]

        else: # Multilabel case
            indices_of_negative_class = [np.where(class_list==0)[0][0] for class_list in self.clf.classes_]
            # Here we pull out the probability for the negative case from what will usually be lists of [p 1-p]
            probs_of_negative_case = [prob[:,index] for prob, index in zip(probs_weird_structure, indices_of_negative_class)]
            probs_of_positive_case = 1-np.array(probs_of_negative_case).T

        return np.split(np.array(probs_of_positive_case), splits, axis=0)
