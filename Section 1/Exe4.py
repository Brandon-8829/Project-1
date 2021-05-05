"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

lottery_numbers = {13, 21, 22, 5, 8}

players =( 
    {'name': 'Brandon',
    'numbers': {1,2,3}},

    {'name': 'Rachel',
    'numbers': {13,21,5}}
)

name = players[0]["name"]
numbers = players[0]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} right")

name = players[1]["name"]
numbers = players[1]["numbers"].intersection(lottery_numbers)
print(f"Player {name} got {len(numbers)} right")

"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}


