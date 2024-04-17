# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()  # Create a dummy node to start the merged list
        tail = dummy        # This will be the last node in the merged list

        while list1 and list2:
            if list1.val <= list2.val:  # Check which node has the smaller value
                tail.next = list1       # Attach list1 node to the merged list
                list1 = list1.next      # Move to the next node in list1
            else:
                tail.next = list2       # Attach list2 node to the merged list
                list2 = list2.next      # Move to the next node in list2
            tail = tail.next            # Move the tail to the end of the merged list

        # Attach the remaining part of list1 or list2, if any
        tail.next = list1 if list1 else list2

        return dummy.next 

        
        