import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="Neha Revankar's Portfolio", layout="wide")

# Layout with columns
col1, col2 = st.columns([1, 2])

# Load image
image = Image.open("C:/Users/Neha/Desktop/weatherapp/neha.jpg")

with col1:
    st.image(image, width=150)

with col2:
    st.markdown("""
        <h1 style='color:#2E86C1;'>🙋‍♀️ Neha Revankar</h1>
        <p style='color:#117A65;'><strong>Email:</strong> neharevankar8@gmail.com<br>
        <strong>Phone:</strong> 8884236887</p>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<h3 style='color:#BA4A00;'>🎯 CAREER OBJECTIVE</h3>
<p style='color:#1B2631;'>To work in an enthusiastic and supportive environment that provides opportunities to explore my knowledge and contribute meaningfully to the organization. Eager to apply my skills, learn continuously, and add value through innovation and dedication.</p>

<h3 style='color:#BA4A00;'>💼 EXPERIENCE</h3>
<ul style='color:#1B2631;'>
<li><strong>COCREATE VENTURES | Research Intern</strong><br><em>Feb 2025 (Ongoing) | Bangalore, Karnataka</em><br>Developing an automated cloud infrastructure provisioning and deployment system using Terraform, RabbitMQ, and cost estimation services.</li>
<li><strong>ELEWAYTE | AI Intern</strong><br><em>May 2024 – June 2024 | Belagavi, Karnataka</em><br>Specialized in Data Analysis and Healthcare AI, skilled in Machine Learning and Agile Project Management.</li>
<li><strong>DLITHE | IoT Intern</strong><br><em>Oct 2023 – Nov 2023 | Belagavi, Karnataka</em><br>Built 'Smart Gas' project and developed sensor expertise.</li>
<li><strong>COACHED | Python Intern</strong><br><em>Oct 2022 – Nov 2022 | Belagavi, Karnataka</em><br>Enhanced Python programming and data visualization skills.</li>
</ul>

<h3 style='color:#BA4A00;'>💻 PROJECTS</h3>
<ul style='color:#1B2631;'>
<li><strong>SmartSort – Municipal Waste Categorization System</strong><br>Used CNN and DenseNet201 on 5000 images achieving 92% accuracy.</li>
<li><strong>Plant Leaf Disease Detection</strong><br>Implemented AI diagnosis using Random Forest, CNN, and HOG features.</li>
<li><strong>License Plate Detection</strong><br>Developed system using OpenCV, Tesseract OCR, and contour detection.</li>
</ul>

<h3 style='color:#BA4A00;'>🎓 EDUCATION</h3>
<p style='color:#1B2631;'><strong>Jain College of Engineering and Research</strong><br>Pursuing Bachelor's in CSE – 8th Sem (Expected 2025), Belgaum<br><strong>CGPA:</strong> 8.5</p>

<h3 style='color:#BA4A00;'>🛠️ SKILLS</h3>
<p style='color:#1B2631;'>Programming: Python, C/C++<br>Technology: Git/GitHub, AWS, Linux, DevOps, AI</p>

<h3 style='color:#BA4A00;'>🌟 EXTRACURRICULAR ACTIVITIES</h3>
<ul style='color:#1B2631;'>
<li>Presented research paper at National Conference (NIT Rourkela, Feb 2024)</li>
<li>Organizer at BelPy 2024 (Python Conference)</li>
<li>Research paper under review: "Rice Leaf Disease Detection using ML"</li>
</ul>

<h3 style='color:#BA4A00;'>📜 CERTIFICATIONS</h3>
<p style='color:#1B2631;'>IIWCS-2024 by Springer and NIT Rourkela</p>

<h3 style='color:#BA4A00;'>🔗 LINKS</h3>
<ul style='color:#1B2631;'>
<li><a href='https://github.com/revankarneha7' target='_blank'>GitHub</a></li>
<li><a href='https://linkedin.com/in/neha-revankar-6540062a1' target='_blank'>LinkedIn</a></li>
</ul>
""", unsafe_allow_html=True)
