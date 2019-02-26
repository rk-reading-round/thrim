import yaml
import subprocess

def start(file):
  f = open(file, "r+")
  data = yaml.load(f)
  print('Thrim start...')
  run_iptables(data, 'input', 'accept')
  run_iptables(data, 'input', 'drop')
  run_iptables(data, 'output', 'accept')
  run_iptables(data, 'output', 'drop')

def run_iptables(data, chain, option):
  option_configs = data[chain][option]

  for i in range(len(option_configs)):
    ip = (option_configs[i]['ip'])
    protocol = (option_configs[i]['protocol'])
    command = 'iptables -A ' + chain.upper() + ' -j '+ str(option).upper() + ' -s ' + ip + ' -p ' + protocol
    print(command)
    subprocess.run(command)