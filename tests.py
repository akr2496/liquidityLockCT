#! usr/bin python
from fileinput import filename
from math import nan
import requests
import csv
import pandas as pd
import random
import subprocess
import os
import mid 
import limits


def test_live_data(type):
    # Set your Alpha Vantage API key
    API_KEY = 'YOUR_API_KEY'

    # Set the list of stocks to retrieve data for
    # stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'UBER', 'AMD','SNAP','F','T', 'WFC']
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    # DataFrame to store all stock
    df_stocks = pd.DataFrame()
    df_stockOrderList = pd.DataFrame()
    # df_stock_row = pd.DataFrame()
    csv_stock = []

    # Loop through the list of stocks and retrieve data
    for stock in stocks:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={API_KEY}&datatype=csv'
        response = requests.get(url)
        data = response.content.decode('utf-8')

        data = data.split('\n')
        label = data[0].split(',')
        label_dict = {}
        for i in range(0, len(label)):
            label_dict[label[i]] = ''
        print(label_dict)
        for i in range(0, len(data)-1):
            if i ==0:
                label_dict['Product'] = ''
                df_stocks = pd.DataFrame(label_dict, index=[0])
            else:
                data[i] = data[i] + ',' + stock
                data[i] = data[i].split(',')
                df_stocks.loc[len(df_stocks.index)] = data[i]
        
        df_stockOrderList = pd.concat([df_stockOrderList, df_stocks],ignore_index=True)
    
    # print(df_stockOrderList)

    df_sol = df_stockOrderList.drop(['open',
                            'timestamp', 
                            'low',
                            'close',
                            'adjusted_close',
                            'dividend_amount',
                            'split_coefficient\r'], axis =1)
    # print(df_sol)

    df_sol.rename(columns={'high':'Price', 'volume':'Quantity'}, inplace=True)
    # print(df_sol)

    df_sol = df_sol[df_sol['Quantity'] !='']
    df_sol = df_sol[df_sol['Quantity'] != nan]
    # print(df_sol)

    #res is direction column
    length = df_sol.shape[0]
    res = random.sample(range(0, length), length)
    # print(res)
    party = [None]*length
    names = ['Aasha', 'Rohan', 'Ravi', 'Prakhar', 'Awanish', 'Robert', 'Michelle', 'Zoe', 'Ayushi', 'Mohit' ]

    for i in range(0, length):
        if res[i]%10 == 1:
            party[i] = names[0]
        elif res[i]%10 == 2:
            party[i] = names[1]
        elif res[i]%10 == 3:
            party[i] = names[2]
        elif res[i]%10 == 4:
            party[i] = names[3]
        elif res[i]%10 == 5:
            party[i] = names[4]
        elif res[i]%10 == 6:
            party[i] = names[5]
        elif res[i]%10 == 7:
            party[i] = names[6]
        elif res[i]%10 == 8:
            party[i] = names[7]
        elif res[i]%10 == 9:
            party[i] = names[8]
        else: 
            party[i] = names[9]
    # print(party)

    for i in range(0, length):
        if res[i]%2 ==0:
            res[i] = 'Buy'
        else:
            res[i] = 'Sell'
        
    # print(res)

    df_sol['Direction'] = res
    df_sol['Party'] = party

    # print(df_sol)

    # df_sol.to_csv('stockOrderList.csv')

    limit_dict = {'Party': '', "Direction":'', "NetLimit":''}
    df_limit =pd.DataFrame(limit_dict, index=[0])
    for name in names:
        df_limit.loc[len(df_limit.index)] = [name, "Sell",  random.randint(4000000,40000000)]
        df_limit.loc[len(df_limit.index)] = [name, "Buy",  random.randint(4000000,40000000)]

    df_limit = df_limit[df_limit['Party'] !='']
    df_limit.to_csv('partyOrderLimit.csv')

    if type == 'DF':
        return df_sol, df_limit

if __name__ == "__main__":
    # print("indriver") 
    #given files in Coding Challenge
    filename = 'ProblemSetData.csv'
    file_limit = 'sampleLimitSet2.csv'

    ###############________________________TESTING FOR CORRECTNESS__________________######################
    ##Testcase1: lets make orderlist in same direction --> No trade --> No Volume & No P&L
    #  [Pre Trade limit Implementation]     ---> Hitting limits for all in same direction if limit breached
    # filename ='allSameDirection.csv'
    # mid.midImplement("File", filename)
    # limits.limitsImplement("File", filename, file_limit)

    ##Testcase2: All trade corresponds to different product [No same product row]
    #----> No trade (either buy or sell order will be there) ----> No Volume & P&L 
    #----> Hitting limits on given direction if breached
    # filename = 'allDifferentProduct.csv'
    # mid.midImplement("File", filename)
    # limits.limitsImplement("File", filename, file_limit)

    ## Testcase3: All order volume/quantity is same and same buy-sell order on  exist 
    #----> Maximum Trade --> volume = sum of order volume /2 since buy-sell pair matching to make it half (7buy vol + 7sell vol = 7 trade vol)
    #----> if volume < Net limit --> No limit breach 
    #      else all party breach ---> volme != sum of order volume /2
    filename = 'testcase3.csv'


    ###testcase4:  NO Net limit ---> Mid.py 

    ###Testcase5: Net limit > highest volume order ---> mid.py
    # filename = 'ProblemSetData.csv'
    # file_limit = 'testcase5.csv'

    ###Testcase6: Zero Price  => No P&L or Zero order volume => No Trade
    # filename = 'testcase6a.csv'

    ###Testcase7: same price & same volume for all order ---> Zero P&L for all party 
    filename = 'testcase7.csv'
    

    print("+++++++++++++++++++++_________mid.py_________++++++++++++++++++++++")
    mid.midImplement("File", filename)
    print("+++++++++++++++++++++_________limits.py_________++++++++++++++++++++++")
    limits.limitsImplement("File", filename, file_limit)


    #-------------------------for live data testing using dataframe--------------------
    #sometime data does not comes from aplhavantage.. so wait for sometime and try again
    # **** DF type is causing some error, please use 'File' type and pass required files
    # df, df_limit = test_live_data('DF')
    #-------by storing data in local storage
    #test_live_data('')
    # filename = 'stockOrderList.csv'
    # file_limit = 'partyOrderLimit.csv'

    ########################-------execute mid.py----------#################### 
    # Using file choose 'File' as type 
    # using DataFrame chose 'DF' as type 
    # mid.midImplement('File',filename)
    # mid.midImplement('File',filename)
    ########################-------execute limits.py----------#################### 
    # Using file choose 'File' as type 
    # limits.limitsImplement('File',filename, file_limit)
    # using DataFrame chose 'DF' as type 
    # limits.limitsImplement('DF',df, df_limit)
    # test_live_data()
    
    
    # subprocess.Popen(["/Users/ashixshranjan/Desktop/InterviewPrep/LiquidityLockTest/mid.py", "File", filename, "Hi"])