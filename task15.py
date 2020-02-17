start = 0
stop = int(input(' your age '))
step = 2

print(list(range(start, stop)))
if stop % 2 == 0:
    print(list(range(start, stop+1, step)))
else:
    print(list(range(1, stop+1, step))) 
