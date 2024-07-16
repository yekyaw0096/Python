price = 12.3
quantity = 3
total = price * quantity
print("price is {} quantity is {} and total is {}".format(price,quantity,total))
print("quantity is {1} price is {0} and total is {2}".format(price,quantity,total))
print("quantity is {qty} price is {price} and total is {total}".format(price=price, qty=quantity, total=total))

print("Quantity is {:d}".format(quantity))#:d is decimal
print("Quantity is {:5d}".format(quantity))
print("Quantity is {:05d}".format(quantity))

print("Total is {:f}".format(total))#:f is float
print("Total is {:.2f}".format(total))#2 decimal
print("Total is {:7.2f}".format(total))#total length=7
print("Total is {:07.2f}".format(total))#start filled with 0

print("Quantity is binary is {:b}".format(quantity))
print("Quantity is octal is {:o}".format(quantity))
print("Quantity is hexa is {:x}".format(quantity))

print("{:5d}".format(18))
print("{:<5d}".format(18))#left aligned
print("{:>5d}".format(18))#right aligned