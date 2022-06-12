from menu_item import MenuItem

menu_item1 = MenuItem('チョコケーキ')
# menu_item1.name = 'みたらし団子'
menu_item1.price = 100
print(menu_item1.info())

print("合計は" +  str(menu_item1.get_total_price(3)) + "円です")