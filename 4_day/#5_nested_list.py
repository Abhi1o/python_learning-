#list in side of list is called nested list.
#Treasure Map 
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do you want to put the treasure? ")
#sepirate input
column = int(position[0])
row = int(position[1])
#selecting row from map list
map_row=map[row-1]
#inserting mark at horizontal
map_row[column-1]="❌"
print(f"{row1}\n{row2}\n{row3}")


#another way to do this thing
#row[column-1]
map[row-1][column-1]= "⭕"


 
































