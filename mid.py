#! usr/bin python
import pandas as pd
import math
import sys


# ASSUMPTIONS
# 1. Trade Matching algorithm is similar to FIFO. Order on top of trade list is matched first, then second and so on
#         matched to nearest order in sequence
# 2. Partial excecution is allowed --> if order is not filled in one trade, multiple trade is allowed to fill it
# 3. Stay on same till filled or no matching available
# 4. No self buy/sell order


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++PSEUDOCODE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

# load csv into dataframe, say df and make copy (new_df)
# Split new_df into n dataframes where n = number of unique product (productDict)
# create 2 dataframe: df_trade_list and df_PL to store trade order and PL associated in those order respectively
# create 2 dictionary: trade and pl to track individual trade and associated pls 
# For each Product:
#     store product orders in dataframe (df_product)
#     create 3 lists: row_indices, sell_indices, buy_indices to track flow of trade
#     i = 0
#     while i < len(row_indices) and sell_indices is not empty and buy_indices is not empty
#         (Sell Order)
#         if firstOrder[Direction] is Sell:
#             create all required variables
#             if sell_quantity > buy_quantity:
#                 sellOrderQuantity[i] = abs(sell_quantity-buy_quantity)
#                 buyOrderQuantity[topIdx in buy_indices]  = 0
#                 remove matching buy order from row_indices, buy_indices sequentially
                
#             else:
#                 buyOrderQuantity[topIdx in buy_indices] = abs(sell_quantity-buy_quantity)
#                 sellOrderQuantity[i] = 0
#                 remove sell order from sell_indices
#                 move to next order in order list (i +=1)
#             stores pl of seller and buyer in df_PL using pl

#         (Buy Order)
#         else:
#             create all required variables
#             if buy_quantity > sell_quantity:
#                 buyOrderQuantity[i] = abs(sell_quantity-buy_quantity)
#                 sellOrderQuantity[topIdx in sell_indices] = 0
#                 remove matching buy order from row_indices, sell_indices sequentially
                
#             else:
#                 sellOrderQuantity[topIdx in sell_indices] = abs(sell_quantity-buy_quantity)
#                 buyOrderQuantity[i] = 0
#                 remove buy order from buy_indices
#                 move to next order in order list (i +=1)
#             stores pl of seller and buyer in df_PL using pl

#     store trade in df_trade_list using trade (dictionary to denote individual trade)

# modify and manipulate df_trade_list and df_PL to extract trade list and PL per Party
# export trade list and pl per party in csv files

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#



