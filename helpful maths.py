s = input()  # Read the input string

# Extract the summands by splitting the string at the '+' character
summands = s.split('+')

# Sort the summands in non-decreasing order
sorted_summands = sorted(summands)

# Join the sorted summands using the '+' character as the separator
new_sum = '+'.join(sorted_summands)

# Print the rearranged sum
print(new_sum)
