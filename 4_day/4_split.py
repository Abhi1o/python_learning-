#split string method
import random
name_string=input("Give me everybody's names, seperated by a comma.: ")
#split input values in list
name=name_string.split(", ")
print(type(name))
#count the length of list
count=len(name)
#pick any random name from list
randon_num=random.randint(0,count-1)
#using choice function
print(random.choice(name)+" is going to buy the meal today")
#DIY
person=(name[randon_num])
print(person + " is going to buy the meal today")
