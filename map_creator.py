# Kandu! Entertainment est. 6/30/2018
# This is the map module. This module will setup the map class
# for all the maps in the game plus the worlds about 1600 rooms to
# explore

import fight as f
import setup
import encounters
from map_creator import *
from store import *
import random
import save
import sys

empty = 'Empty    '
room = 'Dungeon  '
zero = '0        '
player = 'Player   '


def create_dungeon():
    empty = 'Empty    '
    room = 'Dungeon  '
    zero = '0        '
    player = 'Player   '
    
    #A list with the above with probabilities!  NOTE: you could potentially have more than
    #one player but the odds are 1/(1+9+15) 
    weighted_random = [player] * 1 + [room] * 9 + [zero] * 15
    
    #this creates random 5x5 lists of dungeons with the weighted_random
    rand_dungeons = [[random.choice(weighted_random) for i in range(5)] for j in range(5)]
    
    dungeon_1 = [[zero, zero, room, zero, zero],
                 [zero, zero, room, zero, zero],
                 [room, room, player, room, room],
                 [zero, zero, room, zero, zero],
                 [zero, zero, room, zero, zero]]

    dungeon_2 = [[room, zero, room, zero, zero],
                 [room, room, room, room, zero],
                 [room, room, player, room, room],
                 [zero, room, room, room, room],
                 [zero, zero, room, zero, room]]

    
    
    dungeons = [dungeon_1, dungeon_2]
    return random.choice(dungeons)
    #return rand_dungeons #instead of hard coding; you can completely randomize your dungeons but its up to you


class Map:
    def __init__(self, grid, x, y, map_number, world_number):
        self._grid = grid
        self._start_x = x
        self._start_y = y
        self._map_number = map_number
        self._world_number = world_number
        self._played_intro = False

    def choose_different_room(self):
        print()
        print("Next time pick a space that has a Dungeon!!!")
        print()

    def up(self):

        self._start_y -= 1
        if self._grid[self._start_y][self._start_x] == room:
            if self.dungeon_selector():
                pass
            else:
                self._start_y += 1
                return
        if self._grid[self._start_y][self._start_x] == zero:
            self.choose_different_room()
            self._start_y += 1
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_y += 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_y -= 1

    def down(self):

        self._start_y += 1
        if self._grid[self._start_y][self._start_x] == room:
            if self.dungeon_selector():
                pass
            else:
                self._start_y -= 1
                return
        if self._grid[self._start_y][self._start_x] == zero:
            self.choose_different_room()
            self._start_y -= 1
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_y -= 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_y += 1

    def right(self):

        self._start_x += 1
        if self._grid[self._start_y][self._start_x] == room:
            if self.dungeon_selector():
                pass
            else:
                self._start_x -= 1
                return
        if self._grid[self._start_y][self._start_x] == zero:
            self.choose_different_room()
            self._start_x -= 1
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_x -= 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_x += 1

    def left(self):

        self._start_x -= 1
        if self._grid[self._start_y][self._start_x] == room:
            if self.dungeon_selector():
                pass
            else:
                self._start_x += 1
                return
        if self._grid[self._start_y][self._start_x] == zero:
            self.choose_different_room()
            self._start_x += 1
            return
        self._grid[self._start_y][self._start_x] = player
        self._start_x += 1
        self._grid[self._start_y][self._start_x] = empty
        self._start_x -= 1

    def dungeon_selector(self):

        if self._world_number == 1:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_1_random_enemy())
            return defeated_enemy
        if self._world_number == 2:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_2_random_enemy())
            return defeated_enemy
        if self._world_number == 3:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_3_random_enemy())
            return defeated_enemy
        if self._world_number == 4:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_4_random_enemy())
            return defeated_enemy
        if self._world_number == 5:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_5_random_enemy())
            return defeated_enemy
        if self._world_number == 6:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_6_random_enemy())
            return defeated_enemy
        if self._world_number == 7:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_7_random_enemy())
            return defeated_enemy
        if self._world_number == 8:
            defeated_enemy = f.fight(setup.starting_character, encounters.lvl_8_random_enemy())
            return defeated_enemy

    def display_map(self):
        print()
        print("World Level: ", self._world_number)
        print("Map Level: ", self._map_number)
        for i in range(len(self._grid)):
            for j in range(len(self._grid[i])):
                print(self._grid[i][j], end='|')
            print()

    def map_engine(self):
        print()
        while True:
            self.display_map()
            choice = str(input("UP:1 Down:2 Left:3 Right:4 New Map:5 Store:6 Save:7 Quit:8 : "))
            if choice == '1':
                self.up()
                continue
            if choice == '2':
                self.down()
                continue
            if choice == '3':
                self.left()
                continue
            if choice == '4':
                self.right()
                continue
            if choice == '5':
                dungeon = 0
                for row in self._grid:
                    for col in row:
                        if col == room:
                            dungeon += 1
                        else:
                            continue
                if dungeon > 0:
                    print("You need to complete all the dungeons in order to move to a new map")
                else:
                    return
            if choice == '6':
                store = Store(setup.starting_character._type)
                store.display()
                setup.starting_character.playerinfo()
            elif choice == '7':
                save.save_object(setup.starting_character, 'save_file.pkl')
                save.save_object(setup.solar_system, 'solar_system.pkl')
                print("Game Save Successful!")
            elif choice == '8':
                print("Leaving the world of galoo....")
                sys.exit()


