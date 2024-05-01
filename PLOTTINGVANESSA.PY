import matplotlib.pyplot as plt
import math
print('Vanessa')
Chosen = [x for x in range(1, 10, 1)]

Definition = {
    1: lambda: [x**2 - 10 for x in Chosen],
    2: lambda: [x**2 + x - 100 for x in Chosen],
    3: lambda: [x**10 - x**8 + x**2 - 8 for x in Chosen],
    4: lambda: [x**4 + x**3 + x**2 + x + 1 for x in Chosen],
    5: lambda: [(x**2 + x + 10) / (2*x) for x in Chosen],
    6: lambda: [math.sin(x) / (3*x) for x in Chosen],
    7: lambda: [x**3 + 2*x**2 - 10*x + 3 for x in Chosen],
    8: lambda: [math.cos(x) / (5*x) for x in Chosen],
    9: lambda: [(x**3 / (2*x)) - 10*x for x in Chosen],
    10: lambda: [(x+2)*(x+3)*(x-4) for x in Chosen]
}

while True:
    Choice = int(input("Pick a number from 1-10:"))
    if Choice in Definition:
        result = Definition[Choice]()
        break
    else:
        print("Choose from 1 to 10 only")

plt.plot(Chosen)
plt.plot(result)
plt.xlabel('Chosen',)
plt.ylabel('Output')
plt.show()