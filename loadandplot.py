import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Loaded data successfully")
        return data
    except:
        print("Failed to load data from file")
        return None

def plot_data(data):
    plt.figure()

    for col in data.columns:
        plt.plot(data.index, data[col], label=f"Column {col + 1}")

    plt.xlabel("Row Index")
    plt.ylabel("Values")
    plt.title("All Columns Plot")
    plt.legend(loc="best")
    plt.grid()
    plt.show()

data = load_csv("sit.csv")
plot_data(data)

