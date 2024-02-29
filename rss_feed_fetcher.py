# rss_feed_fetcher.py
import feedparser

def fetch_rss_feed(feed_url):
    """
    Fetches articles from the given RSS feed URL.
    
    Args:
        feed_url (str): URL of the RSS feed.
    
    Returns:
        list: List of dictionaries representing articles.
    """
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        article = {
            "title": entry.title,
            "link": entry.link,
            "description": entry.description,
            "pub_date": entry.published
        }
        articles.append(article)
    return articles

def fetch_moneycontrol_feeds():
    """
    Fetches articles from multiple RSS feeds on Moneycontrol.
    
    Returns:
        dict: Dictionary containing articles from different RSS feeds.
    """
    moneycontrol_feeds = {
        "economy": fetch_rss_feed("https://www.moneycontrol.com/rss/economy.xml"),
        "market_reports": fetch_rss_feed("https://www.moneycontrol.com/rss/marketreports.xml"),
        "brokerage_recos": fetch_rss_feed("https://www.moneycontrol.com/rss/brokeragerecos.xml"),
        "buzzing_stocks": fetch_rss_feed("https://www.moneycontrol.com/rss/buzzingstocks.xml"),
        "business": fetch_rss_feed("https://www.moneycontrol.com/rss/business.xml")
    }
    return moneycontrol_feeds

def fetch_livemint_feed():
    """
    Fetches articles from the LiveMint RSS feed.
    
    Returns:
        list: List of dictionaries representing articles.
    """
    return fetch_rss_feed("https://www.livemint.com/rss/markets")
