import random
s=input(("\nShall we start the game (y/n): "))
chance=3
count=0
if s=='y':
    print("\nYou have 3 chances")
    while count<3:
        r=random.randint(1,10)
        a=int(input(("\nGuess the number between 1 to 10: ")))
        if a==0 or a>10:   
            print("\n❗❗❗The guessing number should be between 1 to 10 and not 0❗❗❗")
            chance-=1
            if chance==2:
                print(f'\nYou have {chance} guesses left')
            if chance==1:
                print(f'You have only {chance} guess left, Be carefull')
            if chance==0:
                print(f'You have {chance} guess left️')
                print("\n\n\t\tGAME OVER\n\n\n")
        elif a!=r:
            print("\t❗❗❗WRONG GUESS❗❗❗")
            print(f'The correct guess is {r}')
            chance-=1
            if chance==2:
                print(f'You have {chance} guesses left')
            if chance==1:
                print(f'You have only {chance} guess left, Be carefull')
            if chance==0:
                print(f'You have {chance} guess left')
                print("\n\n\t\tGAME OVER\n\n\n")
        elif a==r:
            print("\n\n\t\tWOW!!!Correct guess")
            print("\t\tCongratulations you won the game")
        count+=1
elif s.isdigit==True:
    print("\nPlease select the correct input")
else:
    print("\nGet lost MATHAFAKA")