# Student Performance Analysis — Day 3 Task
**HisabDo AI/ML Internship Program**

A Pandas-based exploratory analysis of a synthetic student performance
dataset, covering data loading, cleaning, statistical analysis, and
visualization (no ML modeling — that comes later in the program).

## 📁 Repository Structure

```
student_performance/
├── data/
│   ├── student_performance.csv         # raw dataset (41 records, intentionally messy)
│   └── student_performance_clean.csv   # cleaned dataset (output of analysis.py)
├── charts/
│   ├── 1_score_distribution.png
│   ├── 2_avg_score_by_course.png
│   └── 3_attendance_vs_final_score.png
├── generate_dataset.py                 # creates the synthetic raw dataset
├── analysis.py                         # main analysis + chart generation script
├── conclusion.txt                      # auto-generated written summary
└── README.md
```

## 📊 Dataset

40+ synthetic student records with the following fields:
`Student Name, Age, Gender, Course, Attendance, Assignment Score, Midterm Score, Final Score`

Courses covered: Python Basics, Data Science, Web Development, AI Fundamentals.

The raw file deliberately includes missing values, out-of-range scores
(e.g. negative or >100), an unrealistic age, and a duplicate row, so the
cleaning step in `analysis.py` has real issues to fix.

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib
python generate_dataset.py   # regenerates data/student_performance.csv
python analysis.py           # runs full analysis, cleans data, saves charts
```

## 🧪 What `analysis.py` Does

1. **Load the dataset** from `data/student_performance.csv`
2. **Basic info** — `.info()`, `.describe()`, and a preview of the data
3. **Clean the data** — drops duplicates, converts out-of-range/invalid
   values (attendance/scores outside 0–100, unrealistic ages) to `NaN`,
   then imputes missing numeric values with the column **median** and
   missing categorical values with the **mode**
4. **Average scores** — mean attendance, assignment, midterm, and final scores
5. **Highest/lowest scores** — per assessment type, with student names
6. **Low attendance list** — all students under 75% attendance
7. **At-risk students** — flagged if Final Score < 50 **or** Attendance < 75%
8. **Average score by course** — grouped comparison across the 4 courses
9. **Attendance vs. Final Score relationship** — Pearson correlation
   coefficient with a plain-English interpretation

## 📈 Charts

| Chart | Description |
|---|---|
| `1_score_distribution.png` | Histogram of final score distribution across all students |
| `2_avg_score_by_course.png` | Horizontal bar chart comparing average overall score by course |
| `3_attendance_vs_final_score.png` | Scatter plot with trend line showing the attendance–final score relationship |

## ✅ Conclusion

See [`conclusion.txt`](conclusion.txt) for the auto-generated summary. In
short: average final score and attendance were both moderate, roughly a
quarter of students were flagged as at-risk (mainly due to low
attendance), **AI Fundamentals** had the strongest average performance
while **Web Development** lagged behind, and attendance showed **little
to no linear correlation** with final score in this particular dataset —
meaning attendance alone isn't a reliable standalone predictor here,
though it remains a useful early-warning signal when combined with
assignment/midterm performance.

---
*Part of the HisabDo AI/ML Internship — Day 3: Dataset → Pandas → Data
Cleaning → Analysis → Visualization.*
