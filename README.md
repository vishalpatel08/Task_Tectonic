You can run the code by command : python manage.py runserver

We have three data models  1. Items (name, itemid, quantity, price): our inventory  
                           2. Users (name, userid, credits 
                           3. Orders (orderid, userid, Item_data)

-- when user places a buy order using itemId and quantity of item, we will check it in our inventory : if sufficient quantites are present then we place the order else order will be discarded
-- track or order can be kept by fetching orders from order table using userId
