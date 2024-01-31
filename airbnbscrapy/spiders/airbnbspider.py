import scrapy
import os
import json
from datetime import datetime, timedelta



def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    


def parse_data_(json_string_):

    # Remove the leading and trailing single quotes
    # Trim or clean your JSON string if necessary
    # For example, if your string has leading and trailing single quotes, you can remove them:
    if json_string_.startswith("'") and json_string_.endswith("'"):
        json_string_ = json_string_[1:-1]

    # Replace any problematic encoding in your string
    # Example: Replace escaped unicode characters
    json_string_ = json_string_.encode().decode('unicode_escape')

    # Now, try to load it as a JSON object
    try:
        data = json.loads(json_string_)
        print("JSON loaded successfully")

        return json_string_ , data
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)



class FullPageSpider(scrapy.Spider):
    name = 'fullpage'
    counter = 0

    def init___():
        current_directory = os.getcwd()
        output_directory = os.path.join(current_directory,"airbnbscrapy")
        input_data_directory = os.path.join(output_directory, 'inputdata')


        # Path to the JSON file
        json_info_path = os.path.join(output_directory,'info.json')

        # Load data from JSON
        lko= read_json(json_info_path)
        urls = []
        counter__ = 1


        input_data_directory_ = os.path.join(current_directory, 'airbnbscrapy')
        input_data_directory = os.path.join(input_data_directory_, 'inputdata')
        if not os.path.exists(input_data_directory):
            os.makedirs(input_data_directory)



        for j in range (len(lko['location'])):
            for m in range (len(lko['nights'])):
                for o in range (len(lko['starting_from'])):
                    for y in range (len(lko['host']['adults'])):

                            # print (lko['location'][j])
                            # print (lko['nights'][m])
                            # print (lko['starting_from'][o])
                            # print (lko['host']['adults'][y])

                            current_date = datetime.now()
                            #print(current_date)
                            adults = lko['host']['adults'][y]
                            checkin =  current_date +  timedelta(days= lko['starting_from'][o]) 
                            checkout = checkin +  timedelta(days= lko['nights'][m])
                            checkin_f = checkin.strftime("%Y-%m-%d")
                            checkout_f = checkout.strftime("%Y-%m-%d")
                            url_ = 'https://www.airbnb.it/s/' + str(lko['location'][j]) +  '/homes?adults=' + str(adults) +  '&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=' + str(checkin_f) + '&checkout=' + str(checkout_f) + '&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=' + str(checkin_f) + '&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=' + str(lko['nights'][m]) + '&channel=EXPLORE&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&search_type=unknown&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D'
                            #print(url_)
                            urls.append(url_)
                            print(url_)
                            #print('https://www.airbnb.it/s/' + str(lko['location'][j]) +  '/homes?adults=' + str(lko['host']['adults'][y]) +  '&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=' + str(checkin_f) + '&checkout=' + str(checkout_f) + '&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=' + str(checkin_f) + '&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=' + str(lko['nights'][m]) + '&channel=EXPLORE&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&search_type=unknown&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D')
                                                # Create JSON data
                            json_data = {
                                'current_date': current_date.strftime("%Y-%m-%d %H:%M"),
                                'checkin': checkin_f,
                                'checkout': checkout_f,
                                'adults': adults,
                                'url': url_
                            }
                            print(json_data)

                            # Save JSON data to file
                            json_file_name = f"{counter__}.json"
                            json_file_path = os.path.join(input_data_directory, json_file_name)
                            print("path of input file:", json_file_path)
                            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                                json.dump(json_data, json_file, ensure_ascii=False, indent=4)
                            
                            counter__ = counter__ +1
        
        return urls 
    





    start_urls =  init___()
    #print(start_urls)
   
    
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': self.user_agent})


    def parse(self, response):
        current_directory = os.getcwd()
        self.counter += 1

         # Extract query parameters from URL
        # parsed_url = urlparse(response.url)
        # query_params = parse_qs(parsed_url.query)

        # # Extract additional data from URL
        # checkin = query_params.get('checkin', [None])[0]
        # checkout = query_params.get('checkout', [None])[0]
        # adults = query_params.get('adults', [None])[0]
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Extract data using CSS selectors or any other method
        data = {
            'url': response.url,
            'content': response.text,
            'current_date': current_date,
            
        }

        data_html = response.body
        # Define a filename based on the URL or another unique identifier
        filename = f"{self.counter}.html"

        # Define the directory where you want to save the file
        directory = os.path.join(current_directory, 'airbnbscrapy', 'data')
        #print(directory)
        
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Combine the directory and filename
        file_path = os.path.join(directory, filename)

        # Write the extracted data to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(data_html))
            
            self.log(f'Saved file {filename}')




print("ciccio1")