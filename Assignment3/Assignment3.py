import csv
with open('Assignment3_Input.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
           print(', '.join(row))
           
def gradDescent(T,stepize,m,numIteration):
     xTrans = x.transpose()
    for i in range(0, numIterations):
        hypothesis = np.dot(T, stepsize)
        loss = hypothesis - stepize
        cost = np.sum(loss ** 2) / (2 * m)
        print("Iteration %d | Cost: %f" % (i, cost))
        gradient = np.dot(xTrans, loss) / m
        stepsize = stepsize - m * gradient
    return stepize

def genData(T, stepsize, m):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)
    for i in range(0, numPoints):
        x[i][0] = 1
        x[i][1] = i
        y[i] = (i + bias) + random.uniform(0, 1) * variance
    return x, y
 
x, y = genData(T, stepsize, m)
m, n = np.shape(x)
numIterations= 100000
alpha = 0.0005
theta = np.ones(n)
theta = gradientDescent(T, stepsize, m, numIterations)
print(m) 