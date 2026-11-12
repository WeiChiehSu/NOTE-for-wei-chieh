import statistics
import random

#x1 = random.randint(1, 10)
#x2 = random.randint(1, 10)
#x3 = random.randint(1, 10)

x = [0, 0 ,0 ]

for i in range(len(x)):
    x[i] = random.randint(1, 10)
    print(x[i])
    
avg = statistics.mean(x)
print(f"Average = {avg:.2f}")
