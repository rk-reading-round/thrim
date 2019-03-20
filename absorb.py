#coding: UTF-8

import iptc
import ipaddress
import yaml
import ast

def start():
  print('Import iptables Settings...')
  print("=============================")

  input_chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
  for rule in input_chain.rules:
    print("INPUT")
    display_rule(rule)

  output_chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
  for rule in output_chain.rules:
    print("OUTPUT")
    display_rule(rule)

  make_config(input_chain, output_chain)

# debug: delete later
def display_rule(rule):
  print("=============================")
  print("Target:", rule.target.name)
  print("Protocol:", rule.protocol)
  print("Source address:", format_address(rule.src))
  print("Destination address:", format_address(rule.dst))
  print("=============================")

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
  input_text = ""
  input_text += "{'input': {"
  for rule in input_chain.rules:
    input_text += "\'"
    input_text += rule.target.name
    input_text += "\': '', "
  input_text += "}}"
  print(input_text)
  return input_text

def make_config(input_chain, output_chain):
  input_text = read_config(input_chain, output_chain)
  with open("absorbed_config.yml", "w") as ac:
    yaml.dump(ast.literal_eval(input_text), ac, default_flow_style=False)
