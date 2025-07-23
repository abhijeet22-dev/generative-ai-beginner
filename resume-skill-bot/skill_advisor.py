def get_job_recommendation(job_role, skills):
    job_role = job_role.lower()
    skills = [skill.strip().lower() for skill in skills.split(",")]

    recommendations = {
        "data scientist": ["python", "pandas", "numpy", "machine learning", "statistics"],
        "web developer": ["html", "css", "javascript", "react", "node.js"],
        "ai engineer": ["python", "machine learning", "deep learning", "tensorflow", "pytorch"],
        "android developer": ["java", "kotlin", "android studio", "firebase"]
    }

    if job_role in recommendations:
        required_skills = recommendations[job_role]
        matched = [skill for skill in skills if skill in required_skills]

        if matched:
            return f"✅ You're a good match for **{job_role.title()}**.\nMatched skills: {', '.join(matched)}"
        else:
            return f"⚠️ You selected **{job_role.title()}**, but your skills don't match.\nRequired: {', '.join(required_skills)}"
    else:
        # Search by matching skills if job role is unknown or incorrect
        matched_roles = []
        for role, req_skills in recommendations.items():
            matches = [s for s in skills if s in req_skills]
            if matches:
                matched_roles.append((role, matches))
        
        if matched_roles:
            response = "🔎 Based on your skills, possible job roles:\n"
            for role, matched in matched_roles:
                response += f"- {role.title()} (matched: {', '.join(matched)})\n"
            return response
        else:
            return "❌ Sorry, we couldn't find any matching job role for your skills."


# ---------- Run ----------
while True:
    job = input("Enter your desired job role (or 'exit' to stop): ")
    if job.lower() == "exit":
        break
    skills = input("Enter your skills (comma-separated): ")
    print(get_job_recommendation(job, skills))
    print("-" * 50)
