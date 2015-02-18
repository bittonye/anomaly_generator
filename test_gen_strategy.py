import types
class TestGenStrategy :

    def __init__(self, func=None) :
        self.name = "Strategy Example 0"
        if func :
             self.generate = types.MethodType(func, self, TestGenStrategy)

    def generate(self,srcpath="data_sets\\",destpath="res_sets\\",test_set_size=20,delim=",") :
        print("add strategy")
