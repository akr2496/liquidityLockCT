import pandas as pd
import math


# @+@+@+@+@+@+@+@+@+@+@+@+@+@+@+@+@+@+@++@____ASSUMPTIONS___@+@+@+@+@+@+@+@+@++@+@+@+@++@+@+@+@+@+@+@+@+@+@+@+@+@+@+@
# 1. Trade Matching algorithm is similar to FIFO. Order on top of trade list is matched first, then second and so on
#         matched to nearest order in sequence
# 2. Partial excecution is allowed --> if order is not filled in one trade, multiple trade is allowed to fill it
# 3. Stay on same till filled or no matching available
# 4. Net Limit applied before trade or transaction
# 5. No self transaction is allowed [buy/sell order within same party]
# 6. Net limit is implemented on order list before Trading
#7. Assuming trade will happen between all party 


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++PSEUDOCODE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#-----------------------------------Importing File-------------------------------------------------
# load order list file csv into dataframe, say df and make copy (new_df)
# load sample Net limit csv file into dataframe, say df_limit 
#
#-----------------------------------Pre Trade Limit Implementation---------------------------------
#calculate net quantity from order list for each party and stores it in nQpP dictionary
#Identity limit breaching party 
#   for each party:
#       create necessary variables
#       if nQpP[party][nQ]<0:  [sell type] [assigned -ve to sell]
#           limit = limit from sample net limit file
#           if netQuatityParty - limit >0:
#               modify nQpP party attributes 
#           else:
#               leave nQpP party attributes empty
#       else: [buy type] [assigned +ve to buy]
#           limit = limit from sample net limit file
#           if netQuatityParty - limit >0:
#               modify nQpP party attributes 
#           else:
#               leave nQpP party attributes empty
#
# Modify dataframe (df_copy2) for brached party and use it PL gen algo
#
#
#---------------------Preparing data for trade list generation-------------------------------------
#---------------------Implementing Algorithm for TL gen -------------------------------------------
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
#
#----------------------------Exporting outfile and showing results-------------------------------------
# modify and manipulate df_trade_list and df_PL to extract trade list and PL per Party
# export trade list and pl per party in csv files

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


