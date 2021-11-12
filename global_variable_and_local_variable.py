# it's an global variable which cannot be used out of this function
global_variable = "global variable"


def func():

    # it's an local variable which cannot be used out of this function
    local = "local variable"
    print(local, global_variable)


if __name__=="__main__":
    func()