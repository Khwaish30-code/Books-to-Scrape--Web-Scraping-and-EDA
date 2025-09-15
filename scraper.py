import requests
import pandas as pd
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

# --- Safe request helper with retries ---
def safe_get(url, retries=3, delay=2, timeout=10):
    """Make a GET request with retries & timeout."""
    for i in range(retries):
        try:
            return requests.get(url, timeout=timeout)
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error: {e} (attempt {i+1}/{retries})")
            time.sleep(delay)
    return None


def scrape_books_list():
    """Scrape book list (titles, price, rating, stock, links)."""
    data = []
    base_url = "https://books.toscrape.com/"

    for i in tqdm(range(1, 51), desc="Scraping book list"):
        link = f"{base_url}catalogue/page-{i}.html"
        res = safe_get(link)
        if not res:
            continue

        soup = BeautifulSoup(res.text, "html.parser")

        for sp in soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
            book_link = base_url + "catalogue/" + sp.find_all("a")[-1].get("href")
            img_link = base_url + sp.find("img").get("src")
            title = sp.find_all("a")[-1].get("title")
            rating = sp.find("p").get("class")[-1]
            price = sp.find("p", class_="price_color").text[1:]
            stock = sp.find("p", class_="instock availability").text.strip()

            data.append([title, rating, price, stock, img_link, book_link])

        time.sleep(1)  # polite delay

    df = pd.DataFrame(
        data, columns=["title", "rating", "price", "stock", "img_link", "book_link"]
    )
    df.to_csv("Books.csv", index=False)
    return df


def scrape_book_details(book_links):
    """Scrape detailed info from each book page."""
    data = []

    for link in tqdm(book_links, desc="Scraping book details"):
        res = safe_get(link)
        if not res:
            continue

        soup = BeautifulSoup(res.text, "html.parser")

        typ = soup.find("ul", class_="breadcrumb").find_all("a")[-1].text
        tds = soup.find("table").find_all("td")

        upc = tds[0].text
        price_e = tds[2].text[2:]
        price_i = tds[3].text[2:]
        tax = tds[4].text[2:]
        qn = tds[5].text
        reviews = tds[6].text

        data.append([typ, price_e, price_i, tax, qn, upc, reviews])

        time.sleep(0.5)  # smaller delay for details

    df = pd.DataFrame(
        data,
        columns=[
            "category",
            "price_e_tax",
            "price_i_tax",
            "tax",
            "quantity",
            "upc",
            "reviews",
        ],
    )
    df.to_csv("data.csv", index=False)
    return df


def merge_data(df1, df2):
    """Merge basic book info with detailed info."""
    df = pd.DataFrame()

    df["title"] = df1["title"]
    df["upc"] = df2["upc"]
    df["category"] = df2["category"]
    df["price_e_tax"] = df2["price_e_tax"]
    df["price_i_tax"] = df2["price_i_tax"]
    df["tax"] = df2["tax"]
    df["rating"] = df1["rating"]
    df["reviews"] = df2["reviews"]
    df["quantity"] = df2["quantity"]
    df["stock"] = df1["stock"]
    df["book_link"] = df1["book_link"]
    df["img_link"] = df1["img_link"]

    df.to_csv("final.csv", index=False)
    print("✅ Saved final.csv with full dataset!")


if __name__ == "__main__":
    df1 = scrape_books_list()
    df2 = scrape_book_details(df1["book_link"])
    merge_data(df1, df2)