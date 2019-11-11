# a program generate a lottor winner 
play=int(input("please enter you lucky number"))
print("Your number is ")
print(play)
winNumber_1=12
winNumber_2=21

if play == winNumber_1:
    print("congratulation you have an exact match, you win R10 000.00")
elif play ==winNumber_2: 
    print("congratulation you have an exact match, you win R5 000.0")
elif play ==1 or play == 2 :
    print("congratulation you have one correct digit; you win R1 000.0")


else:
    print("sorry no match")
