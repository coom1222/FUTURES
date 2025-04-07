import ccxt
import os
import math
import time
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI
from datetime import datetime

serp_api_key = os.getenv("SERP_API_KEY")  # .env 파일에 SERP_API_KEY 추가 필요
def fetch_bitcoin_news():
    try:
        # SERP API를 사용해 비트코인 관련 최신 뉴스 가져오기
        url = "https://serpapi.com/search.json"
        params = {
            "engine": "google_news",
            "q": "bitcoin",
            "gl": "us",
            "hl": "en",
            "api_key": serp_api_key
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            news_results = data.get("news_results", [])

            # 최신 뉴스 10개만 추출하고 title과 date만 포함
            recent_news = []
            for i, news in enumerate(news_results[:10]):
                news_item = {
                    "title": news.get("title", ""),
                    "date": news.get("date", "")
                }
                recent_news.append(news_item)

            print(f"Collected {len(recent_news)} recent news articles (title and date only)")
            return recent_news
        else:
            print(f"Error fetching news: Status code {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

recent_news = fetch_bitcoin_news()

print(recent_news)