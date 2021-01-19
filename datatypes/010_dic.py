# type , id , input , raw_input , print
# dict --> {k1 : v1 ,  k2 : v2 , k3 : v3}
var = input("enter dict with input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)

var = raw_input("enter dict  with raw_input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)
