print("Enter Your Shopping")
shopping_list = []
while True:
    name = input("> ")
    if name == 'Done':
        break
    shopping_list.append(name)
    
print("here is your list")

for list in shopping_list:
    print(list)
    