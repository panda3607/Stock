import streamlit as st
from newsapi import NewsApiClient

# Replace 'YOUR_API_KEY' with your News API key
news_api_key = '35892c3df4644a40a4a359ecb65a7657'

# Initialize NewsApiClient with your API key
newsapi = NewsApiClient(api_key=news_api_key)

# Mapping of country names to country codes
country_codes = {
    "United States": "us",
    "United Kingdom": "gb",
    "Canada": "ca",
    "Australia": "au",
}

st.title("Stock Market News")

# Sidebar for user input
st.sidebar.header("Filter News:")
keyword = st.sidebar.text_input("Keyword (optional)", "")
category = st.sidebar.selectbox("Category", ["Business", "Technology", "Finance", "Stock Market"])
country = st.sidebar.selectbox("Country", list(country_codes.keys()))

# Fetch news articles based on user input
if keyword:
    articles = newsapi.get_everything(q=keyword, language="en", sort_by="relevancy")
else:
    country_code = country_codes.get(country)
    if not country_code:
        st.error("Invalid country name. Please select a valid country.")
    else:
        articles = newsapi.get_top_headlines(category=category.lower(), country=country_code, language="en")

# Display news articles
if articles:
    for article in articles["articles"]:
        st.subheader(article["title"])
        st.write(article["source"]["name"])
        st.write(article["description"])
        st.write(f"Published at: {article['publishedAt']}")
        st.write(f"Source: [Read more]({article['url']})")
        st.write("---")
else:
    st.warning("No news articles found.")

# Note: You need to replace 'YOUR_API_KEY' with your actual News API key.
