# type , id , input , raw_input , print
# list --> []
var = input("enter list  with input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)

var = raw_input("enter list with raw_input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)
