import fire

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'

if __name__ == '__main__':
  fire.Fire(Thrim)