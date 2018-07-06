#!/usr/bin/python3

from os import listdir, makedirs, path

dcp_abspath = path.abspath(path.dirname(__file__)) # path containing this script
problem_num_dirs = filter(lambda x: x.isdigit(), listdir(dcp_abspath))
next_num = int(max(problem_num_dirs)) + 1
next_dir_name = f'{next_num:03}'

if not path.exists(next_dir_name):
    makedirs(next_dir_name)

unittest_str = '''
import unittest, prob{probnum}

class TestProb{probnum}(unittest.TestCase):
    def test_prob{probnum}(self):
        expected = True
        actual = prob{probnum}.some_function(x, y, z)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
'''.format(probnum=next_dir_name)

with open(f"{next_dir_name}/README.md", 'w') as readme_file:
    readme_file.write("TODO")

open(f"{next_dir_name}/prob{next_dir_name}.py", 'w').close()

with open(f"{next_dir_name}/test_prob{next_dir_name}.py", 'w') as test_file:
    test_file.write(unittest_str)

print(next_dir_name)
for f in listdir(next_dir_name):
    print(f"{next_dir_name}/{f}")




