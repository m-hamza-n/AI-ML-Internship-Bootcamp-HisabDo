import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

RAW_PATH = "data/student_performance.csv"
CLEAN_PATH = "data/student_performance_clean.csv"
CHARTS_DIR = "charts"

SEP = "\n" + "=" * 70

print(SEP)
print("1. LOAD DATASET")
print(SEP)
df = pd.read_csv(RAW_PATH)
print(f"Loaded {len(df)} rows from {RAW_PATH}")

print(SEP)
print("2. BASIC INFORMATION")
print(SEP)
print("\n--- df.info() ---")
df.info()
print("\n--- df.describe() ---")
print(df.describe(include="all"))
print("\n--- First 5 rows ---")
print(df.head())

print(SEP)
print("9. HANDLE MISSING / INVALID VALUES")
print(SEP)

print("\nMissing values per column (raw):")
print(df.isnull().sum())

n_before = len(df)
dup_count = df.duplicated().sum()
print(f"\nDuplicate rows found: {dup_count}")
df = df.drop_duplicates().reset_index(drop=True)

score_cols = ["Assignment Score", "Midterm Score", "Final Score", "Attendance"]
for col in score_cols:
    invalid_mask = (df[col] < 0) | (df[col] > 100)
    n_invalid = invalid_mask.sum()
    if n_invalid:
        print(f"'{col}': {n_invalid} out-of-range value(s) set to NaN "
              f"(will be imputed with column median)")
    df.loc[invalid_mask, col] = np.nan

age_invalid_mask = (df["Age"] < 15) | (df["Age"] > 60)
n_age_invalid = age_invalid_mask.sum()
if n_age_invalid:
    print(f"'Age': {n_age_invalid} unrealistic value(s) set to NaN "
          f"(will be imputed with column median)")
df.loc[age_invalid_mask, "Age"] = np.nan

numeric_cols = ["Age", "Attendance", "Assignment Score", "Midterm Score", "Final Score"]
for col in numeric_cols:
    median_val = df[col].median()
    n_missing = df[col].isnull().sum()
    if n_missing:
        df[col] = df[col].fillna(median_val)
        print(f"'{col}': {n_missing} missing value(s) filled with median = {median_val:.1f}")

for col in ["Gender"]:
    n_missing = df[col].isnull().sum()
    if n_missing:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        print(f"'{col}': {n_missing} missing value(s) filled with mode = '{mode_val}'")

df["Age"] = df["Age"].round().astype(int)
for col in ["Attendance", "Assignment Score", "Midterm Score", "Final Score"]:
    df[col] = df[col].round(1)

print(f"\nRows before cleaning: {n_before}  |  Rows after cleaning: {len(df)}")
df.to_csv(CLEAN_PATH, index=False)
print(f"Cleaned dataset saved to {CLEAN_PATH}")

print(SEP)
print("3. AVERAGE SCORES")
print(SEP)
avg_assignment = df["Assignment Score"].mean()
avg_midterm = df["Midterm Score"].mean()
avg_final = df["Final Score"].mean()
avg_attendance = df["Attendance"].mean()
print(f"Average Attendance:       {avg_attendance:.2f}%")
print(f"Average Assignment Score: {avg_assignment:.2f}")
print(f"Average Midterm Score:    {avg_midterm:.2f}")
print(f"Average Final Score:      {avg_final:.2f}")

print(SEP)
print("4. HIGHEST AND LOWEST SCORES")
print(SEP)
for col in ["Assignment Score", "Midterm Score", "Final Score"]:
    top = df.loc[df[col].idxmax()]
    low = df.loc[df[col].idxmin()]
    print(f"\n{col}:")
    print(f"  Highest -> {top['Student Name']} ({top[col]})")
    print(f"  Lowest  -> {low['Student Name']} ({low[col]})")

