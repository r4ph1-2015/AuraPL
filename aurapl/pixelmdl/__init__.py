import time
def hello():
    print("Hello World!")

def sprint():
    print("What should be printed")
    text = input()

    print("How many times would you like to repeat")
    amount = int(input())  

    for i in range(amount):
        time.sleep(0.05)
        print(text)

def quiz():
    answer1 = input("What is your Name?")
    print("Hello",answer1,",Nice to meet you")
    answer2 = input("What is the capital of Germany")
    if answer2 == "Berlin":
        print("That is correct")
    else:
        print("Incorrect")
    
    answer3 = input("What coding language do you think this module was built in?")
    if answer3 == "Python":
        print("That is correct, Thank you for trying out the Quiz Function")
    else:
        print("Thats is incorrect but Thank you for trying out the Quiz Function...")

def dumby():
    print("9+10=21")

def void():
    print("Welcome to the Void")
    answer4 = input("What do you think the void is?")
    if answer4 == "Nothing":
        print("Thats correct, thank you for trying the void challenge")
    else:
        print("Incorrect, Its Nothing but Thank you for trying the void challenge")

def nothing():
    print("I think you ment Void instead of Nothing")
    answer5 = input("Do you think you meant Void?")
    if answer5 == "Yes":
         void()
    else:
        print("Well Sadly I cant help with that. Try the Void Function instead")
        answer6 = input("Would you like to try the Void Function?")
        if answer6 == "Yes":
             void()
        else:
            print("I cant help yous with that. I will repeat the Nothing Function")
            nothing()

def lol():
    print("This is nothing but a joke")
    answer7 = input("Would you like to try the Nothing Function instead?")
    if answer7 == "Yes":
        print("ok")
        nothing()
    else:
        print("Lets repeat the Lol Function")
        lol()