fruit = ["Grapes", "Mango", "Berry", "Watermelon", "Peach"]
print("The fruit:" + ", ".join(fruit))
print("the first:",fruit[0])
print("the last:",fruit[-1])
fruit[1] = "Mango"
fruit.insert(2, "Watermelon")
enter_fruit = input("Enter a fruit name: ")
if enter_fruit  in fruit:
    print("Yes available")
else:
    print("No available")
