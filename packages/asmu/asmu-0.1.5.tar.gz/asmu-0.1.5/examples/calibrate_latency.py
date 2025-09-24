"""This example calibrates the latency between given input and output."""
import time
from typing import TYPE_CHECKING

from asmu_utils.correlation import get_corrs_sampleshifts

import asmu

if TYPE_CHECKING:
    from asmu.typing import ABuffer


def calibrate_latency(interface: "asmu.Interface",
                      in_ch: int,
                      out_ch: int) -> int:
    sineburst = asmu.generator.SineBurst(interface, 1000, 10)
    with asmu.AFile(interface, mode="w+", channels=2, temp=True) as afile:
        rec = asmu.analyzer.Recorder(interface, afile)

        sineburst.output().connect(interface.ioutput(ch=out_ch))
        sineburst.output().connect(rec.input(0))
        interface.iinput(ch=in_ch).connect(rec.input(1))

        stream = interface.start(end_frame=16)
        while stream.active:
            time.sleep(0.1)
        stream.stop()
        stream.close()

        data: ABuffer = afile.data  # type: ignore

    corrs, shifts = get_corrs_sampleshifts(data, data[:, 0], round(10 / 1000 * interface.samplerate))
    assert shifts[0] == 0
    return int(shifts[1])


if __name__ == "__main__":
    asetup = asmu.ASetup("mysetup.asmu")
    interface = asmu.Interface(asetup=asetup)

    # assuming the first io channels are used for loopback
    in_ch = interface.iinput().channel
    out_ch = interface.ioutput().channel

    latency = calibrate_latency(interface, in_ch, out_ch)
    print(f"Found latency = {latency}")
    # ilatency = interface.get_latency()
    # print(f"Interface internal latency = {ilatency}")

    if input("Save setup? (y|n)") == "y":
        interface.latency = latency
        asetup.save()
