#KITE FLYING GAME
import random
import turtle
import winsound
#fly,kite1:kite of player that is playing,turtle of the kite
#gotcut,kite2:kite of the other player,turtle of the kite
#name1:player that is playing
#name2:the other player
def fly(flying,gotcut,name1,name2,kite1,kite2):
    h=0
    h=random.randrange(10,100,5)
    flying+=h
    kite1.fd((h/5))
    if(flying==gotcut):
     kite2.bk((gotcut/5))
     gotcut=0
     winsound.Beep(freq,dur)
     winsound.Beep(freq, dur)
     print(name1,"cut",name2,"'s kite")
     print(name2,"'s kite is at",gotcut)
    return flying,gotcut
#disrupted,kite1:kite which got disrupted ,turtle of the kite
#gotcut,kite2:kite of the other player,turtle of the kite
#name1:player whose kite got disrupted
#name2:the other player
def wind(disrupted,gotcut,name1,name2,kite1,kite2):
    winsound.Beep(freq, dur)
    print(name1,"'s Kite was disrupted by the wind")
    w=0
    w=random.randrange(5,50,5)
    disrupted-=w
    kite1.bk((w/5))
    if(disrupted==gotcut):
     kite2.bk((gotcut/5))
     gotcut=0
     winsound.Beep(freq, dur)
     winsound.Beep(freq, dur)
     print(name1,"cut",name2,"'s kite")
     print(name2,"'s kite is at",gotcut)
    return disrupted,gotcut
#name1:Name of player who is still playing
#kite:kite of that player
#kite1:turtke of that player
def left(name1,kite,kite1):
    for i in range(3):
       h=0
       h=random.randrange(10,100,5)
       kite+=h
       kite1.fd((h/5))
       print(name1,"is now at",kite)
    return kite
#Boost,kite1:kite of player that chose to use the booster,turtle of the kite
#gotcut,kite2:kite of the other player,turtle of the kite
#name1:player that chose to use the booster
#name2:the other player
#B:no. of booster with the person who choose to use booster
def booster(Boost,gotcut,name1,name2,kite1,kite2,B):
    if(B>0):
     B-=1
     print(B,"Boosters left with",name1)
     b=0
     b=random.randrange(100,200,5)
     Boost+=b
     kite1.fd((b/5))
     print(name1,"is now at",Boost)
     if(Boost==gotcut):
      kite2.bk((gotcut/5))
      gotcut=0
      winsound.Beep(freq,dur)
      winsound.Beep(freq, dur)
      print(name1,"cut",name2,"'s kite")
      print(name2,"'s kite is at",gotcut)
      
    while(B<=0):
        print("You ran out of boosters")
        break
    return Boost,gotcut,B

freq=700
dur=500

    
H1=H2=K1=K2=KS1=KS2=try1=try2=0
B1=B2=3

k1=turtle.Turtle()
k2=turtle.Turtle()
k1.shape("square")
k2.shape("square")
k1.color("lightblue")
k1.fd(30)
k1.color("green")
k2.color("red")
sc=turtle.Screen()
sc.bgcolor("lightblue")
sc.title("sky")
k1.setheading(90)
k2.setheading(90)
print("Player one is green while player two is red")
k1.fd(160)
k2.fd(160)
k1.bk(320)
k2.bk(320)

P1=input("Enter player 1's name")
P2=input("Enter player 2's name")
print("1 for yes and 0 for no and 2 for using a booster")
print(P1,"Ready to play ?")
choice1=int(input())
print(P2,"Ready to play?")
choice2=int(input())
while(K1<1600 and K2<1600):
 if(choice1==0 and choice2==0):
     break
 while((choice1==1 or choice2==1 or choice2==0 or choice1==0 or choice1==2 or choice2==2)and (try1==0 and try2==0)):
    if(K1>1600 or K2>1600):
        break

    #BOTH THE PLAYERS CHOOSE BOOSTER
    elif(choice1==2 and choice2==2):
        K1,K2,B1=booster(K1,K2,P1,P2,k1,k2,B1)
        print(P1,"'s new height is",K1)
        if(K1%50==0 and K1!=0):
           K1,K2=wind(K1,K2,P1,P2,k1,k2)
        K2,K1,B2=booster(K2,K1,P2,P1,k2,k1,B2)
        print(P2,"'s new height is",K2)
        if(K2%50==0 and K1!=0):
           K2,K1=wind(K2,K1,P2,P1,k2,k1)
    #PLAYER 1 chooses booster      
    elif(choice1==2 and choice2==1):
        K1,K2,B1=booster(K1,K2,P1,P2,k1,k2,B1)
        if(K1%50==0 and K1!=0):
           K1,K2=wind(K1,K2,P1,P2,k1,k2)
           print(P1,"'s new height is",K1)
        K2,K1=fly(K2,K1,P2,P1,k2,k1)
        if(K2%50==0 and K1!=0):
           K2,K1=wind(K2,K1,P2,P1,k2,k1)
           print(P2,"'s new height is",K2)
    #PLAYER 2 chooses booster
    elif(choice1==1 and choice2==2):
        K2,K1,B2=booster(K2,K1,P2,P1,k2,k1,B2)
        if(K2%50==0 and K1!=0):
           K2,K1=wind(K2,K1,P2,P1,k2,k1)
           print(P2,"'s new height is",K2)
        K1,K2=fly(K1,K2,P1,P2,k1,k2)
        if(K1%50==0 and K1!=0):
           K1,K2=wind(K1,K2,P1,P2,k1,k2)
           print(P1,"'s new height is",K1)
        print(P1,"'s kite is at",K1,"height")
        print(P2,"'s kite is at",K2,"height")
    
    #Both the players are playing
    elif(choice1==1 and choice2==1):
       K1,K2=fly(K1,K2,P1,P2,k1,k2)
       print(P1,"'s kite is at",K1,"height")   
       if(K1%50==0 and K1!=0):
           K1,K2=wind(K1,K2,P1,P2,k1,k2)
           print(P1,"'s new height is",K1)          
       K2,K1=fly(K2,K1,P2,P1,k2,k1) 
       print(P2,"'s kite is at",K2,"height")
       if(K2%50==0 and K1!=0):
           K2,K1=wind(K2,K1,P2,P1,k2,k1)
           print(P2,"'s new height is",K2)
     ###After one player leaves
           ##the other player cannot use boosters
           #the game will end after giving the other player boost of three turns
           
    elif(choice1==2 and choice2==0):
        print("You can not use boosters once the other player has left")
        try1=1
        K1=left(P1,K1,k1)
        break
    
    elif(choice1==0 and choice2==2):
        print("You can not use boosters once the other player has left")
        choice2==1
        try2=1
        K2=left(P2,K2,k2)
        break
    
    elif(choice1==1 and choice2==0):
       try1=1
       K1=left(P1,K1,k1)
       break
    
    elif(choice1==0 and choice2==1):
       try2=1
       K2=left(P2,K2,k2)
       break
    
    else:
      break
    
    #to choose the option
    
    print(P1,"Enter choice")
    choice1=int(input())
    print(P2,"Enter choice")
    choice2=int(input())
 else:
     break

#result
    
print(P1,"'s kite is at",K1,"height")
print(P2,"'s kite is at",K2,"height")
winsound.Beep(freq, dur)
winsound.Beep(freq, dur)
winsound.Beep(freq, dur)
winsound.Beep(freq, dur)
winsound.Beep(freq, dur)
if(K1==K2):
    print("Its a tie")
elif(K1>K2):
    print(P1,"Won")
elif(K2>K1):
    print(P2,"Won")
