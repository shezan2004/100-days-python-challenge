# Helper function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list for printing
def linked_list_to_list(head):
    arr = []
    current = head
    while current is not None:
        arr.append(current.val)
        current = current.next
    return arr

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode()
        current = dummy
        
        p1 = list1
        p2 = list2
        
        while p1 is not None and p2 is not None:
            
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
                
            current = current.next
            
        if p1 is not None:
            current.next = p1
        elif p2 is not None:
            current.next = p2
            
        return dummy.next

# --- Test Cases ---

print("--- Running Tests ---")
solution = Solution()

# Example 1: Standard merge
list1_arr_1 = [1, 2, 4]
list2_arr_1 = [1, 3, 4]
L1_1 = create_linked_list(list1_arr_1)
L2_1 = create_linked_list(list2_arr_1)
merged_head_1 = solution.mergeTwoLists(L1_1, L2_1)
print(f"Test 1 Input: L1={list1_arr_1}, L2={list2_arr_1}")
print(f"Test 1 Output: {linked_list_to_list(merged_head_1)}")
print(f"Test 1 Expected: [1, 1, 2, 3, 4, 4]")

print("-" * 20)

# Example 2: Empty list
list1_arr_2 = []
list2_arr_2 = [0]
L1_2 = create_linked_list(list1_arr_2)
L2_2 = create_linked_list(list2_arr_2)
merged_head_2 = solution.mergeTwoLists(L1_2, L2_2)
print(f"Test 2 Input: L1={list1_arr_2}, L2={list2_arr_2}")
print(f"Test 2 Output: {linked_list_to_list(merged_head_2)}")
print(f"Test 2 Expected: [0]")

print("-" * 20)

# Example 3: Both empty
list1_arr_3 = []
list2_arr_3 = []
L1_3 = create_linked_list(list1_arr_3)
L2_3 = create_linked_list(list2_arr_3)
merged_head_3 = solution.mergeTwoLists(L1_3, L2_3)
print(f"Test 3 Input: L1={list1_arr_3}, L2={list2_arr_3}")
print(f"Test 3 Output: {linked_list_to_list(merged_head_3)}")
print(f"Test 3 Expected: []")

print("-" * 20)

# Example 4: One list much longer
list1_arr_4 = [5, 6, 7]
list2_arr_4 = [1, 2, 3, 4]
L1_4 = create_linked_list(list1_arr_4)
L2_4 = create_linked_list(list2_arr_4)
merged_head_4 = solution.mergeTwoLists(L1_4, L2_4)
print(f"Test 4 Input: L1={list1_arr_4}, L2={list2_arr_4}")
print(f"Test 4 Output: {linked_list_to_list(merged_head_4)}")
print(f"Test 4 Expected: [1, 2, 3, 4, 5, 6, 7]")