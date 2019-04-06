import unittest
from util import yaml_util

class Test(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_yaml_diff(self):
    diff_input_accept, diff_input_drop, diff_output_accept, diff_output_accept = yaml_util.yaml_diff('test/test_util/files/config.yml', 'test/test_util/files/.state.yml')
    result = diff_output_accept
    self.assertEqual(result, ['77.77.77.77/32'])

if __name__ == '__main__':
  unittest.main()
