#Q70:
import random #only for exercise here
rand = [i for i in range(0, 11, 2)]
print(random.choice(rand))

#Q71:
rand = [i for i in range(0, 151) if i%5 == 0 and i%7 == 0]
print(random.choice(rand))

#Q72:
rand = random.sample(range(100, 201),5 )
print(rand)

#Q73:
rand = random.sample(range(100, 201, 2),5 )
print(rand)