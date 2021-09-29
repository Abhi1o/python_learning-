# add of all even number 
total=0
for even in range(0,101,2):
    total+=even
    print(f"{even} + " ,end=" ")

print("\n")
print(total)


#second method to so

total2=0
for even in range(1,101):
    if even % 2 ==0:
        total2 +=even

print(total2)
