# def hello(name,age):
#     year=2022-age
#     # print("welcome to AkiraChix")
#     # return
#     return f"Hello {name}, you were born in {year}"
# greetings=hello("Effence",21)

def my_country(country="Uganda", student="susan"):
    return f"Hello {student} you are from {country}"

def greet_multiples(*names):
    for name in names:
        print(f"Hello {name}")

# write a function that accepts any number of
#  an integer and returns the sum of all of them
def add(*numbers):
    n=0
    for number in numbers:
      n+=number
    return n

def multiply(*numbers):
    n=1
    for number in numbers:
        n*=number
    return n

# def greet_multiples(**kwargs):
#     print(kwargs)
#     print(kwargs.keys())
#     print(kwargs.values())

def characters(**kwargs):
    keys=kwargs.keys
    if "country" in keys:
        print (f"Hello {kwargs['name']} you are from {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs["age"]
        print(f"Hello {kwargs['name']} you were born in {year}")
    elif not kwargs:
        print (f"Hello Anonymous")

def sum_and_characters(*args,**kwargs):

        sum=0
        for num in args:
         sum+=num
        keys=kwargs.keys()

        if "name" in keys:
             print(f"Hello {kwargs['name']}, the answer is {sum}")

        elif "country" in keys:
          print(f"Hello from {kwargs['country']}, the answer is {sum}")

        elif not kwargs:
          print(f"Hello anonymus the answer is {sum}")





    

