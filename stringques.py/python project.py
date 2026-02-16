# question_bank.py

QUESTION_BANK = {
    "python": [
        "Explain list vs tuple in Python.",
        "What is the difference between deep copy and shallow copy?",
        "Explain decorators in Python.",
        "What are Python generators?",
        "Explain OOP concepts in Python."
    ],
    
    "sql": [
        "What is normalization in SQL?",
        "What is the difference between WHERE and HAVING?",
        "Explain JOIN types in SQL.",
        "What is indexing in SQL?",
        "What are ACID properties?"
    ],
    
    "data analysis": [
        "What is the difference between mean and median?",
        "Explain data cleaning process.",
        "What is exploratory data analysis?",
        "What are outliers?",
        "Explain correlation vs covariance."
    ],
    
    "machine learning": [
        "What is overfitting?",
        "Explain bias-variance tradeoff.",
        "Difference between supervised and unsupervised learning?",
        "What is cross-validation?",
        "Explain logistic regression."
    ]
}


import random
from question_bank import QUESTION_BANK

def read_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().lower()

def extract_skills(resume_text):
    detected_skills = []
    
    for skill in QUESTION_BANK.keys():
        if skill in resume_text:
            detected_skills.append(skill)
    
    return detected_skills

def generate_questions(skills):
    questions = []
    
    for skill in skills:
        skill_questions = QUESTION_BANK[skill]
        selected = random.sample(skill_questions, min(2, len(skill_questions)))
        questions.extend(selected)
    
    return questions

def main():
    resume_text = read_resume("resume.txt")
    skills = extract_skills(resume_text)
    
    if not skills:
        print("No matching skills found.")
        return
    
    print("\nDetected Skills:", skills)
    print("\nGenerated Interview Questions:\n")
    
    questions = generate_questions(skills)
    
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")

if __name__ == "__main__":
    main()



# Detected Skills: ['python', 'sql', 'data analysis']

# Generated Interview Questions:

# 1. Explain list vs tuple in Python.
# 2. What are Python generators?
# 3. What is normalization in SQL?
# 4. Explain JOIN types in SQL.
# 5. What is exploratory data analysis?
# 6. What are outliers?


