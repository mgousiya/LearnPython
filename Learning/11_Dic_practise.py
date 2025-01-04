# Consession stand program

menu = {"Biryani": 300,
        "kebab"  : 250,
        "dessert": 280,
        "softdrink": 80,
        "mandi": 450,
        "icecream":120}

cart = []
total = 0

print("-------MENU------")
for key, value in menu.items():
   print(f"{key:20}:{value:.2f}")
print("---------------------")

while True:
   food = input("Select your food(q to quit): ").lower()
   if food == "q":
       break
   elif menu.get(food) is not None:
      cart.append(food)


for food in cart:
   total  +=  menu.get(food)
print(f"selected food is {cart} total is: ${total: .2f}")
      




