class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def message(self):
        return self.name + ': ' + str(self.price)  + '円'

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

    def get_accept_select_eat_in (self):
        while True:
            select_eat_in = input('店内で過ごされますか？:(y/n)')
            if select_eat_in == 'y':
                return True
            elif select_eat_in == 'n':
                return False
            else:
                print(' y か n を入力してください')
                continue

    def get_taxed_total_price(self, total_price, select_eat_in):
        if select_eat_in :
            return round(total_price * 1.1)
        else :
            return round(total_price * 1.08)

    def get_accept_purchase (self, selected_menu_name, count, taxed_total_price):
        while True:
            accept_purchase = input(selected_menu_name + 'を' + str(count) + '個で税込合計' + str(taxed_total_price) + '円になります。購入されますか？:(y/n)')
            if accept_purchase == 'y':
                print('ありがとうございます！')
                break
            elif accept_purchase == 'n':
                break
            else:
                print(' y か n を入力してください')
                continue

    def get_end(self):
        while True:
            cancel = input('購入を終了しますか？(y/n):')
            if cancel == 'y':
                return True
            elif cancel == 'n':
                return False
            else:
                print(' y か n を入力してください')
                continue