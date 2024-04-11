def maxSum(nums1, nums2):
    MOD = 10**9 + 7  # 用于结果的模运算
    dp1, dp2 = 0, 0  # 初始化两个dp值来记录遍历时的最大得分
    i, j = 0, 0  # 初始化双指针，分别对应nums1和nums2的索引
    n, m = len(nums1), len(nums2)  # 记录两个数组的长度

    # 遍历两个数组直到至少一个数组被完全遍历
    while i < n and j < m:
        if nums1[i] < nums2[j]:
            # 如果nums1的当前元素小于nums2的当前元素，增加dp1的值并移动指针i
            dp1 += nums1[i]
            i += 1
        elif nums1[i] > nums2[j]:
            # 如果nums2的当前元素小于nums1的当前元素，增加dp2的值并移动指针j
            dp2 += nums2[j]
            j += 1
        else:
            # 如果当前元素在两个数组中都出现，选择最大的dp值加上当前值，然后同时移动两个指针
            max_dp = max(dp1, dp2) + nums1[i]
            dp1, dp2 = max_dp, max_dp
            i += 1
            j += 1

    # 处理剩下的元素
    while i < n:
        dp1 += nums1[i]
        i += 1
    while j < m:
        dp2 += nums2[j]
        j += 1

    # 返回两个dp中的最大值，并对MOD取余
    return max(dp1, dp2) % MOD

# 示例输入
nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]

# 调用函数并打印结果
print(maxSum(nums1, nums2))
