from order_class import Menu

# 関数宣言
def get_order(menus):
    while True:
        order = input('商品番号を選択してください:')
        if not order.isdecimal() :
            print('数値で番号を入力してください')
            continue
        elif not 0 <= int(order) < len(menus) :
            print('正しい番号を入力してください')
            continue
        return int(order)

def get_count(selected_menu_name):
    while True:
        count = input('購入する' + selected_menu_name + 'の個数を入力してください:')
        if not count.isdecimal() :
            print('数値で番号を入力してください')
            continue
        return int(count)

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
    # 商品注文を取得
    order = get_order(menus)
    # 選択されたインスタンスを変数に代入
    selected_menu_index = menus[order]
    selected_menu_name = menus[order].name
    # 注文数を取得
    count = get_count(selected_menu_name)
    # 合計金額の算出処理
    total_price = selected_menu_index.get_total_price(count)
    # イートインの有無を取得
    select_eat_in = selected_menu_index.get_accept_select_eat_in()
    # 税込金額の算出
    taxed_total_price = selected_menu_index.get_taxed_total_price(total_price, select_eat_in)
    # 購入の承諾を取得
    selected_menu_index.get_accept_purchase(selected_menu_name, count, taxed_total_price)
    # 終了選択を取得
    end = selected_menu_index.get_end()
    if end :
        break
    else :
        continue