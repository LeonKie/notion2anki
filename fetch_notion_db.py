
import os
import notion_df
notion_df.pandas() #That's it!
import pandas as pd

def main():
    
    # Use secret key from environment variable
    page_url=os.environ.get('NOTION_LINK')
    df = pd.read_notion(page_url, api_key=os.environ.get("NOTION_PYTHON_SECRET"))

    df_filtered=df[df.apply(lambda x: "Knowledge" == x.Type, axis=1)]

    queries=[]
    for i in range(df_filtered.shape[0]):
        name=df_filtered.iloc[i].Name
        queries.append(name)

    return queries


if __name__ == '__main__':
    main()
    