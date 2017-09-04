from tdl.map import Map
from random import randint
from entity import Entity
from components.fighter import Fighter
from components.ai import BasicMonster

class GameMap(Map):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.explored = [[False for y in range(height)] for x in range(width)]

class Rect:
    def __init__(self,x,y,w,h):
        self.x1=x
        self.y1=y
        self.x2=x+w
        self.y2=y+h
    def center(self):
        return (int((self.x1+self.x2)/2),int((self.y1+self.y2)/2))
    def intersect(self,other):
        return (other.x2>=self.x1 and other.x1<=self.x2 and other.y2>=self.y1 and other.y1<self.y2)

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

def place_entities(room, entities, max_monsters_per_room, colors):
    # Get a random number of monsters
    number_of_monsters = randint(0, max_monsters_per_room)

    for i in range(number_of_monsters):
        # Choose a random location in the room
        x = randint(room.x1 + 1, room.x2 - 1)
        y = randint(room.y1 + 1, room.y2 - 1)

        if not any([entity for entity in entities if entity.x == x and entity.y == y]):
            if randint(0, 100) < 80:
                fighter_component=Fighter(hp=10,defense=0,power=3)
                ai_component=BasicMonster()
                monster = Entity(x, y, 's', colors.get('dark_brown'),'Soldier',blocks=True, fighter=fighter_component,ai=ai_component)
            else:
                fighter_component=Fighter(hp=15,defense=1,power=6)
                ai_component=BasicMonster()
                monster = Entity(x, y, 'K', colors.get('slate_gray'),'Knight',blocks=True, fighter=fighter_component,ai=ai_component)

            entities.append(monster)
		

def make_map_demo(game_map):
    # Create two rooms for demonstration purposes
    room1 = Rect(20, 15, 10, 15)
    room2 = Rect(35, 15, 10, 15)
    room3 = Rect(35, 5, 10, 5)

    make_room(game_map, room1)
    make_room(game_map, room2)
    make_room(game_map, room3)
    
    make_h_tunnel(game_map,30,35,20)
    make_v_tunnel(game_map, 10,15,40)
    
def make_map(game_map,max_rooms, room_min_size, room_max_size, map_width,map_height, player, entities, max_monsters_per_room, colors):
    rooms = []
    num_rooms = 0

    for r in range(max_rooms):
        # random width and height
        w = randint(room_min_size, room_max_size)
        h = randint(room_min_size, room_max_size)
        # random position without going out of the boundaries of the map
        x = randint(0, map_width - w - 1)
        y = randint(0, map_height - h - 1)
        new_room=Rect(x,y,w,h)
        new_room_ok_flag=True
        #did away with idiosyncratic python use, went with a simple logical flag
        #I might try to write it in a more pythonic way with map/reduce
        if rooms!=[]:
            for room in rooms:
                new_room_ok_flag=new_room_ok_flag and not new_room.intersect(room)
        if new_room_ok_flag:
		    #make the goddamn room
            make_room(game_map, new_room)
		    #find the center of the new room
            (new_x, new_y) = new_room.center()
            if num_rooms==0:
                #player will start in the first room created
                player.x=new_x
                player.y=new_y
            else:
                (prev_x, prev_y) = rooms[num_rooms - 1].center()
                # flip a coin (random number that is either 0 or 1)
                if randint(0, 1) == 1:
                    # first move horizontally, then vertically
                    make_h_tunnel(game_map, prev_x, new_x, prev_y)
                    make_v_tunnel(game_map, prev_y, new_y, new_x)
                else:
                    # first move vertically, then horizontally
                    make_v_tunnel(game_map, prev_y, new_y, prev_x)
                    make_h_tunnel(game_map, prev_x, new_x, new_y)
            place_entities(new_room, entities, max_monsters_per_room, colors)
            rooms.append(new_room)
            num_rooms+=1
            
