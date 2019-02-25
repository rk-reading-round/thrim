import yaml

def start(file):
  print('Thrim start...')
  f = open(file, "r+")
  data = yaml.load(f)

  accept = data['input']['accept']
  for i in range(len(accept)):
    ip = (accept[i]['ip'])
    protocol = (accept[i]['protocol'])
    print('iptables -A INPUT -j ACCEPT -s ' + ip + ' -p ' + protocol)