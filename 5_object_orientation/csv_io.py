import csv

input_file_name = './input/data.csv'
output_file_name = './output/data.csv'

column = []

with open(input_file_name, mode='r') as f: # r: 読み込み(read)
    reader = csv.reader(f)
    for row in reader:
        column.append(row)

# mode a, not rewrite data, but add data
with open(output_file_name, mode='w') as f: # w: 書き込み(write)
    writer = csv.writer(f)
    writer.writerows(column)
    """
    # or
    for row in column:
        writer.writerow(row)
    """