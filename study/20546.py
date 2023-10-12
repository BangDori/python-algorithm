import sys
input = sys.stdin.readline

def buy_JH(money):
    JH_money = money
    JH_stocks = 0

    for stock in stocks:
        if JH_money == 0:
            break
        if JH_money > stock:
            buy_stock_count = JH_money // stock

            JH_money -= buy_stock_count * stock
            JH_stocks += buy_stock_count
    
    JH_money = JH_money + JH_stocks * stocks[len(stocks)-1]
    return JH_money

def buy_SM(money):
    SM_money = money
    SM_stocks = 0

    state = (0, 0)
    prev = stocks[0]

    for stock in stocks:
        if stock > prev:
            state = (state[0]+1, 0)
        elif stock < prev:
            state = (0, state[1]+1)
        
        if state[0] < 3 and state[1] < 3:
            continue

        if state[0] >= 3:
            SM_money += SM_stocks * stock
            SM_stocks = 0
        elif state[1] >= 3:
            if SM_money > stock:
                buy_stock_count = SM_money // stock

                SM_money -= buy_stock_count * stock
                SM_stocks += buy_stock_count

    SM_money = SM_money + SM_stocks * stocks[len(stocks)-1]
    return SM_money

money = int(input())
stocks = list(map(int, input().split()))

final_JH_money = buy_JH(money)
final_SM_money = buy_SM(money)

if final_JH_money > final_SM_money:
    print('BNP')
elif final_JH_money == final_SM_money:
    print('SAMESAME')
else:
    print('TIMING')