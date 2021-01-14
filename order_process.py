from order_class import Menu
# インスタンス生成
menu1 = Menu("コーヒー", 300)
menu2 = Menu("紅茶", 350)
menu3 = Menu("カフェラテ", 370)
menu4 = Menu("抹茶ラテ", 380)
menu5 = Menu("ハーブティー", 450)

# インスタンスを配列に格納
menus = [
    menu1, menu2, menu3, menu4, menu5
]

# 購入処理
while True:
    index = 0
    # 商品の表示
    for menu in menus :
        print(str(index) + '. ' + menu.message())
        index += 1
    # 商品注文
    order = int(input('商品番号を選択してください:'))
    selected_menu_index = menus[order]
    selected_menu_name = menus[order].name
    count = int(input('購入する' + selected_menu_name + 'の個数を入力してください:'))
    # 合計金額の算出処理
    total_price = selected_menu_index.get_total_price(count)
    # イートインの有無
    select_eat_in = selected_menu_index.get_accept_select_eat_in()
    # 税込金額の算出
    taxed_total_price = selected_menu_index.get_taxed_total_price(total_price, select_eat_in)
    # 購入の承諾
    selected_menu_index.get_accept_purchase(selected_menu_name, count, taxed_total_price)
    # 終了
    end = selected_menu_index.get_end()
    if end :
        break
    else :
        continue