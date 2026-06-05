# 🔍 Insights: What the Data Reveals About Habits and Academic Performance

This document brings together the key findings from the project's exploratory analysis. The goal is not just to describe charts — it is to answer the central question:

> **Studying is the most important factor, but it is far from the only one.**

---

## 1. Study hours: the foundation, but not the ceiling

As expected, there is a positive correlation between study hours and exam scores. Students who study more tend to do better. However, looking at the distribution more carefully, something stands out: **some students study a lot and still get mediocre grades, while others study relatively little and perform reasonably well**.

This suggests that studying is necessary but not sufficient. Other factors determine whether the effort translates into results.

---

## 2. Attendance: one of the most consistent predictors

Class attendance showed a consistent correlation with performance. Students with high attendance tend to have higher and more stable scores.

![School Attendance vs Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/attendance.png)

Being present means exposure to content, the teacher, discussions, and the rhythm of learning. Regular attendance also signals commitment, routine, and engagement — qualities that impact performance in other ways too.

---

## 3. Internet access: a real advantage, but not decisive

![Internet Access and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/internet_access.png)

Students with internet access scored slightly higher on average. The difference is not dramatic, but it is consistent enough to appear in the data. Internet access represents access to study resources, supplementary materials, learning platforms, and communication with peers and teachers.

---

## 4. Extracurricular activities: broader than it looks

![Extracurricular Activities and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/extracurricular.png)

Students who participate in extracurricular activities show a distribution very similar to those who don't, with a slight edge. This suggests that staying engaged outside the classroom — in sports, arts, clubs — does not hurt academic performance and may even help by building discipline and social skills.

---

## 5. Motivation: the factor that most changes the distribution

![Motivation Level and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/motivation_level.png)

Among the behavioral variables analyzed, motivation showed one of the clearest patterns. Highly motivated students not only get better grades — their grades are **more consistent**. The violin shape for "High" motivation is narrower, meaning less variation.

Students with low motivation show a much wider spread: some still do well (possibly due to compensating factors), but the majority falls below average. Motivation acts as a **multiplier**: it amplifies the effect of other habits.

---

## 6. Parental involvement: home support shows up in grades

![Parental Involvement and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/parental_involvement.png)

Students with high parental involvement consistently showed higher score distributions. Engaged parents create routines, monitor development, enforce accountability, and provide emotional support. The pattern is clear across all three levels (Low / Medium / High): more involvement, better performance.

---

## 7. Learning disabilities: real and important impact

![Learning Disabilities and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/learning_disabilities.png)

Students with learning disabilities scored lower on average and showed a compressed distribution. This reinforces the need for **differentiated strategies and specialized support** for this group. Importantly, some students in this group still performed above average — showing that with adequate support, the impact can be mitigated.

---

## 8. Peer influence: the social environment matters

![Peer Influence and Exam Score](https://raw.githubusercontent.com/enzofarina/machine-learning-behaviour-prediction/main/images/peer_influence.png)

Students with positive peer influence tended to perform slightly better than those with negative or neutral influence. The difference is subtle, but the pattern is consistent with educational literature: an environment where studying is valued, asking questions is normal, and academic performance is part of the group's identity shapes individual outcomes.

---

## 9. Health vs. Academic Performance: the full picture

One of the most interesting visualizations in the project is the density plot between `Overall_Health` and `Overall_Academic` — the two composite indices we created (see README for their definitions).

What it shows:
- There is a central cluster of students with both health and academic performance in the intermediate range
- The distribution is wide — there is no single "type" of successful student
- Some students have high health scores but low academic performance (and vice versa), confirming that the two dimensions are related but not interchangeable

This suggests that **health and performance are correlated, but independent**. Improving one may help the other, but neither guarantees the other automatically.

---

## 10. Practical implications

The data supports a broader view of what it means to "care for students":

- **Monitoring attendance** is monitoring risk
- **Supporting motivation** can have a multiplier effect on other habits
- **Identifying students with learning disabilities early** allows intervention before failure
- **Considering family and socioeconomic context** is part of the equation, not noise to be ignored

A predictive model like the one developed here can function as an **early warning system**: given a student's profile at the start of the semester, estimate the likelihood of low performance and direct pedagogical attention before it is too late.

This does not replace the human judgment of teachers and counselors — it informs and amplifies it.
