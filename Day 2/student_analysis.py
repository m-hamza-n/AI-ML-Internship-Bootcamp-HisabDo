import pandas as pd

students = [
    {"name": "Ahmed", "age": 20, "course": "AI", "marks": 85},
    {"name": "Ali", "age": 22, "course": "Data Science", "marks": 62},
    {"name": "Sara", "age": 21, "course": "AI", "marks": 91},
    {"name": "Hina", "age": 23, "course": "Web Development", "marks": 93},
    {"name": "Bilal", "age": 20, "course": "AI", "marks": 55},
    {"name": "Fatima", "age": 22, "course": "Data Science", "marks": 88},
    {"name": "Usman", "age": 24, "course": "Web Development", "marks": 45},
    {"name": "Ayesha", "age": 21, "course": "AI", "marks": 79},
    {"name": "Hamza", "age": 23, "course": "Data Science", "marks": 45},
    {"name": "Zara", "age": 20, "course": "Web Development", "marks": 93},
]

df = pd.DataFrame(students)

marks_gr_70 = df[df["marks"] > 70]
print(marks_gr_70)

avg_marks = df['marks'].mean()
print(f"\nAverage Marks: {avg_marks}\n")

highest_marks = df[df["marks"] == df["marks"].max()]
print(f"---Highest Marks---{highest_marks}\n")

lowest_marks = df[df["marks"] == df["marks"].min()]
print(f"---Lowest Marks---{lowest_marks}\n")

tot_num_of_stu = len(df)
print(f"Total No of Students: {tot_num_of_stu}")