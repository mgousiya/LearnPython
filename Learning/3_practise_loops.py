""" 
"fruits = ["apple","bannana","grapes"]

for anything in fruits:
    for _ in anything:
        print(_)
    print (anything)" """

""" fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    continue """
  
""" fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) """


""" fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
 """

data = [
    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
]



new_list = []
for item in data:
  new_item = item["brand"]
  new_list.append(new_item)
  print(new_list)