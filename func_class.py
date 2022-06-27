# 引数指定
def fugafuga(title,content = 'default_content', number = 4):
    content = 'content'
    print(title, end=' ')
    print(content, end=' ')
    print(number)
 
fugafuga(title = 'title_default', content = 'None', number = 5) 

# returnしていないことに注意
def add(a):   
    b = 10
    print(a + b)
a = 3
print(add(a))

# クラスオブジェクト.関数名(インスタンスオブジェクト, 関数の引数)
class MyClass:

    i = 100

    def f(self, i):
        data = 20
        return data * i

x = MyClass()
print(x.f(300))

# クラス変数呼び出し
class Dog:

    name  = 'Fido'

    def __init__(self, name):
        self.name = name

d = Dog('Buddy')
print(Dog.name)
