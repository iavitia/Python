print(
'''
WELCOME TO OUR USELESS STORE!
*****************************'''
)

item = input('What item are you purchasing? ')
price = float(input(f'What is the price for 1 {item}? '))
quantity = int(input(f'How many {item} are you buying? '))

print(f'\nAdded {quantity} {item}(s) to shopping cart')
subtotal = price * quantity
print(f'Subtotal: {subtotal}')