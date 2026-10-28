
number = 23

running = True

while running:

    guess = int(input("type num : "))

    if guess == number:
        print("Win")
        running = False

    elif guess < number:
        print("up")
    else:
        print("down")
else:
    print("end")
    print("real end")