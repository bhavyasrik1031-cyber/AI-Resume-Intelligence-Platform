import streamlit as st
from PyPDF2 import PdfReader

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="AI Resume Intelligence & Career Guidance Platform",
    layout="centered"
)

# ---------------- Title ----------------
st.title("🧠 AI Resume Intelligence & Career Guidance Platform")
st.caption(" Skill Gap Detection & Career Guidance")

st.markdown("---")

# ---------------- Upload Resume ----------------
uploaded_file = st.file_uploader(
    "📤 Upload your resume (PDF only)",
    type=["pdf"]
)

# ---------------- Career Selection ----------------
job_role = st.selectbox(
    "🎯 Select your target career role",
    ["Software Engineer", "Data Scientist", "Web Developer", "AI/ML Engineer"]
)

# ---------------- Skill Database ----------------
ROLE_SKILLS = {
    "Software Engineer": ["Python", "DSA", "OOP", "Git", "SQL"],
    "Data Scientist": ["Python", "Statistics", "Machine Learning", "Pandas", "SQL"],
    "Web Developer": ["HTML", "CSS", "JavaScript", "React", "Git"],
    "AI/ML Engineer": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "Mathematics"]
}

COURSES = {
    "Software Engineer": [
        "Data Structures & Algorithms",
        "System Design Basics",
        "Git & GitHub",
        "SQL for Developers"
    ],
    "Data Scientist": [
        "Statistics for Data Science",
        "Machine Learning Algorithms",
        "Pandas & NumPy",
        "Data Visualization"
    ],
    "Web Developer": [
        "JavaScript Fundamentals",
        "React Development",
        "Responsive Web Design",
        "Git Version Control"
    ],
    "AI/ML Engineer": [
        "Machine Learning Foundations",
        "Deep Learning",
        "TensorFlow / PyTorch",
        "Mathematics for ML"
    ]
}

INTERVIEW_TOPICS = {
    "Software Engineer": [
        "Arrays & Strings",
        "OOP Concepts",
        "SQL Queries",
        "Git Workflow"
    ],
    "Data Scientist": [
        "Probability & Statistics",
        "ML Algorithms",
        "Data Cleaning",
        "SQL Joins"
    ],
    "Web Developer": [
        "JavaScript Concepts",
        "React Lifecycle",
        "CSS Flexbox & Grid",
        "API Integration"
    ],
    "AI/ML Engineer": [
        "Supervised vs Unsupervised Learning",
        "Neural Networks",
        "Overfitting & Regularization",
        "Model Evaluation Metrics"
    ]
}

# ---------------- PDF Text Extraction ----------------
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# ---------------- Analysis ----------------
if st.button("🔍 Analyze Resume"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a PDF resume.")
    else:
        resume_text = extract_text_from_pdf(uploaded_file)
        resume_lower = resume_text.lower()
        required_skills = ROLE_SKILLS[job_role]

        matched_skills = []
        missing_skills = []

        for skill in required_skills:
            if skill.lower() in resume_lower:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        score = int((len(matched_skills) / len(required_skills)) * 100)

        st.success("✅ Resume Analysis Completed")

        # -------- Resume Score --------
        st.subheader("📊 Resume Score")
        st.progress(score)
        st.write(f"**Score:** {score}/100")

        st.markdown("---")

        # -------- Skill Analysis --------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            for s in matched_skills or ["None"]:
                st.write(f"- {s}")

        with col2:
            st.subheader("❌ Missing Skills")
            for s in missing_skills or ["None 🎉"]:
                st.write(f"- {s}")

        st.markdown("---")

        # -------- Resume Improvement --------
        st.subheader("🛠 Resume Improvement Tips")
        if missing_skills:
            st.write("• Add projects demonstrating missing skills")
            st.write("• Mention tools, technologies, and outcomes clearly")
            st.write("• Quantify achievements (e.g., improved accuracy by 20%)")
        else:
            st.write("• Add advanced projects")
            st.write("• Include internships or certifications")
            st.write("• Focus on impact-based descriptions")

        st.markdown("---")

        # -------- Learning Path --------
        st.subheader("📚 Recommended Learning Path")
        for course in COURSES[job_role]:
            st.write(f"- {course}")

        st.markdown("---")

        # -------- Interview Prep --------
        st.subheader("🎯 Interview Preparation Topics")
        for topic in INTERVIEW_TOPICS[job_role]:
            st.write(f"- {topic}")

