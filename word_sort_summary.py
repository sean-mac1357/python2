from collections import Counter

user_input = input("Please enter a sentence with recurring words: ")

split_it = user_input.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(3)
print(most_occur)

