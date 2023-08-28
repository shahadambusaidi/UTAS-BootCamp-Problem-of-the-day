#Prob 11
'''Given a string S, find the longest palindromic substring in S.
S[i..j] where 0 <= i <= j <= len(S).
A palindrome string is a string that reads the same backward.
More formally, S is a palindrome if reverse(S) = S.
In case of conflict, return the substring which occurs first (with the least starting index).
'''

def longest_palindromic_substring(input_string):
    string_length = len(input_string)
    start_of_longest = 0
    max_length = 1

    # Create a table to store palindromic substring information
    dp = [[False] * string_length for _ in range(string_length)]

    # All substrings of length 1 are palindromic
    for i in range(string_length):
        dp[i][i] = True

    # Check for substrings of length 2
    for i in range(string_length - 1):
        if input_string[i] == input_string[i + 1]:
            dp[i][i + 1] = True
            start_of_longest = i
            max_length = 2

    # Check for substrings of length greater than 2
    for length in range(3, string_length + 1):
        for i in range(string_length - length + 1):
            j = i + length - 1
            if dp[i + 1][j - 1] and input_string[i] == input_string[j]:
                dp[i][j] = True
                if length > max_length:
                    start_of_longest = i
                    max_length = length

    return input_string[start_of_longest:start_of_longest + max_length]

# Example input
input_string = "aaabbaa"
result = longest_palindromic_substring(input_string)
print("Longest palindromic substring:", result)