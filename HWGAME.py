#!/usr/bin/python

from sys import exit

prompt = ' '

crew = "Zoro Nami Usopp Chopper Sanji"

all_crew = crew.split(' ')
later_crew = ['Robin', 'Franky', 'Brook']

print "Luffy is looking for the one piece on his pirate ship"
print "He has several people in his crew"
print crew
print "During the grandline they had others join the crew"
while len(all_crew) != 8:
	next = later_crew.pop()
	print next
	all_crew.append(next)

print "Luffy's crew now consist of"
print all_crew

print "While sailing the grandline they come across serveral isliand"

print "Choose an island [1] Punk Hazard [2] Fishman Island or [3] Dressrosa"

input = int(raw_input(">"))

if input == 1:
	print "The crew sets sail for Punk Hazard"
	print "The villian on this island is Ceasar Clown"
	print "He uses dangerous gas to kill his victims"
	print "Your choices are [1] Try to fight him or [2] Save the prisonors"

	input = int(raw_input(">"))

	if input == 1:
		print "Luffy got posioned, he needs time to rocover"
		print "What should the crew do [1] Have Doctor Chopper tend to Luffy or [2] leave him to die"

		input = int(raw_input(">"))

		if input == 1:
			print "Chopper tends to Luffys wounds"
			print "The crew left the island while Luffy recovered"

		elif input == 2:
			print "The crew abandoned Luffy"
			print "So Luffy died, a slow painful death"

	elif input == 2:
		print "Nami saved the children that Ceasar Clown was experimenting on"
		print "The crew got the children off the island and away to safety"

elif input == 2:
	print "The crew sets sail for Fishman Island"
	print "Upon setting foot on Fishman Island a local says money for the toll humans?"
	print "Enter something to tell him"

	comment = str(raw_input(">"))

	file = open("Response.txt", "w")

	file.write(comment)

	file.close()

	file_appened = open("Response.txt")

	print "You had Luffy tell the local"
	print file_appened.read()
	print "The local was shocked and just let you pass"
	print "So the crew explored the island, and later left without an incident"

elif input == 3:
	print "The crew sets sail for Dressrosa"
	print "Doflamingo the king of the island presented himself to Luffy for a fight"

	punches = []

	for punch in range(1, 11):
		print "Luffy punched Doflamingo %d times" % punch

	print "After all the punches Doflamingo went down"
	print "Luffy was victoriuos"
	print "The crew were heros for defeating the evil king"
	print "The crew then left Dressrosa and continued to sail the grandline"
