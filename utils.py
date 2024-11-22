import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)

        # Drop the last two columns
        data = data.iloc[:, :-2]

        print("Loaded data successfully")
        return data
    except:
        print("Failed to load data from file")
        return None

def plot_data(data):
    plt.figure()

    for col in data.columns:
        plt.plot(data.index, data[col])

    plt.xlabel("Row Index")
    plt.ylabel("Values")
    plt.title("All Columns Plot")
    plt.grid()
    plt.show()
