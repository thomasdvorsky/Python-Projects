import re

print("🚀 Welcome to the Career Analyzer!")

# Ask for user input
career_input = input("Tell me about your career situation, goals, and what you want to achieve:\n")

print("\n📌 Analyzing your career path...\n")

# Extract salary (looks for "$80K", "$120,000", etc.)
salary_match = re.search(r"\$(\d+[,.]?\d*)", career_input)
salary = salary_match.group(1) if salary_match else "Unknown"

# Extract job title (detects variations like "I am an operations analyst at a bank")
role_match = re.search(r"I am (a|an) ([\w\s-]+) (for|at) ([\w\s-]+)", career_input, re.IGNORECASE)
role = role_match.group(2) if role_match else "Unknown Role"
industry = role_match.group(4) if role_match else "Unknown Industry"

# Extract certifications (allows any format like "POPM SAFe certification, Tableau Desktop Specialist, etc.")
certs_match = re.findall(r"([A-Za-z0-9\s-]+certification|certified\s[A-Za-z0-9\s-]+)", career_input, re.IGNORECASE)
certifications = ", ".join(certs_match) if certs_match else "None listed"

# Extract career goal (looks for "I want to...")
goal_match = re.search(r"I want to (.*?)(\.|$)", career_input, re.IGNORECASE)
goal = goal_match.group(1) if goal_match else "Unknown goal"

# Print extracted details
print(f"💰 Current Salary: ${salary}")
print(f"👨‍💼 Current Role: {role}")
print(f"🏢 Industry: {industry}")
print(f"🎓 Certifications: {certifications}")
print(f"🎯 Career Goal: {goal}")

print("\n✨ Career decisions are personal! Keep exploring and aligning with what excites you. 🚀")
