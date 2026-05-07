numbers = [
    5900225475360,
    5878467178551,
    8397471819530,
    7282955966784,
    8182898216504,
    3746102112481,
    4978036293743,
    1720247570470,
]

total = sum(numbers)
count = len(numbers)
mean = total / count
minimum = min(numbers)
maximum = max(numbers)

sorted_nums = sorted(numbers)
mid = count // 2
median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 if count % 2 == 0 else sorted_nums[mid]

print(f"Count:   {count}")
print(f"Sum:     {total}")
print(f"Min:     {minimum}")
print(f"Max:     {maximum}")
print(f"Mean:    {mean:.2f}")
print(f"Median:  {median:.2f}")
