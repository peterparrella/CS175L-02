#CS175L-02
#PeterParrella
#restaurant

vegetarian=False
vegan=False
gluten_free=False

response_1= input("is anyone in your party a vegetarian?: ")

if response_1 == "Yes":
    vegetarian = True

response_2= input("Is anyone in your party a vegan?: ")

if response_2 == "Yes":
    vegan = True

response_3= input("Is anyone in your party gluten free?: ")

if response_3 == "Yes":
    gluten_free = True

print("Here are your restaurant choices:" )

if not vegetarian and not vegan and not gluten_free == True:
    print("Joe's Gourmet Burgers' ")

if not vegan and not gluten_free == True:
    print("Mama's Fine Italian ")

if not vegan == True:
    print("Main Street Pizza ")
    print("Corner Cafe")
    print("Chef's Kitchen")
    

