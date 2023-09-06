from pathlib import Path
import streamlit as st
import base64
from PIL import Image


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path):
    img_html = f"<a href='{img_path['url']}'>" \
               f"<img src='data:image/png;base64,{img_to_bytes(img_path['logo'])}' " \
               f"width='110' " \
               f"class='img-fluid'>" \
               f"</a>"
    return img_html


# ---- Path settings ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "zahid_cv.pdf"
profile_pic = current_dir / "assets" / "zahid-pic.png"

# ---- General settings ----
title = "CV | Zahid Islam"
icon = ":wave:"
name = "Zahid Islam"
description_file = open(f"{current_dir}/assets/description.txt", "r")
description = description_file.read()

email = "zahidcseku@gmail.com"

linkedin = {'url': "https://www.linkedin.com/in/mdzahidislam/",
            'logo': f"{current_dir}/assets/LI-Logo.png"
            }
github = {'url': "https://github.com/zahidcseku",
          'logo': f"{current_dir}/assets/GitHub_Logo.png"
          }
schorar = {'url': "https://scholar.google.com/citations?user=WpBYmZgAAAAJ&hl=en",
          'logo': f"{current_dir}/assets/scholar.png"
          }

st.set_page_config(page_title=title,
                   layout="wide",
                   page_icon=icon,
                   initial_sidebar_state="expanded",
                   )

# -- load stuffs
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as cvfile:
    cvbyte = cvfile.read()

profile_pic = Image.open(profile_pic)

# header section
col1, col2, emptycol = st.columns(3, gap="small")
with col1:
    st.image(profile_pic, width=230)
    st.write(":email:", email)
    #st.write(":iphone:", "0406427413")
    st.markdown(img_to_html(linkedin), unsafe_allow_html=True)
    st.markdown(img_to_html(github), unsafe_allow_html=True)
    st.markdown(img_to_html(schorar), unsafe_allow_html=True)
    st.download_button(
        label="Download Resume",
        data=cvbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )

with col2:
    st.title(name)
    st.write(description)
