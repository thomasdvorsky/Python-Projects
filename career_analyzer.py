import re

print("🚀 Welcome to the Career Analyzer!")

# Ask for user input
career_input = input("Tell me about your career situation, goals, and what you want to achieve:\n")

print("\n📌 Analyzing your career path...\n")

# Extract salary (handles different formats: "$80K", "$75,000 per year", etc.)
salary_match = re.search(r"\$?(\d+[,.]?\d*)\s?(k|K|per year|annually)?", career_input)
if salary_match:
    raw_salary = salary_match.group(1)
    if salary_match.group(2) and "k" in salary_match.group(2).lower():
        salary = f"${raw_salary}K"  # Convert "80 k" to "$80K"
    else:
        salary = f"${raw_salary}"  # For standard formats
else:
    salary = "Unknown"

# Extract job title and industry (handles "I am a ___ for a ___" and "I work as a ___ in ___")
role_match = re.search(r"I (am|work as) (a|an) ([\w\s-]+?) (for|at|in) ([\w\s-]+)", career_input, re.IGNORECASE)
role = role_match.group(3).strip() if role_match else "Unknown Role"
industry = role_match.group(5).strip() if role_match else "Unknown Industry"

# Refine industry (convert raw input like "a bank doing operational work" → "Banking")
industry = re.sub(r"\b(a|the|doing|working in|sector|field|work)\b", "", industry, flags=re.IGNORECASE).strip()
if industry.lower() in ["bank", "banking", "finance"]:
    industry = "Banking"
elif industry.lower() in ["tech", "technology", "software"]:
    industry = "Technology"

# Extract certifications (pulls only proper cert names, ignoring filler words)
certs_match = re.findall(r"\b([\w\s-]+certification|certified\s[\w\s-]+)\b", career_input, re.IGNORECASE)
certifications = ", ".join([cert.strip() for cert in certs_match]) if certs_match else "None listed"

# Extract career goal (ensures structured phrasing without "of some sorts" or "soon")
goal_match = re.search(r"I want to (.*?)($|\.|\ssoon)", career_input, re.IGNORECASE)
goal = goal_match.group(1).strip() if goal_match else "Unknown goal"

# Print extracted details
print(f"💰 Current Salary: {salary}")
print(f"👨‍💼 Current Role: {role}")
print(f"🏢 Industry: {industry}")
print(f"🎓 Certifications: {certifications}")
print(f"🎯 Career Goal: {goal}")

print("\n✨ Career decisions are personal! Keep exploring and aligning with what excites you. 🚀")
