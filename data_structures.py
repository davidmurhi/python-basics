fruits = ["apple", "banna", "orange", "mango"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[-1])

fruits.append("grape")
print(fruits)

fruits.remove("orange")
print(fruits)

print("How many fruits", len(fruits))

for fruit in fruits:
    print("I like", fruit)

person = {
    "name": "David",
    "age": 21,
    "city": "Brisbane",
    "is_student": True
}

print(person)
print(person["name"])
print(person["city"])

person["email"] = "ddavidmurhi@gmail.com"
print(person)

person["age"] = 22
print(person["age"])

del person["is_student"]
print(person)

car = {
    "make": "hyundai",
    "model": "i20",
    "year": 2014,
    "price": 15590
}

print(car["make"])
print(car["price"])
