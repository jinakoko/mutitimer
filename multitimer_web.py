# multitimer_web.py
import streamlit as st
import time

st.set_page_config(page_title="Multi Timer", layout="centered")
st.title("⏱️ Multi Timer")

# 세션 상태 저장
if 'time_left' not in st.session_state:
    st.session_state.time_left = 0
if 'is_running' not in st.session_state:
    st.session_state.is_running = False
if 'is_repeating' not in st.session_state:
    st.session_state.is_repeating = False

col1, col2, col3, col4 = st.columns(4)
if col1.button("10 min"):
    st.session_state.time_left += 600
if col2.button("1 min"):
    st.session_state.time_left += 60
if col3.button("10 sec"):
    st.session_state.time_left += 10
if col4.button("RESET"):
    st.session_state.time_left = 0
    st.session_state.is_running = False

minutes = st.session_state.time_left // 60
seconds = st.session_state.time_left % 60
st.markdown(f"<h1 style='text-align: center;'>{minutes:02d}:{seconds:02d}</h1>", unsafe_allow_html=True)

col5, col6 = st.columns(2)
if col5.button("START / STOP"):
    st.session_state.is_running = not st.session_state.is_running
if col6.button("REPEAT / STOP"):
    st.session_state.is_repeating = not st.session_state.is_repeating

# 타이머 동작
if st.session_state.is_running and st.session_state.time_left > 0:
    time.sleep(1)
    st.session_state.time_left -= 1
    st.experimental_rerun()
elif st.session_state.is_running and st.session_state.time_left == 0:
    st.session_state.is_running = False
    st.success("⏰ 타이머 끝!")
    if st.session_state.is_repeating:
        st.session_state.time_left = 600  # 예: 10분 반복
        st.session_state.is_running = True
        st.experimental_rerun()
