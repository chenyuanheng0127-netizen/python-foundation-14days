"""
Day 2 - LeetCode Practice
包含 5 道经典基础题：Two Sum, Valid Anagram, Contains Duplicate,
Merge Two Sorted Lists, Maximum Subarray
"""

# 1. Two Sum (数组 + 哈希表)
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

# 2. Valid Anagram (字符串 + 哈希表)
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# 3. Contains Duplicate (集合)
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# 4. Merge Two Sorted Lists (链表)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

# Helper: 打印链表
def printList(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    return vals

# 5. Maximum Subarray (动态规划)
def maxSubArray(nums):
    current = best = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


# =============================
# 测试代码
# =============================
if __name__ == "__main__":
    # 1. Two Sum
    print("Two Sum:", twoSum([2,7,11,15], 9))  # [0, 1]

    # 2. Valid Anagram
    print("Valid Anagram:", isAnagram("anagram", "nagaram"))  # True

    # 3. Contains Duplicate
    print("Contains Duplicate:", containsDuplicate([1,2,3,1]))  # True

    # 4. Merge Two Sorted Lists
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLists(l1, l2)
    print("Merge Two Lists:", printList(merged))  # [1,1,2,3,4,4]

    # 5. Maximum Subarray
    print("Maximum Subarray:", maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6