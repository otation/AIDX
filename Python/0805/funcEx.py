def funcA():
    print("Function A start")
    funcB()
    print("Function A end")
def funcB():
    print("Function B start")
    funcC()
    print("Function B end")

def funcC():
    print("Function C start")
    print("Function C end")

funcA()
print('1')