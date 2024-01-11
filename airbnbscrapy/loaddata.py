import mysql.connector
from mysql.connector import Error
import json
import os




def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    



    
def connect_insert2(data):
    try:
        connection = mysql.connector.connect(host='musttest.it',
                                             database='gxwcdfol_dfvz',
                                             user='gxwcdfol_antonov4568',
                                             password='antonov4568')
        if connection.is_connected():
            cursor = connection.cursor()
            for item in data:
                dict_item = json.loads(item) if isinstance(item, str) else item

                # Now you can access the dictionary
                print(dict_item)
                # Assuming your table columns match the keys in the `item` dictionary
                query = "INSERT INTO your_table (ID, Name, City, latitude, longitude, PDP_URL_Type, Room_Type_Category, Room_Rating, Price_per_night, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                #values = (item['ID'], item['Name'], item['City'], item['latitude'], item['longitude'], item['PDP_URL_Type'], item['Room_Type_Category'], item['Room_Rating'], item['Price_per_night'], item['total_price'])
                values = (505055050,"home1", 'Tirana', '115662', '11570', 'www.test.com','luxury', '4.5', '35', '70')
                
                cursor.execute(query, values)
            
            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def connect_insert2000(data):
    try:
        connection = mysql.connector.connect(host='musttest.it',
                                             database='gxwcdfol_dfvz',
                                             user='gxwcdfol_antonov4568',
                                             password='antonov4568')
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL INSERT statement
            query = "INSERT INTO your_table (ID, Name, City, latitude, longitude, PDP_URL_Type, Room_Type_Category, Room_Rating, Price_per_night, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            for item in data:
                # Convert string to dictionary if necessary
                if isinstance(item, str):
                    item = json_data[item]

                # Extract values and execute query
                if all(key in item for key in ['ID', 'Name', 'City', 'latitude', 'longitude', 'PDP_URL_Type', 'Room_Type_Category', 'Room_Rating', 'Price_per_night', 'total_price']):
                    values = (item['ID'], item['Name'], item['City'], item['latitude'], item['longitude'], item['PDP_URL_Type'], item['Room_Type-Category'], item['Room_Rating'], item['Price_per_night'], item['total_price'])
                    cursor.execute(query, values)
                else:
                    print("Error: Missing data in item:", item)

            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




def connect_insert(data):
    try:
        connection = mysql.connector.connect(host='musttest.it',
                                             database='gxwcdfol_dfvz',
                                             user='gxwcdfol_antonov4568',
                                             password='antonov4568')
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL INSERT statement
            query = "INSERT INTO listings (ID, Name, City, latitude, longitude, PDP_URL_Type, Room_Type_Category, Room_Rating, Price_per_night, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"



            # Extract values and execute query
            
            ID = data['ID']
            Name = data['Name']
            City = data['City'] 
            latitude =  data['latitude'] 
            longitude = data['longitude']
            PDP_URL_Type = data['PDP_URL_Type']
            Room_Type_Categorydata = data['Room_Type-Category']
            Room_Ratingdata = data['Room_Rating']
            Price_per_nightdata = data['Price_per_night']['price'] if 'price' in data['Price_per_night'] else (data['Price_per_night']['discountedPrice'] if 'discountedPrice' in data['Price_per_night'] else 0)
            total_price = data['total_price']['price']
            
            #values = (data['ID'], data['Name'], data['City'], data['latitude'], data['longitude'], data['PDP_URL_Type'], data['Room_Type-Category'], data['Room_Rating'], data['Price_per_night'], data['total_price'])
            # values = ( ID, Name , City , latitude, longitude, PDP_URL_Type , Room_Type_Categorydata, Room_Ratingdata, Price_per_nightdata, total_price)
            values = ( ID, Name , City , latitude, longitude, PDP_URL_Type , Room_Type_Categorydata, Room_Ratingdata, Price_per_nightdata, total_price)

            #values = (505055050,"home1", 'Tirana', '115662', '11570', 'www.test.com','luxury', '4.5', '35', '70')

            cursor.execute(query, values)


            connection.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")





current_directory = os.getcwd()
output_directory = os.path.join(current_directory, 'airbnbscrapy', 'output')

# Path to the JSON file
file_path = os.path.join(output_directory,'listing_1_0.json')

# Load data from JSON
json_data = read_json(file_path)

# Insert data into MySQL
connect_insert(json_data)


for i in range(1,6):
    for j in range (17):
        name = 'listing_'+ str(i) +'_' + str(j) + '.json'
        print (i,j)
        print (name)
        file_path_ = os.path.join(output_directory,name)

        # Load data from JSON
        json_data_ = read_json(file_path_)

        # Insert data into MySQL
        connect_insert(json_data_)

