parent_string = input("Enter Master String: ").lower()
check_substring = input("Which letter(s) will you like to check for substring in Master String: ").lower()
# count = parent_string.count(check_substring)

count = 0
for s in range(len(parent_string)):
  if parent_string[s:s+len(check_substring)] == check_substring:
    count += 1
  else:
    pass

print("'{}' is in Master String {} times".format(check_substring.upper(), count))