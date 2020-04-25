
import itertools

# finds all possible combinations of letters

stuff = 'barev'
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, L):
        # print(subset)
        print(''.join(subset))

# finds positions, existing and non existing letters in df

# df[
#     (df['a'].str[1] == 'o')
#     & (   df['a'].str.len() == 5  )
#     & ( df['a'].str.contains('o') )
#     & ( df['a'].str.contains('l') )
#     & ( df['a'].str.contains('d') )
    
#     & ( ~df['a'].str.contains('s') )
  
  
#   ]