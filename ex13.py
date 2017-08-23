import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)

# first with *args
args = ("two", 3, 5)
test_args_kwargs(*args)
arg1: "two"
arg2: 3
arg3: 5

#now with **kwargs:
kwargs = {"arg3": 3, "arg2": "two", "arg1":5}
test_args_kwargs(**kwargs)
arg1: 5
arg2: "two"
arg3: 3

import test
def get_info(self, *args):
    return "Test data"

test.get_info = get_info
