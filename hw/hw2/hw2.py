#hw2 of CIT590 v2 copyrig reserved 9/18/2017
#Quankang Wang
#UID:54162826.
#finised all by myself

#import random module
import random

#first turn of game play first to make sure the is_game_over runs after the human move according to the instruction
def main():
    computer_score=0
    human_score=0
    instructions()
    computer_score+=computer_move(computer_score,human_score)
    human_score+=human_move(computer_score,human_score)
    while not(is_game_over(computer_score,human_score)):
        computer_score+=computer_move(computer_score,human_score)
        human_score+=human_move(computer_score,human_score)
    show_results(computer_score,human_score)

#instruction
def instructions():
    print("=======instructions======\nthis game goes between you and the computer in turns\nboth players rolls till the dice is 6 or end manually\nyou can choose when to end while computer is ending randomly\nthe one reaches 50 wins the game, you will give another shot after\nthe computer reach 50 and who gets greater point who wins, if ties,another turn\
    \n=======game starts======")

#human move return total numbers
def human_move(computer_score, human_score):
    if computer_score>human_score:
        print("computer score is ",computer_score,",human score is ",human_score,",you are",(computer_score-human_score),"points behind")
    elif computer_score<= human_score:
        print("computer score is ",computer_score,",human score is ",human_score,",you are",(0-computer_score+human_score),"points ahead")
    temp_scoresum=0
    while True:
        temp_score=0
        if ask_yes_or_no("Roll again?"):
            temp_score=roll()
            print("human rolls",temp_score)
            if temp_score==6:
                print("human rolls 6 and end this turn")
                return 0
            elif temp_score!=6:
                temp_scoresum+=temp_score
                if human_score+temp_scoresum>=50:
                    print("human reaches 50")
                    break
        else:
            break
    return temp_scoresum

#computer most likely to roll(70%),if he is behind human, he will rolls.
def com_another_turn(computer_score,human_move):
    if (computer_score - human_move)<0: #can change the threshold here
        return True
    elif random.randint(1,10)>3:
        return True
    else:
        print("computer choose to stop")
        return False

#same as people's move
def computer_move(computer_score, human_score):
    temp_scoresum=0
    while True:
        temp_score=0
        if com_another_turn(computer_score,human_score):
            temp_score=roll()
            print("computer rolls",temp_score)
            if temp_score ==6:
                print("computer rolls 6 and end this turn")
                return 0
            elif temp_score != 6:
                temp_scoresum+=temp_score
                if computer_score+temp_scoresum>=50:
                    print("computer reaches 50")
                    break
        else:
            break
    return temp_scoresum

#check whether it is over 50
def is_game_over(computer_score, human_score):
    if computer_score>=50 or human_score>=50:
        if computer_score == human_score:
            return False
        else:
            return True
    else:
        return False

#roll
def roll():
    return random.randint(1,6)

#return after y/n, if wrong character return to itself
def ask_yes_or_no(prompt):
    input_tempt=input(prompt+"\ny or Y for yes, n or N for no")
    if input_tempt=="y" or input_tempt == "Y":
        return True
    elif input_tempt=="n" or input_tempt =="N":
        return False
    else:
        return ask_yes_or_no("input wrong charactor")

#compaire the two parameter to show results
def show_results(computer_score, human_score):
    if computer_score>human_score:
        print("computer wins by",(computer_score-human_score))
    elif human_score>computer_score:
        print("human wins by",(human_score-computer_score))



#entrance
if __name__ =="__main__":
    main()
