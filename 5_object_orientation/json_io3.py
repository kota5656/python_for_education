import json

input_file_name = './input/data3.json'
output_file_name = './output/data3.json'

input_json_data = {}
output_json_data = {}

with open(input_file_name, mode='r') as f:
    input_json_data = json.load(f)

for key, value in input_json_data.items():
    print(key, value)
    if int(key) in [0, 1, 4]: # ORでの複数の一致検索をやる場合の構文
        output_json_data[key] = value

print(output_json_data)

# mode a, not rewrite data, but add data
with open(output_file_name, mode='w') as f:
    json.dump(output_json_data, f, indent=4)