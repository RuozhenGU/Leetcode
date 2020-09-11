
/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int incre = 0;
        
        ListNode* head1 = l1;
        ListNode* head2 = l2;
        
        ListNode* soln = head1;  //important
        int num1, num2;
        while(true) {
            if (!l1 && !l2) {
                break; 
            } else {
                if (!l1) {
                    num1 = 0; // so important
                    soln = head2; //important
                } else {
                    num1 = l1->val;
                }
                if (!l2) {
                    num2 = 0;
                } else {
                    num2 = l2->val;
                }
                
                int sum_num = num1 + num2 + incre;
                
                if (sum_num >= 10) {
                    incre = 1;
                } else {
                    incre = 0;
                }
                
                // update both
                if (l1) l1->val = sum_num % 10;
                if (l2) l2->val = sum_num % 10;
                
                if (l1) l1 = l1->next;
                if (l2) l2 = l2->next;
            }
        }
        if (incre == 1) { // edge case [5], [5]
            //insert nodess
            ListNode *node_to_insert = new ListNode{1, nullptr};
            ListNode *curr = soln;
            while (curr->next) {
                curr = curr->next;
            }
            curr->next = node_to_insert;
        }
        return soln;
        
    }
};