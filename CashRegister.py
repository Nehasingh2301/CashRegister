import json
import stock
SHOW = 1
PURCHASE = 2
VIEWCART = 3
EDITCART =4
TOTAL = 5
CLEARCART = 6
QUIT = 7

def main():
    listInCarts = []
    choice = 0
    # Process menu selections until user quits program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()
        # Proces the choice.
        if choice == SHOW:
            jsonString = stock.make_list()
            print(jsonString)

        elif choice == PURCHASE:
            itemCode =purchase()
            items = stock.make_list()
            aList = json.loads(items)
            res = next((sub for sub in aList if sub['code'] == itemCode), None)
            if(res is not None):
                existingItem = next((sub for sub in listInCarts if sub['code'] == itemCode), None)
                if(existingItem is not None):
                    if(res['units'] ==  existingItem['units']):
                        print("Item is not available. You can not buy more than the existing stock in the shop")
                        return
                    existingItem['units'] += 1
                else:
                    res['units'] = 1
                    listInCarts.append(res)

        elif choice == VIEWCART:
            print('Please find the items in the cart')
            print('*******************************************************************************')
            jsonmyList = json.dumps(listInCarts, indent=3)
            print(jsonmyList)
            print('*******************************************************************************')
            total = 0
            for item in listInCarts:
                total += item['units'] * item['price']
            print("--------------------------------------------------------------------------------")
            print("Total Purchase Bill : " + str(total))
            print("--------------------------------------------------------------------------------")
        elif choice == EDITCART:
            actiontype = Action()
            if(int(actiontype) == 1):
                itemCode = AddItem()
                res = next((sub for sub in listInCarts if sub['code'] == itemCode), None)
                if (res is not None):
                    res['units'] = res['units'] + 1
            elif(int(actiontype) == 2):
                res = [i for i in listInCarts if not (i['code'] == itemCode)]
                listInCarts = res
        elif choice == TOTAL:
            total = 0
            for item in listInCarts:
                total += item['units'] * item['price']
            print("--------------------------------------------------------------------------------")
            print("Total Purchase Bill : " + str(total))
            print("--------------------------------------------------------------------------------")
        elif choice == CLEARCART:
            listInCarts = []

def get_menu_choice():
    print()
    print('CASH REGISTER MENU')
    print('-------------------------')
    print('1. Show Retial Items')
    print('2. Purchase an Item(s)')
    print('3. Show Current Shopping Cart')
    print('4. Edit Current Shopping Cart')
    print('5. Show Total of Items Purchased')
    print('6. Empty Your Shopping Cart')
    print('7. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < SHOW or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # Return the user's choice.
    return choice

def purchase():
    item_purchase = input('Enter the item you wish to purchase: ')
    return item_purchase
def Action():
    action = input('Enter 1 for Add and 2 for delete ')
    return action
def AddItem():
    itemName = input('Enter the item Name to add: ')
    return itemName

def DeleteItem():
    itemName = input('Enter the item Name to delete: ')
    return itemName

main()