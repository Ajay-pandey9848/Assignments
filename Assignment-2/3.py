import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

#Read the csv file
df = pd.read_csv(r"D:\AI with python\Assignment\Assignment-2\weight-height.csv")

#Read length and weight values from the file
lengths_inch = df['length']
weights_pound = df['weight']

#Convert the length and weight to cm and kg
lengths_cm = np.array(lengths_inch * 2.54)
weights_kg = np.array(weights_pound * 0.453592)

#Calculate the mean of length and weight
lengths_cm_mean = np.mean(lengths_cm)
weights_pound_mean = np.mean(weights_kg)

#Create histogram of length (cm)
plt.hist(lengths_cm, edgecolor='black')
plt.title('Histogram of lengths')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')

plt.show()