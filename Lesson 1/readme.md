# Welcome to the First Class of Python for Data Analytics

In this session, we'll explore the fundamentals of Google Colab and dive into descriptive statistics, including **Tukey's 5-number summary**. Let's get started!

---

## Agenda

1. **Introduction to Google Colab**
   - Setting up Google Colab
   - Basic functionalities and interface
   - Writing and running Python code

2. **Introduction to Descriptive Statistics**
   - Understanding key statistical concepts
   - Hands-on calculations of key measures

3. **Tukey's 5-Number Summary**
   - Minimum
   - First Quartile (Q1)
   - Median
   - Third Quartile (Q3)
   - Maximum

4. **Practical Exercise**
   - Importing and analyzing a dataset
   - Computing the 5-number summary in Python

---

## Step 1: Getting Started with Google Colab

Google Colab is a cloud-based platform for running Python code. To get started:

1. Open [Google Colab](https://colab.research.google.com).
2. Sign in with your Google account.
3. Create a new notebook and name it `class1_intro.ipynb`.

### Key Features of Colab
- Free access to GPUs and TPUs.
- Easy sharing and collaboration.
- Direct integration with Google Drive.

Try this simple Python code:
```python
print("Welcome to Python for Data Analytics!")
```

---

## Step 2: Introduction to Descriptive Statistics

Descriptive statistics summarize the central tendency, dispersion, and shape of a dataset's distribution. Key measures include:

- **Mean**: The average value.
- **Median**: The middle value when sorted.
- **Mode**: The most frequent value.
- **Range**: The difference between the maximum and minimum values.

---

## Step 3: Understanding Tukey's 5-Number Summary

Tukey's 5-number summary provides a concise description of a dataset:

1. **Minimum**: The smallest data value.
2. **First Quartile (Q1)**: The median of the lower half of the data.
3. **Median**: The middle value of the dataset.
4. **Third Quartile (Q3)**: The median of the upper half of the data.
5. **Maximum**: The largest data value.

### Python Implementation

Here's how to compute the 5-number summary in Python:
```python
import numpy as np

data = [10, 15, 14, 18, 12, 25, 22, 19]

# Calculating the 5-number summary
minimum = np.min(data)
q1 = np.percentile(data, 25)
median = np.median(data)
q3 = np.percentile(data, 75)
maximum = np.max(data)

print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)
```

---

## Step 4: Practical Exercise

1. Import a dataset (use any small dataset, e.g., a list of numbers or a CSV file).
2. Use Python to calculate the 5-number summary.
3. Analyze and interpret the results.

### Sample Dataset
```python
# Example dataset
data = [22, 28, 29, 24, 32, 36, 38, 25, 21, 34]
```

---

## Summary

By the end of this class, you should be able to:

1. Navigate and use Google Colab effectively.
2. Understand and calculate descriptive statistics.
3. Compute and interpret Tukey's 5-number summary using Python.

---

**Happy Analyzing!**
