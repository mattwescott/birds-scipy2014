import sklearn.metrics


def write_submission_csv(prediction_df, filename):
    """Take a dataframe of predictions in the same form as data.labels_df and
    write a submission csv"""

    clipnames = sorted(prediction_df.index.values)

    submission = "ID,Probability\n"
    for clipname in clipnames:
        for call_id in sorted(prediction_df.columns.values):
            submission += "%s_classnumber_%s,%f\n" % (clipname, call_id, prediction_df.ix[clipname, call_id])

    with open(filename, 'w') as f:
        f.write(submission)


def evaluate(prediction_df, truth_df):

    return sklearn.metrics.roc_auc_score(truth_df.values.ravel(), prediction_df.values.ravel())

