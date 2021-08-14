def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, tell me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("Are you in love programming (yes/no)?")
    ans=str(input())
    if ans=="yes":
        print("You are my friend")
        print("Why do we use methods?")
        print("1. To repeat a statement multiple times.")
        print("2. To decompose a program into several small subroutines.")
        print("3. To determine the execution time of a program.")
        print("4. To interrupt the execution of a program.")
        while True:
            n = int(input())
            if n != 2:
                print("Please, try again")
            else:
                print("Completed, have a nice day!")
                break
        print('Completed, have a nice day!')
    elif ans=="no":
        print("No problem we can talk other topics")
    else:
        print("please enter ans in yes or no")
def end():
    print('Congratulations, have a nice day!')


greet('RESH', '2020')  # change it as you need
remind_name()
age()
count()
test()
end()
