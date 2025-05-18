from customer import Customer
from coffee import Coffee

c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 3.5)
c1.create_order(latte, 4.0)
c2.create_order(latte, 5.0)

print(latte.num_orders())  
print(latte.average_price()) 
print(Customer.most_aficionado(latte))  
