price = 12.3
quantity = 3
total = price * quantity
print("price is {} quantity is {} and total is {}".format(price,quantity,total))
print("quantity is {1} price is {0} and total is {2}".format(price,quantity,total))
print("quantity is {qty} price is {price} and total is {total}".format(price=price, qty=quantity, total=total))

print("Quantity is {:d}".format(quantity))
print("Quantity is {:5d}".format(quantity))
print("Quantity is {:05d}".format(quantity))
