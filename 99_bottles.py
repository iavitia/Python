
# while loop
# num = 99
# while num >= 1:
#     print(f'{num} bottles of beer on the wall.')
#     print(f'{num} bottles of beer.')
#     num -= 1
#     if num >= 1:
#         print(f'Take one down, pass it around, {num} bottles of beer on the wall')
#     else:
#         print(f'Take one down, pass it around, no more bottles of beer on the wall')
#     print('*' * 40)

# for loop with range
for num in range(100, 0, -1):
    if num > 1:
        print(f'{num} bottles of beer on the wall.')
        print(f'{num} bottles of beer.')
        print(f'Take one down, pass it around, {num} bottles of beer on the wall')
    else:
        print(f'{num} bottle of beer on the wall.')
        print(f'{num} bottle of beer.')
        print(f'Take one down, pass it around, no more bottles of beer on the wall')
    print('*' * 40)