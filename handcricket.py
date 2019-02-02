import random
n_balls=int(input("ENTER NUMBER of balls to be played: "))
n_wickets=int(input("ENTER NUMBER OF WICKETS: "))

print("No of balls to be played = ",n_balls)
score=[]
while(n_balls>0 and n_wickets>0):
    print("ENTER RUNS (0-6)")
    p1=int(input())
    r=random.randint(0,6)
    if(p1 in range(0,7)):
        print("Player 1 = ",p1)
        print("Random Bot = ", r)
        if(r==p1):
            print("HOWAZZATTT")
            n_wickets-=1
        else:
            score.append(p1)
            print("Score = ",sum(score)," with ",n_balls," remaining and ",n_wickets," wickets in hand")
    else:
        print("ERROR, ONLY 0-6 runs allowed")
    n_balls-=1

