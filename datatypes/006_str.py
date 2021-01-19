# type , id , input , raw_input , print
# str==>  ''  / "" / ''' '''
var = input("enter str with input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)

var = raw_input("enter str with raw_input function  : ")
print "data in var : ",var
print type(var) # datatype
print "memory loc : ",id(var)
