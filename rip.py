import requests
import argparse
import time

import pymongo
from pymongo import MongoClient

from tqdm import tqdm



def get_item_list( ):
    req = requests.get("http://warframe.market/api/get_all_items_v2")
    item_list = req.json( )
    return item_list

def get_orders(item_type, item_name):
    uri = 'http://warframe.market/api/get_orders/'
    uri += item_type + '/'
    uri += item_name

    req = requests.get(uri)
    orders = req.json( )

    return orders



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-c','--clear', help='Input file name', default=False, action='store_true')
    args = parser.parse_args()


    client = MongoClient("127.0.0.1", 27017)
    db = client.warframe
    c_item_list = db.item_list
    c_orders = db.orders
    # wipe orders
    c_orders.remove({})

    # init item master list
    cursor = c_item_list.find({ })
    if cursor.count( ) == 0 or args.clear:
        client.drop_database("warframe")

        # init table:
        item_list = get_item_list( )
        c_item_list.insert(item_list)
        cursor = c_item_list.find({ })


    # retrieve updated prices for all.
    with tqdm( ) as t:
        t.total = cursor.count( )
        for item in cursor:
            online_count = 0

            item_type = item["item_type"]
            item_name = item["item_name"]

            # print "Checking. . ."
            # print item_name
            orders = get_orders(item_type, item_name)
            buy = orders["response"]["buy"]
            sell = orders["response"]["sell"]


            sell_lowest_price = 0
            sell_popularity = 0 
            sell_near_lowest_count = 0 
            # obj is: {u'count': 1, u'price': 5, u'ingame_name': u'Paphi', u'online_ingame': False, u'online_status': True}
            for sell_order in sell:
                price = sell_order["price"]
                online_status = sell_order["online_status"]
                online_ingame = sell_order["online_ingame"]

                if online_status or online_ingame:
                    if price < sell_lowest_price or sell_lowest_price == 0:
                        sell_lowest_price = price

            for sell_order in sell:
                price = sell_order["price"]
                online_status = sell_order["online_status"]
                online_ingame = sell_order["online_ingame"]

                if online_status or online_ingame:
                    sell_popularity += 1
                    if sell_lowest_price-1 <= price <= sell_lowest_price+1:
                        sell_near_lowest_count += 1

                if online_ingame:
                    online_count += 1


            buy_lowest_price = 0
            buy_highest_price = 0
            buy_popularity = 0 
            for buy_order in buy:
                price = sell_order["price"]
                online_status = sell_order["online_status"]
                online_ingame = sell_order["online_ingame"]

                if online_status or online_ingame:
                    buy_popularity += 1
                    if price < buy_lowest_price or buy_lowest_price == 0:
                        buy_lowest_price = price

                    if price > buy_highest_price or buy_highest_price == 0:
                        buy_highest_price = price

                if online_ingame:
                    online_count += 1

            c_orders.insert({
                "item_name": item_name,
                "lowest_price": sell_lowest_price,
                "popularity": sell_popularity,
                "near_lowest_count": sell_near_lowest_count,
                "buy_lowest_price": buy_lowest_price,
                "buy_highest_price": buy_highest_price,
                "buy_popularity": buy_popularity,
                "online_count": online_count
            })
            t.update(1)
            time.sleep(1) # be polite...
























