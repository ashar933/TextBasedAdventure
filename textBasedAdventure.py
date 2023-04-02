#textbased adventure game-Python Mini project.

import random, time, sys, os
from tkinter import *  
from PIL import ImageTk,Image  

def user_input(values): #to take correct input from user
    invalid=True
    ans=""
    q=["quit", "q"]
    while invalid:
        ans=input(">>")
        if ans.isdigit():
            ans=int(ans)
        else:
            ans=ans.lower()
        if ans in values:
            invalid=False
        elif ans in q:
            endgame()
            print("\nEnter your input:", values)
        else:
            if type(values[0]) is int:
                print("\nEnter a valid input:", [i for i in values])
            else:
                print("\nEnter a valid input:", values)
    return ans

def delayprint(str,t=0.02): #prints each character with a time delay
    for i in str:
        #sys.stdout.write(i)
        #sys.stdout.flush()
        print(i,end="",flush=True)
        if i=='\n':
            time.sleep(t+0.3)
        elif i==',':
            time.sleep(t+0.2)
        elif i=='.':
            time.sleep(t+0.3)
        else:
            time.sleep(t)
        
def celebration(bg='0',text='7'):
    for i in range(2):
        os.system("color {0}{1}".format(bg,text))
        time.sleep(.15)
        os.system("color 07")
        time.sleep(.15) 

def cmdcolor(bg='0',text='7'):
    os.system("color {0}{1}".format(bg,text))

def game1(lives):
    print("<<game1>>\n")
    return lives
    
def game2(lives):
    print("<<game2>>\n")
    return lives

def game3(lives): #marbles guess game
    print()
    comp_total=6
    user_total=6
    count=1
    while user_total<12 and user_total>0:
        if user_total==6:
            cmdcolor(1,'f')
        elif user_total>6:
            cmdcolor(2,'f')
        else:
            cmdcolor(4,'f')
        print()
        print("Your marbles=", user_total,"\tComputer marbles=",comp_total)
        print()
        if count%2!=0:  #user guess
            print("Choose no of marbles you bet")
            user_marbles=user_input(range(1,user_total+1))
            comp_marbles=random.choice(range(1,comp_total+1))
            
            print("Guess if comp has odd or even")
            user_choice=user_input(["odd","even",'o','e'])
            if user_choice=='o':
                user_choice="odd"
            elif user_choice=='e':
                user_choice="even"
            
            comp_choice=""
            if comp_marbles in [1,3,5,7,9,11]:
                comp_choice="odd"
            elif comp_marbles in [2,4,6,8,10]:
                comp_choice="even"
            
            print("Computer has", comp_choice, "\tComputer marbles chosen=",comp_marbles)
            print("You have guessed", user_choice, "\tYour marbles wagered=",user_marbles)
            
            if user_choice==comp_choice:
                if user_marbles<=comp_total:
                    print("Computer gives you",user_marbles)
                    user_total=user_total+user_marbles
                    comp_total=comp_total-user_marbles
                elif user_marbles>comp_total:
                    print("Computer gives you",comp_total)
                    user_total=user_total+comp_total
                    comp_total=comp_total-comp_total
            else:
                print("You give computer",user_marbles)
                comp_total=comp_total+user_marbles
                user_total=user_total-user_marbles
            count+=1
        
        elif count%2==0:    #comp guess
            print("Choose no of marbles you keep")
            user_marbles=user_input(range(1,user_total+1))
            if comp_total<6:#<=3
                comp_marbles=random.choice(range(1,comp_total+1))
            else:
                comp_marbles=random.choice(range(1,comp_total-1))
            
            user_choice=""
            if user_marbles in [1,3,5,7,9,11]:
                user_choice="odd"
            elif user_marbles in [2,4,6,8,10]:
                user_choice="even"

            comp_choice=random.choice(["odd","even"])
            if user_total==1:
                comp_choice="odd"

            print("Computer has guessed", comp_choice, "\tComputer marbles wagered=",comp_marbles)
            print("You have", user_choice, "\tYour marbles chosen=",user_marbles)
            
            if user_choice==comp_choice:
                if comp_marbles<=user_total:
                    print("You give computer",comp_marbles)
                    comp_total=comp_total+comp_marbles
                    user_total=user_total-comp_marbles
                elif comp_marbles>user_total:
                    print("You give computer",user_total)
                    comp_total=comp_total+user_total
                    user_total=user_total-user_total
            else:
                print("Computer gives you",comp_marbles)
                user_total=user_total+comp_marbles
                comp_total=comp_total-comp_marbles
            count+=1
    
    if user_total>6:
        cmdcolor(2,'f')
        print("You win!")
    else:
        cmdcolor(4,'f')
        print("You lost a life")
        lives-=1
        if lives>0:
            print("Lives remaining:",lives)
    return lives

