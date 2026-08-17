import numpy as np

pts = 0
N=1000000

for i in range(N):
    doors = np.array([0,0,1])
    np.random.shuffle(doors)
    choice1 = np.random.randint(0, 3) # This is the first choice
    
    doors = list(doors)
    doors.pop(choice1)
    doors = np.array(doors)
    
    # Now, one of the doors that doesn't hold the prize is revealed
    no_prize = np.where(doors != 1)[0][0]
    doors = list(doors)
    doors.pop(no_prize)
    doors = np.array(doors)
    pts += doors[0]

print(pts/N)