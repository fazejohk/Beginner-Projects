import random
data=str(input("Rock(r) Paper (p) Scissors(s): "))
randi=random.randint(1,3)
dicrand={1:"Rock", 2:"Paper", 3:"Scissors"}
datafull=dicrand[randi]
#NOT WORKING CURRENTLY
if data=="r" > datafull=="Scissors":
    print ("HUMAN")
elif data=="p" > datafull=="Rock":
    print("HUMAN")
elif data=="s" > datafull=="Paper":
    print("HUMAN")
elif data=="r" < datafull=="Paper":
    print ("AI")
elif data=="p" < datafull=="Scissors":
    print("AI")
elif data=="s" < datafull=="Rock":
    print("AI")
else:
    pass
