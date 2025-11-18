from typing import Optional

# Definition for singly-linked list.
# You need this class in your file to test it.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy head node. This simplifies the logic, as we
        # don't need a special case for creating the first node of the result.
        dummy_head = ListNode(0)
        
        # 'current' will point to the last node we've added to our result list.
        current = dummy_head
        
        # 'carry' will store the amount we carry over to the next digit.
        carry = 0

        # We loop as long as there are digits in l1, l2, or we have a remaining carry.
        while l1 is not None or l2 is not None or carry != 0:
            
            # 1. Get the values of the current nodes. If a list is
            #    shorter, we treat its value as 0 for this position.
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            # 2. Calculate the sum for the current digit position.
            total_sum = val1 + val2 + carry

            # 3. Update the 'carry' and 'new_digit'.
            #    e.g., divmod(15, 10) returns (1, 5) -> (carry, new_digit)
            carry, new_digit = divmod(total_sum, 10)

            # 4. Create a new node with this digit and attach it to our result list.
            current.next = ListNode(new_digit)
            
            # 5. Move 'current' forward to this new node.
            current = current.next

            # 6. Move l1 and l2 pointers forward, if they are not null.
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # The 'dummy_head' was just a placeholder. The actual
        # start of our summed list is dummy_head.next.
        return dummy_head.next

# Helper function to print a linked list
# Notice the indentation here - this fixes the IndentationError
def print_list(node: Optional[ListNode]):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result) if result else "[]")

# This "if __name__ == '__main__':" block ensures this
# test code only runs when you execute the file directly.
if __name__ == "__main__":
    
    # 1. Create the input lists: l1 = [2, 4, 3] and l2 = [5, 6, 4]
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    print("Input List 1:")
    print_list(l1)
    
    print("Input List 2:")
    print_list(l2)

    # 2. Create an instance of the Solution class
    sol = Solution()

    # 3. Call the method
    result_list = sol.addTwoNumbers(l1, l2)

    # 4. Print the result
    print("\nResult List:")
    print_list(result_list)