class SolarSystem:

    def __init__(self, solar_system):
        self._solar_system = solar_system
        self._world = 0
        self._row = 0
        self._col = 0

    def play_solar_system(self):

        for world in enumerate(self._solar_system):
            index = world[0]
            world_obj = world[1]
            if index == self._world:
                for row in enumerate(world_obj):
                    index_row = row[0]
                    world_row = row[1]
                    if index_row == self._row:
                        for col in enumerate(world_row):
                            index_col = col[0]
                            world_col = col[1]
                            if index_col == self._col:
                                world_col.map_engine()
                                self._col += 1
                            else:
                                continue
                        self._col = 0
                        self._row += 1
                    else:
                        continue
                self._row = 0
                self._world += 1
            else:
                continue
        print("Congratulations you have completed the Mysteries of Galoo...")

# world 1

new_map_1 = Map(create_dungeon(), 2, 2, 1, 1)
new_map_2 = Map(create_dungeon(), 2, 2, 2, 1)
new_map_3 = Map(create_dungeon(), 2, 2, 3, 1)
new_map_4 = Map(create_dungeon(), 2, 2, 4, 1)
new_map_5 = Map(create_dungeon(), 2, 2, 5, 1)
new_map_6 = Map(create_dungeon(), 2, 2, 6, 1)
new_map_7 = Map(create_dungeon(), 2, 2, 7, 1)
new_map_8 = Map(create_dungeon(), 2, 2, 8, 1)
new_map_9 = Map(create_dungeon(), 2, 2, 9, 1)
new_map_10 = Map(create_dungeon(), 2, 2, 10, 1)
new_map_11 = Map(create_dungeon(), 2, 2, 11, 1)
new_map_12 = Map(create_dungeon(), 2, 2, 12, 1)
new_map_13 = Map(create_dungeon(), 2, 2, 13, 1)
new_map_14 = Map(create_dungeon(), 2, 2, 14, 1)
new_map_15 = Map(create_dungeon(), 2, 2, 15, 1)
new_map_16 = Map(create_dungeon(), 2, 2, 16, 1)
new_map_17 = Map(create_dungeon(), 2, 2, 17, 1)
new_map_18 = Map(create_dungeon(), 2, 2, 18, 1)
new_map_19 = Map(create_dungeon(), 2, 2, 19, 1)
new_map_20 = Map(create_dungeon(), 2, 2, 20, 1)
new_map_21 = Map(create_dungeon(), 2, 2, 21, 1)
new_map_22 = Map(create_dungeon(), 2, 2, 22, 1)
new_map_23 = Map(create_dungeon(), 2, 2, 23, 1)
new_map_24 = Map(create_dungeon(), 2, 2, 24, 1)
new_map_25 = Map(create_dungeon(), 2, 2, 25, 1)

# world 2

