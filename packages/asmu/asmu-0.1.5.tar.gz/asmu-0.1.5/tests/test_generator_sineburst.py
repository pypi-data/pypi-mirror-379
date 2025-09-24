"""PyTest for the RMSAverage Analyzer."""
import logging

import numpy as np
import pytest

import asmu

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PLOT = False


def test_generator_sineburst(out_buffer: bool, benchmark):  # type: ignore[no-untyped-def]
    """Test the SineBurst generator."""
    freq = 100
    # create objects
    interface = asmu.TestInterface(samplerate=10000,
                                   blocksize=5000,
                                   analog_output_channels=[1, 2])
    # reference sine
    sineburst = asmu.generator.SineBurst(interface, freq, 2, out_buffer=out_buffer)

    # establish connections
    sineburst.output().connect(interface.ioutput(ch=1))
    sineburst.output().connect(interface.ioutput(ch=2))

    # setup vector for callback to write to
    outdata = np.zeros((interface.blocksize, 2), dtype=np.float32)

    # call callback once (_inc() is not called)
    interface.callback(None, outdata, None, None, None)  # type: ignore[arg-type]

    assert outdata[:, 0] == pytest.approx(outdata[:, 1])
    assert outdata[0, 0] == pytest.approx(0)
    assert outdata[25, 0] == pytest.approx(1)
    assert outdata[75, 0] == pytest.approx(-1)
    assert outdata[100: 0] == pytest.approx(0)
    assert outdata[210: 0] == pytest.approx(0)

    if PLOT:
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(outdata[:, 0])
        ax.plot(outdata[:, 1])
        plt.show()

    # benchmark (calls callback very often)
    if benchmark is not None:
        benchmark(interface.callback, None, outdata, None, None, None)


if __name__ == "__main__":
    pass
    test_generator_sineburst(False, benchmark=None)
