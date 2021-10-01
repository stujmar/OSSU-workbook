# identifyng the type of exception

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except SyntaxError:
        print("syntax error!")
    except TypeError:
        print("type error!")
    except ValueError:
        print("value error!")
    except NameError:
        print("name error!")
    else:
        print("result is", result)

divide("1", "2")
divide("1", 2)
divide(int('1'), 2.0)

def list_asign():
    try:
        mylist = [1, 2, 3]
        mylist.index(11)
    except ZeroDivisionError:
        print("division by zero!")
    except SyntaxError:
        print("syntax error!")
    except TypeError:
        print("type error!")
    except ValueError:
        print("value error!")
    except NameError:
        print("name error!")
    else:
        print("No error is raised")

list_asign()

# A ValueError is raised when the value of an argument is not of the expected type.

def multiply():
    try:
        A = 2
        3*a
    except ZeroDivisionError:
        print("division by zero!")
    except SyntaxError:
        print("syntax error!")
    except TypeError:
        print("type error!")
    except ValueError:
        print("value error!")
    except NameError:
        print("name error!")
    else:
        print("No error is raised")

multiply()

# A name error is raised when a variable is not defined.