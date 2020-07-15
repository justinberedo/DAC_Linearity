import numpy as np


class Linearity:
    # Input must be a numpy array
    def __init__(self, reading, codes, bits, ideal_lsb, ideal_zeroscale):
        self.y = reading
        self.x = codes
        self.bits = bits
        self.ideal_lsb = ideal_lsb
        self.ideal_zeroscale = ideal_zeroscale

    def dnl(self):
        y = self.y
        x = self.x

        # Computes for LSB
        lsb = [(y[-1] - y[0]) / (2 ** self.bits - 1)]

        # Computes for the DNL in LSB
        y_dnl = (np.diff(y) / (lsb * (np.diff(x)))) - 1
        dac_dnl = np.append([0], y_dnl)  # append '0' to the first element since DNL at code 0 is 0.
        return dac_dnl

    def inl(self):
        y = self.y
        x = self.x

        # Computes for LSB
        lsb = [(y[-1] - y[0]) / (2 ** self.bits - 1)]

        # Computes for the INL in LSB
        dac_inl = ((y - (y[0] + lsb * (x - x[0]))) / lsb)
        return dac_inl

    def tue(self):
        dac_tue = (self.y - (self.ideal_zeroscale + (self.ideal_lsb * self.x)))
        return dac_tue
