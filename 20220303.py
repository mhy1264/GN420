myString="i like Python";

bigger = myString.upper() 
split = myString.split(' ')
connections ='%'.join(split)
newConn=connections.replace('%','$')

print(bigger)
print(split)
print(connections)
print(newConn)
