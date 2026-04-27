# Research-Paper
#  Impact of Content Recommendation Systems on User Polarization

##  Authors

* **Harshdeep Singh - 2210991630**
* **Sarthak Malan - 2210992262**
* **Shivam Dubey - 2210992308**
* **Dr. Shikha Tuteja - Associate Professor**
  
*Paper submitted to ICST 2026 (SCRS) via CMT, under review (Paper ID: 69)

**Department of Computer Science & Engineering**
Chitkara University Institute of Engineering and Technology
Chitkara University, Patiala, India

---

##  Project Overview

This project analyzes how different content recommendation strategies influence **user polarization** on social media platforms. It is based on our research paper:

> *“Impact of Content Recommendation Systems on User Polarization”*

We simulate and compare two types of recommendation systems:

*  **Engagement-Based Model**
  Prioritizes popular or highly engaged content

*  **Diversity-Based Model**
  Promotes exposure to a mix of viewpoints

###  Evaluation Metrics

* **Sentiment Variance** → Measures polarization
* **Average Sentiment** → Indicates overall opinion trend

---

##  Code Explanation (`analysis.py`)

### 1.  Data Loading

* Loads dataset: `Reddit_Data.csv`

### 2.  Data Preparation

* Removes missing values
* Converts `category` column into sentiment labels:

  * `1` → Positive
  * `0` → Neutral
  * `-1` → Negative

---

### 3.  Engagement-Based Model

```python
reddit['engagement'] = reddit.index
engagement_df = reddit.sort_values(by='engagement', ascending=False).head(100)
```

* Simulates engagement using ranking (index-based)
* Selects **top 100 posts** (high engagement)

**Calculations:**

* Sentiment Variance
* Average Sentiment

💡 **Insight:**
Higher variance suggests **echo chambers**, where users are repeatedly exposed to similar viewpoints.

---

### 4.  Diversity-Based Model

```python
neutral = reddit[reddit['sentiment'] == 0].sample(50)
positive = reddit[reddit['sentiment'] == 1].sample(30)
negative = reddit[reddit['sentiment'] == -1].sample(20)
```

* Samples a **balanced mix** of sentiments
* Combines into a single dataset

**Calculations:**

* Sentiment Variance
* Average Sentiment

 **Insight:**
Lower variance indicates **reduced polarization** due to exposure to diverse perspectives.

---

### 5.  Visualization

* Generates a **bar chart** comparing:

  * Engagement-Based Model vs Diversity-Based Model
* Clearly highlights differences in polarization levels

---

##  Results Interpretation

###  Engagement-Based Model

* Higher variance → **More polarization**
* Reinforces existing beliefs
* Creates **echo chambers**

###  Diversity-Based Model

* Lower variance → **Less polarization**
* Encourages **balanced exposure**
* Promotes broader perspectives

---

##  Datasets Used

### 1. Reddit_Data.csv

* **Source:** Kaggle
* Contains Reddit comments with pre-labeled sentiment (`category`)
* Used as the primary dataset

### 2. Twitter_Data.csv

* **Source:** Kaggle
* Included for future extension
* Can be used for similar analysis on Twitter data

---

##  How to Run

### 1. Install Dependencies

```bash
pip install pandas matplotlib
```

### 2. Execute the Script

```bash
python analysis.py
```

---

##  Output

The program will:

* Print:

  * Sentiment Variance
  * Average Sentiment (for both models)
* Display:

  *  Bar chart comparing polarization

---

##  Conclusion

This project demonstrates that:

* **Engagement-based recommendation systems** tend to **increase polarization**
* **Diversity-based systems** help **reduce polarization** by exposing users to varied viewpoints

---

##  Acknowledgements

We sincerely thank **Chitkara University** and our mentors for their continuous guidance and support throughout this research.

---

##  Contact

For queries or collaboration:

* **Harshdeep Singh**
   [harshdeep1630.be22@chitkara.edu.in](mailto:harshdeep1630.be22@chitkara.edu.in)

* **Sarthak Malan**
   [sarthak2262.be22@chitkara.edu.in](mailto:sarthak2262.be22@chitkara.edu.in)

* **Shivam Dubey**
   [shivam2308.be22@chitkara.edu.in](mailto:shivam2308.be22@chitkara.edu.in)

---
