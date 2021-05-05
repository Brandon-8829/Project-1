nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
name = str(input("Please enter your friends name: "))
# Add the name to the empty set
user_friends.add(name)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
set_three = nearby_people.intersection(user_friends)
print(set_three)