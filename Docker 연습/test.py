import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, "html.parser")

titles = [a.text for a in soup.select(".titleline a")]
df = pd.DataFrame(titles, columns=["Headline"])
print(df.head())
