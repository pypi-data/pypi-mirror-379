"""
@Author  : 李欣怡
@File    : variance_of_spell_durations.py
@Time    : 2025/9/24 14:22
@Desc    : Variance of spell durations of individual state sequences.

        The corresponding function name in TraMineR is seqivardur,
        with the source code available at: https://github.com/cran/TraMineR/blob/master/R/seqivardur.R

"""
import os
from contextlib import redirect_stdout

import numpy as np
import pandas as pd

from sequenzo.dissimilarity_measures.utils.seqdss import seqdss
from sequenzo.dissimilarity_measures.utils.seqlength import seqlength
from sequenzo.dissimilarity_measures.utils.seqdur import seqdur
from .state_frequencies_and_entropy_per_sequence import get_state_freq_and_entropy_per_seq
from .simple_characteristics import cut_prefix

def get_spell_duration_variance(seqdata, type=1):
    if not hasattr(seqdata, 'seqdata'):
        raise ValueError(" [!] data is NOT a sequence object, see SequenceData function to create one.")
    if type not in [1, 2]:
        raise ValueError(" [!] type must be 1 or 2.")

    with open(os.devnull, 'w') as fnull:
        with redirect_stdout(fnull):
            dss = seqdss(seqdata)

            lgth = seqlength(seqdata)
            dlgth = seqlength(dss)
            sdist = get_state_freq_and_entropy_per_seq(seqdata)
            nnvisit = (sdist==0).sum(axis=1)

    def realvar(x):
        n = len(x)
        var_val = 1 / n * np.sum((x - np.mean(x)) ** 2)
        return var_val

    dur = pd.DataFrame(seqdur(seqdata)).apply(lambda row: cut_prefix(row, 1), axis=1)

    if type == 1:
        ret = dur.apply(realvar)
        meand = dur.apply(np.nanmean)
        var_max = (dlgth - 1) * (1 - meand) ** 2

    elif type == 2:
        meand = dur.apply(lambda arr: np.nansum(arr))
        meand /= dlgth + nnvisit.to_numpy()

        ddur = dur.to_frame("arr").join(meand.rename("m")).apply(
                    lambda row: (np.array(row["arr"]) - row["m"]) ** 2, axis=1
                )
        # ret = (np.nansum(ddur, axis=1) + nnvisit * (meand ** 2)) / (dlgth + nnvisit)
        ddur = pd.DataFrame(ddur.tolist())
        sum_sqdiff = np.nansum(ddur.to_numpy(), axis=1)
        ret = (sum_sqdiff + nnvisit.to_numpy() * (meand.to_numpy() ** 2)) / (dlgth + nnvisit.to_numpy())

        alph = seqdata.states.copy()
        alph_size = len(alph)
        if alph_size < 2:
            maxnnv = 0
        else:
            maxnnv = np.where(dlgth == 1, alph_size - 1, alph_size - 2)

        meand_max = meand.to_numpy() * (dlgth + nnvisit.to_numpy()) / (dlgth + maxnnv)
        var_max = ((dlgth-1) * (1-meand_max)**2 + (lgth - dlgth + 1 - meand_max)**2 + maxnnv * meand_max**2) / (dlgth + maxnnv)

    return {
        "meand": meand,
        "result": ret,
        "vmax": var_max
    }