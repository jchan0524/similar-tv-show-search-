# Similar TV Show Finder

This script finds TV shows that have a similar genre and rating to a given TV show. This data is scraped from IMDB's TV shows listing page. The user needs to input the name of a TV show, and the script will list the names of TV shows that are similar in genre and have a similar or higher rating

## Requirements

- Python 3
- pandas
- requests
- BeautifulSoup
- scikit-learn

## Installation

You can install the required libraries using pip: `pip install pandas requests beautifulsoup4 scikit-learn`

## How to Run

1. Clone this repository or download the script.
2. Run the script using Python: `python similar_tv_show_finder`
3. Enter the name of a TV show when prompted
4. The script will display a list of similar TV shows.

## Technologies Used

- **Python**: The script is written in Python
- **pandas**: A Python data analysis library used for creating and manipulating programming languages for data manipulation and analysis
- **requests**: A Python library for making HTTP requests. It is used to scrape the data from the IMDB website
- **BeautifulSoup**: A Python library for parsing HTML documents.
- **scikit-learn**: A Python machine leaning library. It is used in this project for text vectorization and calculating cosine similarities between TV show genres

## Accomplishments

- **Web Scraping**: Scraped data from a website using Python libraries like `requests` and `BeautifulSoup`. This includes making HTTP requests and parsing HTML to extract the necessary information.
- **Data Processing**: Processed and manipulated data using pandas. This includes creating data frames, cleaning data, and combining data from different sources.
- **Text Vectorization**: Through this project, I gained an understanding of converting text data into numerical vectors using the TF-IDF vectorizer.
- **Cosine Similarity**: Used cosine similarity for finding the similarity between different text data. This is useful in recommendations based on content.