def glassgame(lives):
    #round 3 final
    #glass
    celebration(2,'f')
    delayprint("\nGAME MASTER:\"Congratulations!!! You have made it through to the final room.\" \n\n")
    time.sleep(0.5)
    delayprint("\nNow you are going to see a preview of the map of the house.\n")
    time.sleep(1)
    mapprint(140,150,lives,name)
    
    str='''GAME MASTER:\"There is a glass bridge in front of you with 5 pairs of glass stepping stones.
The stepping stones before you are made from one of two types of glass, 
One tempered glass, and the other normal glass.
Only the tempered glass is strong enough to hold your weight
In this game you will guess which of the two tiles is made of tempered glass
And only step on those across the 5 pairs of tiles
But if you choose the normal glass, you will plummet to your death and loose a life.
You may then cross over to the other side safely and finish the game.
Additionally, you have been given 3 marbles.
They make a low pitched "THUD" sound when thrown on the tempered glass
And a high pitched "TING" sound when thrown on the normal glass.
Use these marbles to make it across the bridge safely.\" \n\n\n'''
    delayprint(str)
    time.sleep(1)
    #glassgame
    correct_choice=["right","left"]
    marbles=["marble","m"]
    glass_num=5
    marble=3
    ctr=True
    while glass_num>0 and lives>0:
        print("Enter 'left' or 'right' to choose the step\nNOTE: Enter 'Marble' or 'M' to throw a marble")
        print('(', lives, "LIVES, \t", glass_num, "STEPS LEFT and \t", marble, "MARBLES LEFT", ')')
        glass_choice=user_input(correct_choice+marbles+['l','r'])
        if glass_choice=='r':
            glass_choice="right"
        elif glass_choice=='l':
             glass_choice="left"
         
        if ctr==True:
            random.shuffle(correct_choice)
        if marble>0 and glass_choice in marbles:
            cmdcolor(1,'f')
            print("\nEnter 'left' or 'right' to throw the marble on the step.")
            marble_choice=user_input(correct_choice+['l','r'])
            if marble_choice=='r':
                marble_choice="right"
            elif marble_choice=='l':
                marble_choice="left"
            if marble_choice==correct_choice[0]:
                print("It makes a low pitched THUD sound")
            else:
                print("It makes a high pitched TING sound")
            marble-=1
            print("Marbles left=", marble,"\n")
            ctr=False
           
        if marble==0 and glass_choice in marbles:
            print("You cannot use any more marbles!!!\n\n")
        
        if glass_choice==correct_choice[0]:
            glass_num-=1
            if glass_num!=0:
                cmdcolor(2,'f')
                print("Your guess was CORRECT!\n")
            ctr=True
        elif glass_choice==correct_choice[1]:
            lives-=1
            cmdcolor(4,'f')
            print("Your guess was INCORRECT. You have lost a life.\n")
            ctr=False
        time.sleep(1.5)
    return lives

def mapprint(x,y,lives,name):#to display player's position
    root = Tk()  
    root.title("HOUSE MAP")
    
    canvas = Canvas(root, width = 700, height = 350)  
    canvas.pack()  
    # Opening the primary image (used in background)
    img1 = Image.open(r"map.png")
      
    # Opening the secondary image (overlay image)
    img2 = Image.open(r"playerpos.png")
      
    # Pasting img2 image on top of img1 
    # starting at coordinates (0, 0)
    img1.paste(img2, (x, y), mask = img2)
      
    img = ImageTk.PhotoImage(img1)  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    
    myLabel = Label(root, text ="PLAYER NAME: {0} \t LIVES LEFT: {1}".format(name,lives))
    myLabel.pack() 

    root.mainloop() 
    # round1 584,150
    # round2 370,150
    # round3 140,150

def endgame(): #to quit game
    print("\nAre you sure you want to quit the game?(Y/N)")
    ans_yes=["y","yes"]
    ans_no=["n","no"]
    end=user_input(ans_yes+ans_no)
    if end in ans_yes:
        delayprint("You are now the Game Master's prisoner for life!")
        time.sleep(3)
        clear()
        sys.exit()
    else:
        delayprint("You almost became the Game Master's prisoner! Anyway...")
        
def clear(): #to clear screen
        _ = os.system('cls')


valid=True
clear()
cmdcolor(7,0)
str='''Welcome to the adventure game!
You are in a house and have to complete three rounds of different games
With 5 lives in hand in order to escape it!

NOTE: If you wish to quit the game, input quit or q at any point

But first, what would you like to be called as?\n>>'''
delayprint(str)
name=input()
str='''\nLETS BEGIN in '''
delayprint(str)
time.sleep(0.4)
delayprint("3 2 1",0.5)
time.sleep(0.5)
while valid:
    cmdcolor()
    clear()
    lives=5
    ans_yes=["y","yes"]
    ans_no=["n","no"]
    door_choice1=["d1","d2","d3"]
    door_choice2=["d4","d5"]
    
