a,b,c=1,2,"house"
print(a)
print(b)
print(c)

#illustrations of string in python
str = 'python editor'
print(str)                                     #prints complete string
print(str[0])                                  #prints first element of string
print(str[2:5])                                #prints string from 2nd element to 5th
print(str[2:])                                 #prints string from 3rd element
print(str * 2)                                 #prints string two times
print(str + "test")                            #concanates str and test

#illustration of lists in python 
list = ['house', 7248,'JOOUST', 16.9]
tinylist = [254, 'python']
print(list)                                    #prints complete list
print(list[0])                                 #prints list first element of list
print(list[1:3])                               #prints list from 2nd element to 3rd 
print(list[2:])                                #prints list from 3rd element
print(tinylist*2)                              #prints tinylist two times
print(list + tinylist)                         #concanates list and tiny list


#illustration of python tuples
tuple = ('house', 7248,'JOOUST', 16.9)
tinytuple = (254, 'python')
print(tuple)                                   #prints complete tuple
print(tuple[0])                                #prints first element of tuple
print(tuple[1:3])                              #prints from 2nd element to 3rd 
print(tuple[2:])                               #prints from 3rd element
print(tinytuple*2)                             #prints tinytuple two times
print(tuple + tinytuple)                       #concanates tuple and tinytuple

#illustration of python dictionaries
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name':'deemee', "code":7248,"dept":'ICT'}
print(dict['one'])                              #prints value for 'one' key
print(dict[2])                                  #prints value for 2 key
print(tinydict)                                 #prints complete dictionary
print(tinydict.keys())                          #prints all keys
print(tinydict.values())                        #prints all values