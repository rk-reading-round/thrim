import iptc
import ipaddress
import yaml
import ast

def start():
  print('Import iptables Settings...')
  input_chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
  output_chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
  make_config(input_chain, output_chain)
  print('Import success!!\n$ cat absorbed_config.yml')

def make_config(input_chain, output_chain):
  text = read_config(input_chain, output_chain)
  print(text)

  with open("absorbed_config.yml", "w") as ac:
    yaml.dump(ast.literal_eval(text), ac, default_flow_style=False)

# format IP address to prefix
def format_address(address):
  if isinstance(address, (str, ipaddress.IPv4Address)):
    try:
     address = ipaddress.ip_network(address)
    except ValueError:
      raise
  elif isinstance(address, ipaddress.IPv4Network):
    pass
  else:
    raise TypeError
  return address.with_prefixlen

def read_config(input_chain, output_chain):
  text = "{'input': {"
  text = add_chain_rules(text, input_chain)
  text += "}, 'output': {"
  text = add_chain_rules(text, output_chain)
  text += "}}"
  return text

def add_chain_rules(text, chain):
  # null check
  if not chain.rules:
    return text

  previous_target = ''
  for rule in chain.rules:
    target_name = rule.target.name.lower()
    if previous_target == '':
      pass
    elif target_name != previous_target:
      text = text.rstrip(', ')
      text += "], "

    if target_name == previous_target:
      text += "{'ip': '"
    else:
      text += "'"
      text += target_name
      text += "': [{'ip': '"
    previous_target = target_name

    text += format_address(rule.src)
    text += "', 'protocol': '"
    text += rule.protocol
    text += "'}, "
  text = text.rstrip(', ')
  text += "]"
  return text
