#!/sur/bin/python
# Filename: Balls
# 4 balls in 4 boxes. There's one (and only one) boxe is empty. How many cases are there?

def emptyboxCounter(balls, numberOfBoxes = 4):
	'''Count the number of empty boxes in the input array.

	Blablabla...'''
	emptybox = 0
	for m in range(0,numberOfBoxes):
		for n in balls:
			if n == m:
				break
		else:
			emptybox += 1
	return emptybox


caseCounter = 0
balls = [0]*4
for i in range(0,4):
	balls[0] = i
	for j in range(0,4):
		balls[1] = j
		for k in range(0,4):
			balls[2] = k
			for l in range(0,4):
				balls[3] = l
				if emptyboxCounter(balls) == 1:
					if __name__ == '__main__':
						print(balls)
					caseCounter += 1

if __name__ == '__main__':
	print(caseCounter)
