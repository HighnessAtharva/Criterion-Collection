# TODO

## Gathering Data

- Update frequency will be monthly
- Data source will be <https://www.criterion.com/shop/browse/list?sort=spine_number>
- Collection of data will be done using Scrapy
- Get the data from the website and save it in a CSV file
- Scroll the main page to get all the data, get additional data from the individual pages by clicking on the link and scraping the data from the page.
- Fields for the CSV will be [Spine, Title, Director, Country, Year, URL, IsBluRayAvailable, BluRayPrice, IsDVDAvailable, DVDPrice, Runtime, IsColor, Aspect Ratio, Language]

## Set Up Cloud Database

- Migrate CSV data to a cloud hosted database
- Data will be saved in a Cloud Hosted Postgres Database

## API Design

- Design API based on the data collected from the database.
- Django Rest Framework will be used to create the API

## API Deployment

- Deploy and monetize the API.
