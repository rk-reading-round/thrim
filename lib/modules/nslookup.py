def dryrun_nslookup(data, type, option):
  option_configs = data[type][option]

  for i in range(len(option_configs)):
    site = option_configs[i]['site']
    port = option_configs[i]['port']
    print('[Dryrun] nslookup -type=' + type + ' -' + option + ' -port=' + str(port) + ' ' + site)

def run_nslookup(data, type, option):
  option_configs = data[type][option]

  for i in range(len(option_configs)):
    site = option_configs[i]['site']
    port = option_configs[i]['port']
    command = ['nslookup', '-type={}'.format(type), '-{}'.format(option), '-port={}'.format(port), site]
    print('[Running] nslookup -type=' + type + ' -' + option + ' -port=' + str(port) + ' ' + site)
    subprocess.run(command)
