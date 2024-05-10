/*
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]

 

Constraints:

    2 <= arr.length <= 1000
    1 <= arr[i] <= 3 * 104
    arr[0] == 1
    arr[i] is a prime number for i > 0.
    All the numbers of arr are unique and sorted in strictly increasing order.
    1 <= k <= arr.length * (arr.length - 1) / 2

 
Follow up: Can you solve the problem with better than O(n2) complexity?
*/


func kthSmallestPrimeFraction(arr []int, k int) []int {
	fractionsArray := [][]float64{}

	for i := 0; i < len(arr); i++ {
		for j := i; j < len(arr); j++ {
			if j > i {
				frac := float64(float64(arr[i]) / float64(arr[j]))
				fractionsArray = append(fractionsArray, []float64{float64(arr[i]), float64(arr[j]), float64(frac)})
			}
		}
	}
	sort.Slice(fractionsArray, func(i, j int) bool {
		return fractionsArray[i][2] < fractionsArray[j][2]
	})
	res := []int{}
	for _, val := range fractionsArray[k-1][:2] {
		res = append(res, int(val))
	}
	return res
}
