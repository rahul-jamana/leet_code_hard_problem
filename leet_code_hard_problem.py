def de():
    def fun(nums, k):

        l = 0
        dici = {}
        ans = 0
        for r in range(len(nums)):
            if nums[r] not in dici:
                dici[nums[r]] = 1
            else:
                dici[nums[r]] += 1
            while len(dici) > k:
                dici[nums[l]] -= 1
                if dici[nums[l]] == 0:
                    dici.pop(nums[l])
                l += 1
            ans += r - l + 1
            print(ans)
            print(nums[l:r + 1])
        return ans

    nums = [1, 2, 1, 2, 3]
    k = 2
    ans = (fun(nums, k) - fun(nums, k - 1))
    return ans


print(de())