import iptc
import ipaddress

def start():
  print('Import iptables Settings...')
  print("=============================")
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'INPUT')
  for rule in chain.rules:
    print("INPUT")
    display_rule(rule)
  chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), 'OUTPUT')
  for rule in chain.rules:
    print("OUT")
    display_rule(rule)

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