new_map_26 = Map(create_dungeon(), 2, 2, 1, 2)
new_map_27 = Map(create_dungeon(), 2, 2, 2, 2)
new_map_28 = Map(create_dungeon(), 2, 2, 3, 2)
new_map_29 = Map(create_dungeon(), 2, 2, 4, 2)
new_map_30 = Map(create_dungeon(), 2, 2, 5, 2)
new_map_31 = Map(create_dungeon(), 2, 2, 6, 2)
new_map_32 = Map(create_dungeon(), 2, 2, 7, 2)
new_map_33 = Map(create_dungeon(), 2, 2, 8, 2)
new_map_34 = Map(create_dungeon(), 2, 2, 9, 2)
new_map_35 = Map(create_dungeon(), 2, 2, 10, 2)
new_map_36 = Map(create_dungeon(), 2, 2, 11, 2)
new_map_37 = Map(create_dungeon(), 2, 2, 12, 2)
new_map_38 = Map(create_dungeon(), 2, 2, 13, 2)
new_map_39 = Map(create_dungeon(), 2, 2, 14, 2)
new_map_40 = Map(create_dungeon(), 2, 2, 15, 2)
new_map_41 = Map(create_dungeon(), 2, 2, 16, 2)
new_map_42 = Map(create_dungeon(), 2, 2, 17, 2)
new_map_43 = Map(create_dungeon(), 2, 2, 18, 2)
new_map_44 = Map(create_dungeon(), 2, 2, 19, 2)
new_map_45 = Map(create_dungeon(), 2, 2, 20, 2)
new_map_46 = Map(create_dungeon(), 2, 2, 21, 2)
new_map_47 = Map(create_dungeon(), 2, 2, 22, 2)
new_map_48 = Map(create_dungeon(), 2, 2, 23, 2)
new_map_49 = Map(create_dungeon(), 2, 2, 24, 2)
new_map_50 = Map(create_dungeon(), 2, 2, 25, 2)

# world 3

new_map_51 = Map(create_dungeon(), 2, 2, 1, 3)
new_map_52 = Map(create_dungeon(), 2, 2, 2, 3)
new_map_53 = Map(create_dungeon(), 2, 2, 3, 3)
new_map_54 = Map(create_dungeon(), 2, 2, 4, 3)
new_map_55 = Map(create_dungeon(), 2, 2, 5, 3)
new_map_56 = Map(create_dungeon(), 2, 2, 6, 3)
new_map_57 = Map(create_dungeon(), 2, 2, 7, 3)
new_map_58 = Map(create_dungeon(), 2, 2, 8, 3)
new_map_59 = Map(create_dungeon(), 2, 2, 9, 3)
new_map_60 = Map(create_dungeon(), 2, 2, 10, 3)
new_map_61 = Map(create_dungeon(), 2, 2, 11, 3)
new_map_62 = Map(create_dungeon(), 2, 2, 12, 3)
new_map_63 = Map(create_dungeon(), 2, 2, 13, 3)
new_map_64 = Map(create_dungeon(), 2, 2, 14, 3)
new_map_65 = Map(create_dungeon(), 2, 2, 15, 3)
new_map_66 = Map(create_dungeon(), 2, 2, 16, 3)
new_map_67 = Map(create_dungeon(), 2, 2, 17, 3)
new_map_68 = Map(create_dungeon(), 2, 2, 18, 3)
new_map_69 = Map(create_dungeon(), 2, 2, 19, 3)
new_map_70 = Map(create_dungeon(), 2, 2, 20, 3)
new_map_71 = Map(create_dungeon(), 2, 2, 21, 3)
new_map_72 = Map(create_dungeon(), 2, 2, 22, 3)
new_map_73 = Map(create_dungeon(), 2, 2, 23, 3)
new_map_74 = Map(create_dungeon(), 2, 2, 24, 3)
new_map_75 = Map(create_dungeon(), 2, 2, 25, 3)

# world 4

