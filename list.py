# 定義
foods = ['pasta','curry','sushi','nattou','moyashi']
print('好きな食べ物は'+ foods[2] +'です')

# 更新
foods[1] = 'pizza'
print('「購入商品は', foods[1],'です。」')
print('「購入商品は' + foods[1] + 'です。」')

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

# 2次元配列の更新、抽出
pairs = [['Alice', 'Bob'],['Eve', 'Mike']]
pairs[1] = ['Don','Diop']

if pairs[1][0] == 'Eve':
    print('Welcome,', pairs[1][0])
else:
    print('Oops!,', pairs[0][1])

# for,continue文
numbers = [1,2,3,4,5]
for number in numbers:
    if number % 3 == 0:
        continue
    print(number)

## 1はtrue扱いなので無限に表示される。
# while 1:
#     print('「お疲れ様でした」')

## 空のシーケンスまたはコレクション: ‘’, (), [], {}, set(), range(0) は False と判断される。
if []:
    print('True')
else:
    print('False') 

# range
print(range(5))
print(list(range(5)))

# リスト内包表記
num = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10]]

col = [row[2] for row in num]
print(col)

# for-else文：最後にelse節内を実行
n = 3
number = [[10,3],[16,3],[12,9]]

for i in range(n):
    # 切り捨て除算
    if number[i][0] // number[i][1] % 2 == 0:
        print('偶数です')
        break
else:
    print('すべて奇数です')

# zip
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)