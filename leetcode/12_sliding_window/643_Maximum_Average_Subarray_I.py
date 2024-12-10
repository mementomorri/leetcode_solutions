def findMaxAverage(nums: list[int], k: int) -> float:
    left, right = 0, k - 1
    curr_sum = sum(nums[left:k])
    max_sum = curr_sum

    while right < len(nums) - 1:
        curr_sum -= nums[left]
        left += 1

        right += 1
        curr_sum += nums[right]

        max_sum = max(curr_sum, max_sum)

    return max_sum / k


if __name__ == '__main__':
    print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
