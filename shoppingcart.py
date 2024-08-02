print("WELCOME TO THE USELESS STORE")
print("*" * 30)

item = input("what item are you purchasing:")
price = float(input(f"what is the price of the {item}:"))
quantity = float(input(f"how many {item} are you buying: "))

print(f"added {quantity} {item}(s) to shopping cart")
print(f"subtotal :${quantity*price}")
                       