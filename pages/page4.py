import streamlit as st
import time
from st_pages import Page, show_pages, add_page_title
from PIL import Image

# ... (rest of your code)


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
st.header(':fire: 뉴스 공유하기', divider='orange')

# 영상 파일 경로 리스트
video_files = ["news1.mp4", "news2.mp4", "news4.mp4"]
current_video_index = 0

# Streamlit 앱 시작
st.subheader("국제 분쟁 뉴스 모음")

# 현재 영상 파일
current_video_file = video_files[current_video_index]

# 영상 보여주기
video_placeholder = st.empty()
video_placeholder.video(current_video_file)

def main():
    # Call the function to set the background image
     set_background()


with st.form(key='my_form'):
        st.markdown('**의견 공유하기** :pencil:')
        student_result1 = st.text_input("훌륭한 점을 써 보세요. :blush:")
        student_result2 = st.text_input("바라는 점을 써 보세요. 🤔")

        if st.form_submit_button('답변 제출'):
            st.write(f"**1:** '{student_result1}', **2:** '{student_result2}'")
            st.success("답변이 제출되었습니다. 수고하셨어요 :clap:")

# 다음 영상으로 넘어가는 버튼
if st.button("다음 영상"):
    current_video_index = (current_video_index + 1) % len(video_files)
    current_video_file = video_files[current_video_index]

    # 버튼 클릭 후 동적으로 업데이트
    video_placeholder.video(current_video_file)
    st.success("다음 영상으로 이동합니다. 🚀")