# 定義
fruits = {'apple':'red','banana':'yellow','grape':'purple'}
print("appleの色は" + fruits['apple'] + "です")

# 更新
fruits['apple'] = 'green'
print("appleの色は" + fruits['apple'] + "です")

# 追加
fruits['peach'] = 'pink'
print("peachの色は" + fruits['peach'] + "です")

# 削除　※他にもメソッドあり
target = fruits.pop('banana')
print(target)
print(fruits)
print("=====================================")

# for文で取得
for fruit_key in fruits:
    print(fruit_key + 'の色は' + fruits[fruit_key] + 'です')
    if fruit_key == 'apple':
        break