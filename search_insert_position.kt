// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.

// My solution:
class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        nums.forEachIndexed { index, i ->
            if (i >= target) {
                return index
            }
        }
        return nums.size
    }
}
