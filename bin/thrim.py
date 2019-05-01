import fire
import run
import absorb

class Thrim(object):
  def hello(self):
    return 'Hello, Thrim!'
  def run(self, f='config.yml'):
    run.start(f)
  def absorb(self):
    absorb.start()

def main():
  fire.Fire(Thrim)

if __name__ == '__main__':
  fire.Fire(Thrim)
