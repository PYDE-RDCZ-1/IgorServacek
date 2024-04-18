import csv

def read_csv_file(file_name):
    try:
        with open(file_name, "r", newline="",  encoding="utf-8", delimiter = ";") as file:
            reder =csv.reader(file)
            for row in reder:
                print(row)
    except FileNotFoundError:
        print("Súbor nebol nájdený")
    return

file_name = "prikladx.csv"
read_csv_file(file_name)