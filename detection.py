import pandas as pd
import numpy as np

from utils import *

data = load_csv("Old_data/sit.csv")

spike_threshold = 10
min_sensors_trig = 3

only_seat_data = data[:, 7:]


