#love calculator using upper case and count
name1=input("enter your name: ")
name2=input("enter friend name: ")
#combine both name 
combine_name=name1+name2
lower_case = combine_name.lower()
#true & love alphabate count in name
t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
print(type(e))

# add all values of true

true = t+r+u+e

# add all values of love

love = l+o+v+e

love_score=int(str(true)+str(love))

if love_score<=10 or love_score>=90:
    print(f"your score is {love_score}, you go together like coke and mentos")

elif love_score>=40 and  love_score<=50:
    print(f"your score is {love_score}, you are together always")
else:
    print(f"your score is {love_score}")



