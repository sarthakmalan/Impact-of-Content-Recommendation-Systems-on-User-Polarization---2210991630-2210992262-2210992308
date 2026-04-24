# Research-Paper
#  Impact of Content Recommendation Systems on User Polarization

##  Authors

* **Harshdeep Singh**
* **Sarthak Malan**
* **Shivam Dubey**
* **Dr. Shikha Tuteja**

Department of Computer Science & Engineering
Chitkara University Institute of Engineering and Technology
Chitkara University, Patiala, India

---
##### **Project Overview**



This project analyzes how different recommendation strategies affect user polarization on social media, based on our research paper “Impact of Content Recommendation Systems on User Polarization.”



We simulate two types of recommendation systems:



Engagement-Based Model → prioritizes popular content

Diversity-Based Model → ensures exposure to mixed viewpoints



We then measure their impact using:



Sentiment Variance → indicates polarization

Average Sentiment → shows overall opinion direction.



##### **Code Explanation** (analysis.py)



The script performs the following steps:



###### 1\. Data Loading

Loads the Reddit dataset (Reddit\_Data.csv)

Uses the first 1000 rows for faster execution.



###### 2\. Data Preparation

Removes missing values

Uses the category column as sentiment:

1 → Positive

0 → Neutral

\-1 → Negative



###### 3\. Engagement-Based Model



reddit\['engagement'] = reddit.index

engagement\_df = reddit.sort\_values(by='engagement', ascending=False).head(100)



Simulates engagement using ranking (top posts)

Selects top 100 posts (high engagement)

Calculates:

\- Variance → measures polarization

\- Average sentiment



**Insight**:

Higher variance = users see similar content → echo chambers



###### 4\. Diversity-Based Model



neutral = reddit\[reddit\['sentiment'] == 0].sample(50)

positive = reddit\[reddit\['sentiment'] == 1].sample(30)

negative = reddit\[reddit\['sentiment'] == -1].sample(20)



Samples a balanced mix of sentiments

Combines them into one dataset

Calculates:

\- Variance

\- Average sentiment



**Insight**:

Lower variance = users see mixed viewpoints → reduced polarization



###### 5\. Visualization

A bar chart compares the variance of both models

Clearly shows polarization difference.





##### **Results Interpretation**



Engagement-Based Model

Higher variance → more polarization

Reinforces existing beliefs (echo chambers)



Diversity-Based Model

Lower variance → less polarization

Encourages exposure to different opinions





##### **Datasets Used**



###### 1\. Reddit\_Data.csv

Source: Kaggle

Contains Reddit comments with pre-labeled sentiment (category)

Used as the primary dataset for analysis.



###### 2\. Twitter\_Data.csv

Source: Kaggle

Included for extension/future work

It can be used to perform similar analysis on Twitter data.



##### **How to Run**



1\. Install dependencies

pip install pandas matplotlib



2\. Run the script

python analysis.py



##### **Output**



The program will:



Print the variance and average sentiment for both models

Display a bar chart comparing polarization.



##### **Conclusion**



This project demonstrates that:



Engagement-based recommendation systems increase polarization, while diversity-based systems help reduce it by exposing users to varied viewpoints.


##  Acknowledgements

We would like to thank Chitkara University and our mentors for their guidance and support throughout this research.

---

##  Contact

For any queries or collaboration:

* Harshdeep Singh – [harshdeep1630.be22@chitkara.edu.in](mailto:harshdeep1630.be22@chitkara.edu.in)
* Sarthak Malan – [sarthak2262.be22@chitkara.edu.in](mailto:sarthak2262.be22@chitkara.edu.in)
* Shivam Dubey – [shivam2308.be22@chitkara.edu.in](mailto:shivam2308.be22@chitkara.edu.in)

---
