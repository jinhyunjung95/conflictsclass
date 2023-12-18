import streamlit as st
st._is_running_with_streamlit = False

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
st.title("PROJECT 지구촌 분쟁 해결하기")
st.header(' ')
st.subheader(':fire: 지구촌 갈등에 대한 나의 생각', divider='orange')

def main():
    # Call the function to set the background image
    set_background()


    with st.form(key='my_form'):
        st.markdown('**생각해 보기** :pencil:')
        student_result1 = st.text_input("지구촌에는 어떠한 갈등이 발생하고 있을까요? 🤔")
        student_result2 = st.text_input("이러한 갈등의 원인에는 어떤 것들이 있을까요? 🤔")

        if st.form_submit_button('갈등의 종류 및 원인 제출'):
            st.write(f"**갈등의 종류:** '{student_result1}', **갈등의 원인:** '{student_result2}'")
            st.success("답변이 제출되었습니다. 수고하셨어요 :clap:")

if __name__ == "__main__":
    main()

# 페이지 연결
show_pages(
    [
        Page("main.py", "생각 나누기", ":pencil:"),
        Page("pages\page2.py", "세계 분쟁 지도 탐색하기", ":airplane:"),
        Page("pages\page3.py", "세계 분쟁 뉴스 만들기", ":📰:"),
        Page("pages\page4.py", "뉴스 공유하기", ":🤝:"),
        Page("pages\page5.py", "가장 시급한 분쟁은?", ":fire:"),
        Page("pages\page6.py", "모의 UN 개최하기", ":🌐:")
    ]
)