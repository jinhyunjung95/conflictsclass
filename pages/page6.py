import streamlit as st
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
st.subheader(':fire: 모의 UN 개최하기', divider='orange')




def main():
    st.subheader("🌐 실제 UN 회의 영상")

    # YouTube 영상의 공유 링크
    youtube_link = "https://www.youtube.com/live/lsTBwjm4WVI?si=n6e3KawYBQENlmLC"

    # YouTube 영상 삽입
    st.video(youtube_link)

if __name__ == "__main__":
    main()


def main():
    st.subheader("🌐 모의 UN 회의 진행 절차")

    # YouTube 영상의 공유 링크
    youtube_link = "https://youtu.be/d-kcKJm8cjk?si=47HShj5kXL1yiePH"

    # YouTube 영상 삽입
    st.video(youtube_link)

if __name__ == "__main__":
    main()


def main():
    st.subheader("내가 대표할 국가 선택하기")

    # 나라 목록
    countries = ['미국', '캐나다', '독일', '이집트', '영국', '이스라엘', '팔레스타인']

    # 선택 박스를 통해 나라 선택
    selected_country = st.selectbox("나라 선택", countries)

    # 선택된 나라의 정보 표시
    st.markdown(f"선택한 나라: {selected_country}")
    

if __name__ == "__main__":
    main()


def get_mun_procedure(topic):
    # 여기에 모의 UN 진행 절차를 가져오는 로직을 추가합니다.
    # 예를 들어, 각 단계에 해당하는 설명을 리스트에 담아 반환하도록 합니다.
    procedure_steps = [
        "1. 회의 시작 및 개회식",
        "2. 의사진행규칙 제정",
        "3. 의제 발표",
        "4. 의제 토론",
        "5. 토의 진행 중 특별 발언 및 질문",
        "6. 토의 종료 및 토의 결과 투표",
        "7. 성과 보고 및 평가",
        "8. 회의 종료"
    ]

    return procedure_steps

def main():
    st.subheader("🌐 모의 UN 진행 절차 확인")

    # 의제 입력 받기
    mun_topic = st.text_input("의제를 입력하세요:", "")

    # '모의 UN 진행 절차 보기' 버튼 클릭 여부 확인
    if st.button("모의 UN 진행 절차 보기"):
        # 모의 UN 진행 절차 가져오기
        procedure_steps = get_mun_procedure(mun_topic)

        # 모의 UN 진행 절차 표시
        st.header("모의 UN 진행 절차")
        for step in procedure_steps:
            st.write(f"- {step}")

if __name__ == "__main__":
    main()

    def main():
    # Call the function to set the background image
     set_background()


    with st.form(key='my_form'):
        st.markdown('**준비하기** :pencil:')
        student_result1 = st.text_input("자신이 맡은 국가의 외교관이 되어 의제를 해결하기 위한 방안을 적어 보세요. 🤔")
        student_result2 = st.text_input("회의에 참석하는 다른 나라들에게 질문할 내용을 적어 보세요. 🤔")

        if st.form_submit_button('답변 제출'):
            st.write(f"**1:** '{student_result1}', **2:** '{student_result2}'")
            st.success("답변이 제출되었습니다. 수고하셨어요 :clap:")