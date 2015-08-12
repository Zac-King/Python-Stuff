f = open('classNames.txt')	#Pulls doc as is  && seperated by line

tmp1 = []
for i in f:
	tmp1.append(i)		# /n left in

tmp2 = []
for i in tmp1:
	i = i.replace("\n", "")
	tmp2.append(i)		# /n taken out

firstName = []
lastName = []
for i in tmp2:
	t = i.split()	#from start to ' '
	firstName.append(t[0])
	lastName.append(t[1])
	
#print(tmp1)		
#print(tmp2)		
	
print (firstName)
print (lastName)