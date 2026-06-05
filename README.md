# 📊 Academic Performance Prediction Based on Habits and Lifestyle

> Data Science Project — Matheus Vilella · Guilherme Santos · Enzo Farina

---

## 🎯 What does this project do?

Studying is important. Everyone knows that. But **is studying the only factor that defines a student's performance?**

This project starts from a simple and relevant question:

> *How do a student's habits and lifestyle influence their grades?*

Using real data, we explore the impact of factors like sleep quality, physical activity, internet access, motivation, peer influence, and parental involvement — and show that **academic performance goes far beyond study hours**.

Beyond exploratory analysis, we developed a **Machine Learning model capable of predicting a student's exam score** based on their conditions and habits. This kind of tool has real-world applications: identifying at-risk students, guiding personalized pedagogical interventions, and supporting data-driven educational decisions.

---

## 💡 Why does this matter?

Imagine a school that could identify, at the beginning of the semester, which students are most at risk of struggling — not just because they study too little, but because they sleep poorly, have little support at home, or low motivation. With this information, counselors and teachers could act before the problem becomes a failing grade.

Machine Learning applied to education is not science fiction. It is a real, accessible tool that, when used responsibly, has the potential to transform how institutions support their students.

---

## 📁 Project structure

```
student-performance/
├── main.py                          # Main analysis and modeling script
├── requirements.txt                 # Python dependencies
├── StudentPerformanceFactors.csv    # Dataset
├── README.md                        # This file
├── METRICS.md                       # Detailed explanation of MAE, RMSE and R²
└── INSIGHTS.md                      # Key findings from the exploratory analysis
```

---

## 🗂️ Dataset

We used the public dataset [**Student Performance Factors**](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors), available on Kaggle.

Each row represents a student, with the following variables:

| Variable | Description |
|---|---|
| `Hours_Studied` | Weekly study hours |
| `Attendance` | Percentage of classes attended |
| `Sleep_Hours` | Average hours of sleep per night |
| `Physical_Activity` | Frequency of physical activity |
| `Motivation_Level` | Motivation level (Low / Medium / High) |
| `Internet_Access` | Internet access (Yes / No) |
| `Parental_Involvement` | Parental involvement (Low / Medium / High) |
| `Access_to_Resources` | Access to study resources |
| `Extracurricular_Activities` | Participation in extracurricular activities |
| `Tutoring_Sessions` | Number of tutoring sessions |
| `Family_Income` | Family income (Low / Medium / High) |
| `Teacher_Quality` | Teacher quality (Low / Medium / High) |
| `School_Type` | School type (Public / Private) |
| `Peer_Influence` | Peer influence (Positive / Negative / Neutral) |
| `Learning_Disabilities` | Learning disability (Yes / No) |
| `Parental_Education_Level` | Parents' education level |
| `Distance_from_Home` | Distance from home to school |
| `Gender` | Student gender |
| `Exam_Score` | **Target variable** — exam score (0 to 100) |

---

## 🔧 How to run

### Prerequisites

- Python 3.8 or higher

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python main.py
```

The script expects `StudentPerformanceFactors.csv` in the same folder. To use a different path:

```bash
# macOS / Linux
export STUDENT_CSV=/path/to/StudentPerformanceFactors.csv
python main.py

# Windows (CMD)
set STUDENT_CSV=C:\path\to\StudentPerformanceFactors.csv
python main.py
```

---

## 🧹 Data treatment

Three columns had missing values and were handled as follows:

- **`Teacher_Quality`** — filled with the most frequent value (mode), since it is an ordinal categorical variable with a clear distribution.
- **`Parental_Education_Level`** — filled with `"None"`, as the absence may indicate the student didn't know or that parents have no formal education.
- **`Distance_from_Home`** — filled with `"Complex"`, a category representing atypical commuting situations.

---

## ⚙️ Feature engineering

We created two composite metrics that summarize important dimensions of each student:

### `Overall_Academic`
Combines study hours, attendance, previous scores, tutoring sessions, teacher quality, school type, and exam score — all normalized from 0 to 100. Serves as a general index of the student's academic context.

### `Overall_Health`
Combines sleep hours, motivation, distance from home, and physical activity, also normalized from 0 to 100. Represents the student's overall well-being and living conditions.

These two metrics are used together to visualize how health and academic performance relate across the student population.

---

## 🤖 Models tested

We trained and compared three regression models to predict exam scores:

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Linear Regression | 3.2 | 3.9 | 0.81 |
| Random Forest | 2.1 | 2.6 | 0.88 |
| **XGBoost** ✅ | **1.9** | **2.3** | **0.90** |

**XGBoost** was chosen as the final model for delivering the best results across all three metrics: lowest absolute error, least penalization for large errors, and highest capacity to explain data variation.

For a detailed explanation of what each metric means and how to interpret them, see [`METRICS.md`](METRICS.md).

---

## 🔍 Key findings

The analysis revealed that several factors beyond study hours significantly influence academic performance:

- Students with **internet access** tend to have slightly higher grades
- **High motivation** is associated with higher scores and lower variation
- **Positive peer influence** correlates with better performance
- **Parental involvement** directly impacts grades
- **Learning disabilities** considerably reduce average performance

For the full analysis with visualizations and interpretations, see [`INSIGHTS.md`](INSIGHTS.md).

---

## 👥 Team

| Name |
|---|
| Matheus Vilella |
| Guilherme Santos |
| Enzo Farina |
