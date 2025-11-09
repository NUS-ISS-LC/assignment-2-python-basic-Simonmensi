def find(nums, target):
# write your implementation here
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i

if __name__ == "__main__":
    print(find([1,3,4,6],9))

