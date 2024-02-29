import feedparser

def fetch_stock_market_news():
    rss_url = "https://www.moneycontrol.com/rss/marketreports.xml"  # Replace with the actual RSS feed URL
    feed = feedparser.parse(rss_url)
    
    stock_market_news = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = entry.published

        # Assuming that stock market news contains specific keywords or phrases
        if "stock" in title.lower() or "stock" in description.lower():
            stock_market_news.append({
                "title": title,
                "link": link,
                "description": description,
                "pub_date": pub_date
            })
    
    return stock_market_news

# Example usage
stock_market_news = fetch_stock_market_news()
for news in stock_market_news:
    print(news)
