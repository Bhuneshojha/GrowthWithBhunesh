import streamlit as st

st.set_page_config(page_title="Growth Mindset App", layout="centered")
st.title("🌱 Growth Mindset App")

# Hero Section
st.markdown(
    """
    <div style="padding: 2em; text-align: center; background-color: #f0f8ff; border-radius: 20px; margin-bottom: 2em;">
        <h2>Ready to grow? 🚀</h2>
        <p>Welcome to the Growth Mindset App! This app is designed to help you develop a growth mindset, which is the belief that you can improve your abilities through hard work and dedication. Research shows that people with a growth mindset are more likely to succeed in school, work, and life. So let's get started!</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Daily Quote Section
st.markdown(
    """
    <div style="padding: 1.5em; background-color: #e6f7ff; border-radius: 15px; margin-bottom: 2em;">
        <h3>Today's Quote 🌟</h3>
        <p>“Focus on your actions, not the results.” - Lord Krishna</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Goal Input Section
st.subheader("What's your goal for today? 🎯")
user_input = st.text_input("Enter your goal for today:")
if user_input:
    st.success(f"✅ Your goal for today is: {user_input} Keep up the good work!")
else:
    st.warning("Tell us about your goal to get started!")

# Reflection Section
st.subheader("Daily Reflection on Your Learning 🤔")
reflection = st.text_area("What did you learn today? Write here.")
if reflection:
    st.success(f"✨ Great! You learned: {reflection} Keep up the good work!")
else:
    st.info("Reflect on your past experiences to grow better! Share your hardships and success stories here.")

# Achievements Section
st.subheader("Celebrate Your Achievements 🎉🏆")
achievement = st.text_input("Share something you recently accomplished!")
if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("😊 Big or small, every achievement matters! Share your success stories here 💫")

st.write("---")
st.write("🙏 Remember, developing a growth mindset is a journey! Stay positive, and never give up! ❤️")
st.write("**💻💡 Developed by Bhunesh Kumar**")
