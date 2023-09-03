import streamlit as st

# Function to display resources based on skill level
def display_resources(skill_level):
    st.subheader(f"Resources for {skill_level}:")
    if skill_level == "Beginners":
        st.markdown("1. [Investopedia - Stock Basics](https://www.investopedia.com/investing-4689748)")
        st.markdown("2. [Yahoo Finance - Stock Market Basics](https://finance.yahoo.com/stock-market-basics/)")
        st.markdown("3. [Investor.gov - Introduction to Investing](https://www.investor.gov/introduction-investing)")
    elif skill_level == "Intermediate":
        st.markdown("1. [Investopedia - Intermediate Stock Trading](https://www.investopedia.com/intermediate-stock-trading-tips-4772024)")
        st.markdown("2. [Investing.com - Technical Analysis](https://www.investing.com/education/technical-analysis)")
        st.markdown("3. [Investopedia - Fundamental Analysis](https://www.investopedia.com/terms/f/fundamentalanalysis.asp)")
    elif skill_level == "Advanced":
        st.markdown("1. [Investopedia - Advanced Stock Trading Strategies](https://www.investopedia.com/advanced-stock-trading-tips-4771946)")
        st.markdown("2. [Investing.com - Options Trading](https://www.investing.com/education/options-trading)")
        st.markdown("3. [Investopedia - Quantitative Analysis](https://www.investopedia.com/terms/q/quantitativeanalysis.asp)")

st.title("Stocks and Stock Prediction Educational Resources")

# Sidebar for skill level selection
st.sidebar.header("Select Skill Level:")
skill_level = st.sidebar.radio("Choose your skill level:", ("Beginners", "Intermediate", "Advanced"))

# Display resources based on skill level
display_resources(skill_level)
