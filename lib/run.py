import yaml
import subprocess
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
  dryrun_iptables(data, 'input', 'accept')
  dryrun_iptables(data, 'input', 'drop')
  dryrun_iptables(data, 'output', 'accept')
  dryrun_iptables(data, 'output', 'drop')

def realrun_thrim(data):
  print('Thrim start...')
  run_iptables(data, 'input', 'accept')
  run_iptables(data, 'input', 'drop')
  run_iptables(data, 'output', 'accept')
  run_iptables(data, 'output', 'drop')
  print('Thrim complete.')

def dryrun_iptables(data, chain, option):
  option_configs = data[chain][option]

  for i in range(len(option_configs)):
    ip = option_configs[i]['ip']
    protocol = option_configs[i]['protocol']
    print('[Dryrun] iptables -A ' + chain.upper() + ' -j '+ str(option).upper() + ' -s ' + ip + ' -p ' + protocol)

def run_iptables(data, chain, option):
  option_configs = data[chain][option]

  for i in range(len(option_configs)):
    ip = option_configs[i]['ip']
    protocol = option_configs[i]['protocol']
    command = ['iptables', '-A', chain.upper(), '-j', str(option).upper(), '-s', ip, '-p', protocol]
    print('[Running] iptables -A ' + chain.upper() + ' -j '+ str(option).upper() + ' -s ' + ip + ' -p ' + protocol)
    subprocess.run(command)
