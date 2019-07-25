#!/usr/bin/env python3

def showInstructions():
    print('''
Save the princess in the castle! Note: you will need a key to escape! Optionally: Save Chad!
=========
Commands:
  go [direction]
  get [item]
  help
  exit (exits the game)
''')

def showStatus():
    print('\n----------------------------')
    print('You are in the ' + currentRoom)
    print('Inventory : ' + str(inventory))
    if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] != 'chad':
        print('You see a ' + rooms[currentRoom]['item'])
    if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] == 'chad':
        print('You see Chad Feeser! He is here to help you learn Python! Take \'chad\' with you!')   
    print('----------------------------\n')

inventory = []

rooms = {
        'Foyer' : {
            'north' : 'Hall',
            'south' : 'Door'
            },
        'Hall' : {
            'south' : 'Foyer',
            'west' : 'Dining Hall',
            'north' : 'Stairway',
            'east' : 'Throne Room'
            },
        'Kitchen' : {
            'east' : 'Dining Hall',
            'north' : 'Pantry'
            },
        'Dining Hall' : {
            'east' : 'Hall',
            'west' : 'Kitchen',
            'item' : 'sword'
            },
        'Stairway' : {
            'south' : 'Hall',
            'west' : 'Dungeon'
            },
        'Dungeon' : {
            'east' : 'Stairway',
            'north' : 'Cell',
            'item' : 'key'
            },
        'Throne Room' : {
            'west' : 'Hall',
            'item' : 'princess'
            },
        'Door' : {
            'north' : 'Foyer'
            },
        'Cell' : {
            'south' : 'Dungeon',
            'item' : 'chad'
            },
        'Pantry' : {
            'south' : 'Kitchen',
            'east' : 'Dungeon',
            'item' : 'monster'
            }
        }

currentRoom = 'Foyer'

showInstructions()

while True:
    showStatus()
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

#GO
    if move[0] == 'go':
        if currentRoom == 'Foyer' and move[1] == 'south':
            print('\nYou don\'t have a key to exit the door!')
        if currentRoom == 'Pantry' and move[1] == 'east':
            print('\nYou found a slide into the dungeon!')
            currentRoom = rooms[currentRoom][move[1]]
        elif move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]       
        else:
            print('\nYou can\'t go that way!')

#GET
    if move[0] == 'get':
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' picked up!')
            del rooms[currentRoom]['item']
        else:
            print('\nCan\'t get ' + move[1] + '!')

#HELP
    if move[0] == 'help':
        showInstructions()

#EXITTHEGAME
    if move[0] == 'exit':
        break

#DEATHBYMONSTER
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster' and 'sword' not in inventory:
        print('\nYou open the Pantry. A monster jumps out and eats your soul!  GAME OVER!')
        break

#MONSTERDEFEAT
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == 'monster' and 'sword' in inventory:
        print('\nYou open the Pantry. A monster jumps out! You pull out your sword and defeat the monster.')
        rooms[currentRoom]['item'] = 'deadmonster'

#SAVE PRINCESS AND CHAD
    if currentRoom == 'Door' and 'princess' in inventory and 'chad' in inventory:
        print('\nYou escaped the castle with the princess and also saved Chad! YOU WIN!')
        break

#SAVE PRINCESS
    if currentRoom == 'Door' and 'princess' in inventory:
        print('\nYou escaped the house with the castle with the princess! YOU WIN!')
        break