def midImplement(type, data):
# Read file from source location  and create a copy to work on
# df = pd.read_csv('sampleMid2.csv')
    if type == 'File':
        # df = pd.read_csv('ProblemSetData.csv')
        df = pd.read_csv(data)
    elif type == "DF":
        df = data
    else:
        print("Not suitable format")
        exit()

    new_df = df.copy()
    new_df = new_df.sort_values(by = ['Product'],
                                ascending=[True])

    # Split trade order on basis of product
    uniqueProduct = new_df.Product.unique()
    productDict = { elem : new_df for elem in uniqueProduct}
    for key in productDict.keys():
        productDict[key] = new_df[:][new_df.Product == key]

    # print(productDict)
    uniqueParty = new_df.Party.unique()

    ## trade list and associated pl intiailization
    df_trade_list = pd.DataFrame()
    df_PL = pd.DataFrame()
    trade = dict()
    pl = dict()

    # Rate function 
    def Rate(quantity1, quantity2, price1, price2):
        if quantity1+quantity2 == 0:
            print("rate can't be determined. No Trade. Quantities are zeros")
            exit()
        else:
            rate = (quantity1 * price1 + quantity2 * price2)/(quantity1 + quantity2)
        return math.ceil(rate)

    # Extracting transaction or trade from each product one by one
    for key in productDict.keys():
        # print(productDict[key])
        df_product = productDict[key].sort_index(axis =0)
        # print(df_product)
        # print("Product", key, "+++++++++++++_-----------------------")
        # print(df_product)
        row_indices = df_product.index.tolist()
        
        sell_indices = df_product.index[df_product['Direction'] == 'Sell'].tolist()
        buy_indices = df_product.index[df_product['Direction'] == 'Buy'].tolist()
        
        validRange = max(len(sell_indices), len(buy_indices))
        i =0 
        while i < df_product.shape[0] and len(buy_indices) !=0 and len(sell_indices)!=0 :
            # print(df_product.loc[row_indices[i]]['Direction'])
            

            # print("iteration", i, "+++++++++++++_-----------------------")
            # print("Before iteration")
            # print(i, df_product.shape[0], buy_indices, sell_indices, row_indices)
            # print(df_product)

            # sell trade
            if df_product.loc[row_indices[i]]['Direction'] == 'Sell':
                sell_quantity = df_product.loc[row_indices[i]]['Quantity']
                sell_price = df_product.loc[row_indices[i]]['Price']
                buy_quantity = df_product.loc[buy_indices[0]]['Quantity']
                buy_price = df_product.loc[buy_indices[0]]['Price']

                party = df_product.loc[row_indices[i]]['Party']
                counterParty = df_product.loc[buy_indices[0]]['Party']
                direction = 'Sell'
                tradeQuantity = min(sell_quantity, buy_quantity)
                tradeRate = Rate(buy_quantity, sell_quantity, buy_price, sell_price)
                # print(party,counterParty,direction,tradeQuantity, tradeRate)
                if sell_quantity > buy_quantity:
                    df_product.loc[row_indices[i],'Quantity'] = abs(sell_quantity - buy_quantity)
                    # print(row_indices, buy_indices, row_indices.index(buy_indices[0]))
                    df_product.loc[buy_indices[0], 'Quantity'] = 0
                    row_indices.pop(row_indices.index(buy_indices[0]))
                    buy_indices.pop(0)
                else:
                    # print(df_product.loc[buy_indices[0]]['Quantity'], type(df_product.loc[buy_indices[0]]['Quantity']), type(abs(sell_quantity - buy_quantity)))
                    df_product.loc[row_indices[i],'Quantity'] = 0
                    df_product.loc[buy_indices[0],'Quantity'] = abs(sell_quantity - buy_quantity)
                    sell_indices.pop(0)
                    i +=1
                
                #inserting pl buyer and seller into df_PL (P&L list)
                pl_seller = {
                    'partyType': 'Seller',
                    'party': party,
                    'product': key,
                    'pl': tradeQuantity*(tradeRate-sell_price)
                }
                pl_buyer = {
                    'partyType': 'Buyer',
                    'party': counterParty,
                    'product': key,
                    'pl': tradeQuantity*(buy_price -tradeRate)
                }
                df_pl_seller = pd.DataFrame([pl_seller])
                df_pl_buyer = pd.DataFrame([pl_buyer])
                df_PL = pd.concat([df_PL, df_pl_seller, df_pl_buyer])
            
            # buy trade
            else:
                buy_quantity = df_product.loc[row_indices[i]]['Quantity']
                buy_price = df_product.loc[row_indices[i]]['Price']
                sell_quantity = df_product.loc[sell_indices[0]]['Quantity']
                sell_price = df_product.loc[sell_indices[0]]['Price']

                party = df_product.loc[row_indices[i]]['Party']
                counterParty = df_product.loc[sell_indices[0]]['Party']
                direction = 'Buy'
                tradeQuantity = min(sell_quantity, buy_quantity)
                tradeRate = Rate(buy_quantity, sell_quantity, buy_price, sell_price)

                if buy_quantity > sell_quantity:
                    df_product.loc[row_indices[i],'Quantity'] = abs(sell_quantity - buy_quantity)
                    # df_product.drop(buy_indices[0])
                    df_product.loc[sell_indices[0],'Quantity'] = 0
                    row_indices.pop(row_indices.index(sell_indices[0]))
                    sell_indices.pop(0)
                else:
                    df_product.loc[row_indices[i],'Quantity'] = 0
                    df_product.loc[sell_indices[0], 'Quantity'] = abs(sell_quantity - buy_quantity)
                    buy_indices.pop(0)
                    i +=1

                #inserting pl buyer and seller into df_PL (P&L list)
                pl_seller = {
                    'partyType': 'Seller',
                    'party': counterParty,
                    'product': key,
                    'pl': tradeQuantity*(tradeRate-sell_price)
                }
                pl_buyer = {
                    'partyType': 'Buyer',
                    'party': party,
                    'product': key,
                    'pl': tradeQuantity*(buy_price -tradeRate)
                }
                df_pl_seller = pd.DataFrame([pl_seller])
                df_pl_buyer = pd.DataFrame([pl_buyer])
                df_PL = pd.concat([df_PL, df_pl_seller, df_pl_buyer])


            # print("After iteration")
            # print(i, df_product.shape[0], buy_indices, sell_indices, row_indices)
            # print(df_product)

            #inserting trade or transaction into trade list (df_trade_list)
            trade['Party'] = party
            trade['CounterParty'] = counterParty
            trade['Direction'] = direction
            trade['Product'] = key
            trade['Quantity'] = min(sell_quantity, buy_quantity)
            trade['Rate'] = Rate(buy_quantity, sell_quantity, buy_price, sell_price)

            df_trade = pd.DataFrame([trade])
            df_trade_list = pd.concat([df_trade_list, df_trade])

    #indexing trade list
    indexTradeList = pd.Index(range(0, df_trade_list.shape[0],1))
    df_trade_list = df_trade_list.set_index(indexTradeList)
    print(df_trade_list)

    #indexing P&L list and extracting P&L per Party
    indexPL = pd.Index(range(0,df_PL.shape[0],1))
    print("Party P&L", df_PL.set_index(indexPL))
    # print(uniqueParty, type(uniqueParty), df_PL['party'])
    PL_per_party = dict()
    for party in uniqueParty:
        if df_PL.shape[0]!=0:
            PL_per_party[party] = df_PL[df_PL['party'] == party]['pl'].sum()
        else:
            print(" NO P&L generated:: No Trade")
    print("++++++++++++++++++++++++===========P&L per Party===========+++++++++++++++++++++")
    print(PL_per_party)
    
    print("++++++++++++++++++++++++===========Total Volume Matched===========+++++++++++++++++++++")
    if df_trade_list.shape[0]!= 0:
        totalMatchedVolume = df_trade_list['Quantity'].sum()
        print(totalMatchedVolume)
    else:
        print("No trade --->No volume ")
    #Exporting trade list and P&L per Party list into csv file
    df_trade_list.to_csv('mid_results.csv')
    pd.DataFrame([PL_per_party]).to_csv('P&L_per_party')

if __name__== "__main__":
    # type = sys.argv[0]
    print("In")

