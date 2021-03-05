# A program that returns the second largest number from user input
user_input = input("Please enter five integers: ")
user_inputs = user_input.split(" ")

user_inputs[0] = int(user_inputs[0])
user_inputs[1] = int(user_inputs[1])
user_inputs[3] = int(user_inputs[3])
user_inputs[2] = int(user_inputs[2])
user_inputs[4] = int(user_inputs[4])

user_inputs.sort()


print(f"The the second largest integer is {user_inputs[-2]}.")
