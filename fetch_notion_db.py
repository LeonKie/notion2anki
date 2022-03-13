
import os
import notion_df
notion_df.pandas() #That's it!
import pandas as pd

database_id="c47dc072-ec05-4737-a122-c2afb036cf76"
page_url="https://www.notion.so/leonkie/c47dc072ec054737a122c2afb036cf76?v=115ad9d0fdca484b8985869824d5b5bd"

df = pd.read_notion(page_url, api_key=os.environ.get("NOTION_PYTHON_SECRET"))

df.Tags

print(df[df.Tags == "[Important]"].head())

#print(df.head(50))


def generator():
    yield "Hello"