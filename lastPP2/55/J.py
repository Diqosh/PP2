import json, math


if __name__ == "__main__":
    with open(r'D:\kbtu\2\pp2\PP2\lastPP2\55\js.json', 'r', encoding='utf8') as rfile:
        a = rfile.read()
        listOfSubscrption = json.loads(a)['Subscriptions']
        myList = list()
        for subscription in listOfSubscrption:
            name = subscription["name"]
            price = int(subscription['price'])
            discount = int(subscription['discount'])
            count = price * (1 - discount/100)
            myList.append((name, count))
    
        myTarget = min(myList, key=lambda k: k[1])
        
        print(f"Name: {myTarget[0]}\nPrice: {int(round(myTarget[1], 0))}")

    

