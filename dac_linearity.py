import numpy as np


def dnl(x, y, bits):
    # Computes for LSB
    lsb = [(y[-1] - y[0]) / (2 ** bits - 1)]

    # Computes for the DNL in LSB
    y_dnl = (np.diff(y) / (lsb * (np.diff(x)))) - 1
    dac_dnl = np.append([0], y_dnl)  # append '0' to the first element since DNL at code 0 is 0.
    return dac_dnl


def inl(x, y, bits):
    # Computes for LSB
    lsb = [(y[-1] - y[0]) / (2 ** bits - 1)]

    # Computes for the INL in LSB
    dac_inl = ((y - (y[0] + lsb * (x - x[0])))/lsb)
    return dac_inl


def tue(x, y, ideal_lsb, ideal_zeroscale):
    # Compute for the TUE
    dac_tue = (y - (ideal_zeroscale + (ideal_lsb * x)))
    return dac_tue
