import streamlit as st
from PIL import Image
import base64
from st_pages import Page, show_pages, add_page_title


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
st.header(':fire: 지구촌 분쟁 뉴스 제작하기', divider='orange')



import streamlit as st

def main():
    st.subheader("🎬 영상편집 어플 capcut 사용법", divider='orange')

    # YouTube video link
    youtube_link = "https://youtu.be/rlFIYrWy-LI?si=T-TKlOMIB11GvyA5"

    # Display the video
    st.video(youtube_link)

if __name__ == "__main__":
    main()






def main():
    st.subheader("🎥 관심 있는 국제 분쟁을 한 가지 선택하여 뉴스를 제작해 봅시다.", divider='orange')

    # 파일 업로드 섹션
    st.text_area("영상을 제작하는 과정에서 맡은 역할을 각자 적어보세요.")

    st.text_area("영상에 대한 소개를 적어보세요.")

    # 영상 파일 업로드
    video_file = st.file_uploader("영상 파일 업로드", type=["mp4", "avi", "mov"])

    if video_file is not None:
        st.video(video_file)

        # 업로드된 비디오를 세션에 저장
        st.session_state.uploaded_video = video_file

        # 다음 페이지로 이동하는 버튼
        if st.button("다음 페이지로 이동"):
            st.experimental_rerun()

def show_video():
    st.title("우리 모둠의 뉴스")

    # 세션에서 업로드된 비디오를 가져옴
    uploaded_video = st.session_state.get("uploaded_video", None)

    if uploaded_video is not None:
        st.video(uploaded_video)

if __name__ == "__main__":
    # 메인 페이지를 표시
    if "uploaded_video" not in st.session_state:
        main()
    # 다음 페이지를 표시
    else:
        show_video()
