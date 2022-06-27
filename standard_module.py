# random.sample：重複なし
import random
ans = random.sample(["apple", "banana", "orange", "grape", "peach"], k=2)
print(ans)

# random.choices：重複あり
ans = random.choices(["apple", "banana", "orange", "grape", "peach"], k=2)
print(ans)

# statistics
import statistics
print(statistics.mean([3, 4, 5, 4]))

# string
import string

t = string.Template('My name is ${name}. I am ${age} years old.')
t.substitute({'name': 'Diop', 'age': 24})
# 同様の結果
'My name is {name}. I am {age} years old.'.format(name = 'Diop', age = 24)

# heapq.heapify() はリストをヒーププロパティを持つリストに変換する。
from heapq import heapify
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
print(data)