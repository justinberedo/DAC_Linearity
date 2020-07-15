import dac_linearity_class
import pandas as pd

# Read .csv file
linearity = pd.read_csv('linearity.csv')

# Extract relevant data
single = ['Single']
dev1 = ['DEV145']
is_dev1 = linearity[linearity.DUT_ID.isin(dev1) & linearity.Write.isin(single)]
dev1_a = is_dev1[is_dev1.Channel == 'CHA']

x = dev1_a['Code']
y_vload = dev1_a['VRload']
y_dnl = dev1_a['DNL(LSB)']
y_inl = dev1_a['INL(LSB)']
y_tue = dev1_a['TUE(%FSR)']

# Convert DataFrame to numpy array
x_arr = x.to_numpy()
y_vload_arr = y_vload.to_numpy()

# For comparison of the actual and computed values
y_dnl_arr = y_dnl.to_numpy()
y_inl_arr = y_inl.to_numpy()
y_tue_arr = y_tue.to_numpy()

# ideal LSB
ideal_lsb = 6.25 / (2**13 - 1)

# Computing for the linearity parameters
dev145 = dac_linearity_class.Linearity(y_vload_arr, x_arr, 13, ideal_lsb, 0)
dev145_dnl = dev145.dnl()
dev145_inl = dev145.inl()
dev145_tue = (dev145.tue()/6.25)*100

print("Actual DNL: ", y_dnl_arr[:5])
print("Computed DNL: ", dev145_dnl[:5])
print("Actual INL: ", y_inl_arr[:5])
print("Computed INL: ", dev145_inl[:5])
print("Actual TUE: ", y_tue_arr[:5])
print("Computed TUE: ", dev145_tue[:5])
