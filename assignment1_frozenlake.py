fl_mdp = dict()
for state in range(0,16):
    fl_mdp[state]=dict()
    if state==0 :
        fl_mdp[state]={
            "up" :
            [
                (2/3, 0, 0, False),
                (1/3, 1, 0,False),
            ],
            "down" : 
            [
                (1/3, 0, 0, False),
                (1/3, 1, 0, False),
                (1/3, 4, 0, False),
            ],
            "left" : 
            [
                (2/3, 0, 0, False),
                (1/3, 4, 0,False),   
            ],
            "right" :
            [
                (1/3, 0, 0, False),
                (1/3, 1, 0, False),
                (1/3, 4, 0, False),
            ],
        }
    elif state==3 :
        fl_mdp[state]={
            "up" :
            [
                (2/3, 3, 0, False),
                (1/3, 2, 0,False),
            ],
               "down" : 
            [
                (1/3, 3, 0, False),
                (1/3, 2, 0, False),
                (1/3, 7, 0, False),
            ],
            "left" : 
            [
                (1/3, 2, 0, False),
                (1/3, 3, 0, False),
                (1/3, 7, 0, False),   
            ],
            "right" :
            [
                (2/3, 3, 0, False),
                (1/3, 7, 0, False),
            ],
        }
    elif state==14 :
        fl_mdp[state]={
            "up" :
            [ 
                (1/3, 10, 0, False),
                (1/3, 13, 0, False),
                (1/3, 15, 1, True),
            ],
            "down" :
            [ 
                (1/3, 14, 0, False),
                (1/3, 13, 0, False),
                (1/3, 15, 1, True),
            ],
            "left" :
            [ 
                (1/3, 14, 0,False),
                (1/3, 13, 0, False),
                (1/3, 10, 0, False),
            ],
            "right" :
            [ 
                (1/3, 14, 0, False),
                (1/3, 10, 0, False),
                (1/3, 15, 1, True),
            ],
        }
    elif state==5 or state==7 or state==11 or state==12 or state==15 :
        for action in ["up","down","left","right"]:
            fl_mdp[state][action]=[
                (1, state, 0, True),
            ],
    elif state==2 or state==1 :
        fl_mdp[state]={
            "up" :
            [ 
                (1/3, state, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state-1, 0, False),
            ],           
            "down" :
            [ 
                (1/3, state+4, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state-1, 0 ,False),
            ],
            "left" :
            [ 
                (1/3, state, 0, False),
                (1/3, state-1, 0, False),
                (1/3, state+4, 0, False),
            ],
            "right" :
            [ 
                (1/3, state, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state+4, 0, False),
            ],
        }
    elif state%4==0 :
        fl_mdp[state]={
            "up":
            [ 
                (1/3, state, 0, False),
                (1/3, state-4, 0, False),
                (1/3, state+1, 0, False),
            ],
            "down" :
            [ 
                (1/3, state, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state+4, 0 ,False),
            ],
            "left" :
            [                 
                (1/3, state, 0, False),
                (1/3, state-4, 0, False),
                (1/3, state+4, 0, False),
            ],
            "right":
            [ 
                (1/3, state-4, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state+4, 0, False),
            ],
        }
    elif state%4==3 :
        fl_mdp[state]={
            "up":
            [ 
                (1/3, state, 0, False),
                (1/3, state-4, 0, False),
                (1/3, state-1, 0, False),
            ],
            "down":
            [ 
                (1/3, state, 0, False),
                (1/3, state-1, 0, False),
                (1/3, state+4, 0 ,False),
            ],
            "left":
            [ 
                (1/3, state-1, 0, False),
                (1/3, state-4, 0, False),
                (1/3, state+4, 0, False),
            ],            
            "right":
            [ 
                (1/3, state-4, 0, False),
                (1/3, state, 0, False),
                (1/3, state+4, 0, False),
            ],
        }
    elif state==13 :
        fl_mdp[state]={
            "up" :
            [ 
                (1/3, 12, 0, False),
                (1/3, 9, 0, False),
                (1/3, 14, 0, False),
            ],
            "down":
            [ 
                (1/3, 14, 0, False),
                (1/3, 13, 0, False),
                (1/3, 12, 0, False),
            ],
            "left":
            [ 
                (1/3, 12, 0,False),
                (1/3, 13, 0, False),
                (1/3, 9, 0, False),
            ],
            "right":
            [ 
                (1/3, 14, 0, False),
                (1/3, 13, 0, False),
                (1/3, 9, 0, False),
            ],
        }
    else :
        fl_mdp[state]={
            "up" :
            [ 
                (1/3, state-4, 0, False),
                (1/3, state+1, 0, False),
                (1/3, state-1, 0, False),
            ],
            "down":
            [ 
                (1/3, state+4, 0, False),                
                (1/3, state-1, 0, False),
                (1/3, state+1, 0, False),
        ],
            "left":
            [ 
                (1/3, state-1, 0,False),
                (1/3, state-4, 0, False),
                (1/3, state+4, 0, False),
            ],
            "right":
            [ 
                (1/3, state+1, 0, False),
                (1/3, state-4, 0, False),
                (1/3, state+4, 0, False),
            ],
        }