new_map_76 = Map(create_dungeon(), 2, 2, 1, 4)
new_map_77 = Map(create_dungeon(), 2, 2, 2, 4)
new_map_78 = Map(create_dungeon(), 2, 2, 3, 4)
new_map_79 = Map(create_dungeon(), 2, 2, 4, 4)
new_map_80 = Map(create_dungeon(), 2, 2, 5, 4)
new_map_81 = Map(create_dungeon(), 2, 2, 6, 4)
new_map_82 = Map(create_dungeon(), 2, 2, 7, 4)
new_map_83 = Map(create_dungeon(), 2, 2, 8, 4)
new_map_84 = Map(create_dungeon(), 2, 2, 9, 4)
new_map_85 = Map(create_dungeon(), 2, 2, 10, 4)
new_map_86 = Map(create_dungeon(), 2, 2, 11, 4)
new_map_87 = Map(create_dungeon(), 2, 2, 12, 4)
new_map_88 = Map(create_dungeon(), 2, 2, 13, 4)
new_map_89 = Map(create_dungeon(), 2, 2, 14, 4)
new_map_90 = Map(create_dungeon(), 2, 2, 15, 4)
new_map_91 = Map(create_dungeon(), 2, 2, 16, 4)
new_map_92 = Map(create_dungeon(), 2, 2, 17, 4)
new_map_93 = Map(create_dungeon(), 2, 2, 18, 4)
new_map_94 = Map(create_dungeon(), 2, 2, 19, 4)
new_map_95 = Map(create_dungeon(), 2, 2, 20, 4)
new_map_96 = Map(create_dungeon(), 2, 2, 21, 4)
new_map_97 = Map(create_dungeon(), 2, 2, 22, 4)
new_map_98 = Map(create_dungeon(), 2, 2, 23, 4)
new_map_99 = Map(create_dungeon(), 2, 2, 24, 4)
new_map_100 = Map(create_dungeon(), 2, 2, 25, 4)

# world 5

new_map_101 = Map(create_dungeon(), 2, 2, 1, 5)
new_map_102 = Map(create_dungeon(), 2, 2, 2, 5)
new_map_103 = Map(create_dungeon(), 2, 2, 3, 5)
new_map_104 = Map(create_dungeon(), 2, 2, 4, 5)
new_map_105 = Map(create_dungeon(), 2, 2, 5, 5)
new_map_106 = Map(create_dungeon(), 2, 2, 6, 5)
new_map_107 = Map(create_dungeon(), 2, 2, 7, 5)
new_map_108 = Map(create_dungeon(), 2, 2, 8, 5)
new_map_109 = Map(create_dungeon(), 2, 2, 9, 5)
new_map_110 = Map(create_dungeon(), 2, 2, 10, 5)
new_map_111 = Map(create_dungeon(), 2, 2, 11, 5)
new_map_112 = Map(create_dungeon(), 2, 2, 12, 5)
new_map_113 = Map(create_dungeon(), 2, 2, 13, 5)
new_map_114 = Map(create_dungeon(), 2, 2, 14, 5)
new_map_115 = Map(create_dungeon(), 2, 2, 15, 5)
new_map_116 = Map(create_dungeon(), 2, 2, 16, 5)
new_map_117 = Map(create_dungeon(), 2, 2, 17, 5)
new_map_118 = Map(create_dungeon(), 2, 2, 18, 5)
new_map_119 = Map(create_dungeon(), 2, 2, 19, 5)
new_map_120 = Map(create_dungeon(), 2, 2, 20, 5)
new_map_121 = Map(create_dungeon(), 2, 2, 21, 5)
new_map_122 = Map(create_dungeon(), 2, 2, 22, 5)
new_map_123 = Map(create_dungeon(), 2, 2, 23, 5)
new_map_124 = Map(create_dungeon(), 2, 2, 24, 5)
new_map_125 = Map(create_dungeon(), 2, 2, 25, 5)

# world 6

