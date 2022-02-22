def funct_name():
    print("abc")

def greet(name, age):
    print(f"hi {name} your age is {age}")

def getFirstName(name):
    if(name!=""):
        return name.split(" ")[0]


funct_name()
greet('Suman Manna',25)
print(getFirstName('Suman Manna'))