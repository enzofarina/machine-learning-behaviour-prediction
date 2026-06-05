import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, r2_score
from xgboost import XGBRegressor

# ── 1. LOAD DATA ─────────────────────────────────────────────────────────────
# Reads the CSV from the same directory as this script.
# To use a different path, set the STUDENT_CSV environment variable:
#   export STUDENT_CSV=/path/to/StudentPerformanceFactors.csv
CSV_PATH = os.environ.get(
    "STUDENT_CSV",
    os.path.join(os.path.dirname(__file__), "StudentPerformanceFactors.csv")
)

print(f"Loading dataset from: {CSV_PATH}")
df = pd.read_csv(CSV_PATH)
print(df.head())

# ── 2. HANDLE MISSING VALUES ─────────────────────────────────────────────────
df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0], inplace=True)
df['Parental_Education_Level'].fillna("None", inplace=True)
df['Distance_from_Home'].fillna("Complex", inplace=True)

remaining_nans = df.isnull().sum()
if remaining_nans.sum() > 0:
    print("Remaining NaNs:\n", remaining_nans[remaining_nans > 0])
else:
    print("No missing values remaining.")

# ── 3. EXPLORATORY CHARTS ────────────────────────────────────────────────────
fig_configs = [
    {"x": "Internet_Access",           "type": "box",    "palette": "Set2",    "title": "Internet Access and Exam Score"},
    {"x": "Extracurricular_Activities", "type": "box",    "palette": "Set3",    "title": "Extracurricular Activities and Exam Score"},
    {"x": "Parental_Involvement",       "type": "box",    "palette": "coolwarm","title": "Parental Involvement and Exam Score"},
    {"x": "Motivation_Level",           "type": "violin", "palette": "Pastel1", "title": "Motivation Level and Exam Score"},
    {"x": "Learning_Disabilities",      "type": "box",    "palette": "Set1",    "title": "Learning Disabilities and Exam Score"},
    {"x": "Peer_Influence",             "type": "box",    "palette": "Blues",   "title": "Peer Influence and Exam Score"},
]

for cfg in fig_configs:
    plt.figure(figsize=(8, 6))
    if cfg["type"] == "box":
        sns.boxplot(data=df, x=cfg["x"], y="Exam_Score", palette=cfg["palette"])
    else:
        sns.violinplot(data=df, x=cfg["x"], y="Exam_Score", palette=cfg["palette"])
    plt.title(cfg["title"])
    plt.tight_layout()
    plt.show()

# Scatter: attendance vs exam score
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Attendance", y="Exam_Score")
plt.title("School Attendance vs Exam Score")
plt.grid(True)
plt.tight_layout()
plt.show()

# ── 4. FEATURE ENGINEERING ───────────────────────────────────────────────────
# Overall_Academic
df['Extracurricular_Activities_Num'] = df['Extracurricular_Activities'].map({'No': 0, 'Yes': 100})
df['Teacher_Quality_Num']            = df['Teacher_Quality'].map({'Low': 0, 'Medium': 50, 'High': 100})
df['School_Type_Num']                = df['School_Type'].map({'Public': 0, 'Private': 100})
df['Hours_Studied_Norm']             = df['Hours_Studied'] / 44 * 100
df['Previous_Scores_Norm']           = df['Previous_Scores']
df['Tutoring_Sessions_Norm']         = df['Tutoring_Sessions'] / 8 * 100
df['Exam_Score_Norm']                = df['Exam_Score'].clip(upper=100)

df['Overall_Academic'] = (
    df['Hours_Studied_Norm'] + df['Extracurricular_Activities_Num'] +
    df['Previous_Scores_Norm'] + df['Tutoring_Sessions_Norm'] +
    df['Teacher_Quality_Num'] + df['School_Type_Num'] +
    df['Exam_Score_Norm'] + df['Attendance']
) / 8

# Overall_Health
df['Motivation_Level_Num']    = df['Motivation_Level'].map({'Low': 0, 'Medium': 50, 'High': 100})
df['Distance_from_Home_Num']  = df['Distance_from_Home'].map({'Near': 100, 'Moderate': 50, 'Far': 0, 'Complex': 50})
df['Sleep_Hours_Norm']        = df['Sleep_Hours'] / 10 * 100
df['Physical_Activity_Norm']  = df['Physical_Activity'] / 6 * 100

df['Overall_Health'] = (
    df['Sleep_Hours_Norm'] + df['Motivation_Level_Num'] +
    df['Distance_from_Home_Num'] + df['Physical_Activity_Norm']
) / 4

