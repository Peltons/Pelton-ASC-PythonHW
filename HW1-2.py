
#!/usr/bin/python

length = int(raw_input("Enter the lenght of the rectangle: "))

width = int(raw_input("Enter the width of the rectangle: "))

area = length * width

perimeter = (length + width) * 2

print "Please enter a or b for the question"

input = str(raw_input("Do you need the [a] area or [b] perimeter of the rectangle?: "))

if (input == "a"):
	print "The area of the rectangle is: %i" % area

elif (input == "b"):
	print "The perimeter of the rectangle is: %i" % perimeter

elif (input != "a" or "b"):
	print "Its wasn't a hard choice a or b, make this program work harder you can too"
