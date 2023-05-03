# Name: Siddhesh Jadhav, Batch: A1, Roll-no: 08

codelist = [5, 6, 7, 4, -1, 0, 3, 2, 1]

#Function to generate chain code
def getChainCode(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    hashKey = 3 * dy + dx + 4
    return codelist[hashKey]
# Function to generate list of Chain code's for given list of Points
def generateChainCode(ListOfpoints):
    ChainCode = []
    for i in range (len(ListOfpoints) - 1):
        a = ListOfpoints[i]
        b = ListOfpoints[i + 1]
        ChainCode.append(getChainCode(a[0], a[1], b[0], b[1]))
        return ChainCode
# Function to generate list of points using Bresenham's Algorithm
def Bresenham2D(x1, y1, x2, y2):
    ListOfPoints = []
    ListOfPoints.append ([x1, y1])
    xdif = x2 - x1
    ydif = y2 - y1
    dx = abs(xdif)
    dy = abs(ydif)
    if (xdif > 0):
        xs = 1
    else:
        xs = -1
    if (ydif > 0):
        ys = 1
    else:
        ys = -1
    if (dx > dy):

        # Setting x-axis as driving axis
        p = 2 * dy-dx
        while (x1 != x2):
            x1 += xs
            if (p >= 0):
                y1 += ys
                p -= 2 * dx
            p += 2 * dy
            ListOfPoints.append([x1, y1])
        else :
            # Settings y-axis as driving axis
            p = 2 * dx-dy
            while (y1 != y2):
                y1 += ys
                if (p >= 0):
                    x1 += xs
                    p -= 2 * dy
                p += 2 * dx
                ListOfPoints.append([x1,y1])
    return ListOfPoints

# Defining Driver Function
def DriverFunction():
    (x1 , y1) = (-7, -3)
    (x2 , y2) = (9, 3)
    ListOfPoints = Bresenham2D( x1, y1, x2, y2)
    chaincode = generateChainCode (ListOfPoints)
    chaincodestring = "".join(str(e) for e in chaincode)
    print (" Chain code for straight line from", (x1, y1),"to",(x2,y2), "is", chaincodestring)

DriverFunction()