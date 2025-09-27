import pandas as pd
from ..core import pipeline
from ..core import helpers

def score_accuracy(row, legacy=False):
    try:
        if legacy:
            return row["user_response"] == row["correct_response"]
        else:
            return row["user_response_index"] == row["correct_response_index"]
    except Exception as e:
        print(f"Error processing row: {e}")
        return None

def summarize(x, trials_expected=20, rt_outlier_low=100, rt_outlier_high=10000):

    # ABSTRACTION TO APPEAR IN EACH SCORING SCRIPT
    d = helpers.summarize_common_metadata(x, trials_expected)


    # trial counts (for various denominators)
    d["n_trials_total"] = x["trial_index"].nunique()
    d["n_trials_lure"] = (x["trial_type"] == "lure").sum()
    d["n_trials_normal"] = (x["trial_type"] == "normal").sum()


    # tabulate accuracy
    d["n_trials_correct"] = (
        x["user_response_index"] == x["correct_response_index"]
    ).sum()

    d["n_trials_incorrect"] = (
        x["user_response_index"] != x["correct_response_index"]
    ).sum()

    # Filter out outliers: RT < 100 ms or RT > 10,000 ms
    rt_filtered = x.loc[
        (x["response_time_duration_ms"] >= rt_outlier_low)
        & (x["response_time_duration_ms"] <= rt_outlier_high),
        "response_time_duration_ms",
    ]
    d["median_response_time_filtered"] = rt_filtered.median()
    
    # correct AND RT within bounds
    correct_and_filtered = x.loc[
        (x["user_response_index"] == x["correct_response_index"])
        & (x["response_time_duration_ms"] >= rt_outlier_low)
        & (x["response_time_duration_ms"] <= rt_outlier_high),
        "response_time_duration_ms"
    ]
    d["median_response_time_correct_filtered"] = correct_and_filtered.median()
    d["std_response_time_correct_filtered"] = correct_and_filtered.std()

    # get RTs for correct and incorrect trials
    d["median_response_time_overall"] = x["response_time_duration_ms"].median()
    d["median_response_time_correct"] = x.loc[
        (x["user_response_index"] == x["correct_response_index"]),
        "response_time_duration_ms",
    ].median()
    d["median_response_time_incorrect"] = x.loc[
        (x["user_response_index"] != x["correct_response_index"]),
        "response_time_duration_ms",
    ].median()

    # return as series
    indices = list(d.keys())
    return pd.Series(
        d,
        index=indices,
    )
