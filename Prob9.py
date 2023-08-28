#Prob9

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head, k):
    prev = None
    current = head
    count = 0

    while current and count < k:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        count += 1

    return prev, current

def reverse_first_k_and_remaining(head, k):
    n = 0
    temp = head
    while temp:
        n += 1
        temp = temp.next
    
    if n < k:
        return head
    
    first_part_head, second_part_head = reverse_linked_list(head, k)
    second_part_head, _ = reverse_linked_list(second_part_head, n - k)
    first_part_end = first_part_head

    while first_part_end.next:
        first_part_end = first_part_end.next

    first_part_end.next = second_part_head

    return first_part_head

# Create the linked list
head = ListNode(1)
current = head
for val in [2, 3, 4, 5]:
    current.next = ListNode(val)
    current = current.next

# Reverse the first k elements and the remaining elements with k=2
k = 2
new_head = reverse_first_k_and_remaining(head, k)

# Print the reversed linked list
while new_head:
    print(new_head.value, end=" ")
    new_head = new_head.next