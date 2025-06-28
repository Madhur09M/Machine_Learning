# streamlit 
# python lib

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time

##page configuration
st.set_page_config(
    page_title="streamlit function demo",         
    page_icon="😂",
    layout="centered"
)

## title and text element
st.title("hello world")
st.header("1.Text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,code text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")


st.divider()

### metrices and messages
st.header("2. Metrices and messages")
st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")
st.error("this is an error message")
st.warning("this is a warning message")
st.info("info message")
st.success("success message")
st.exception(ValueError("this is an exception message"))


st.divider()


###data display#

st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

st.divider()


## charts
st.header("4.charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)

st.divider()

# widgets
st.header("5. Widgets")
with st.form("input form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    mood = st.radio("Select your mood", ("happy", "sad", "neutral"))
    languages = st.multiselect("Select your languages", ("Englist", "French", "German", "Hindi", "Sanskrit"))
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Name : {name}, {name}'s Age : {int(age)}, {name}'s Mood : {mood} Languages : {languages}")

col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
with col2:
    mood = st.radio("Select your mood", ("happy", "sad", "neutral"))
    languages = st.multiselect("Select your languages", ("Englist", "French", "German", "Hindi", "Sanskrit"))
with col3:
    # st.header("maxim")
    pass

# form using nested with and col
with st.form("input form2"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age")
    with col2:
        mood = st.radio("Select your mood", ("happy", "sad", "neutral"))
        languages = st.multiselect("Select your languages", ("Englist", "French", "German", "Hindi", "Sanskrit"))
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Name : {name}, {name}'s Age : {int(age)}, {name}'s Mood : {mood} Languages : {languages}")

col1, col2 = st.columns(2)
with col1:
    volumn = st.slider("Select a volumn", 0, 100)
with col2:
    color = st.color_picker("Choose the color", "#00FF3A")


st.text_area("Enter the msg")
st.date_input("select the data")
st.time_input("Select the time")
st.file_uploader("uplode the file")

st.divider()

# media
st.header("6. Media")
st.image("https://puzzlemania-154aa.kxcdn.com/products/2024/puzzle-schmidt-1000-pieces-random-galaxy.webp", caption = "random image")
# st.video("")
# st.audio("")


# sidebar and layout

st.sidebar.header("SideBar Header")
st.sidebar.write("this is a side bar text")
st.sidebar.button("click me")
option = st.sidebar.selectbox("Select an option", ("option1", "option2", "option3"))


# container
with st.container():
    st.write("this is a container")

with st.expander("expander.header"):
    st.write("this is a expander")

with st.spinner("loading data..."):
    time.sleep(5)

# st.success("data loaded")
st.toast("toast message", icon = "😒")

st.page_link("https://github.com/Madhur09M", label = "github account", icon = "😉")