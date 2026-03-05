from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    if request.method == 'POST':
        # รับข้อมูลจากแบบสอบถาม 
        user_skills = request.form.getlist('skills')
        user_interest = request.form.get('interest')

        # อัลกอริทึมวิเคราะห์เบื้องต้น (Scoring System)
        scored_jobs = []
        for job in jobs_data:
            score = 0
            # ตรวจสอบทักษะที่ตรงกัน
            matched_skills = set(user_skills) & set(job['skills'])
            score += len(matched_skills) * 2
            
            # ตรวจสอบความสนใจ
            if user_interest == job['interest']:
                score += 3
            
            if score > 0:
                scored_jobs.append({"name": job['name'], "score": score})

        # เรียงลำดับตามคะแนน และเลือก 3-5 อันดับแรก 
        scored_jobs.sort(key=lambda x: x['score'], reverse=True)
        recommendations = scored_jobs[:5]

    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    # รันบน Local server ตามขอบเขตโครงงาน [cite: 8]
    app.run(debug=True)