balance=345345
def buy_things(item, price):
    global balance
    balance=balance-price*item
    print('balance inside the function', balance)

buy_things(23,345)