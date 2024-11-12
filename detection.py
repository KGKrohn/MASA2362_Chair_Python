import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import *

# Load the CSV data
data = load_csv("sit.csv")

# Parameters
spike_threshold = 6
min_sensors_trig = 4

# Select only the seat data (excluding first 7 columns)
only_seat_data = data.iloc[:, 7:]

# Apply a 3-point moving average filter for smoothing
smoothed_data = only_seat_data.rolling(window=3, min_periods=1).mean()

# Calculate delta for seat data
delta_seat_data = smoothed_data.diff().fillna(0)

# Detect spikes based on delta changes exceeding the threshold
delta_spikes = delta_seat_data.abs() > spike_threshold

# Detect events where at least 3 sensors exceed the delta spike threshold simultaneously
sit_down_events_delta = delta_spikes.sum(axis=1) >= min_sensors_trig

# Get the indices of detected events with delta-based method
sit_down_indices_delta = np.where(sit_down_events_delta)[0]

# Plot the smoothed seat sensor data with detected events marked
plt.figure(figsize=(12, 6))
for i, col in enumerate(smoothed_data.columns):
    plt.plot(smoothed_data.index, smoothed_data[col], label=f"Seat Sensor {i + 1}", alpha=0.6)

# Mark detected sit-down events with vertical lines
for idx in sit_down_indices_delta:
    plt.axvline(x=idx, color='red', linestyle='--', alpha=0.7)

plt.xlabel("Row Index")
plt.ylabel("Seat Sensor Values (Smoothed)")
plt.title("Sit-Down Event Detection (Delta-Based)")
plt.legend(loc="upper right", ncol=3, fontsize='small')
plt.grid(True)
plt.show()

# Show detected event indices for delta-based detection
sit_down_indices_delta
