class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #O(N+N)t 
        # O(N)s
        # using the hashtable visited solution
        node_hash_table = {}
        
        current_1 = headA
        current_2 = headB 
        
        while current_1:
            
            node_hash_table[current_1] = current_1
            
            current_1 = current_1.next 
            
        while current_2:
            
            if current_2 in node_hash_table:
                return current_2
            current_2 = current_2.next 
            
        return None
            
