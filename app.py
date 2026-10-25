import streamlit as st
import pandas as pd
import joblib

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Student Placement PREDICTION",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

/* Main title */
.hero {
    text-align: center;
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(135deg, #172033, #111827);
    border: 1px solid #263247;
    margin-bottom: 30px;
}

.hero-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 8px;
}

.hero-text {
    font-size: 17px;
    color: #aab4c3;
}

/* Section headers */
.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 15px;
}

/* Result */
.result-card {
    padding: 25px;
    border-radius: 18px;
    background: #151c28;
    border: 1px solid #2b374a;
    text-align: center;
    margin-top: 20px;
}

.probability {
    font-size: 42px;
    font-weight: 700;
    margin: 10px;
}

.small-text {
    color: #9ca8b8;
    font-size: 15px;
}

/* Model info */
.info-card {
    padding: 20px;
    border-radius: 15px;
    background: #151c28;
    border: 1px solid #2b374a;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# Load Model
# -----------------------------------
model = joblib.load("model/placement_model.pkl")


# -----------------------------------
# Hero Section
# -----------------------------------
st.markdown("""
<div class="hero">

<div class="hero-title">
🎓 Student Placement PREDICTION
</div>

<div class="hero-text">
Machine Learning based Student Placement Prediction System
</div>

</div>
""", unsafe_allow_html=True)


# -----------------------------------
# Academic Details
# -----------------------------------
st.markdown(
    '<div class="section-title">🎓 Academic Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    branch = st.selectbox(
        "Branch",
        ["CSE (AI/ML) ", "CSE", "ECE", "ME", "CE", "EE", "IT"]
    )

with col2:
    college_tier = st.selectbox(
        "College Tier",
        ["1", "2", "3"]
    )

with col3:
    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0,
        step=0.1
    )

with col4:
    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=20,
        value=0
    )


# -----------------------------------
# Technical Skills
# -----------------------------------
st.markdown(
    '<div class="section-title">💻 Technical Skills</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    coding_skills = st.number_input(
        "💻 Coding Skills (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

with col2:
    dsa_score = st.number_input(
        "🧠 DSA Score (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

col1, col2 = st.columns(2)

with col1:
    aptitude_score = st.number_input(
        "📚 Aptitude Score (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

with col2:
    communication_skills = st.number_input(
        "🗣️ Communication Skills (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

col1, col2 = st.columns(2)

with col1:
    ml_knowledge = st.number_input(
        "🤖 ML Knowledge (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

with col2:
    system_design = st.number_input(
        "🏗️ System Design (0–10)",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )


# -----------------------------------
# Experience
# -----------------------------------
st.markdown(
    '<div class="section-title">🚀 Experience & Activities</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    internships = st.number_input(
        "💼 Internships",
        min_value=0,
        max_value=10,
        value=1
    )

with col2:
    projects_count = st.number_input(
        "📁 Projects",
        min_value=0,
        max_value=20,
        value=2
    )

with col3:
    certifications = st.number_input(
        "🏆 Certifications",
        min_value=0,
        max_value=20,
        value=1
    )

col1, col2, col3 = st.columns(3)

with col1:
    hackathons = st.number_input(
        "⚡ Hackathons",
        min_value=0,
        max_value=20,
        value=0
    )

with col2:
    open_source_contributions = st.number_input(
        "🌐 Open Source Contributions",
        min_value=0,
        max_value=50,
        value=0
    )

with col3:
    extracurriculars = st.number_input(
        "🎯 Extracurricular Activities",
        min_value=0,
        max_value=20,
        value=2
    )


st.divider()


# -----------------------------------
# Prediction
# -----------------------------------
if st.button(
    "🔮  PREDICT PLACEMENT",
    use_container_width=True,
    type="primary"
):

    input_data = pd.DataFrame({
        "branch": [branch],
        "college_tier": [college_tier],
        "cgpa": [cgpa],
        "backlogs": [backlogs],
        "coding_skills": [coding_skills],
        "dsa_score": [dsa_score],
        "aptitude_score": [aptitude_score],
        "communication_skills": [communication_skills],
        "ml_knowledge": [ml_knowledge],
        "system_design": [system_design],
        "internships": [internships],
        "projects_count": [projects_count],
        "certifications": [certifications],
        "hackathons": [hackathons],
        "open_source_contributions": [open_source_contributions],
        "extracurriculars": [extracurriculars]
    })

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    probability_percent = probability * 100


    # -----------------------------------
    # Result
    # -----------------------------------
    st.markdown(
        '<div class="section-title">📊 Prediction Result</div>',
        unsafe_allow_html=True
    )

    if prediction == 1:

        st.success("🎉 STUDENT IS LIKELY TO BE PLACED")

        st.markdown(
            f"""
            <div class="result-card">

            <div class="small-text">
            Placement Probability
            </div>

            <div class="probability">
            {probability_percent:.2f}%
            </div>

            <div class="small-text">
            🟢 High placement potential
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.error("❌ STUDENT IS UNLIKELY TO BE PLACED")

        st.markdown(
            f"""
            <div class="result-card">

            <div class="small-text">
            Placement Probability
            </div>

            <div class="probability">
            {probability_percent:.2f}%
            </div>

            <div class="small-text">
            🔴 Placement probability is currently low
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("### Placement Probability")

    st.progress(float(probability))

# -----------------------------------
# Model Information
# -----------------------------------
st.divider()

with st.expander("🤖 About This Prediction Model"):

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Algorithm**")
        st.write("Logistic Regression")

    with col2:
        st.write("**Prediction Type**")
        st.write("Binary Classification")

    with col3:
        st.write("**Purpose**")
        st.write("Student Placement Prediction")

    




