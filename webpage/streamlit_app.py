from PIL import Image
import requests
import streamlit as st
from streamlit_lottie as st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":smile:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_p4q9ra7d.json")
img_contact_form = Image.open("image/_MG_2274-min.jpg")
img_lottie_animation = Image.open("image/_MG_2293 (2)-min-min.jpg")
# Header Section
with st.container():
    st.subheader("Hi, I am Puji :smirk:")
    st.title("A newbie in programing")
    st.write("I am learning web developer for develop my skills")
    st.write("[My Social>](https://www.instagram.com/pujiprastyo24/)")

# What I Do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
        """
        On my life i am like a lot things like:
        - learn proggraming
        - learn robotic 
        - learn to service electronic tools
        - learn photography.
        """
        )
        st.write("[My Project>](https://www.youtube.com/playlist?list=PLwvmhtXiU1SXjRpc7dfMD5i5Y9388KP1a)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#Project
with st.container():
    st.write("---")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
        
    with text_column:
        st.subheader("Simple web project")
        st.write(
            """
            I am learning web developmet with python programing lenguage, 
            because python lenguage is very simple and easy to anderstand.
            I am learn python lenguage in 
            """
        )
        st.markdown("[youtube...](https://www.youtube.com/c/KelasTerbuka)")


    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        
    with text_column:
        st.subheader("Simple web project")
        st.write(
            """
            I am learning web developmet with python programing lenguage, 
            because python lenguage is very simple and easy to anderstand.
            I am learn python lenguage in 
            """
        )
        st.markdown("[youtube...](https://www.youtube.com/c/KelasTerbuka)")
