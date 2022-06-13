# 無名関数
x1 = lambda a,b :a + b + 2
print(x1(1,3))

# map
nums = [1,3,5,7,9]
x2 = lambda x :x + 2
print(map(x2,nums))
# mapオブジェクトからlistに変換
print(list(map(x2,nums)))

print(list(map(lambda x : x * 2,nums)))

# filter
nums = [1,2,3,4,11,12,13,14,15]
print(list(filter(lambda x : (x % 2) == 0, nums)))