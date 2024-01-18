import mysql.connector
from mysql.connector import Error
import json
import os




def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    




def connect_insert2(data): #code to add to mysql the data form the json (data is the json)
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






def connect_insert(data_input, data_output ): #code to add to mysql the data form the json (data is the json)
    try:
        connection = mysql.connector.connect(host='musttest.it',
                                             database='gxwcdfol_dfvz',
                                             user='gxwcdfol_antonov4568',
                                             password='antonov4568')
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL INSERT statement
            #query = "INSERT INTO listings (ID, Name, City, latitude, longitude, PDP_URL_Type, Room_Type_Category, Room_Rating, Price_per_night, total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            


            query = """INSERT INTO gxwcdfol_dfvz.listing_db(Request_date, Checkin_date, Checkout_date, Adults, url_TEMP, ID, Name, City, Latitude, Longitude, PDP_URL_Type, Room_Type_Category, Room_Rating, Price_per_night, Total_price, URL)VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            # Extract values and execute query

            current_data = data_input['current_date']
            checkin = data_input['checkin']
            checkout = data_input['checkout']
            adults = data_input['adults']
            url_temp = data_input['url']


            ID = data_output['ID']
            Name = data_output['Name']
            City = data_output['City'] 
            latitude =  data_output['latitude'] 
            longitude = data_output['longitude']
            PDP_URL_Type = data_output['PDP_URL_Type']
            Room_Type_Categorydata = data_output['Room_Type-Category']
            Room_Ratingdata = data_output['Room_Rating']
            Price_per_nightdata = data_output['Price_per_night']['price'] if 'price' in data_output['Price_per_night'] else (data_output['Price_per_night']['discountedPrice'] if 'discountedPrice' in data_output['Price_per_night'] else 0)
            total_price = data_output['total_price']['price']
            
            #values = (data['ID'], data['Name'], data['City'], data['latitude'], data['longitude'], data['PDP_URL_Type'], data['Room_Type-Category'], data['Room_Rating'], data['Price_per_night'], data['total_price'])
            # values = ( ID, Name , City , latitude, longitude, PDP_URL_Type , Room_Type_Categorydata, Room_Ratingdata, Price_per_nightdata, total_price)
            #values = ( ID, Name , City , latitude, longitude, PDP_URL_Type , Room_Type_Categorydata, Room_Ratingdata, Price_per_nightdata, total_price)
            values = (  current_data, checkin, checkout, adults, url_temp, ID, Name , City , latitude, longitude, PDP_URL_Type , Room_Type_Categorydata, Room_Ratingdata, Price_per_nightdata, total_price , url_temp)
            print("Number of elements in values tuple:", len(values))

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
input_directory = os.path.join(current_directory, 'airbnbscrapy', 'inputdata')


def process_all_files_in_directory2(directory):
    # List all files in the directory
    all_files = os.listdir(directory)

    # Filter out non-JSON files
    json_files = [file for file in all_files if file.endswith('.json')]

    # Process each JSON file
    for file_name in json_files:
        print(f"Processing file: {file_name}")
        file_path = os.path.join(directory, file_name)

        # Load data from JSON
        json_data = read_json(file_path)
        #. json_data_input = read_json(f)

        # Insert data into MySQL
        connect_insert(json_data)

def process_all_files_in_directory(input_directory, output_directory):


    
    #cycle based on these number: numb of item each page 17>0 - 16; num of listing 480> 1 - 480
        
        for i in range(1, 481):
              for index in range (0,17):
                output_file_path = os.path.join(output_directory, f'listing_{i}_{index}.json')
                input_file_path = os.path.join(input_directory, f'{i}.json')
                json_data_input = read_json(input_file_path)
                json_data_output = read_json(output_file_path)
                connect_insert(json_data_input, json_data_output)

            
    # List all files in the directory
    # all_files = os.listdir(output_directory)

    # # Filter out non-JSON files
    # json_files = [file for file in all_files if file.endswith('.json')]

    # # Process each JSON file
    # for file_name in json_files:
    #     print(f"Processing file: {file_name}")
    #     output_file_path = os.path.join(output_directory, file_name)


    #     input_file_path = os.path.join(output_directory, input_file_name)

    #     # Load data from JSON
    #     json_data_output = read_json(output_file_path)
    #     json_data_input= read_json(input_file_path)
    #     #. json_data_input = read_json(f)

    #     # Insert data into MySQL
    #     connect_insert(json_data_input, json_data_output)






if __name__ == "__main__":
    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, 'airbnbscrapy', 'output')
    input_directory = os.path.join(current_directory, 'airbnbscrapy', 'inputdata')

    # Process all JSON files in the output directory
    process_all_files_in_directory(input_directory , output_directory)