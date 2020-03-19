
import itertools

stuff = 'barev'
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        # print(subset)
        print(''.join(subset))