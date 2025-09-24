"""This example can be used to calibrate an Interface IInput and IOutput channel for voltage."""
import asmu


def calibrate_iinput_cV(interface: "asmu.Interface",
                        in_ch: int):
    calcV = asmu.analyzer.CalIInput(interface, 1, "Vp", gain=0)
    interface.iinput(ch=in_ch).connect(calcV.input())

    print(f"Connect a {calcV.actual:.1f}Vp sine generator to input channel {in_ch}.")
    input("\tPress ENTER to start.")
    stream = interface.start()
    result = calcV.evaluate()
    while result is False:
        result = calcV.evaluate()
    stream.stop()
    stream.close()
    del calcV  # disconnect
    print(result)
    print(f"cV = {interface.iinput(ch=in_ch).cV}")
    print(f"fV = {interface.iinput(ch=in_ch).fV}")


def calibrate_ioutput_cV(interface: "asmu.Interface",
                         in_ch: int,
                         out_ch: int):
    outgain = 0.1
    sine = asmu.generator.Sine(interface, 1000)
    gain = asmu.effect.Gain(interface, outgain)
    calcV = asmu.analyzer.CalIOutput(interface, outgain, "V", interface.ioutput(ch=out_ch), gain=0)
    sine.output().connect(gain.input())
    gain.output().connect(interface.ioutput(ch=out_ch))
    interface.iinput(ch=in_ch).connect(calcV.input())

    print("Disconnect the generator and connect "
          f"the input channel {in_ch} to the output channel {out_ch}?")
    input("\tPress ENTER to start.")
    stream = interface.start()
    result = calcV.evaluate()
    while result is False:
        result = calcV.evaluate()
    stream.stop()
    stream.close()
    del calcV  # disconnect
    print(result)
    print(f"cV = {interface.ioutput(ch=out_ch).cV}")
    print(f"fV = {interface.ioutput(ch=out_ch).fV}")


def generate_sine(interface: "asmu.Interface",
                  out_ch: int,
                  freq: float = 1000,
                  Vp: float = 0.5):
    # verify if everything worked correctly
    sine = asmu.generator.Sine(interface, freq)

    cV = interface.ioutput().cV
    assert cV is not None
    gain = asmu.effect.Gain(interface, Vp / cV)
    sine.output().connect(gain.input())
    gain.output().connect(interface.ioutput(ch=out_ch))

    print("Starting sine generator...")
    stream = interface.start()
    print(f"You now should measure a {Vp:.2f}Vp sine wave "
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

    calibrate_iinput_cV(interface, in_ch)

    calibrate_ioutput_cV(interface, in_ch, out_ch)

    if input("Save setup? (y|n)") == "y":
        asetup.save()

    if input("Start generator? (y|n)") == "y":
        generate_sine(interface, out_ch)
