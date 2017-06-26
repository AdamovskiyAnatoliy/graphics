import turtle

def fraktal(mylen,n):
	if n > 1 :
		fraktal(mylen, n-1)
	else:
		turtle.forward(mylen)
	turtle.left(90)
	if n > 1 :
		fraktal(mylen, n-1)
	else:
		turtle.forward(mylen)
	turtle.right(90)
	if n > 1 :
		fraktal(mylen, n-1)
	else:
		turtle.forward(mylen)
	turtle.right(90)
	if n > 1 :
		fraktal(mylen, n-1)
	else:
		turtle.forward(mylen)
	if n > 1 :
		turtle.left(90)
		fraktal(mylen, n-1)
	else:
		turtle.left(90)	
		turtle.forward(mylen)
	
def zvizda():
	for i in range(4):
		fraktal(5, 3)
		turtle.right(90)
	

def fraktalnull(mylen, n):
	for i in range(3):
		if n > 1:
			fraktalnull(mylen, n-1)
		else:
			turtle.forward(mylen)
		if i%2 == 0:
			turtle.left(60)
		else:
			turtle.right(120)
			
	if n > 1:
		fraktalnull(mylen, n-1)
	else :
		turtle.forward(mylen)

def zvizdanull():
	for i in range(3):
		fraktalnull(5, 4)
		turtle.right(120)
	
turtle.penup()   
turtle.goto(-200,100)
turtle.pendown()
turtle.speed(1000)

fraktalnull(10,3)

turtle.mainloop()

