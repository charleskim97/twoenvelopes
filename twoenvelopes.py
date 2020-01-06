import random
import matplotlib.pyplot as plt

random.seed(1)

# Set the initial envelopes value (default: $100)
a = 100

# Set the desired number of experiments
epochs = 200
epoch = 0
e = []
g = []

# Run experiment
while epoch < epochs:
  gains = 0
  less = 0
  more = 0
  i = 0
  while i < epoch:
    
    rand = random.random()
    if rand >=0.5:
      b = a/2
      less += 1
    else:
      b = 2*a
      more += 1
    gains += b - a
    i += 1
  e.append(epoch)
  g.append(gains)
  epoch += 1

# Display results
plt.plot(g)
plt.xlabel('Number of Epochs')
plt.ylabel('Gains')
plt.show();