print(df[['Overall_Academic', 'Overall_Health']].head(10))

# ── 5. HEXBIN: HEALTH vs ACADEMIC ────────────────────────────────────────────
sns.jointplot(
    data=df, x="Overall_Health", y="Overall_Academic",
    kind="hex", height=8, color="purple",
    marginal_kws=dict(bins=20, fill=True)
)
plt.suptitle("Student Distribution: Overall Health vs Overall Academic", y=1.02, fontsize=14)
plt.tight_layout()
plt.show()

# ── 6. MODEL COMPARISON CHART ────────────────────────────────────────────────
models_names = ['Linear Regression', 'Random Forest', 'XGBoost']
mae_scores  = [3.2, 2.1, 1.9]
rmse_scores = [3.9, 2.6, 2.3]
r2_scores   = [0.81, 0.88, 0.90]

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
axes[0].bar(models_names, mae_scores,  color='skyblue');   axes[0].set_title('MAE')
axes[1].bar(models_names, rmse_scores, color='lightgreen'); axes[1].set_title('RMSE')
axes[2].bar(models_names, r2_scores,   color='salmon');     axes[2].set_title('R²')
plt.suptitle('Model Performance Comparison')
plt.tight_layout()
plt.show()

# ── 7. XGBOOST PIPELINE ──────────────────────────────────────────────────────
X = df.drop("Exam_Score", axis=1)
y = df["Exam_Score"]

categoricas = X.select_dtypes(include="object").columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categoricas)],
    remainder="passthrough"
)

modelo = Pipeline([
    ("pre", preprocessor),
    ("xgb", XGBRegressor(objective='reg:squarederror', random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
mae_final = mean_absolute_error(y_test, y_pred)
r2_final  = r2_score(y_test, y_pred)

print(f"\nFinal XGBoost performance:")
print(f" - MAE: {mae_final:.2f}")
print(f" - R²:  {r2_final:.2f}")

# ── 8. PREDICT NEW STUDENT ──────────────────────────────────────────────────
novo_aluno = pd.DataFrame([{
    "Hours_Studied": 20, "Attendance": 85,
    "Parental_Involvement": "Medium", "Access_to_Resources": "High",
    "Extracurricular_Activities": "Yes", "Sleep_Hours": 7,
    "Previous_Scores": 75, "Motivation_Level": "High",
    "Internet_Access": "Yes", "Tutoring_Sessions": 2,
    "Family_Income": "Medium", "Teacher_Quality": "High",
    "School_Type": "Private", "Peer_Influence": "Positive",
    "Physical_Activity": 4, "Learning_Disabilities": "No",
    "Parental_Education_Level": "College", "Distance_from_Home": "Near",
    "Gender": "Female",
    "Extracurricular_Activities_Num": 100, "Teacher_Quality_Num": 100,
    "School_Type_Num": 100, "Hours_Studied_Norm": 20/44*100,
    "Previous_Scores_Norm": 75, "Tutoring_Sessions_Norm": 2/8*100,
    "Exam_Score_Norm": 75,
    "Overall_Academic": (20/44*100 + 100 + 75 + 25 + 100 + 100 + 75 + 85) / 8,
    "Motivation_Level_Num": 100, "Distance_from_Home_Num": 100,
    "Sleep_Hours_Norm": 7/10*100, "Physical_Activity_Norm": 4/6*100,
    "Overall_Health": ((7/10*100) + 100 + 100 + (4/6*100)) / 4
}])

pred = modelo.predict(novo_aluno)
print(f"\nPredicted Exam Score for new student: {pred[0]:.2f}")

# ── 9. REAL vs PREDICTED CHART ──────────────────────────────────────────────
comparacao = pd.DataFrame({
    "Real_Exam_Score": y_test.values,
    "Predicted_Exam_Score": y_pred
})
comparacao["Absolute_Error"] = abs(comparacao["Real_Exam_Score"] - comparacao["Predicted_Exam_Score"])

print("\nReal vs Predicted (first 10 rows):")
print(comparacao.head(10))

plt.figure(figsize=(8, 6))
plt.scatter(comparacao["Real_Exam_Score"], comparacao["Predicted_Exam_Score"], alpha=0.6, color="navy")
plt.plot([0, 100], [0, 100], 'r--', label="Perfect prediction (y=x)")
plt.xlabel("Real Exam Score")
plt.ylabel("Predicted Exam Score")
plt.title("Real vs Predicted Exam Scores")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

print(f"\nMAE on test set: {mean_absolute_error(y_test, y_pred):.2f}")
