## WEB SCRAPING 

### Gathering Data

- Update frequency will be monthly
- Data source will be <https://www.criterion.com/shop/browse/list?sort=spine_number>
- Collection of data will be done using Scrapy
- Get the data from the website and save it in a CSV file
- Scroll the main page to get all the data, get additional data from the individual pages by clicking on the link and scraping the data from the page.
- Fields for the CSV will be [Spine, Title, Director, Country, Year, URL, IsBluRayAvailable, BluRayPrice, IsDVDAvailable, DVDPrice, Runtime, IsColor, Aspect Ratio, Language]

## API Development

[x] Define the requirements of your API - this includes its purpose, target audience, and what data you want to provide.
[x] Set up a Django project and install Django Rest Framework - this can be done by following the official Django documentation.
[x] Create a new Django app within the project that will handle the API - this app will contain the models, views, and serializers for the API.
[x] Define the models that will represent the data in the provided relational database - each model will map to a table in the database and will contain the fields specified in the table.
[x] Create serializers for each model - these serializers will define how the data from the models should be presented in the API's response.
[ ] Define the views that will handle the API requests - these views will define the logic for retrieving data from the models and formatting it for the response.
[ ] Implement authentication and authorization using API keys and auth headers - this can be done using - Django Rest Framework's built-in authentication and permission classes.
[ ] Test the API - you can use tools like Postman to test the API's endpoints and make sure it's working as expected.

## API Deployment  
