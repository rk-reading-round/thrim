import yaml
import json
import ast

def yaml_sort(yaml_file):
  f = open(yaml_file, "r+")
  data = yaml.load(f)

  input_accept_list = data['input']['accept']
  input_accept_list.sort(key=lambda x: x['ip'])
  input_drop_list = data['input']['drop']
  input_drop_list.sort(key=lambda x: x['ip'])
  output_accept_list = data['output']['accept']
  output_accept_list.sort(key=lambda x: x['ip'])
  output_drop_list = data['output']['drop']
  output_drop_list.sort(key=lambda x: x['ip'])
  
  sorted_config = "{'input': {'accept': " + json.dumps(input_accept_list) + ", 'drop': " + json.dumps(input_drop_list) + "}, 'output': {'accept':" + json.dumps(output_accept_list) + ", 'drop': " + json.dumps(output_drop_list) + "}}"

  with open(yaml_file, "w") as yf:
    yaml.dump(ast.literal_eval(sorted_config), yf, default_flow_style=False)

def yaml_diff(yaml_file1, yaml_file2):
  data1 = yaml.load(open(yaml_file1, "r+"))
  data2 = yaml.load(open(yaml_file2, "r+"))
  diff_input_accept = data2_minus_data1(data1, data2, 'input', 'accept')
  diff_input_drop = data2_minus_data1(data1, data2, 'input', 'drop')
  diff_output_accept = data2_minus_data1(data1, data2, 'output', 'accept')
  diff_output_drop = data2_minus_data1(data1, data2, 'output', 'drop')

def data2_minus_data1(data1, data2, command, option):
  data1_list = [v.get('ip') for v in data1[command][option]]
  data2_list = [v.get('ip') for v in data2[command][option]]
  return list(set(data2_list) - set(data1_list))

yaml_diff('config.yml', '.state.yml')
