# "What's your name?"
# "Hello XY, I am your phone book."
# "How old are you?"
# - "You are so young! Life is ahead of you!"
# - "That's a nice age!"
# - "You must be very wise!"
# - "That doesn't seem to be an integer."
print("What's your name?")
name = input()
print(f"Hello {name}, I am your phone book.")
print(f"How old are you {name}?")
while True:
    try:
        age = int(input())
    except ValueError: 
        print("That doesn't seem to be an integer, mate.")
        continue
    else:
        break
if age <= 18:
    print("You are so young! Life is ahead of you!")
elif age > 18 and age < 40:
    print("That's a nice age, bro!")
elif age >= 40:
    print("You must be very wise, bro!")