new_map_126 = Map(create_dungeon(), 2, 2, 1, 6)
new_map_127 = Map(create_dungeon(), 2, 2, 2, 6)
new_map_128 = Map(create_dungeon(), 2, 2, 3, 6)
new_map_129 = Map(create_dungeon(), 2, 2, 4, 6)
new_map_130 = Map(create_dungeon(), 2, 2, 5, 6)
new_map_131 = Map(create_dungeon(), 2, 2, 6, 6)
new_map_132 = Map(create_dungeon(), 2, 2, 7, 6)
new_map_133 = Map(create_dungeon(), 2, 2, 8, 6)
new_map_134 = Map(create_dungeon(), 2, 2, 9, 6)
new_map_135 = Map(create_dungeon(), 2, 2, 10, 6)
new_map_136 = Map(create_dungeon(), 2, 2, 11, 6)
new_map_137 = Map(create_dungeon(), 2, 2, 12, 6)
new_map_138 = Map(create_dungeon(), 2, 2, 13, 6)
new_map_139 = Map(create_dungeon(), 2, 2, 14, 6)
new_map_140 = Map(create_dungeon(), 2, 2, 15, 6)
new_map_141 = Map(create_dungeon(), 2, 2, 16, 6)
new_map_142 = Map(create_dungeon(), 2, 2, 17, 6)
new_map_143 = Map(create_dungeon(), 2, 2, 18, 6)
new_map_144 = Map(create_dungeon(), 2, 2, 19, 6)
new_map_145 = Map(create_dungeon(), 2, 2, 20, 6)
new_map_146 = Map(create_dungeon(), 2, 2, 21, 6)
new_map_147 = Map(create_dungeon(), 2, 2, 22, 6)
new_map_148 = Map(create_dungeon(), 2, 2, 23, 6)
new_map_149 = Map(create_dungeon(), 2, 2, 24, 6)
new_map_150 = Map(create_dungeon(), 2, 2, 25, 6)

# world 7

new_map_151 = Map(create_dungeon(), 2, 2, 1, 7)
new_map_152 = Map(create_dungeon(), 2, 2, 2, 7)
new_map_153 = Map(create_dungeon(), 2, 2, 3, 7)
new_map_154 = Map(create_dungeon(), 2, 2, 4, 7)
new_map_155 = Map(create_dungeon(), 2, 2, 5, 7)
new_map_156 = Map(create_dungeon(), 2, 2, 6, 7)
new_map_157 = Map(create_dungeon(), 2, 2, 7, 7)
new_map_158 = Map(create_dungeon(), 2, 2, 8, 7)
new_map_159 = Map(create_dungeon(), 2, 2, 9, 7)
new_map_160 = Map(create_dungeon(), 2, 2, 10, 7)
new_map_161 = Map(create_dungeon(), 2, 2, 11, 7)
new_map_162 = Map(create_dungeon(), 2, 2, 12, 7)
new_map_163 = Map(create_dungeon(), 2, 2, 13, 7)
new_map_164 = Map(create_dungeon(), 2, 2, 14, 7)
new_map_165 = Map(create_dungeon(), 2, 2, 15, 7)
new_map_166 = Map(create_dungeon(), 2, 2, 16, 7)
new_map_167 = Map(create_dungeon(), 2, 2, 17, 7)
new_map_168 = Map(create_dungeon(), 2, 2, 18, 7)
new_map_169 = Map(create_dungeon(), 2, 2, 19, 7)
new_map_170 = Map(create_dungeon(), 2, 2, 20, 7)
new_map_171 = Map(create_dungeon(), 2, 2, 21, 7)
new_map_172 = Map(create_dungeon(), 2, 2, 22, 7)
new_map_173 = Map(create_dungeon(), 2, 2, 23, 7)
new_map_174 = Map(create_dungeon(), 2, 2, 24, 7)
new_map_175 = Map(create_dungeon(), 2, 2, 25, 7)

# world 8

new_map_176 = Map(create_dungeon(), 2, 2, 1, 8)
new_map_177 = Map(create_dungeon(), 2, 2, 2, 8)
new_map_178 = Map(create_dungeon(), 2, 2, 3, 8)
new_map_179 = Map(create_dungeon(), 2, 2, 4, 8)
new_map_180 = Map(create_dungeon(), 2, 2, 5, 8)
new_map_181 = Map(create_dungeon(), 2, 2, 6, 8)
new_map_182 = Map(create_dungeon(), 2, 2, 7, 8)
new_map_183 = Map(create_dungeon(), 2, 2, 8, 8)
new_map_184 = Map(create_dungeon(), 2, 2, 9, 8)
new_map_185 = Map(create_dungeon(), 2, 2, 10, 8)
new_map_186 = Map(create_dungeon(), 2, 2, 11, 8)
new_map_187 = Map(create_dungeon(), 2, 2, 12, 8)
new_map_188 = Map(create_dungeon(), 2, 2, 13, 8)
new_map_189 = Map(create_dungeon(), 2, 2, 14, 8)
new_map_190 = Map(create_dungeon(), 2, 2, 15, 8)
new_map_191 = Map(create_dungeon(), 2, 2, 16, 8)
new_map_192 = Map(create_dungeon(), 2, 2, 17, 8)
new_map_193 = Map(create_dungeon(), 2, 2, 18, 8)
new_map_194 = Map(create_dungeon(), 2, 2, 19, 8)
new_map_195 = Map(create_dungeon(), 2, 2, 20, 8)
new_map_196 = Map(create_dungeon(), 2, 2, 21, 8)
new_map_197 = Map(create_dungeon(), 2, 2, 22, 8)
new_map_198 = Map(create_dungeon(), 2, 2, 23, 8)
new_map_199 = Map(create_dungeon(), 2, 2, 24, 8)
new_map_200 = Map(create_dungeon(), 2, 2, 25, 8)


