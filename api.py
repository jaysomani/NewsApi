# api.py
from flask import Flask, jsonify
from rss_feed_fetcher import fetch_moneycontrol_feeds, fetch_livemint_feed
from data_models import Article

app = Flask(__name__)

@app.route('/moneycontrol-feeds')
def moneycontrol_feeds():
    moneycontrol_articles = fetch_moneycontrol_feeds()
    return jsonify(moneycontrol_articles)

@app.route('/livemint-feed')
def livemint_feed():
    livemint_articles = fetch_livemint_feed()
    return jsonify(livemint_articles)

if __name__ == '__main__':
    app.run(debug=True)