def limitsImplement(type, data, limitData):

    # Read file from source location  and create a copy to work on
    # df = pd.read_csv('sampleMid2.csv')
    if type == 'File':
        # df = pd.read_csv('ProblemSetData.csv')
        df = pd.read_csv(data)
        # df_limit = pd.read_csv('sampleLimitSet2.csv')
        df_limit = pd.read_csv(limitData)

    elif type == "DF":
        df = data
        df_limit = limitData

    else:
        print("Not suitable format")
        exit()

    # df = pd.read_csv('ProblemSetData.csv')
    new_df = df.copy()
    new_df = new_df.sort_values(by = ['Product'],
                                ascending=[True])

    # print(df)
    # Importing limit file into dataframe
    # df_limit = pd.read_csv('sampleLimitSet2.csv')
    # print(df_limit)
    df_copy_limit = df_limit.copy()

    # Split trade order on basis of party
    # uniqueProduct = new_df.Product.unique()
    # productDict = { elem : new_df for elem in uniqueProduct}
    # for key in productDict.keys():
    #     productDict[key] = new_df[:][new_df.Product == key]

    uniqueParty = new_df.Party.unique()
    partyDict = { elem : new_df for elem in uniqueParty}
    for key in partyDict.keys():
        partyDict[key] = new_df[:][new_df.Party == key]
    # print(productDict)
    # uniqueParty = new_df.Party.unique()

    ## trade list and associated pl intiailization
    df_trade_list = pd.DataFrame()
    df_PL = pd.DataFrame()
    buy_sell_matrix = pd.DataFrame()
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

    # Pre-transaction limit application: before starting trade, filter order list on basis on Net limit
    # decide which order will go for trade or transaction
    nQpP = {}
    for party in uniqueParty:
        nQpP[party] = {"nQ": 0, "limitBreachWidth": 0, "limitBreachType": ''}

    for party in partyDict.keys():
        netQuantity = 0
        
        df_party = partyDict[party]
        party_row_indices = df_party.index.tolist()
        for i in range(df_party.shape[0]):
            if new_df.loc[i,'Direction'] == 'Sell':
                netQuantity -= df_party.loc[party_row_indices[i], 'Quantity']
            else:
                netQuantity += df_party.loc[party_row_indices[i], 'Quantity'] 
        nQpP[party]["nQ"] = netQuantity
    # print(nQpP)


    #identifying breaching parties 
    breachingParty = []
    df_copy2 = df.copy()
    #limit breach checking 
    for party in uniqueParty:
        #selling limit comes into play
        df_limit_party = df_copy_limit[df_copy_limit['Party'] == party]
        if nQpP[party]["nQ"]<0:
            
            limit = df_limit_party[ df_limit_party['Direction'] == 'Sell']['NetLimit'].tolist()[0]
            # print(limit)
            if (abs(nQpP[party]["nQ"]) - limit)> 0:
                nQpP[party]["limitBreachWidth"] = (abs(nQpP[party]["nQ"]) - limit)
                nQpP[party]["limitBreachType"] = 'Sell'
                breachingParty.append(party)
            else:
                nQpP[party]["limitBreachWidth"] = 0
                nQpP[party]["limitBreachType"] = ''
        else:
            
            limit = df_limit_party[ df_limit_party['Direction'] == 'Buy']['NetLimit'].tolist()[0]
            # print(limit)
            if (abs(nQpP[party]["nQ"]) - limit)> 0:
                nQpP[party]["limitBreachWidth"] = (abs(nQpP[party]["nQ"]) - limit)
                nQpP[party]["limitBreachType"] = 'Buy'
                breachingParty.append(party)
            else:
                nQpP[party]["limitBreachWidth"] = 0
                nQpP[party]["limitBreachType"] = ''
            
    # print(nQpP)

    #modifying order list to accomodate Net Limit criteria
    for party in breachingParty:
        df_req = df_copy2[df_copy2['Party'] == party]
        lbWidth = nQpP[party]['limitBreachWidth']
        # print(party, lbWidth, nQpP[party]['limitBreachType'])
        if nQpP[party]['limitBreachType'] == 'Sell':
            df_req = df_req[df_req['Direction'] == 'Sell']  
        else:
            df_req = df_req[df_req['Direction'] == 'Buy']

        req_row_indices = df_req.index.tolist()  
        i=0  
        while i < df_req.shape[0]:
            if lbWidth <= df_req.loc[req_row_indices[i], 'Quantity']:
                df_req.loc[req_row_indices[i], 'Quantity'] = df_req.loc[req_row_indices[i], 'Quantity'] - lbWidth
                # print(df_req)
                break
            else:
                lbWidth = lbWidth - df_req.loc[req_row_indices[i], 'Quantity'] 
                df_req.loc[req_row_indices[i], 'Quantity'] = 0
                i +=1
        for i in range(df_req.shape[0]):
            df_copy2.loc[req_row_indices[i]] = df_req.loc[req_row_indices[i]]
    # print(df_req)        
    print(df_copy2)

    ##splitting modified df_copy2 (satifying limit condition) into product df
    uniqueProduct = new_df.Product.unique()
    productDict = { elem : df_copy2 for elem in uniqueProduct}
    for key in productDict.keys():
        productDict[key] = df_copy2[:][df_copy2.Product == key]


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

            # sell trade
            if df_product.loc[row_indices[i]]['Direction'] == 'Sell':
                seller = df_product.loc[row_indices[i], 'Party']
                sell_quantity = df_product.loc[row_indices[i]]['Quantity']
                sell_price = df_product.loc[row_indices[i]]['Price']

                buyer = df_product.loc[buy_indices[0],'Party']
                buy_quantity = df_product.loc[buy_indices[0]]['Quantity']
                buy_price = df_product.loc[buy_indices[0]]['Price']

                party = seller
                counterParty = buyer
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
            # trade['sellPrice'] = sell_price
            # trade['buyPrice'] = buy_price

            df_trade = pd.DataFrame([trade])
            df_trade_list = pd.concat([df_trade_list, df_trade])

    #indexing trade list
    indexTradeList = pd.Index(range(0, df_trade_list.shape[0],1))
    df_trade_list = df_trade_list.set_index(indexTradeList)
    print(df_trade_list)

    #indexing P&L list and extracting P&L per Party
    indexPL = pd.Index(range(0,df_PL.shape[0],1))
    # print(df_PL.set_index(indexPL))
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
    print("++++++++++++++++++++++++===========Limit hitting party===========+++++++++++++++++++++")
    print(breachingParty)

    #Exporting trade list and P&L per Party list into csv file
    df_trade_list.to_csv('limits_results.csv')
    pd.DataFrame([PL_per_party]).to_csv('P&L_per_party_limits.csv')

if __name__== "__main__":
    print("in limit")
