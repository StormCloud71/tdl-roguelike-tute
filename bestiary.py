from random import random

def weighted_choice(weights_dict):
    total_weight=sum([weights_dict[i] for i in weights_dict])
    choice=total_weight*random()
    init=0
    for i in weights_dict:
        init+=weights_dict[i]
        if init>=choice: return i

bestiary_dict={1:('s','dark_brown','Soldier',(10,0,3)),
   2:('K','slate_gray','Knight',(15,1,6)),
   3:('T','crimson','Templar',(20,1,8))}
bestiary_weights={1:50,2:9,3:1}

def ReturnBeast():
	return (bestiary_dict[weighted_choice(bestiary_weights)])



