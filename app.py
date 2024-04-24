from pathlib import Path

import streamlit as st
from PIL import Image

# -- PATHs ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Vinicius Pavezi en.pdf"
profile_picture = current_dir / "assets" / "profile_pic.png"


# -- SETTINGS ---
PAGE_TITLE = "Digital CV | Vinicius Pavezi"
PAGE_ICON = ":wave:"
NAME = "Vinicius Pavezi"
DESCRIPTION = """
Full Stack Developer, assisting enterprise by giving representativity on the web
"""
EMAIL = "pavezivinicius@gmail.com"
SOCIAL_MEDIA = {
    "Blog": "https://distritodev.blogspot.com/",
    "Github": "https://github.com/Pavezi",
    "LinkedIn": "https://www.linkedin.com/in/vinicius-pavezi-53976b162/",
    "Instagram": "https://www.instagram.com/vinicius.pavezi/",
}
PROJECTS={
    "Fidelizou.me app -": "https://app.fidelizou.me/admin/index.html#/login",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

# -- LOAD --
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_picture)

# -- Hero --
col1,col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, use_column_width=True)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📥 Download Resume",
        data=PDFbyte,
        file_name=f"{NAME}.pdf",
        mime="application/octet-stream",
    )
    st.write("📮",EMAIL)

# -- SOCIAL --
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (plataform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{plataform}]({link})")

# -- EXPERIENCE --
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔ 5 Yeas experience on the tech industry
- ✔ 1 year working in global setup
- ✔ 3 years on web developent
- ✔ Excellent team-player and tasks solver
"""
)

# --SKILLS --
st.write("#")
st.subheader("🧰️ Hard Skills")
st.write(
    """
- 🇻ue JS
- 👾 Cypress
- 🔧 Node JS, TypeScript, Python
- ✈️ GitHub, CI/CD, Actions, AWS, GCP
"""
)

# -- Work --
st.write("#")
st.subheader("🗃 Work History")
st.write("---")

# -- Job 1 --

st.write("🖥","**Mid Level Full Stack Developer | Fidelizou.me**")
st.write("03/2023 - 03/2024")
st.write(
    """
- Fix and rebuild Startup Product 
- AWS ecossistem
- PSQL database
- Github Actions
"""
)

# -- Job 3 --

st.write("👔","**Analist | KTO**")
st.write("03/2023 - 03/2024")
st.write(
    """
- Detect Bugs 
- Track AWS ecossistem
- Quicksight
- Java (Spring Boot)
"""
)

# -- Job 2 --

st.write("📊","**Developer | Mercur**")
st.write("03/2023 - 03/2024")
st.write(
    """
- Generate reports and interpret data from the Prophix
- Integrate data with TalendStudio
- PSQL database
- VRaptor (Java)
"""
)


# # -- PROJECTS --
st.write("#")
st.subheader("🗃 Projects & Accomplhisments")
st.write("---")

for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# # -- Contact --