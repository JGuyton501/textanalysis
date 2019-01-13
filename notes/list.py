# ## print diamond shit
# for i in range(25):
# 	for j in range(25):
# 		if i == j:
# 			print "+",
# 		elif i < j:
# 			print "-",
# 		else:
# 			print ".",
# 	print


# Swirlly shit
# Distance formula
import math
sym = ['+ ', "0 "]

def distance(x1, x2):
	return math.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

for i in range(25):
	for j in range(25):
		d = distance((0,0), (i,j))
		b = int(d/5)
		if b % 2 == 0:
			print sym[0],
		else:
			print sym[1],
	print 
