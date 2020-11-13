/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {

    var ans = new ListNode(0)
    var head = ans
    var partial = 0
    var carry = 0

    while (l1 !== null || l2 !== null || partial > 0) {
        if (l1 !== null) {
            partial = partial + l1.val
            l1 = l1.next
        }
        if (l2 !== null) {
            partial = partial + l2.val
            l2 = l2.next
        }
        if (partial >= 10) {
            carry = 1
            partial -= 10
        }

        head.next = new ListNode(partial)
        head = head.next

        partial = carry
        carry = 0
    }

    return ans.next

};
