# メッセージの表示順を確認
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("ゼロで割ってるよ！")
    else:
        print("計算結果はこちら", result)
    finally:
        print("後処理！")

divide("2", "1")

