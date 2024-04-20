def funcThree():
    print("3")
    return 3
    
def funcTwo():
    funcThree()
    print("2")
    return 2
    
def funcOne():
    funcTwo()
    print("1")
    return 1
    
funcOne()