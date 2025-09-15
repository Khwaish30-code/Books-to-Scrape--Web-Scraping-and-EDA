# 📚 Books to Scrape – Web Scraping & EDA  

## 🔍 Project Overview  
This project demonstrates an **end-to-end data pipeline** starting from **web scraping**, followed by **data storage**, and then **exploratory data analysis (EDA)**.  
Data was scraped from the [Books to Scrape](https://books.toscrape.com) website, which provides book details such as title, category, price, rating, and stock availability.  

---

## 📂 Project Structure  
```
data/
├── Books.csv        # Scraped book details (title, rating, price, etc.)
├── data.csv         # Additional details from book pages (category, upc, etc.)
├── final.csv        # Combined cleaned dataset for analysis
scraper.py      # Python script for scraping
main.ipynb  # Jupyter notebook with EDA & insights
requirements.txt      # Required Python libraries
README.md             # Project README
```

---

## 🛠️ Tools & Libraries Used
- **Python**
- **requests, beautifulsoup4** → web scraping
- **pandas** → data cleaning & manipulation
- **matplotlib, seaborn** → data visualization
- **tqdm** → progress tracking

---

## 📑 Dataset Description
Final dataset (`final.csv`) contains the following columns:

| Column       | Description |
|--------------|-------------|
| title        | Book title |
| category     | Category/genre of the book |
| price_e_tax  | Price (excluding tax) |
| price_i_tax  | Price (including tax) |
| tax          | Tax amount |
| rating       | Book rating (out of 5) |
| quantity     | Quantity available in stock |
| stock        | Stock status |
| upc          | Unique product code |
| book_link    | Link to book page |
| img_link     | Link to book image |
| reviews      | (empty in this dataset) |

---

## 📊 Key Insights from EDA
- Most books are priced between **£20–£50**, showing a mid-market pricing focus.  
- **Ratings** are skewed toward higher values (4–5 stars), meaning most books are positively reviewed.  
- **Categories** have varied price ranges, with some genres more expensive than others.  
- **Stock availability** is generally poor, only a small number of titles have a large quantity available.  
- No clear link between **price and rating**, meaning customer rating does not influence book pricing.

---

## 🚀 How to Run the Project  

1. **Clone the repository / download files**  

2. **Create and activate a virtual environment**  
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

3. **Install requirements**
   ```bash
   pip install -r requirements.txt

4. **Run the scraper**
   ```bash
   python scraper.py
→ This will generate CSV files inside the data/ folder.

5. **Open the Jupyter notebook**
    ```bash
   jupyter notebook main.ipynb

---

## ✅ Conclusion

This project highlights how raw website data can be transformed into a structured dataset using web scraping, and how meaningful insights can be drawn through EDA and visualization.


