ingredients = {"huevos", 'leche', 'queso'}




input_user = input("Enter the ingredients you have: ")
user_ingredients = set(input_user.split(", "))

missing_ingredients = ingredients - user_ingredients


if missing_ingredients :
    print("Te faltan estos ingredientss:", " - ".join(missing_ingredients))
else:
    print("You have all the ingredients needed")