import streamlit as st

# ข้อมูลอาชีพและเงื่อนไขเบื้องต้น (Knowledge Base)
jobs_data = [
    {"name": "Data Scientist", "skills": ["Python", "Math"], "interest": "Data"},
    {"name": "Web Developer", "skills": ["HTML", "CSS"], "interest": "Design"},
    {"name": "AI Engineer", "skills": ["Python", "Logic"], "interest": "AI"},
    {"name": "Business Analyst", "skills": ["English", "Logic"], "interest": "Business"},
    {"name": "UX/UI Designer", "skills": ["Design", "Art"], "interest": "Design"},
    {"name": "Cybersecurity Analyst", "skills": ["Network", "Logic"], "interest": "Security"},
    {"name": "Digital Marketer", "skills": ["English", "Content"], "interest": "Business"},
    {"name": "Software Tester", "skills": ["Logic", "Detail"], "interest": "Quality"},
    {"name": "Game Developer", "skills": ["Python", "Design"], "interest": "Gaming"},
    {"name": "Data Engineer", "skills": ["SQL", "Python"], "interest": "Data"}
]

st.title("ระบบช่วยตัดสินใจเลือกสายอาชีพ")

# รับข้อมูลจากแบบสอบถาม
st.subheader("ทักษะที่คุณถนัด (เลือกได้หลายข้อ):")
col1, col2 = st.columns(2)
with col1:
    s1 = st.checkbox("Python")
    s2 = st.checkbox("HTML/CSS")
    s3 = st.checkbox("SQL/Database")
    s4 = st.checkbox("Network & Security")
    s5 = st.checkbox("Logic/Algorithm")
with col2:
    s6 = st.checkbox("Graphic Design")
    s7 = st.checkbox("English Communication")
    s8 = st.checkbox("Content Creation")
    s9 = st.checkbox("Mathematics")

user_skills = []
if s1: user_skills.append("Python")
if s2: user_skills.append("HTML")
if s3: user_skills.append("SQL")
if s4: user_skills.append("Network")
if s5: user_skills.append("Logic")
if s6: user_skills.append("Design")
if s7: user_skills.append("English")
if s8: user_skills.append("Content")
if s9: user_skills.append("Math")


st.subheader("ความสนใจหลัก:")
user_interest = st.selectbox("เลือกความสนใจของคุณ", 
    ["Data", "AI", "Design", "Business", "Security", "Gaming"])

if st.button("วิเคราะห์อาชีพ"):
    scored_jobs = []
    for job in jobs_data:
        score = 0
        matched_skills = set(user_skills) & set(job['skills'])
        score += len(matched_skills) * 2
        
        if user_interest == job['interest']:
            score += 3
        
        if score > 0:
            scored_jobs.append({"name": job['name'], "score": score})

    scored_jobs.sort(key=lambda x: x['score'], reverse=True)
    recommendations = scored_jobs[:5]

    st.divider()
    st.subheader("สายอาชีพที่เหมาะสมสำหรับคุณ:")
    for job in recommendations:
        st.write(f"**{job['name']}** (คะแนนความเหมาะสม: {job['score']})")

