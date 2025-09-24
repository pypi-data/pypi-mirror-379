"""This example can be used to calibrate an Interface IInput and IOutput channel for acceleration."""
import asmu


def calibrate_iinput_cA(interface: "asmu.Interface",
                        in_ch: int):
    calcA = asmu.analyzer.CalIInput(interface, 1, "Ap", gain=0)
    interface.iinput(ch=in_ch).connect(calcA.input())

    print(f"Connect a {calcA.actual:.1f}m/s^2 peak sine calibrator to input channel {in_ch}.")
    input("\tPress ENTER to start.")
    stream = interface.start()
    result = calcA.evaluate()
    while result is False:
        result = calcA.evaluate()
    stream.stop()
    stream.close()
    del calcA  # disconnect
    print(result)
    print(f"cA = {interface.iinput(ch=in_ch).cA}")
    print(f"fA = {interface.iinput(ch=in_ch).fA}")


def calibrate_ioutput_cA(interface: "asmu.Interface",
                         in_ch: int,
                         out_ch: int):
    outgain = 0.1
    sine = asmu.generator.Sine(interface, 1000)
    gain = asmu.effect.Gain(interface, outgain)
    calcA = asmu.analyzer.CalIOutput(interface, outgain, "A", interface.ioutput(ch=out_ch), gain=0)
    sine.output().connect(gain.input())
    gain.output().connect(interface.ioutput(ch=out_ch))
    interface.iinput(ch=in_ch).connect(calcA.input())

    print("Disconnect the calibrator and connect "
          f"the sensor on input channel {in_ch} "
          f"to the trancducer on output channel {out_ch}?")
    input("\tPress ENTER to start.")
    stream = interface.start()
    result = calcA.evaluate()
    while result is False:
        result = calcA.evaluate()
    stream.stop()
    stream.close()
    del calcA  # disconnect
    print(result)
    print(f"cA = {interface.ioutput(ch=out_ch).cA}")
    print(f"fA = {interface.ioutput(ch=out_ch).fA}")


def generate_sine(interface: "asmu.Interface",
                  out_ch: int,
                  freq: float = 1000,
                  Ap: float = 0.5):
    # verify if everything worked correctly
    sine = asmu.generator.Sine(interface, freq)

    cA = interface.ioutput().cA
    assert cA is not None
    gain = asmu.effect.Gain(interface, Ap / cA)
    sine.output().connect(gain.input())
    gain.output().connect(interface.ioutput(ch=out_ch))

    print("Starting sine generator...")
    stream = interface.start()
    print(f"You now should measure a {Ap:.2f}m/s^2 sine wave "
          f"on the output channel {interface.ioutput(ch=out_ch).channel}.")
    input("\tPress ENTER to stop.")
    stream.stop()
    stream.close()


if __name__ == "__main__":
    in_ch = 1
    out_ch = 1
    asetup = asmu.ASetup("mysetup.asmu")
    interface = asmu.Interface(device="ASIO MADIface USB",
                               analog_input_channels=[in_ch],
                               analog_output_channels=[out_ch],
                               blocksize=1024,
                               samplerate=44100)
    asetup.interface = interface

    calibrate_iinput_cA(interface, in_ch)

    calibrate_ioutput_cA(interface, in_ch, out_ch)

    if input("Save setup? (y|n)") == "y":
        asetup.save()

    if input("Start generator? (y|n)") == "y":
        generate_sine(interface, out_ch)
