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
    
def suggest_skills(job_role):
    suggestions = {
        "ai engineer": ["Python", "TensorFlow", "NLP", "Prompt Engineering"],
        "data scientist": ["Python", "Pandas", "Scikit-learn", "Statistics"],
        "web developer": ["HTML", "CSS", "JavaScript", "React"]
    }

    return suggestions.get(job_role.lower(), ["Explore more to get suggestions!"])

# Input from user
name = "Abhijeet"
job_role = "ai engineer"

skills = suggest_skills(job_role)

print(f"Hi {name}! For becoming a {job_role.title()}, you should focus on:")
for skill in skills:
    print("✅", skill)

# Step 1: User input via keyboard
name = input("Enter your name: ")
job_role = input("Enter your dream job role: ")

# Step 2: Suggest skills based on job role
def suggest_skills(job_role):
    suggestions = {
        "ai engineer": ["Python", "TensorFlow", "NLP", "Prompt Engineering"],
        "data scientist": ["Python", "Pandas", "Scikit-learn", "Statistics"],
        "web developer": ["HTML", "CSS", "JavaScript", "React"]
    }
    return suggestions.get(job_role.lower(), ["Explore more to get suggestions!"])

# Step 3: Show personalized output
skills = suggest_skills(job_role)

print(f"\nHi {name}! For becoming a {job_role.title()}, you should focus on:")
for skill in skills:
    print("✅", skill)

