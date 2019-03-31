import yaml
import iptc
import sys

def start(file):
  f = open(file, "r+")
  data = yaml.load(f)
  dryrun_thrim(data)
  # require_confirmation()
  # realrun_thrim(data)

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
  try:
    run_iptables(data, 'input', 'accept')
    run_iptables(data, 'input', 'drop')
    run_iptables(data, 'output', 'accept')
    run_iptables(data, 'output', 'drop')
    print('Thrim complete.')
  except FileNotFoundError:
    print('[Error] command iptables not found')

def dryrun_iptables(data, chain, target):
  rules = data[chain][target]
  opt_dict = {'src': '-s', 'protocol': '-p', 'in_interface': '-i', 'dport': '--dport'}
  for i in rules:
    command = ['iptables -A', chain.upper(), '-j', target.upper()]
    for j in i:
      command.append(opt_dict[j])
      command.append(i[j])
    print(' '.join(map(str, command)))

def run_iptables(data, command, option):
  option_configs = data[command][option]

  for i in range(len(option_configs)):
    ip = option_configs[i]['ip']
    protocol = option_configs[i]['protocol']
    print('[Running] iptables -A ' + command.upper() + ' -j '+ str(option).upper() + ' -s ' + ip + ' -p ' + protocol)

    rule = iptc.Rule()
    rule.src = ip
    rule.protocol = protocol
    rule.create_target(str(option).upper())
    chain = iptc.Chain(iptc.Table('filter'), command.upper())
    chain.insert_rule(rule)