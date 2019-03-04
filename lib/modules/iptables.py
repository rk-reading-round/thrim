import subprocess

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
