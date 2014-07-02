# -*- coding: utf-8 -*-

import os.path
import pandas as pd

import numpy as np
import scipy.io.wavfile as wavfile

import config


# Check that data directories exist
if not os.path.isdir(config.WAV_DIR):
    raise Exception("Update config.py. Path to audio data missing: %s" % config.WAV_DIR)
if not os.path.isdir(config.MFCC_DIR):
    raise Exception("Update config.py. Path to mfcc data missing: %s" % config.MFCC_DIR)
if not os.path.isdir(config.LABEL_DIR):
    raise Exception("Update config.py. Path to label data missing: %s" % config.LABEL_DIR)


def is_test(clipname):
    return clipname[13:17]=="test"


def clip_name_to_id(clipname):
    return int(clipname[-7-int(is_test(clipname)):-4])


def clip_name_to_path(clipname):

    if is_test(clipname):
        subdir = 'test'
    else:
        subdir = 'train'

    path = os.path.join(config.WAV_DIR, subdir, clipname)
    return path


def get_wav_sig_and_rate(clipname):

    rate, sig = wavfile.read(clip_name_to_path(clipname))
    if clipname == 'nips4b_birds_trainfile060.wav':
        sig = sig[:93000]
    return rate, sig


def get_wav_array(clipname):
    return get_wav_sig_and_rate(clipname)[1]


def get_mfcc_array(clipname):
    #our default mfcc_arrays are transposed from the input data

    clipid = clip_name_to_id(clipname)

    test_dir = os.path.join(config.MFCC_DIR, 'test')
    train_dir = os.path.join(config.MFCC_DIR, 'train')

    if is_test(clipname):
        filename = "cepst_conc_cepst_nips4b_birds_testfile%04d.txt" % clipid
        path = os.path.join(test_dir, filename)
    else:
        filename = "cepst_conc_cepst_nips4b_birds_trainfile%03d.txt" % clipid
        path = os.path.join(train_dir, filename)

    mfccs = np.array( [[float(x) for x in line.strip().split(" ") if x] for line in open(path, 'rt').readlines()]).transpose()

    # Drop columns with nans or infs
    mfccs_without_nans = mfccs[~np.isnan(mfccs).any(axis=1)]
    mfccs_without_nans_or_infs = mfccs_without_nans[~np.isinf(mfccs_without_nans).any(axis=1)]

    return mfccs_without_nans_or_infs


def get_clip_names(test=False):
    if test:
        return os.listdir(os.path.join(config.WAV_DIR, "test"))
    else:
        return os.listdir(os.path.join(config.WAV_DIR, "train"))


def get_wav_dict(clipnames=False, test=False):
    if not(clipnames):
        clipnames = get_clip_names(test)
    return dict((clipname, get_wav_array(clipname)) for clipname in get_clip_names(test))


def get_mfcc_dict(clipnames=False, test=False):
    if not(clipnames):
        clipnames = get_clip_names(test)
    return dict((clipname, get_mfcc_array(clipname)) for clipname in clipnames)


def get_label_df(label_csv_path):

    raw_df = pd.read_csv(label_csv_path)

    # Pull out the labels for columns and rows
    filename = raw_df.iloc[2:-1,0]
    card_species = raw_df.iloc[2:-1,1]
    call_names = raw_df.iloc[0, 4:]
    call_ids = raw_df.iloc[1, 4:].astype(int)

    # Trim off the empty and label rows and columns
    trimmed_df = raw_df.iloc[2:-1, 4:]

    # Set non-present call_id values to 0 instead of null
    trimmed_df.fillna(0, inplace=True)

    # Add labels for the rows and columns
    trimmed_df.columns = call_ids
    trimmed_df.columns.names = ['call_ids']
    trimmed_df.index = filename
    trimmed_df.index.names = ['filename']

    return trimmed_df.astype(float)

label_df = get_label_df(os.path.join(config.LABEL_DIR, "nips4b_birdchallenge_train_labels.csv"))


def get_call_info_df(call_info_csv_path):

    raw_df = pd.read_csv(call_info_csv_path)
    raw_df.set_index("class number")
    return raw_df

call_df = get_call_info_df(os.path.join(config.LABEL_DIR, "nips4b_birdchallenge_espece_list.csv"))


def calls_in_clip(clipname):
    has_label = label_df.ix[clipname] == 1
    present_labels = label_df.columns[has_label]
    return call_df.ix[present_labels]
