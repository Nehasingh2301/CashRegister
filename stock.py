import json
def make_list():
    myList = [
                {'item': 'HP Laptop','code':'HP101','units':8,"price":500},
                {'item': 'HP Desktop', 'code': 'HP102', 'units': 7, "price": 800},
                {'item': 'Samsung Mobile', 'code': 'Sam101', 'units': 6, "price": 600},
                {'item': 'IPhone 11', 'code': 'Apple101', 'units': 25, "price": 20},
             ]
    jsonmyList = json.dumps(myList, indent=3)
    return jsonmyList