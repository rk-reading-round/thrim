import yaml
import iptc
import sys

def start(file):
  f = open(file, "r+")
  data = yaml.load(f)
  dryrun_thrim(data)
  require_confirmation()
  realrun_thrim(data)

def require_confirmation():
  while True:
    choice = input('Run Thrim? [y/N]: ').lower()
    if choice in ['y', 'yes']:
      return True
    elif choice in ['n', 'no']:
      print('Thrim end...')
      sys.exit()

def dryrun_thrim(data):
  print('Thrim Dryrun...')
  opt_pattern = {}
  for i in data:
    opt_pattern[i] = list(data[i].keys())

  for i in opt_pattern:
    chain = i
    for j in range(len(opt_pattern[i])):
      target = opt_pattern[i][j]
      dryrun_iptables(data, chain, target)

def realrun_thrim(data):
  print('Thrim start...')
  opt_pattern = {}
  for i in data:
    opt_pattern[i] = list(data[i].keys())

  for i in opt_pattern:
    chain = i
    for j in range(len(opt_pattern[i])):
      target = opt_pattern[i][j]
      try:
        run_iptables(data, chain, target)
      except FileNotFoundError:
        print('[Error] command iptables not found')

def dryrun_iptables(data, chain, target):
  try:
    rules = data[chain][target]
  except KeyError:
    return
  for i in rules:
    command = create_command(i, chain, target)
    print(' '.join(map(str, command)))

def run_iptables(data, chain, target):
  try:
    rules = data[chain][target]
  except KeyError:
    return
  for i in rules:
    command = create_command(i, chain, target)
    print(' '.join(map(str, command)))

    rule = iptc.Rule()
    for j in i:
      setattr(rule, j, i[j])
    rule.create_target(str(target).upper())
    table_chain = iptc.Chain(iptc.Table('filter'), chain.upper())
    table_chain.insert_rule(rule)

def create_command(rule, chain, target):
  opt_dict = {'src': '-s', 'protocol': '-p', 'in_interface': '-i', 'out_interface': '-o', 'sport': '--sport', 'dport': '--dport'}
  command = ['iptables -A', chain.upper(), '-j', target.upper()]
  for i in rule:
    command.append(opt_dict[i])
    command.append(rule[i])
  return command