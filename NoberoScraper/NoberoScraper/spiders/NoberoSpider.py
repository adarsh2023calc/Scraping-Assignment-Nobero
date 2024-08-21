

#My Python Webscraping Project using Scrapy

# Link = https://nobero.com/

import scrapy


class NoberoSpider(scrapy.Spider):
    name = "nobero"
    start_urls=['https://nobero.com/pages/men']
    domain_name='https://nobero.com/'
    def parse(self,response):
        category_link=[]
        categories=[]
        for category in response.css('div.custom-page-season-grid-item'):
            category_link.append(category.css('a.flex').attrib['href'])
            categories.append(category.css('a.flex').attrib['href'].strip().split('/')[-1])
        
    
        for index,next_page in enumerate(category_link):
            next_page_link = self.domain_name + next_page.strip()[1:]
            yield response.follow(next_page_link, self.parse_category,cb_kwargs={'product_category':\
                                                                                 categories[index]})
            
        
            
        


    def parse_category(self,response,product_category):
        product_link=[]
        for product in response.css('section.product-card-container'):
            product_link.append(product.css('a.product_link').attrib['href'] +"?"+ "variant=" +\
                                product.css('a.product_link').attrib['data-id'])
       
        for product_info in product_link:
            product_info_link = self.domain_name + product_info.strip()[1:]
            
            yield response.follow(product_info_link, self.parse_product,cb_kwargs={'category':product_category,\
                                                                                   'product_url':product_info_link})

    
    def parse_product(self,response,category,product_url):
        for product_info in response.css('div.justify-between'):
            if(product_info.css('h1') != []):
                
                price= response.css('spanclass::text').getall()[0]
                MRP = response.css('spanclass::text').getall()[1]
                Last_7_day_shopping_tag = response.css('div.pb-\[1rem\]')
                
                if(Last_7_day_shopping_tag==[]):
                    Last_7_day_shopping_text='0'
                else:
                    Last_7_day_shopping_no_text= Last_7_day_shopping_tag.css('span::text').get().strip()
                    Last_7_day_shopping_text = Last_7_day_shopping_no_text.split(' ')[0]
                
                color = response.css('span#selected-color-title::text').get().strip().replace('-','').strip()
                Sizes = response.css('input.size-select-input')
                size_array = []
                for Selector in Sizes:
                    size_array.append(Selector.attrib['value'])
                print(size_array)
                Product_parameters = response.css('div.product-metafields-values')
                Product_parameters_list = Product_parameters.css('p::text').getall()
                Description_Selector = response.css('div#description_content')
                Description_Selector = Description_Selector.css('p')
                Content_headers=Description_Selector.css('strong::text').getall()
                Content_info = Description_Selector.css('span::text').getall()
                description_string=""
                for index1,Content in enumerate(Content_headers):
                    if index1 < len(Content_info):
                        description_string+=Content + " " + Content_info[index1] + "\n"
                try:
                    
                    yield{

                        'category': category,
                        'url':product_url,
                        'title':product_info.css('h1::text').get().strip(),
                        'price':price,
                        'MRP':MRP,
                        'product_url':[  ],
                        "last_7_day_sale":Last_7_day_shopping_text,
                        "available_skus": [
                                        {
                                        "color": color,
                                        "size": size_array[:int(len(size_array)/2)]
                                        },
                                        {
                                        "color": "",
                                        "size": []
                                        }
                                    ],
                        "fit": Product_parameters_list[0],
                        "fabric": Product_parameters_list[1],
                        "neck": Product_parameters_list[2],
                        "sleeve": Product_parameters_list[3],
                        "pattern": Product_parameters_list[4],
                        "length": Product_parameters_list[5],
                        "description":description_string
                    }

                except:
                    print("Yes")
                    continue

                    

            
        


        



        

        
            
    