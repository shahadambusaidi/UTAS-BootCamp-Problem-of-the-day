#Prob5
'''given a list of N fractions, represented of two  lists numerator and donominator the task is to determine the count of pairs of fractions that equals 1'''


from math import gcd

# Function to calculate the count of pairs equal to 1
def countPairsEqualOne(numerators, denominators):
    count = 0
    n = len(numerators)

    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the greatest common divisor (GCD)
            common_divisor = gcd(numerators[i], denominators[i])
            
            # Check if the fractions are equivalent to 1
            if (
                numerators[i] // common_divisor == denominators[j] // common_divisor and
                numerators[j] // common_divisor == denominators[i] // common_divisor
            ):
                count += 1

    return count

# Input: List of numerators and denominators
numerators = [1, 2, 3, 4, 5, 6]
denominators = [2, 4, 6, 8, 10, 12]

# Calculate the count of pairs equal to 1
result = countPairsEqualOne(numerators, denominators)

# Print the result
print(f"The count of pairs of fractions equal to 1 is: {result}")