**Times Higher Education Scraper**

This Python script uses BeautifulSoup and Selenium to scrape data from the Times Higher Education website, specifically from the world university rankings page.

*Importing Libraries:*

The script begins by importing libraries for web scraping (BeautifulSoup, requests), web automation (Selenium), and CSV handling (csv).

*Setting Up Selenium WebDriver:*

Initializes a Chrome WebDriver for Selenium.

*Opening the Website:*

Navigates to the specified URL using the Chrome WebDriver.

*Executing JavaScript to Get Page HTML:*

Executes JavaScript to obtain the entire HTML content of the page and stores it in a variable.

*Parsing HTML with BeautifulSoup:*

Creates a BeautifulSoup object to parse the HTML content.

*Finding the Table with BeautifulSoup:*

Finds all <table> elements with a specific ID on the webpage.

*Getting the Number of Rows and Columns in the Table using Selenium:*

Counts the number of rows and columns in the table using XPath with Selenium.

*Printing Number of Rows and Columns:*

Prints the number of rows and columns to the console.

*Looping Through the Table and Printing Cell Values:*

Iterates through each row and the first two columns of the table using Selenium.
Extracts the text content of each cell and prints it to the console.

**Prerequisites**

We will need the following dependencies installed:

- Python 3.x
- Selenium
- BeautifulSoup
- Chrome WebDriver

**To run this project**

Installation
Clone the repository: git clone https://github.com/Shruti-Shete/times-higher-education-scraper.git

                      cd web_scraping_3.py
Install dependencies:

pip install -r requirements.txt

Usage

Run the script: web_scraping_3.py

**Universities_100**

It is a csv file with all extracted data using web_scraping_3.py 
