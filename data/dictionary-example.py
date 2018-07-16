

spanish_english = {
    "hola": "hello",
    "gato": "cat",
    "mujer": "woman"
}

word = spanish_english["hola"]

print(word)
# hello

users = {}

users["Diana"] = 30

print(users)
# {'Diana': 30}

# HAVE THEM DO THIS WITH A TURN AND TALK PARTNER?

prices = {
  "banana": 6,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

for food_item in prices:
  print(food_item)
  print("price: %d" %prices[food_item])
  print("stock: " + str(stock[food_item]))
