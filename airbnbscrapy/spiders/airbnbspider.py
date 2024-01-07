import scrapy
import os
import json

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        # This is just a placeholder structure. You would need to inspect the actual
        # web page to find the correct selectors for the data you want to extract.
        for listing in response.css('div.listing'):
            yield {
                'title': listing.css('h2.title::text').get(),
                'price': listing.css('span.price::text').get(),
                # Add more fields as needed
            }




class FullPageSpider(scrapy.Spider):
    name = 'fullpage'
    counter = 0
    start_urls = [

        'https://www.airbnb.it/s/Blloku--Tirana--Albania/homes?adults=1&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=2024-01-08&checkout=2024-01-10&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&search_type=unknown&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D',  # Replace with the URL you want to scrape

        'https://www.airbnb.it/s/Blloku--Tirana--Albania/homes?adults=1&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=2024-01-08&checkout=2024-01-10&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&search_type=unknown&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D',

        'https://www.airbnb.it/s/Blloku--Tirana--Albania/homes?adults=1&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=2024-01-08&checkout=2024-01-10&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&search_type=unknown&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjozNiwidmVyc2lvbiI6MX0%3D',

        'https://www.airbnb.it/s/Blloku--Tirana--Albania/homes?adults=1&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=2024-01-08&checkout=2024-01-10&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&search_type=unknown&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo1NCwidmVyc2lvbiI6MX0%3D',

        'https://www.airbnb.it/s/Blloku--Tirana--Albania/homes?adults=1&place_id=ChIJoSl7wgIxUBMR7oW2ikd2PAg&refinement_paths%5B%5D=%2Fhomes&checkin=2024-01-08&checkout=2024-01-10&tab_id=home_tab&query=Blloku%2C%20Tirana%2C%20Albania&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-02-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=2&channel=EXPLORE&search_type=unknown&federated_search_session_id=1ec00596-b0c3-4488-9388-3e31e419f561&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo3MiwidmVyc2lvbiI6MX0%3D',


    ]

    # def parse(self, response):
    #     filename = 'page_content.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #         self.log(f'Saved file {filename}')



    # def parse(self, response):
    #         # Select the div with the specified classes
    #         target_div = response.css('.g1qv1ctd.atm_u80d3j_1lqfgyr.atm_c8_o7aogt.atm_g3_8jkm7i.c1v0rf5q.atm_9s_11p5wf0.atm_cx_d64hb6.atm_dz_7esijk.atm_e0_1lo05zz.dir.dir-ltr')
            
    #         # Extract the entire HTML content of the div
    #         html_content = target_div.get()

    #         # You can yield the HTML content or parse it further to extract specific data
    #         yield {
    #             'html_content': html_content,
    #         }
    
    
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'User-Agent': self.user_agent})


    def parse(self, response):
        current_directory = os.getcwd()
        self.counter += 1

        # Extract data using CSS selectors or any other method
        data = {
            'url': response.url,
            #'content': response.css('.g1qv1ctd.atm_u80d3j_1lqfgyr.atm_c8_o7aogt.atm_g3_8jkm7i.c1v0rf5q.atm_9s_11p5wf0.atm_cx_d64hb6.atm_dz_7esijk.atm_e0_1lo05zz.dir.dir-ltr').get(),
            'content': response.text,
        }

        data_html = response.body
        # Define a filename based on the URL or another unique identifier
        filename = f"{self.counter}.html"
        #filename = f"jjj.txt"
        # Define the directory where you want to save the file
        directory = os.path.join(current_directory, 'airbnbscrapy', 'data')
        print(directory)
        
        # Create directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Combine the directory and filename
        file_path = os.path.join(directory, filename)

        # Write the extracted data to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(data_html))
            
            self.log(f'Saved file {filename}')


