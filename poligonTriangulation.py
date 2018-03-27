import random

def principal():
        while(True):
                edges = int(input("Introduce the number of size for your regular polygon: "))
                firstVertex = int(input("Introduce the number of vertex that you want first: "))
                numTriangles = edges-2
                numDiagonal = edges-3
                poliganTriangulation(numTriangles, numDiagonal, firstVertex)
                numCombinationTriangles = catalanNumber(numTriangles)
                
                print("Polygon size: ",edges)
                print("Number of posible triangles in the polygon: ", numTriangles)
                print("Number of posible diagonals in the polygon: ", numDiagonal)
                print("Number of posible diferent combinations of triangles in the polygon: ", numCombinationTriangles)



	
def poliganTriangulation(numTriangles, numDiagonal, firstVertex):
	diagonalList = []
	for i in range(numDiagonal):
		drawDiagonalIrregular(firstVertex, diagonalList,i+3)
		drawDiagonal(firstVertex, diagonalList,i+3)

def drawDiagonal(firstVertex, diagonalList,i):
	diagonalList.append([firstVertex, i])
	return diagonalList

def drawDiagonalIrregular(firstVertex, diagonalList,i):
        distance = random.randint(1,20)
        print("Irregular poligon Distance between one vertex to another: " + str(distance))

def factorial(number):
	if(number > 0):
		n = number-1
		while(n>0):
			number *= n
			n -= 1
	return(number)

	
def catalanNumber(n):
        if(n == 0):
                print("Debe ingresar un numero de vertices mayor a 2")
        else:
                a = factorial(2*n)
                b = factorial(n+1)
                c = factorial(n)
                catalanNumber = a // (b*c)
                return(catalanNumber)


        
principal()


