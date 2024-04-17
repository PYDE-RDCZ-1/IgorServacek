import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def compute(file_name):
    # Initialize an empty list to store numerical values
    numbers = []
    try:
        # Open the CSV file
        with open(file_name, "r") as csvfile:
            reader = csv.reader(csvfile)
            # Iterate over each row in the CSV file
            for row in reader:
                numbers.append(int(row[1]))

        salaries_array = np.array(numbers)

        mean_salary = round(np.mean(numbers), 2)

        median_salary = np.median(numbers)

        smerodajna_odchylka = round(np.std(numbers))

        print("pole numbers : ", salaries_array)
        print("Priemer: ", mean_salary)
        print("Median: ", median_salary)
        print("Smerodajna odchylka: ", smerodajna_odchylka)

        # PRINT
        # CREATE HISTOGRAM
        plt.hist(salaries_array, bins=10, color="skyblue", edgecolor = "black")

        plt.axvline(mean_salary, color ="red", linestyle="dashed", linewidth=1)
        plt.axvline(median_salary, color="green", linestyle="dashed", linewidth=1)

        plt.xlabel("Salary")
        plt.ylabel("Frequency")
        plt.title("Salary distribution")
        plt.show()
    except FileNotFoundError:
            print("File not found.")
    except IndexError:
            print("Index out of range in CSV file.")
    except ValueError:
            print("Unable to convert value to float.")
    return


# program
compute("average_salary.csv")

x = [1,2,3,4,5,6,7]
y = [1, 4, 9, 16, 25, 36, 49]

plt.plot(x, y)

plt.xlabel("x ová os")
plt.xlabel("y ová os")
plt.title("Demo graf.")

# zobrazenie grafu
plt.show()