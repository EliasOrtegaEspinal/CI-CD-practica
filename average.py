import csv
def calculate_average(file_path, column_name):
    total = 0
    count = 0
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            try:
                value = float(row[column_name])
                total += value
                count += 1
            except ValueError:
                pass
    return total / count if count > 0 else 0

if __name__ == "__main__":
    print(calculate_average("data.csv", "Value"))
