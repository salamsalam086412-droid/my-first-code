# 6-Year Roadmap Code for Germany & Dubai Journey

def show_my_plan():
    # 1. Current Personal Profile
    my_profile = {
        "current_age": 15,
        "current_skills": ["Python Basics", "English (6/10)"],
        "financial_status": "Secure (Zero local expenses)"
    }
    
    # 2. The 5 Skills Timeline (One Skill Per Year)
    the_5_skills = [
        "Year 1: Python Programming & Core Logic",
        "Year 2: Networking Foundations & Protocols",
        "Year 3: Cybersecurity Basics & Defense",
        "Year 4: Hacker Mindset & Penetration Testing",
        "Year 5: Artificial Intelligence & Neural Networks"
    ]
    
    # 3. Career & Income Strategy 
    career_timeline = {
        "phase_1": "2 Years - Paid Training / Internship (Salary increase after 6 months)",
        "phase_2": "4 Years - Remote Contract Job with Foreign Companies",
        "target_minimum_salary": "$1,800 per month"
    }
    
    # 4. Ultimate Milestones
    ultimate_goals = [
        "Graduate from high school at 19/20",
        "Travel to Germany for University (Bachelor & Master in Computer Science)",
        "Reach British English level 10/10",
        "Permanently settle in the UAE (Dubai) and buy a private apartment"
    ]
    
    # Printing the roadmap cleanly on the screen
    print("=== MY 6-YEAR LEGENDARY PLAN ===")
    print(f"[*] Current Age: {my_profile['current_age']} Years Old")
    print(f"[*] Target Minimum Salary: {career_timeline['target_minimum_salary']}\n")
    
    print("--- THE 5 SKILLS TIMELINE ---")
    for skill in the_5_skills:
        print(f" {skill}")
        
    print("\n--- CAREER & TRAINING TIMELINE ---")
    print(f"[+] Training Duration: {career_timeline['phase_1']}")
    print(f"[+] Job Duration: {career_timeline['phase_2']}\n")
    
    print("--- ULTIMATE GOALS ---")
    for goal in ultimate_goals:
        print(f"[-] {goal}")
    print("================================")

# Execute the function to view the roadmap
show_my_plan()
