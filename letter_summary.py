user_input = input("Please enter a word ")

all_freq = {} 
  
for i in user_input: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
print(all_freq)