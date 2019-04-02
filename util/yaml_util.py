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
