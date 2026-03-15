
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for char in word:
    print(char)

# Write a while loop that does the same thing!
num = 0;
while num < len(word):
    print(word[num])
    num += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
num2 = 100
while num2 <= 140:
    print(num2)
    num2 += 2
    
# Write a for loop that does the same thing (with range())
for num3 in range(100, 142, 2):
    print(num3)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
user_input = ''
while user_input != 'sillygoose':
    user_input = input('Enter the passphrase: ').lower()
