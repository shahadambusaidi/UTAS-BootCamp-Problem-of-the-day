#Prob 13
'''Given a set of integers, find all distinct numbers that can
be generated from the subsets of the given set.'''

def generate_subsets(input_set):
    n = len(input_set)
    all_subsets = []

    # Generate all possible subsets using bitwise manipulation
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(input_set[j])
        all_subsets.append(subset)

    return all_subsets

def find_distinct_subset_sums(input_set):
    subsets = generate_subsets(input_set)
    distinct_sums = set()

    for subset in subsets:
        subset_sum = sum(subset)
        distinct_sums.add(subset_sum)

    return distinct_sums

# Example input
input_set = [1, 2, 3, 4, 5]
result = find_distinct_subset_sums(input_set)
print("Distinct subset sums:", result)