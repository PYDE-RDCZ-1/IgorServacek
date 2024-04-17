import csv
import numpy as np
import pandas as pd


def compute_median_from_csv(file_name):
    # Initialize an empty list to store numerical values
    numbers = []
    try:
        # Open the CSV file
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Iterate over each row in the CSV file
            for row in reader:
                # Assuming the numerical value is in the second column (index 1)
                # You may need to adjust this depending on the structure of your CSV file
                value = float(row[1])
                numbers.append(value)
        # Compute the median of the numerical values
#        print(numbers)
        vysl = np.median(numbers)
#       print(vysl)
        return vysl
    except FileNotFoundError:
            print("File not found.")
    except IndexError:
            print("Index out of range in CSV file.")
    except ValueError:
            print("Unable to convert value to float.")


def compute_priem_mzda_csv(file_name):
# Initialize an empty list to store numerical values
    numbers = []
    try:
        # Load data from CSV file
        data = pd.read_csv(file_name)
        # Convert strings to floats, filtering out non-numeric values
        print(data)
        numeric_data = [float(value) for value in data if value.replace('.', '', 1).isdigit()]
        numeric_data = np.
        # Compute the average
    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Index out of range in CSV file.")
    except ValueError:
        print("Unable to convert value to float.")
    average = np.mean(data)
    return average

def compute_priem_mzda(file_name):
    # Initialize an empty list to store numerical values
    numbers = []
    try:
        # Open the CSV file
        with open(file_name, newline='') as csvfile:
            reader = csv.reader(csvfile)
            # Iterate over each row in the CSV file
            print(str(reader))
            value = 0
            pocet = 0
            with open("pomocny1.txt", "w+") as subor:
                for row in reader:
                    # Assuming the numerical value is in the second column (index 1)
                    # You may need to adjust this depending on the structure of your CSV file
                    pocet += 1
                    value += float(row[1])
                    subor.write(row[1] + "\n")
    #                print(row)
        # Compute the median of the numerical values
#        print(type(pocet), type(value))
#        print(float(value)/float(pocet))
        vysl = float(value)/float(pocet)
        print(vysl)
        return vysl
    except FileNotFoundError:
        print("File not found.")
    except IndexError:
        print("Index out of range in CSV file.")
    except ValueError:
        print("Unable to convert value to float.")


print("median: ", compute_median_from_csv("average_salary.csv"))
print("priemer: ", compute_priem_mzda("average_salary.csv"))
print("priemer csv: ", compute_priem_mzda_csv("average_salary.csv"))