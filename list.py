# 定義
foods = ['pasta','curry','sushi','nattou','moyashi']
print('好きな食べ物は'+ foods[2] +'です')

# 更新
foods[1] = 'pizza'
print(foods[1])

# 追加
foods.append('kimuchi')
print(foods)

# 指定した文字列にヒットした要素を削除
# 存在しないとエラーになるので注意
foods.remove('sushi')
print(foods)

# 削除したい要素をインデックスで指定する
del foods[-1]
print(foods)

# 全削除
foods.clear()
print(foods)

# for,continue文
numbers = [1,2,3,4,5]
for number in numbers:
    if number % 3 == 0:
        continue
    print(number)
