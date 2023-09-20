first = 'First\n'
second = 'Second\n'
third = 'Third\n'
fourth = 'Fourth\n'

f = open('home_work.17.txt', 'w')
f.write(first)
f.write(second)
f.close()

with open('home_work.17.txt', 'a') as f:
    f.write(third)
    f.write(fourth)
