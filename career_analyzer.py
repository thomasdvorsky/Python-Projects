import re

print("🚀 Welcome to the Career Analyzer!")

# Ask for user input
career_input = input("Tell me about your career situation, goals, and what you want to achieve:\n")

print("\n📌 Analyzing your career path...\n")

# Extract salary (if mentioned)
salary_match = re.search(r"\$(\d+[,.\d]*)", career_input)
salary = salary_match.group(1) if salary_match else "Unknown"

# Extract current role and industry
role_match = re.search(r"I am a (.*?) for a (.*?)[.,]", career_input)
role = role_match.group(1) if role_match else "Unknown Role"
industry = role_match.group(2) if role_match else "Unknown Industry"

# Extract certifications
certs_match = re.findall(r"\bCFA|CPA|MBA|AWS|PMP|Google\sCerts\b", career_input, re.IGNORECASE)
certifications = ", ".join(certs_match) if certs_match else "None listed"

# Extract career goal
goal_match = re.search(r"I want to (.*?)\.", career_input)
goal = goal_match.group(1) if goal_match else "Unknown goal"

# Print extracted details
print(f"💰 Current Salary: ${salary}")
print(f"👨‍💼 Current Role: {role}")
print(f"🏢 Industry: {industry}")
print(f"🎓 Certifications: {certifications}")
print(f"🎯 Career Goal: {goal}")

print("\n✨ Career decisions are personal! Keep exploring and aligning with what excites you. 🚀")
