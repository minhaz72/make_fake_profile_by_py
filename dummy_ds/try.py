# creating a random fake profile : 
# which doesnot exist : 
import random 
names= ['azim', 'nazim', 'akib', 'nokib', 'zohir', 'rabbi ','faruk' , 'fordin']
age=[]
for i in  range(0 , 60): 
    age.append(list(i))
job=['student', 'programmer', 'hacker', 'teacher']
for j in range(100): 
    n= random.choice(names)
    print(f'your name is {n}')
    a= random.choice(age)
    print(f'hi {n} , you  are {a}  , years old  ')
    j= random.choice(job)
    print(f'{n}  your are doing {j} right :  ')
    
    print( ' your fake data is ', b )
    