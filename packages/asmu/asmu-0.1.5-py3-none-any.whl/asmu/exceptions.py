

class DeviceError(Exception):
    """Used if something is wrong with the device specified."""
    pass


class UnitError(Exception):
    """Used if the physical unit is unknown or does not match."""
    pass
