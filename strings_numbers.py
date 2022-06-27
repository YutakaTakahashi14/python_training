# 変数 letters から ‘Happy Birthday’ の真ん中のスペースを取り除いて ‘HappyBirthday’ を作りたい。
letters = "Happy Birthday"
print(letters[:5] + letters[6:] )

#  / は無限には表示されず、四捨五入もされない。
print(2 / 3)

# 負の数でも指定可能。
letter = 'diveintoexam'
print(letter[-8])

# 文字列は不変のためエラー
# Zen = 'SimpleIsBetterThanComplex'
# Zen[0] = 'J'

# 空白が表示
Zen = 'BeautifulIsBetterThanUgly'
print(Zen[1000:10000])