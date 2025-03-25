import random


for i in range(3):
    print(random.random())


for j in range(5):
    print(random.randint(10,20))


members= ['sandeep','shantha','paddi','ada']
leader = random.choice(members)
print(leader)
