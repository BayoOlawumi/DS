

"""my_list=[]
for num in range(1,101):
    if num % 3 == 0:
        my_list.append(num)
print(my_list)"""

"""fav_foods = ['beans','yam','bread']
my_list =[food[0].upper() for food in fav_foods]
print(my_list)"""




products_and_price = {'rice': 300, 'beans': 500, 'yam':700}
print("You are welcome to our resturant ")
country = input("Enter your country ").lower()
shopping_status = True
products =[]
# Products Purchase
while shopping_status:
    product_name =input("Enter the product you want to buy ").lower()
    products.append(product_name)
    status = input("Do you want to keep on shooping")
    if status =='yes':
        shopping_status = True
    else:
        shopping_status =False

    
# Product valuation in relation with price

total_cost = 0
for product in products:
    if product in products_and_price.keys():
        total_cost = total_cost + products_and_price[product]

# Shipping fee addition
if country =='nigeria':
    total_cost += 60

elif country =='ghana':
    total_cost += 50

else:
    total_cost+=100


print(f'Your total balance plus shipping fee is {total_cost} dollars')













