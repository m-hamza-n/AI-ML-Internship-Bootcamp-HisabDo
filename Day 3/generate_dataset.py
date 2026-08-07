import numpy as np
import pandas as pd

np.random.seed(42)

first_names = [
    "Ali", "Ahmed", "Sara", "Fatima", "Hassan", "Ayesha", "Bilal", "Zainab",
    "Usman", "Hira", "Omar", "Mariam", "Hamza", "Sana", "Farhan", "Nida",
    "Imran", "Sadia", "Kashif", "Rabia", "Adeel", "Mahnoor", "Waqas", "Iqra",
    "Shahid", "Amna", "Noman", "Alina", "Faisal", "Komal", "Danish", "Sidra",
    "Zeeshan", "Nadia", "Tariq", "Warda", "Salman", "Anum", "Junaid", "Laiba",
]

courses = ["Python Basics", "Data Science", "Web Development", "AI Fundamentals"]
genders_pool = ["Male", "Female"]

n = 40
records = []

for i in range(n):
    name = first_names[i]
    age = int(np.random.randint(18, 26))
    gender = genders_pool[i % 2]
    course = courses[i % len(courses)]
    attendance = round(np.random.uniform(50, 100), 1)
    assignment_score = round(np.random.uniform(40, 100), 1)
    midterm_score = round(np.random.uniform(30, 100), 1)
    final_score = round(np.random.uniform(30, 100), 1)

    records.append({
        "Student Name": name,
        "Age": age,
        "Gender": gender,
        "Course": course,
        "Attendance": attendance,
        "Assignment Score": assignment_score,
        "Midterm Score": midterm_score,
        "Final Score": final_score,
    })

df = pd.DataFrame(records)

df.loc[3, "Attendance"] = np.nan
df.loc[7, "Assignment Score"] = np.nan
df.loc[15, "Final Score"] = np.nan
df.loc[22, "Age"] = np.nan
df.loc[30, "Gender"] = np.nan


df.loc[5, "Attendance"] = 130      # impossible attendance %
df.loc[12, "Midterm Score"] = -10  # negative score
df.loc[18, "Final Score"] = 150    # impossible score
df.loc[27, "Age"] = 3              # unrealistic age


df = pd.concat([df, df.iloc[[9]]], ignore_index=True)

df.to_csv("data/student_performance.csv", index=False)
print(f"Dataset created with {len(df)} rows -> data/student_performance.csv")
