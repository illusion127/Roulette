# roulette
import random
import time
a = 0
bet = 0
bet2 = 0
bet3 = 0
bet4 = 0
bet2a = 0
bet3a = 0
bet4a = 0
list1 = []
blacknumbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36]
rednumbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
nspin = 0
bankbalance = 20000

def numtocolour():
    if spin in blacknumbers:
        A = "black"
        return A
    elif spin == 0:
        A = "green"
        return A
    elif spin in rednumbers:
        A = "red"
        return A

def bust(bankbalance):
    if bankbalance <= 0:
        print("you went bust, try again :(")
        exit()
        bust1 = True
        return bust1
    else:
        pass

def menu():
    print()
    print("This is a roulette game")
    print("you can win money by betting on the number that is landed on.")
    print("you start of with £20000\n")

def menu2(bet, bet2, bet3, bet4, bankbalance):
    if bankbalance - (bet + bet2 + bet3 + bet4) == 0:
        print("You have no more money to bet")
        print("Please press 6 to start the spin")
        menu_choice = int(input(": "))
        return menu_choice
    else:
        print("Your remaining bank balance is £", bankbalance - (bet + bet2 + bet3 + bet4))
        print("to pick individual numbers press 1")
        print("to pick a colour group press 2")
        print("to pick a section of 12 press 3")
        print("to pick odd or evens press 4")
        print("to see the payout menu press 5")
        print("press 6 to start the spin")
        menu_choice = int(input(": "))
        return menu_choice

def menu3():
    print()
    print("If you want to bet the same and on the same things type 'same'")
    print("If you want to change your bets and choices type 'change'")
    print("If you want to close out of the program type 'exit'")

def payoutmenu():
    print("The payouts for winning are as follows:")
    print("Individual number: 35:1")
    print("Even/Odd: 1:1")
    print("Black/Red: 1:1")
    print("Dozen: 2:1\n")

def odd_or_even(bet, bet2, bet3):
    dogo = True
    while dogo:
        choice1 = str(input("if you want to pick all of the odd numbers type 'odd' and 'even' to bet on the even ones, if not type 'no': "))
        if choice1 == "no":
            print("ok")
            dogo = False
        elif choice1 == "odd":
            bet4a = "odd"
            loop5 = True
            while loop5:
                bet4 = int(input("how many pounds do you want to bet on it: "))
                if bet4 < 0:
                    print("Please put a positive number smart-arse")
                    bet4 = 0
                elif bet4 > bankbalance - (bet + bet2 + bet3):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet2 + bet3) + 1)
                    bet4 = 0
                else:
                    loop5 = False
                    return bet4, bet4a
            dogo = False
        elif choice1 == "even":
            bet4a = "even"
            loop5 = True
            while loop5:
                bet4 = int(input("how many pounds do you want to bet on it: "))
                if bet4 < 0:
                    print("Please put a positive number smart-arse")
                    bet4 = 0
                elif bet4 > bankbalance - (bet + bet2 + bet3):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet2 + bet3) + 1)
                    bet4 = 0
                else:
                    loop5 = False
                    return bet4, bet4a
            dogo = False
        else:
            print("please put in one of the options above")


def groups_of_twelves(bet, bet2, bet4):
    doggy = True
    while doggy:
        oe = str(input("Type 'first' to pick the 1st 12 numbers, 'second' for the 2nd 12, 'third' for the 3rd and 'no' if you don't want to: "))
        if oe == "no":
            print("ok")
            doggy = False
        elif oe == "first":
            bet3a = "first"
            loop4 = True
            while loop4:
                bet3 = int(input("how many pounds do you want to bet on it: "))
                if bet3 < 0:
                    print("Please put a positive number smart-arse")
                    bet3 = 0
                elif bet3 > bankbalance - (bet + bet2 + bet4):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet2 + bet4) + 1)
                    bet3 = 0
                else:
                    loop4 = False
                    return bet3, bet3a
            doggy = False
        elif oe == "second":
            bet3a = "second"
            loop4 = True
            while loop4:
                bet3 = int(input("how many pounds do you want to bet on it: "))
                if bet3 < 0:
                    print("Please put a positive number smart-arse")
                    bet3 = 0
                elif bet3 > bankbalance - (bet + bet2 + bet4):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet2 + bet4) + 1)
                    bet3 = 0
                else:
                    loop4 = False
                    return bet3, bet3a
            doggy = False
        elif oe == "third":
            bet3a = "third"
            loop4 = True
            while loop4:
                bet3 = int(input("how many pounds do you want to bet on it: "))
                if bet3 < 0:
                    print("Please put a positive number smart-arse")
                    bet3 = 0
                elif bet3 > bankbalance - (bet + bet2 + bet4):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet2 + bet4) + 1)
                    bet3 = 0
                else:
                    loop4 = False
                    return bet3, bet3a
            doggy = False
        else:
            print("please put in one of the options above")

