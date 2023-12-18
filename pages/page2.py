import streamlit as st
import requests
from streamlit_folium import folium_static
import folium
from st_pages import Page, show_pages, add_page_title
from PIL import Image


def set_background():
    # Set background image using custom CSS
    st.markdown(
        """
        <style>
            body {
                background-image: url('mainpic.png');  /* Update with your image file name */
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(layout="wide")

# header 부분
image = Image.open('mainpic.png')
st.image(image)
st.header(' ')
st.header(':fire: 지구촌 분쟁 지도', divider='orange')


# Naver API credentials
naver_client_id = "VLPDmrDeeEcO7kkPtHXD"
naver_client_secret = "9_Jk3P62kF"

# Streamlit app configuration
st.subheader('🔍 분쟁이 일어나는 부분을 선택하면 해당 내용을 검색할 수 있어요.')

# Coordinates for specified locations
locations = {
    '시리아': (34.8021, 38.9968),
    '이스라엘': (31.0461, 34.8516),
    '독도': (37.2423, 131.8613),
    '미얀마': (21.9162, 95.9560),
    '우크라이나': (48.3794, 31.1656),
    '수단': (12.8628, 30.2176),
}

# Display a map with markers
m = folium.Map(location=[20, 0], zoom_start=2)
for location, coords in locations.items():
    folium.Marker(location=coords, popup=location, icon=folium.Icon(color='red', icon='fire')).add_to(m)
folium_static(m)

# Placeholder for displaying news articles and images
news_display = st.empty()

# Function to get news articles for a specific location from Naver API

def get_news_articles(query):
    url = f"https://openapi.naver.com/v1/search/news.json"
    params = {
        'query': query,
        'display': 5,  # Number of results to display
        'sort': 'sim',  # Sort by relevance
        'start': 1,  # Start from the first result
        'dsc': 'ko',  # Display Korean articles
    }
    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        news_data = response.json()
        return news_data.get('items', [])
    except requests.exceptions.HTTPError as errh:
        st.error(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.error(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.error(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.error(f"Error: {err}")
    return []




# Streamlit app to handle marker clicks
clicked_location = st.selectbox("Select a location:", list(locations.keys()))

# If a marker is clicked, show a button to search for news for that location
if st.button(f"Search {clicked_location} News"):
    st.info(f"Searching for {clicked_location} news...")
    articles = get_news_articles(clicked_location)  # Adjust the query as needed
    # Display news articles and images
    news_display.header(f"{clicked_location} 뉴스 최신 기사")
    for article in articles:
        title = article['title']
        description = article.get('description', '')
        link = article.get('link', '')
        image_url = article.get('thumbnail', '')
        
        st.write(f"**제목:** {title}")
        st.write(f"**설명:** {description}")
        st.write(f"**링크:** [{link}]({link})")
        
        if image_url:
            st.image(image_url, caption='Article Image', use_column_width=True)

        st.write('-' * 40)

def main():
    # Call the function to set the background image
    set_background()

    st.title("지구촌 갈등에 대한 나의 생각")

    with st.form(key='my_form'):
        st.markdown('**정리해보기** :pencil:')
        student_result1 = st.text_input("어느 나라를 선택하였나요? :blush:")
        student_result2 = st.text_input("조사한 내용을 정리해 봅시다. :blush:")

        if st.form_submit_button('갈등의 종류 및 원인 제출'):
            try:
                # Assuming you want to store the user's responses or perform some action
                store_user_responses(student_result1, student_result2)
                
                # Display confirmation
                st.write(f"**나라:** '{student_result1}', **갈등의 내용:** '{student_result2}'")
                st.success("답변이 제출되었습니다. 수고하셨어요 :clap:")
            except Exception as e:
                st.error(f"Error processing form submission: {str(e)}")
