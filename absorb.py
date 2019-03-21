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
  for rule in input_chain.rules:
    text += "'"
    text += rule.target.name.lower()
    text += "': [{'ip': '"
    text += format_address(rule.src)
    text += "', 'protocol': '"
    text += rule.protocol
    text += "'}], "
  text = text.rstrip(', ')
  text += "}, 'output': {"
  for rule in output_chain.rules:
    text += "'"
    text += rule.target.name.lower()
    text += "': [{'ip': '"
    text += format_address(rule.src)
    text += "', 'protocol': '"
    text += rule.protocol
    text += "'}], "
  text = text.rstrip(', ')
  text += "}}"
  return text
