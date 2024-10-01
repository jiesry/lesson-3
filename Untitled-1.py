fruit = int(input("how many fruit do you like: "))
mgafruits = []

for i in range(fruits):
    ask = input("WHAT YOUR FAVORITE FRUIT : ")
    mgafruits.append(ask)
    
    print(mgafruits)
    
    for fruits in mgafruits:
        if fruits == "banana":
            break
        elif fruits =="apple":
            print("HAPPY EATING")