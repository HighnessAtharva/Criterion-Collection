# Criterion Read Only API

## Requirements

The purpose of the API is to provide read-only access to the movie data stored in a relational database. The target audience of the API could be developers or movie enthusiasts who want to access and consume the movie data programmatically.

The API should be designed to provide information about the movies, including movie title, director, media type, country, year, runtime, aspect ratio, language, availability of Blu-ray and DVD, their prices, poster URL, page URL, and thumbnail URL. The data should be returned in a structured format, such as JSON, so that it can be easily consumed by the client application.

To ensure that the API is monetized and secure, it should require API key/auth headers. This will allow the API provider to track usage and enforce access control policies. Additionally, the API provider should consider implementing rate limiting or other throttling mechanisms to prevent abuse and ensure that the API remains responsive and available to its intended users.  

## API Design
