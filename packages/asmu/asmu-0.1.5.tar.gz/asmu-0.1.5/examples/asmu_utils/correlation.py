from typing import TYPE_CHECKING

import numpy as np
import scipy as sp

if TYPE_CHECKING:
    from asmu.typing import ABlock, ABuffer, Avg


def get_corrs_sampleshifts(indata: "ABuffer",
                           refdata: "ABlock",
                           burstLength: int) -> tuple["ABuffer", "Avg"]:
    """This function calculates the crosscorrelation between all channels of the indata relative to refdata.
    Additionally the maximum peak is exported.

    Args:
        indata: Input data.
        refdata: Reference data.
        burstLength: The length of the burst in samples, to better fit the peak finding algorithm.

    Returns:
        The full cross correlations in the format (Blocksize x Channel)
        and a vector containing the peak positions for each channel.
    """
    corrs = []
    sampleshifts = []
    n = int(np.size(refdata))
    for cidx in range(np.ma.size(indata, axis=1)):
        v = indata[:, cidx]
        corr = sp.signal.correlate(v, refdata)
        corr = corr / np.max(corr)
        peaks, _ = sp.signal.find_peaks(corr, prominence=0.8, distance=burstLength, height=0.5)

        # shift correlation correctly
        corrs.append(corr[n - 1:])
        sampleshifts.append(peaks[0] - (n - 1))
    return np.array(corrs, dtype=np.float32).T, np.array(sampleshifts, dtype=np.float32)
