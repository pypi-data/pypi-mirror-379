import math

def voltage(current=None, resistance=None, power=None):
    if current is not None and resistance is not None:
        # V = I * R
        return current * resistance

    elif current is not None and power is not None:
        # V = P / I
        return power / current

    elif power is not None and resistance is not None:
        # V = √(P * R)
        return math.sqrt(power * resistance)

    else:
        raise ValueError("برای محاسبه ولتاژ باید حداقل دو مقدار از (current, resistance, power) داده شود.")
def power(current=None, voltage=None):
    if current is not None and voltage is not None:
        return current * voltage
    elif current is not None and resistance is not None:
        # P = I² * R
        return current ** 2 * resistance
    elif voltage is not None and resistance is not None:
        # P = V² / R
        return voltage ** 2 / resistance
    else:
        raise ValueError("برای محاسبه توان باید دو مقدار از (current, voltage, resistance) داده شود.")

def current(power=None, voltage=None, resistance=None):
    if power is not None and voltage is not None:
        # I = P / V
        return power / voltage
    elif voltage is not None and resistance is not None:
        # I = V / R
        return voltage / resistance
    elif power is not None and resistance is not None:
        # I = √(P / R)
        return math.sqrt(power / resistance)
    else:
        raise ValueError("برای محاسبه جریان باید دو مقدار از (power, voltage, resistance) داده شود.")

def resistance(voltage=None, current=None, power=None):
    if voltage is not None and current is not None:
        # R = V / I
        return voltage / current
    elif voltage is not None and power is not None:
        # R = V² / P
        return voltage ** 2 / power
    elif power is not None and current is not None:
        # R = P / I²
        return power / (current ** 2)
    else:
        raise ValueError("برای محاسبه مقاومت باید دو مقدار از (voltage, current, power) داده شود.")
