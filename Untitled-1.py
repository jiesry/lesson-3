fruit = int(input("how many fruit do you like: "))
mgafruits = []

for i in range(fruit):
    ask = input("WHAT YOUR FAVORITE FRUIT : ")
    mgafruits.append(ask)
    
    if ask == "banana":
        break
    elif ask == "apple":
        print("happy eating")

print(mgafruits)

       