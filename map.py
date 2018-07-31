#Kandu! Entertainment est. 6/30/2018
#This is the map module. This module will setup the map class
#for all the maps in the game plus the worlds about 1600 rooms to
#explore

from game import *

def choose_differant_room():
        print()
        print("Next time pick a space that has a Dungeon!!!")
        print()

class Map:
    def __init__(self, grid, x, y):
        self._grid = grid
        self._start_x = x
        self._start_y = y
        current_location = self._grid[self._start_y][self._start_x]
        
    def up(self):
        
        self._start_y -= 1
        if self._grid[self._start_y][self._start_x] == room:
            start_menu()
        if self._grid[self._start_y][self._start_x] == zero:
            choose_differant_room()
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_y += 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_y -= 1

    def down(self):

        self._start_y += 1
        if self._grid[self._start_y][self._start_x] == room:
            start_menu()
        if self._grid[self._start_y][self._start_x] == zero:
            choose_differant_room()
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_y -= 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_y += 1
        
    def right(self):
        
        self._start_x += 1
        if self._grid[self._start_y][self._start_x] == room:
            start_menu()
        if self._grid[self._start_y][self._start_x] == zero:
            choose_differant_room()
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_x -= 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_x += 1
        
        
    def left(self):
        
        self._start_x -= 1
        if self._grid[self._start_y][self._start_x] == room:
            start_menu()
        if self._grid[self._start_y][self._start_x] == zero:
            choose_differant_room()
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_x += 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_x -= 1
        
    def display_map(self):

        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                print(self._grid[i][j], end = '|')
            print()
            
    def map_engine(self):

        print("You Found a Map!")
        self.display_map()
        while True:
            choice = str(input("UP:1 Down:2 Left:3 Right:4...: "))
            if choice == '1':
                self.up()
                self.display_map()
                continue
            if choice == '2':
                self.down()
                self.display_map()
                continue
            if choice == '3':
                self.left()
                self.display_map()
                continue
            if choice == '4':
                self.right()
                self.display_map()
                continue
            if choice == '5':
                return
            
empty = 'Empty    '      
room = 'Dungeon  '
zero = '0        '
player = 'Player   '

dungeon_1 = [[zero,zero,room,zero,zero],
             [zero,zero,room,zero,zero],
             [room,room,player,room,room],
             [zero,zero,room,zero,zero],
             [zero,zero,room,zero,zero]]


new_map_1 = Map(dungeon_1, 2, 2)
new_map_2 = Map(dungeon_1, 2, 2)
new_map_3 = Map(dungeon_1, 2, 2)
new_map_4 = Map(dungeon_1, 2, 2)
new_map_5 = Map(dungeon_1, 2, 2)
new_map_6 = Map(dungeon_1, 2, 2)
new_map_7 = Map(dungeon_1, 2, 2)
new_map_8 = Map(dungeon_1, 2, 2)
new_map_9 = Map(dungeon_1, 2, 2)
new_map_10 = Map(dungeon_1, 2, 2)
new_map_11 = Map(dungeon_1, 2, 2)
new_map_12 = Map(dungeon_1, 2, 2)
new_map_13 = Map(dungeon_1, 2, 2)
new_map_14 = Map(dungeon_1, 2, 2)
new_map_15 = Map(dungeon_1, 2, 2)
new_map_16 = Map(dungeon_1, 2, 2)
new_map_17 = Map(dungeon_1, 2, 2)
new_map_18 = Map(dungeon_1, 2, 2)
new_map_19 = Map(dungeon_1, 2, 2)
new_map_20 = Map(dungeon_1, 2, 2)
new_map_21 = Map(dungeon_1, 2, 2)
new_map_22 = Map(dungeon_1, 2, 2)
new_map_23 = Map(dungeon_1, 2, 2)
new_map_24 = Map(dungeon_1, 2, 2)
new_map_25 = Map(dungeon_1, 2, 2)

world_1 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_2 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_3 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_4 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_5 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_6 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_7 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

world_8 = [[new_map_1,new_map_2,new_map_3,new_map_4,new_map_5],
           [new_map_6,new_map_7,new_map_8,new_map_9,new_map_10],
           [new_map_11,new_map_12,new_map_13,new_map_14,new_map_15],
           [new_map_16,new_map_17,new_map_18,new_map_19,new_map_20],
           [new_map_21,new_map_22,new_map_23,new_map_24,new_map_25]]

def play_world(world):
    for i in range(len(world)):
        for j in range(len(world[i])):
            world[i][j].map_engine()

def play_solar_system():

    play_world(world_1)
    play_world(world_2)
    play_world(world_3)
    play_world(world_4)
    play_world(world_5)
    play_world(world_6)
    play_world(world_7)
    play_world(world_8)


play_solar_system()

        























        