world_1 = [[new_map_1, new_map_2, new_map_3, new_map_4, new_map_5],
           [new_map_6, new_map_7, new_map_8, new_map_9, new_map_10],
           [new_map_11, new_map_12, new_map_13, new_map_14, new_map_15],
           [new_map_16, new_map_17, new_map_18, new_map_19, new_map_20],
           [new_map_21, new_map_22, new_map_23, new_map_24, new_map_25]]

world_2 = [[new_map_26, new_map_27, new_map_28, new_map_29, new_map_30],
           [new_map_31, new_map_32, new_map_33, new_map_34, new_map_35],
           [new_map_36, new_map_37, new_map_38, new_map_39, new_map_40],
           [new_map_41, new_map_42, new_map_43, new_map_44, new_map_45],
           [new_map_46, new_map_47, new_map_48, new_map_49, new_map_50]]

world_3 = [[new_map_51, new_map_52, new_map_53, new_map_54, new_map_55],
           [new_map_56, new_map_57, new_map_58, new_map_59, new_map_60],
           [new_map_61, new_map_62, new_map_63, new_map_64, new_map_65],
           [new_map_66, new_map_67, new_map_68, new_map_69, new_map_70],
           [new_map_71, new_map_72, new_map_73, new_map_74, new_map_75]]

world_4 = [[new_map_76, new_map_77, new_map_78, new_map_79, new_map_80],
           [new_map_81, new_map_82, new_map_83, new_map_84, new_map_85],
           [new_map_86, new_map_87, new_map_88, new_map_89, new_map_90],
           [new_map_91, new_map_92, new_map_93, new_map_94, new_map_95],
           [new_map_96, new_map_97, new_map_98, new_map_99, new_map_100]]

world_5 = [[new_map_101, new_map_102, new_map_103, new_map_104, new_map_105],
           [new_map_106, new_map_107, new_map_108, new_map_109, new_map_110],
           [new_map_111, new_map_112, new_map_113, new_map_114, new_map_115],
           [new_map_116, new_map_117, new_map_118, new_map_119, new_map_120],
           [new_map_121, new_map_122, new_map_123, new_map_124, new_map_125]]

world_6 = [[new_map_126, new_map_127, new_map_128, new_map_129, new_map_130],
           [new_map_131, new_map_132, new_map_133, new_map_134, new_map_135],
           [new_map_136, new_map_137, new_map_138, new_map_139, new_map_140],
           [new_map_141, new_map_142, new_map_143, new_map_144, new_map_145],
           [new_map_146, new_map_147, new_map_148, new_map_149, new_map_150]]

world_7 = [[new_map_151, new_map_152, new_map_153, new_map_154, new_map_155],
           [new_map_156, new_map_157, new_map_158, new_map_159, new_map_160],
           [new_map_161, new_map_162, new_map_163, new_map_164, new_map_165],
           [new_map_166, new_map_167, new_map_168, new_map_169, new_map_170],
           [new_map_171, new_map_172, new_map_173, new_map_174, new_map_175]]

world_8 = [[new_map_176, new_map_177, new_map_178, new_map_179, new_map_180],
           [new_map_181, new_map_182, new_map_183, new_map_184, new_map_185],
           [new_map_186, new_map_187, new_map_188, new_map_189, new_map_190],
           [new_map_191, new_map_192, new_map_193, new_map_194, new_map_195],
           [new_map_196, new_map_197, new_map_198, new_map_199, new_map_200]]

solar_system = [world_1, world_2, world_3, world_4, world_5, world_6, world_7, world_8]


