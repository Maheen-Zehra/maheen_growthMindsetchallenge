#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Challenge", project_icon=" 🌱")
st.title("Growth Mindset Challenge: Web App with Streamlit ")

st.header("🚀 Welcome To Your Growth Journey!")
st.write("Push your limits, transform obstacles into opportunities, and unlock the power of persistence! 🚀✨ Embrace the journey of continuous growth and unleash your limitless potential! 💡")

#quote section
st.header("Today's Growth Mindset Quote🌟")
st.write("'Success is the sum of small efforts, repeated day in and day out.'– Robert Collier 💪🌱Keep going, every step counts! 🚀")

st.header("🔗What's Your Challenge?")
user_input = st.text_input("Describe Your Challenge here.")


#condition
if user_input:
    st.success(f"Your Challenge: {user_input}. Keep advancing toward your vision, the finish line is within reach! 🌟💪
               Push ahead with unwavering determination! 🚀🔥")
    
else:
    st.warning("Tell us about your challenge to get started!")


#reflection
st.header("Reflection on your Learning 📚💡")
reflection = st.text_area("Write your Reflections here.")

if reflection:
    st.success(f"✨Great Insight!Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties.")

#achievement
st.header("🏆Celebrate Your Wins!🎉")
achievement = st.text_input("Share something You've recently accomplished:")

if achievement:
    st.success(f"🎉Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now😊")

#footer
st.write("- - -")
st.write("'Embrace every challenge as a chance to grow and become the best version of yourself!' 🌱💪✨") 
st.write("**©️ created by 'Maheen Zehra'**")
   


