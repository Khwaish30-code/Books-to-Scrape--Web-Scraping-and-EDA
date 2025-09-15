# 📚 Books to Scrape – Web Scraping & EDA  

## 🔍 Project Overview  
This project demonstrates an **end-to-end data pipeline** starting from **web scraping**, followed by **data storage**, and then **exploratory data analysis (EDA)**.  
Data was scraped from the [Books to Scrape](https://books.toscrape.com) website, which provides book details such as title, category, price, rating, and stock availability.  

---

## 📂 Project Structure  
├── data/
│ ├── Books.csv # Scraped book details (title, rating, price, etc.)
│ ├── data.csv # Additional details from book pages (category, upc, etc.)
│ ├── final.csv # Combined cleaned dataset for analysis
├── books_scraper.py # Python script for scraping
├── books_analysis.ipynb # Jupyter notebook with EDA & insights
├── requirements.txt # Required Python libraries
├── README.md