print(SEP)
print("5. STUDENTS WITH ATTENDANCE BELOW 75%")
print(SEP)
low_attendance = df[df["Attendance"] < 75][["Student Name", "Course", "Attendance"]]
print(f"Count: {len(low_attendance)}")
print(low_attendance.to_string(index=False))

print(SEP)
print("6. STUDENTS AT RISK OF FAILING")
print(SEP)
at_risk = df[(df["Final Score"] < 50) | (df["Attendance"] < 75)].copy()
at_risk["Risk Reason"] = np.where(
    (at_risk["Final Score"] < 50) & (at_risk["Attendance"] < 75),
    "Low final score & low attendance",
    np.where(at_risk["Final Score"] < 50, "Low final score", "Low attendance"),
)
print(f"Count: {len(at_risk)}")
print(at_risk[["Student Name", "Course", "Attendance", "Final Score", "Risk Reason"]]
      .to_string(index=False))

print(SEP)
print("7. AVERAGE SCORE BY COURSE")
print(SEP)
by_course = df.groupby("Course")[["Assignment Score", "Midterm Score", "Final Score"]].mean().round(2)
by_course["Overall Average"] = by_course.mean(axis=1).round(2)
print(by_course.sort_values("Overall Average", ascending=False))

print(SEP)
print("8. ATTENDANCE vs FINAL SCORE RELATIONSHIP")
print(SEP)
correlation = df["Attendance"].corr(df["Final Score"])
print(f"Correlation coefficient (Attendance vs Final Score): {correlation:.3f}")
if correlation > 0.5:
    strength = "a strong positive relationship"
elif correlation > 0.2:
    strength = "a moderate positive relationship"
elif correlation > -0.2:
    strength = "little to no linear relationship"
elif correlation > -0.5:
    strength = "a moderate negative relationship"
else:
    strength = "a strong negative relationship"
print(f"Interpretation: There is {strength} between attendance and final score.")

print(SEP)
print("GENERATING CHARTS")
print(SEP)
plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

plt.figure(figsize=(8, 5))
plt.hist(df["Final Score"], bins=10, color="#4C72B0", edgecolor="black")
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/1_score_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
by_course["Overall Average"].sort_values().plot(kind="barh", color="#55A868")
plt.title("Average Overall Score by Course")
plt.xlabel("Average Score")
plt.ylabel("Course")
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/2_avg_score_by_course.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Final Score"], color="#C44E52", alpha=0.7)
z = np.polyfit(df["Attendance"], df["Final Score"], 1)
trend = np.poly1d(z)
x_line = np.linspace(df["Attendance"].min(), df["Attendance"].max(), 100)
plt.plot(x_line, trend(x_line), color="black", linestyle="--", label="Trend line")
plt.title(f"Attendance vs Final Score (corr = {correlation:.2f})")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.legend()
plt.tight_layout()
plt.savefig(f"{CHARTS_DIR}/3_attendance_vs_final_score.png", dpi=150)
plt.close()

print(f"3 charts saved to {CHARTS_DIR}/")

print(SEP)
print("CONCLUSION")
print(SEP)
best_course = by_course["Overall Average"].idxmax()
worst_course = by_course["Overall Average"].idxmin()
conclusion = f"""
Out of {len(df)} students analyzed, the average final score was {avg_final:.1f}
and average attendance was {avg_attendance:.1f}%. {len(low_attendance)} student(s)
had attendance below 75%, and {len(at_risk)} student(s) were flagged as at risk
of failing (final score below 50 or attendance below 75%). '{best_course}' had
the highest overall average score, while '{worst_course}' had the lowest. The
correlation between attendance and final score was {correlation:.2f}, indicating
{strength} - suggesting that {"consistent attendance is associated with better final performance" if correlation > 0.2 else "attendance alone is not a strong standalone predictor of final performance in this dataset"}.
"""
print(conclusion)

with open("conclusion.txt", "w") as f:
    f.write(conclusion.strip() + "\n")
print("Conclusion saved to conclusion.txt")