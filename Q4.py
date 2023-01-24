# Create function to generate data randomly with python standard library
import random
import string


def randgen(count):
    megalist=[str(i) for i in range(10)] + list(string.ascii_lowercase) + list(string.ascii_uppercase) 
    return ["".join(random.choices(megalist,k=10)) for i in range(count)]
    
count=int(input("Enter the number of random words you want to generate: "))
print(randgen(count))    