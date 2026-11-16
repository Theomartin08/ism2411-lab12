# ISM2411 Lab 12
# Theo Martin
#
# Reflection 1 (Python vs Excel):
# Doing this in Excel I would open the file, add a total column, filter it,
# and save a new copy. That is fine for one file. In Python I write the steps
# once and can run them again on any file without clicking around. Excel is
# still easier when I just want to look at the data or fix a cell by hand.
#
# Reflection 2 (append mode log):
# A store could keep a log file that adds a line every night when the sales
# report runs, with the date and the total sales. Append mode is the right
# choice because it adds to the end and keeps the old lines. Write mode would
# erase the whole history every time the script ran.

import csv
from datetime import datetime

# Exercise 1: make sure the file opens
with open("data/sales.csv") as f:
    print("File opened fine")

# Exercise 2: print every row, including the header
print("\n--- Exercise 2 ---")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3: skip the header with next()
print("\n--- Exercise 3 ---")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: totals for each row and overall
print("\n--- Exercise 4 ---")
total_revenue = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        name = row[0]
        price = float(row[1])
        qty = int(row[2])
        total = price * qty
        total_revenue = total_revenue + total
        print(f"{name}: {qty} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: write cleaned.csv with only orders over $100
print("\n--- Exercise 5 ---")
original_rows = 0
written_rows = 0
with open("data/sales.csv", newline="") as infile:
    with open("data/cleaned.csv", "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        next(reader)
        writer.writerow(["Product", "Price", "Qty", "Total"])
        for row in reader:
            original_rows = original_rows + 1
            price = float(row[1])
            qty = int(row[2])
            total = price * qty
            if total > 100:
                writer.writerow([row[0], price, qty, round(total, 2)])
                written_rows = written_rows + 1
print("Rows in original file:", original_rows)
print("Rows written to cleaned.csv:", written_rows)

# Exercise 6: same thing with DictReader
# reader uses the position (row[0]) which is quick for small files.
# DictReader uses the column name (row["product"]) which is easier to read
# and doesn't break if the columns get moved around.
print("\n--- Exercise 6 ---")
dict_total = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        dict_total = dict_total + total
        print(f"{row['product']}: {qty} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
if round(dict_total, 2) == round(total_revenue, 2):
    print("Same total as Exercise 4")

# Exercise 7: add up revenue for each product
print("\n--- Exercise 7 ---")
summary = {}
with open("data/sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = float(row["price"]) * int(row["quantity"])
        name = row["product"]
        if name in summary:
            summary[name] = summary[name] + total
        else:
            summary[name] = total
for name in sorted(summary):
    print(f"{name}: ${summary[name]:.2f}")

# Exercise 8: add a line to the log file each time the script runs
print("\n--- Exercise 8 ---")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{now} - total revenue: ${total_revenue:.2f}\n")
print("Added a line to data/run_log.txt")