import fire

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'
  def run(self, f='config.yml'):
    import run
    run.start(f)

def main():
  fire.Fire(Thrim)

if __name__ == '__main__':
  fire.Fire(Thrim)