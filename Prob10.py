#Prob10

# Input string
S = "WomensDAY"

# Initialize variables
diff_count = 0  # Difference count
diff_dict = {0: 1}  # Dictionary to store difference counts

count = 0  # Initialize the count of substrings with equal case letters

for char in S:
    if char.islower():
        diff_count -= 1
    else:
        diff_count += 1

    # Check if the negative counterpart exists in the dictionary
    if diff_count in diff_dict:
        count += diff_dict[diff_count]

    # Update the dictionary with the current difference count
    if diff_count in diff_dict:
        diff_dict[diff_count] += 1
    else:
        diff_dict[diff_count] = 1

# The final 'count' variable