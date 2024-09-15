from configparser import ConfigParser
import random

config = ConfigParser()
config.read("number.ini")

user = input("Enter your username:")
if user == "Shreya":
    password = input("pasword:")
    if password != "Shreya":
        print("oops! Wrong Password")
        exit(0)

try:
    config_data = config[user]
except:
    print("invalid user!!!")
    exit(0)

number = random.randint(1, int(config_data["digits"]))
max_tries = int(config_data["max_tries"])
tries = 0
done = False

while not done:
    guess = input("guess something")
    if guess == "cheat":
        if "cheat" in config_data.keys() and config_data["cheat"] == "on":
            print(f"You Won!!!! the number was {number}")
            exit(0)
        else:
            print("you are not allowed to cheat!")
            guess = int(input("guess something"))

    else:
        guess = int(guess)

    tries += 1

    if guess == number:
        print("you won")
    else:
        if tries == max_tries:
            print("you lost")
            print(f"the number was {number}")
            exit(0)
        else:
            if guess > number:
                print("too high")
            elif guess < number:
                print("too low")
