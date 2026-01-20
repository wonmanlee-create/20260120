import streamlit as st
import time

# 페이지 설정 (타이틀, 아이콘)
st.set_page_config(page_title="내 MBTI 맞춤 직업 탐구", page_icon="🚀", layout="centered")

# --- 커스텀 스타일링 (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stSelectbox div[data-baseweb="select"] {
        cursor: pointer;
    }
    h1 {
        color: #6200EA;
        text-align: center;
    }
    .job-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 데이터 정의 ---
mbti_jobs = {
    "ISTJ": {"desc": "책임감이 강하고 현실적인 관리자 📋", "jobs": ["회계사", "공무원", "사서", "웹 개발자"]},
    "ISFJ": {"desc": "타인을 돕는 따뜻한 수호자 🛡️", "jobs": ["간호사", "초등교사", "사회복지사", "인사담당자"]},
    "INFJ": {"desc": "통찰력 있는 이상주의자 🔮", "jobs": ["상담심리사", "작가", "환경 컨설턴트", "예술가"]},
    "INTJ": {"desc": "전략을 세우는 완벽주의자 💡", "jobs": ["데이터 과학자", "전략 기획자", "대학교수", "연구원"]},
    "ISTP": {"desc": "객관적이고 손재주가 좋은 분석가 🛠️", "jobs": ["엔지니어", "파일럿", "소방관", "데이터 분석가"]},
    "ISFP": {"desc": "예술적 감각이 뛰어난 예술가 🎨", "jobs": ["디자이너", "작곡가", "수의사", "플로리스트"]},
    "INFP": {"desc": "꿈꾸는 열정적인 중재자 🌈", "jobs": ["소설가", "카피라이터", "심리치료사", "영상 편집자"]},
    "INTP": {"desc": "논리적인 아이디어가 넘치는 전략가 🧪", "jobs": ["소프트웨어 개발자", "철학자", "경제학자", "수학자"]},
    "ESTP": {"desc": "스릴을 즐기는 활동가 🏃", "jobs": ["기업가", "스포츠 매니저", "마케터", "경찰관"]},
    "ESFP": {"desc": "분위기를 주도하는 연예인 🎤", "jobs": ["이벤트 플래너", "배우", "홍보 전문가", "여행 가이드"]},
    "ENFP": {"desc": "자유로운 영혼의 활동가 ✨", "jobs": ["콘텐츠 크리에이터", "광고 기획자", "유치원 교사", "파티 플래너"]},
    "ENTP": {"desc": "지적인 도전을 즐기는 발명가 🔍", "jobs": ["변호사", "벤처 캐피탈리스트", "정치인", "기획자"]},
    "ESTJ": {"desc": "체계적인 리더십의 관리자 👔", "jobs": ["경영자", "프로젝트 매니저", "은행원", "군 장교"]},
    "ESFJ": {"desc": "친절하고 사교적인 협력자 🤝", "jobs": ["승무원", "홍보팀원", "상담가", "호텔 지배인"]},
    "ENFJ": {"desc": "정의로운 사회 운동가 📢", "jobs": ["정치 리더", "코칭 전문가", "아나운서", "외교관"]},
    "ENTJ": {"desc": "비전을 제시하는 지도자 🗺️", "jobs": ["CEO", "경영 컨설턴트", "판사", "대학 총장"]}
}

# --- 메인 화면 구성 ---
st.title("🌈 내 꿈을 찾는 MBTI 진로 탐험대 🚀")
st.write("---")

st.header("✨ 당신의 MBTI는 무엇인가요?")
choice = st.selectbox("아래 목록에서 선택해주세요!", ["선택안함"] + list(mbti_jobs.keys()))

if choice != "선택안함":
    with st.spinner('당신의 미래를 분석 중입니다... 🔍'):
        time.sleep(1) # 효과를 위한 대기 시간
    
    st.balloons() # 풍선 효과!
    
    # 결과 섹션
    st.success(f"### 🎊 결과 발표: 당신은 **{choice}** 타입이군요!")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"#### 🧐 어떤 특징이 있나요?\n{mbti_jobs[choice]['desc']}")
    
    with col2:
        st.markdown("#### 🛠️ 추천 직업 리스트")
        for job in mbti_jobs[choice]['jobs']:
            st.markdown(f"- {job}")

    # 추가 꾸미기 (이미지/아이콘 영역)
    st.info(f"💡 **{choice}**에게 어울리는 환경은 '창의적이고 자유로운 곳'일 가능성이 높아요!")
    
    # 하단 응원 메시지
    st.write("---")
    st.markdown("#### 💌 미래의 주인공에게")
    st.write(f"MBTI는 성격의 한 단면일 뿐이에요. {choice}라는 틀에 갇히기보다, 당신의 가능성을 믿고 도전해보세요! 화이팅! 🔥")

else:
    st.write("위에 있는 드롭다운 메뉴를 클릭해서 MBTI를 골라보세요! 👇")
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60", caption="여러분의 꿈을 응원합니다!")

# 푸터
st.markdown("<br><br><p style='text-align: center; color: grey;'>© 2024 미래 진로 교육 연구소 🎓</p>", unsafe_allow_html=True)
