Write a program that returns the number of time a word or letter  occurs in a string
user_input = input("Enter a word: ").lower()
txt = input("Enter the word you want to check: ").lower()
count = user_input.count(txt)
print("\"{}\"appears {} times.".format(txt.upper(), count))

# solution two:

user_input = input("Enter a word: ").lower()
txt = input("Enter the word you want to check: ").lower()
count = 0
txt_len = len(txt)
for word in range(len(user_input)):
    if user_input[word:word + txt_len] == txt:
        count += 1
    else:
        pass    
print("\"{}\" appears {} times.".format(txt.upper(), count))