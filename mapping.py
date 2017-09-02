class Rect:
    def __init__(self,x,y,w,h):
        self.x1=x
        self.y1=y
        self.x2=x+w
        self.y2=y+h

def make_room(game_map,room):
    for i in range(room.x1+1,room.x2):
        for j in range(room.y1+1,room.y2):
            game_map.walkable[i,j]=True
            game_map.transparent[i,j]=True	

def make_h_tunnel(game_map,x1,x2,y):
    for i in range(min(x1,x2),max(x1,x2)+1):
        game_map.walkable[i,y]=True
        game_map.transparent[i,y]=True

def make_v_tunnel(game_map,y1,y2,x):
    for i in range(min(y1,y2),max(y1,y2)+1):
        game_map.walkable[x,i]=True
        game_map.transparent[x,i]=True
		

def make_map(game_map):
    # Create two rooms for demonstration purposes
    room1 = Rect(20, 15, 10, 15)
    room2 = Rect(35, 15, 10, 15)
    room3 = Rect(35, 5, 10, 5)

    make_room(game_map, room1)
    make_room(game_map, room2)
    make_room(game_map, room3)
    
    make_h_tunnel(game_map,30,35,20)
    make_v_tunnel(game_map, 10,15,40)
    