def numbers(bet2, bet3, bet4):
    dog = True
    while dog:
        table = int(input("input the number (between 0 & 36) you want to bet on: \n"))
        if table <= 36 and table >= 0:
            list1.append(table)
            repeat = str(input("Type 'yes' to pick on another number and type 'no': "))
            if repeat == 'yes':
                print()
            else:
                dog = False
                doge = True
                while doge:
                    bet = int(input("how many pounds do you want to bet on each one?: "))
                    if bet < 0:
                        print("Please put a positive number smart-arse")
                        bet = 0
                    elif bet > bankbalance - (bet2 + bet3 + bet4):
                        print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet2 + bet3 + bet4) + 1)
                        bet = 0
                    else:
                        bet = bet * len(list1)
                        doge = False
                        return bet, list1
        elif table > 36 or table < 0:
            print("please put in a number between 0 and 36")

def colours(bet, bet3, bet4):
    dog = True
    while dog:
        colour = str(input("if you want to bet on all of either red, or black type the colour, if not type 'no': "))
        if colour == "no":
            print("ok")
            dog = False
        elif colour == "red":
            bet2a = "red"
            loop2 = True
            while loop2:
                bet2 = int(input("how many pounds do you want to bet on it: "))
                if bet2 < 0:
                    print("Please put a positive number smart-arse")
                    bet2 = 0
                elif bet2 > bankbalance - (bet + bet3 + bet4):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet3 + bet4) + 1)
                    bet2 = 0
                else:
                    loop2 = False
                    return bet2, bet2a
            dog = False
        elif colour == "black":
            bet2a = "black"
            loop2 = True
            while loop2:
                bet2 = int(input("how many pounds do you want to bet on it: "))
                if bet2 < 0:
                    print("Please put a positive number smart-arse")
                    bet2 = 0
                elif bet2 > bankbalance - (bet + bet3 + bet4):
                    print("Sorry, you don't have that much money, please put a number less than £", bankbalance - (bet + bet3 + bet4) + 1)
                    bet2 = 0
                else:
                    loop2 = False
                    return bet2, bet2a
            dog = False
        else:
            print("please put in one of the options above")

# Start of Run
menu()
Run = True
while Run:
    # Bet menu
    loop3 = True
    while loop3:
        menu_choice = menu2(bet, bet2, bet3, bet4, bankbalance)
        if 0 < menu_choice < 7:
            if menu_choice == 1:
                bet, list1 = numbers(bet2, bet3, bet4)
            elif menu_choice == 2:
                bet2, bet2a = colours(bet, bet3, bet4)
            elif menu_choice == 3:
                bet3, bet3a = groups_of_twelves(bet, bet2, bet4)
            elif menu_choice == 4:
                bet4, bet4a = odd_or_even(bet, bet2, bet3)
            elif menu_choice == 5:
                payoutmenu()
            else:
                print("SPINNING...\n")
                time.sleep(2)
                loop3 = False
        else:
            print("please put in a number between or equal to 1 and 6")

    loop = True
    while loop:
        # taking of money
        bankbalance = bankbalance - (bet + bet2 + bet3 + bet4)
        # random spinner
        spin = random.randint(0,36)
        # giving num a colour
        A = numtocolour()
        # checking for winners
        if A == bet2a:
            bankbalance = bankbalance + (bet2 * 2)
            print("You won £",(bet2 * 2),"on",A)
        elif spin in list1:
            bankbalance = bankbalance + (bet * 35)
            print("You won £",(bet * 35),"on",A,spin)
        elif (bet3a == "first" and 1 <= spin <= 12) or (bet3a == "second" and 13 <= spin <= 24) or (bet3a == "third" and 25 <= spin <= 36):
            print("You won £",(bet3 * 3),"on",A,spin,"as it was in the",bet3a,"group of 12")
            bankbalance += (bet3 * 3)
        elif bet4a == "odd" or "even":
            if spin % 2 == 0 and (bet4a == "even"):
                bankbalance = bankbalance + (bet4 * 2)
                print("You won £",bet4 * 2,"on",A,spin,"as it was",bet4a)
            elif (spin % 2 != 0) and (bet4a == "odd"):
                bankbalance = bankbalance + (bet4 * 2)
                print("You won £", bet4 * 2, "on", A, spin, "as it was", bet4a)
            else:
                print("Sorry, the ball landed on", A, spin, ", You lose :(")
                bust1 = bust(bankbalance)
                if bust1 == True:
                    Run = False
                    loop = False
        else:
            print("Sorry, the ball landed on",A,spin,", You lose :(")
            bust1 = bust(bankbalance)
        print("Your bank balance now is: £",bankbalance)
        # asking for loop
        menu3()
        menu3_ans = str(input(": "))
        if menu3_ans == "same":
            print("spinning...")
            time.sleep(2)
        elif menu3_ans == "change":
            bet = 0
            bet2 = 0
            bet3 = 0
            bet4 = 0
            bet2a = 0
            bet3a = 0
            bet4a = 0
            list1 = []
            loop = False
        else:
            print("Bye :(")
            loop = False
            Run = False
