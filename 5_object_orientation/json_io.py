import json

input_file_name = './input/data.json'
output_file_name = './output/data.json'

json_data = {}

with open(input_file_name, mode='r') as f:
    json_data = json.load(f)

json_data["name"] = "Kotaro Tomita"
json_data["age"] = 15
json_data["has-driver-license"] = False

# mode a, not rewrite data, but add data
with open(output_file_name, mode='w') as f:
    json.dump(json_data, f, indent=4)