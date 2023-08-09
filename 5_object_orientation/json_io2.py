import json

input_file_name = './input/data2.json'
output_file_name = './output/data2.json'

input_json_data = []
output_json_data = []

with open(input_file_name, mode='r') as f:
    input_json_data = json.load(f)

for data in input_json_data:
    print(data)
    if int(data["id"]) in [0, 1, 4] and bool(data["has-driver-license"]): # ORでの複数の一致検索をやる場合の構文
        output_json_data.append(data)

# mode a, not rewrite data, but add data
with open(output_file_name, mode='w') as f:
    json.dump(output_json_data, f, indent=4)