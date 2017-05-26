import numpy as np
import pandas as pd
import time
start_time = time.time() #for efficiency

#neuron activation function(sigmoid function)
def sigmoid(x, deriv=False):
    if(deriv==True):
        return (x*(1-x))
    
    return 1/(1+np.exp(-x))

#find maximum positive number in given array
def findSharpestValue(d):
	upper=[d.index(i) for i in d if i >= 0]
	maximum=0
	for i in upper:
		if d[i]>maximum:
			maximum=i
	return i		
	
#input data
datafile = pd.read_excel('wakeup-time-data.xlsx')
data=datafile.as_matrix()

X = data[:,:4]

#output data
Y = data[:,4:]

thresholdD1=0.6
thresholdD2=0.232512
thresholdD3=0.788136
thresholdD4=0.22863654

# The seed for the random generator is set so that it will return the same random numbers each time.
np.random.seed(1)


# Now we intialize the weights to random values. syn0 are the weights between the input layer and the hidden layer.  
#syn1 are the weights between the hidden layer and the output layer. 

#synapses
syn0 = 2*np.random.random((4,4)) - 1  # 4x4 matrix of weights (4 inputs x 4 nodes in the hidden layer)
syn1 = 2*np.random.random((4,4)) - 1  # 4x4 matrix of weights. (4 nodes x 4 output) 

l2_error=1 
j=0

#training loop
while (np.mean(np.abs(l2_error)))>0.1:
    j+=1;
    
    # Calculate the output
    l0 = X
    l1 = sigmoid(np.dot(l0, syn0))
    l2 = sigmoid(np.dot(l1, syn1))
    
    # Back propagation of errors using the chain rule. 
    l2_error = Y - l2
    
    if(j % 100) == 0:   # Only print the error every 100 steps, you can increase that.
        print("Error: " + str(np.mean(np.abs(l2_error))))
        
    l2_delta = l2_error*sigmoid(l2, deriv=True)
    
    l1_error = l2_delta.dot(syn1.T)
    
    l1_delta = l1_error * sigmoid(l1,deriv=True)
    
    #update weights
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
    
#print error rate after training
print("Error Rate: " + str(np.mean(np.abs(l2_error))))   

#to print results after training you can uncomment belows.
#print("Output after training")
#print l2

#read expected results excel file
expectedResults = pd.read_excel('Expected-Result.xlsx')
expectedData=expectedResults.as_matrix()[:,4]

#print predictions

effectiveness=0;

for i in xrange(l2.shape[0]):
	#for decision class 1, easy to determine if value bigger than threshold it is positive.
	if l2[i,0] > thresholdD1:
		print "No."+str(i+1)+" "+"Person can wake up at 6.00"
		if expectedData[i]==6.0:
			effectiveness+=1
	else:
	#for other classes, check difference between value and threshold
		diffThres = []
		diffThres.append(l2[i,1]-thresholdD2)
		diffThres.append(l2[i,2]-thresholdD3)
		diffThres.append(l2[i,3]-thresholdD4)
	#find which difference is maximum and return index
		k=findSharpestValue(diffThres)
		if k==0:
			print "No."+str(i+1)+" "+"Person can wake up at 7.00"
			if expectedData[i]==7.0:
				effectiveness+=1
		elif k==1:
			print "No."+str(i+1)+" "+"Person can wake up at 8.00"
			if expectedData[i]==8.0:
				effectiveness+=1	
		elif k==2:
			print "No."+str(i+1)+" "+"Person can wake up at 9.00"
			if expectedData[i]==9.0:
				effectiveness+=1
				
#Calculate effectiveness and Efficiency

effectiveness=effectiveness/float(l2.shape[0])*100
print ("Effectiveness: %.2f%%" %effectiveness)
print("Efficiency: %.4f seconds" % (time.time() - start_time))