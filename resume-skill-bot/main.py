def suggest_skills(job_role):
    skills = {
        "data scientist": ["Python", "Pandas", "Machine Learning", "Statistics"],
        "web developer": ["HTML", "CSS", "JavaScript", "React"],
        "ai engineer": ["Python", "TensorFlow", "NLP", "Prompt Engineering"],
        "android developer": ["Java", "Kotlin", "Android SDK"],
    }

    job_role = job_role.lower()
    return skills.get(job_role, ["General Programming", "Problem Solving"])

name = input("Enter your name: ")
job = input("Enter your dream job role: ")

suggested = suggest_skills(job)

print(f"\nHi {name}! For becoming a {job.title()}, you should focus on:")
for skill in suggested:
    print(f"✅ {skill}")
