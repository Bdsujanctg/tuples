class employee:
    def __init__(self):
        print("Employee creator")
    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Making object...")
    obj=employee()
    print("Functions end")
    return obj
print("Calling object function")
obj= create_obj()
print("Program end")
