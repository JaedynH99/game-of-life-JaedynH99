SEQUENCE_LENGTH = 300
fibonacci=[0,1]
function=[]
for i in range(2, SEQUENCE_LENGTH):
    fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
print(fibonacci)
for num in range(2,len(fibonacci)):
    function.append(fibonacci[num]/fibonacci[num-1])
print(function)

import matplotlib.pyplot as plt

fig, seq = plt.subplots()
t = range(1, len(fibonacci) - 1)
seq.plot(fibonacci[1:], 'b.')
seq.set_yscale('log')
# Make the y-axis label, ticks and tick labels match the line color.
seq.set_ylabel('Fibonacci Sequence', color='b')
seq.tick_params('y', colors='b')

rat = seq.twinx()
rat.plot(function, 'g-')
rat.set_ylabel('Golden Ratio', color='g')
rat.tick_params('y', colors='g')

fig.tight_layout()
plt.show()
