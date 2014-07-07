import numpy as np
import pandas as pd


class WindowMFCCs:

    def __init__(self, window_length, overlap):
        self.window_length = window_length
        self.overlap = overlap

    def split_into_windows(self, mfcc_array):
        #input: mfcc array of shape (n_s samples, k coefficients)
        #output: window array of shape (n_w windows, n_f frames, k coefficients)

        window_length = self.window_length
        overlap = self.overlap

        windows = []
        start_frame = 0
        while start_frame+window_length < len(mfcc_array):
            windows.append(mfcc_array[start_frame:start_frame+window_length])
            start_frame += int(window_length*(1-overlap))

        return np.array(windows)

    def transform(self, list_of_frames):
        return [self.split_into_windows(mfcc_array) for mfcc_array in list_of_frames]


class SummarizeWindowedMFCCs:

    def __init__(self, summary_function):
        self.summary_function = summary_function

    def summarize_window(self, window):
        return np.apply_along_axis(self.summary_function, 1, window)

    def transform(self, list_of_windows):
        return [self.summarize_window(window) for window in list_of_windows]


class CollapseWindowPredictions:

    def __init__(self, collapse_function):
        self.collapse_function = collapse_function

    def transform(self, list_of_window_predictions):
        return np.array([np.apply_along_axis(self.collapse_function, 0, prediction_array) for prediction_array in list_of_window_predictions])


def make_prediction_df(list_of_preds, clipnames, call_ids):
    """Make a prediction df in the same format as data.label_df"""

    return pd.DataFrame(np.array(list_of_preds), index=clipnames, columns=call_ids)
