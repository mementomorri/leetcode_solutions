/*
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

 

Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
*/
func calculateArea(low, high, first, second int ) int { 
    if second > first {
        return first * (high - low)
    } else {
        return second * (high - low)
    }
}

func maxArea(height []int) int {
    low_pointer := 0
    high_pointer := len(height) - 1
    max_area := 0
    for low_pointer < high_pointer {
        newSum := calculateArea(low_pointer, high_pointer, height[low_pointer], height[high_pointer] ) 
        if newSum > max_area {
            max_area = newSum
        }
        if height[low_pointer] < height[high_pointer] {
            low_pointer++
        } else {
            high_pointer--
        }

    }
    return max_area
}
