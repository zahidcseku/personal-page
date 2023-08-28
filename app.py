from pathlib import Path
import streamlit as st

from PIL import Image

# ---- Path settings ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "zahid_cv.pdf"
profile_pic = current_dir / "assets" / "zahid-pic.png"

# ---- General settings ----
title = "CV | Zahid Islam"
icon = ":wave:"
name = "Zahid Islam"
description = """
Passionate about the intersection of machine learning and real-world impact, 
I'm a seasoned researcher with expertise in machine learning, text analysis, and 
explainability methods. With a PhD in Computer and Information Science, I've 
pioneered innovative approaches to enhance the accuracy and validity of machine 
learning models.

Throughout my journey as a Post-Doctoral Research Fellow at CSIRO Australia, 
I've collaborated with diverse business units to develop cutting-edge, 
explainable machine learning models. My proficiency extends to Deep Neural 
Networks, Graph Neural Networks, Natural Language Processing, and 
Sentiment Analysis.

My programming prowess in C, C++, Java, and Python enables me to bridge 
theoretical innovation with practical implementation. Additionally, my commitment 
to transparency and robustness has led me to specialize in explainability 
methods, ensuring the reliability of models in critical applications.

From academia to industry, I've contributed as an educator, guiding students in 
grasping complex concepts, and as a researcher, addressing research gaps with 
innovative mathematical techniques. My track record as an Assistant Professor, 
Online Tutor, and Research Assistant has equipped me with strong communication 
and pedagogical skills, enabling me to translate intricate technical ideas 
into accessible insights.

If you're seeking an expert who can drive impactful machine learning solutions 
while prioritizing transparency and reliability, let's connect. Together, we can 
harness the power of data to make informed decisions that shape industries and 
empower innovation.
"""
email = "zahidcseku@gmail.com"
linkedin = "https://www.linkedin.com/in/mdzahidislam/"
#    "GitHub": "https://github.com/zahidcseku"

st.set_page_config(page_title=title, page_icon=icon)

#st.title("Hello there!!")

# -- load stuffs
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as cvfile:
    cvbyte = cvfile.read()

profile_pic = Image.open(profile_pic)

# header section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    st.download_button(
        label="Download Resume",
        data=cvbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(":email:", email)
    st.write(":iphone:", "0406427413")
    st.markdown(f"[![Title]('{current_dir}/assets/LinkedIn-Logos/LI-Logo.png')]({linkedin})")

with col2:
    st.title(name)
    st.write(description)

