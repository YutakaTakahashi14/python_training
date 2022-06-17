# listからiteratorを取り出す
nums = [1,2,3]
print(iter(nums))

i = iter(nums)
print(next(i))
print(next(i))
print(next(i))
# StopIteration
# print(next(i))

# generator
def get1to3():
    yield 1;
    yield 2;
    yield 3;

gen = get1to3()
print(gen)
for i in gen:
    print(i)