#round1
    
    str='''You wake up in an empty dark room with no windows and a very high ceiling
There is only a small hole acting as a skylight through which you can see the night sky.
It is very chilly and you have no memory of how you came here but slowly your eyes adjust to the darkness.

Here is a preview of the map of the house.'''
    delayprint(str)
    time.sleep(1)
    mapprint(584,150,lives,name)
    str='''\n\nNow you notice that there are 3 identical doors in front of you.
There is a board in the room that says\n'''
    delayprint(str)
    delayprint("CHOOSE ONE OF THE DOORS\n",0.07)
    time.sleep(1)
    delayprint("Which door do you choose (D1/D2/D3):")
    str='''As you enter the room, you hear a booming voice say:
GAME MASTER:"{0}, You have been chosen to complete a set of tasks for our experiment.
Complete the given tasks and you are free to go never to hear from us again.
You are under constant observation so make sure to not be foolish and make irrational decisions" \n'''.format(name)
    ans_1=user_input(door_choice1)
    random.shuffle(door_choice1)
    delayprint(str)
    if (ans_1==door_choice1[0]): 
        str="GAME MASTER:\"You sure are lucky {0} \nYou have a free pass to the next round and the cost is one of your lives. \nHead on to the next room using the door in front.\"\n\n".format(name)
        delayprint(str)
        lives-=1
        
    elif(ans_1==door_choice1[1]):
        #game1
        lives=game1(lives)
    
    elif(ans_1==door_choice1[2]):
        #game2
        lives=game2(lives)
    
#round 2
    if lives>0:
        celebration('a',0)
        str='''GAME MASTER:\"Congratulations {0}!! You have made it to the second round in the experiment.
Just another few to go, will you make it out of here... Only time will tell.

Here is a preview of your location in the house.\n'''.format(name)
        delayprint(str)
        time.sleep(1)
        mapprint(370,150,lives,name)
        str='''\n\nYou realize that this is a sick game to entertain twisted minds that enjoy watching people suffer in these death matches.
Nevertheless, you just want to get out of this hellhole as fast as possible.

You have entered another room and there are 2 more identical doors in front of you.
You see a board similar to the first one\n'''
        delayprint(str)
        delayprint("CHOOSE ONE OF THE DOORS\n",0.07)
        time.sleep(0.5)
        delayprint("Which door do you choose (d4/d5):")
        ans_1=user_input(door_choice2)
        random.shuffle(door_choice2)
        
        if (ans_1==door_choice2[0]):
            str="\nGAME MASTER:\"You are lucky {0}, You have a free pass to the next round but lose a life! Head on to the next room.\"\n\n".format(name)
            delayprint(str)
            lives-=1
        elif(ans_1==door_choice2[1]):
            #game3
            flag=True
            str='''\n\nYou and a computer have been given 6 marbles each.
In this game you have to wager a certain number of marbles 
And guess whether the opponent has odd or even number of marbles chosen.
If you are right, the loser has to give you the number of marbles wagered.
But if you lose all the wagered marbles have to be given to the opponent.
Each round alternates between you and the computer wagering a given number of marbles.
The goal of the game is to obtain all 12 marbles to advance to the next round.
Remember, every time you fail to do so, You lose a life.\n\n'''
            delayprint(str)
            while lives>0 and flag:
                lifecheck=lives
                lives=game3(lives)
                if lives==lifecheck:
                    flag=False    

#final round
    if lives>0:
        lives=glassgame(lives)        

    #end restart
    if lives>0:
        celebration('a',0)
        str='''\n\nCongratulations {0}!
You have made it across the glass bridge and escaped the house successfully!!\n\n'''.format(name)
        delayprint(str)
    else:
        print("\n\n\n")
        celebration(4,'f')
        print("G    A    M    E      O    V    E    R    ! ! !".center(118))
        delayprint("You have zero lives remaining\n")
        time.sleep(1)
        
    #Game ends
    
    delayprint("\nDo you wish to restart the adventure game? (Yes/No)\n")
    Your_ans=user_input(ans_yes+ans_no)
    if Your_ans in ans_yes:
        delayprint("Alright! The game will restart in a few seconds.\n")
        time.sleep(3)
        valid=True
        
    elif Your_ans in ans_no:
        delayprint("Our journey together ends here.\n\n")
        print("Goodbye!")
        time.sleep(2)
        clear()
        valid=False
