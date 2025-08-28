grocery_list = []


for item in grocery_list:
    if item == "no":
     break
else:
 for i in range(5):
    item = input("Enter your item: ")
    if item == "no":
        break
    else:
     grocery_list.append(item)

    print(grocery_list)



