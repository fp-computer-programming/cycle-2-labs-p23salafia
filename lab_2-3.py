from re import A


a = 2               #A=2
print(a)            
print(type(a))      #<class 'int'>
a = float(a)
print(type(a))      #<class 'float'>
a = str(a)
print(type(a))      #<class 'str'>
a = bool(a)      
print(type(a))      #<class 'bool'>
print(a==2)
#It is false because after converint to a boolean, a=true and true=/=false
