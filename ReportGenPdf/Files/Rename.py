import os
import csv

# Specify the path to the CSV file containing the file names and new names
csv_path = "E:/XI-SC 2023 Result/ReportGenPdf/Files/StudentPics/Rename1.csv"

# Open the CSV file and read the contents
with open(csv_path, "r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row

    # Iterate over each row in the CSV file
    for row in reader:
        old_name = row[0]  # Get the old file name from Column A
        print(old_name)
        new_name = row[1]  # Get the new file name from Column B
        print(new_name)
        os.rename(old_name, new_name)  # Rename the file
