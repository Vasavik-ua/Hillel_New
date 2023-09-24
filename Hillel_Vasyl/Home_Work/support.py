import random

my_list = ['095', '066', '098', '096', '050', '097']
new_list = random.choice(my_list)
last = random.randint(00000000, 9999999)
new_value = new_list+(str(last))
print(new_value)