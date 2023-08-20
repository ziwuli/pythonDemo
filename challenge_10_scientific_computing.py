"""
Using pandas and the matplotlib library, analyze data from a CSV file and create a graph to visualize certain key statistics within it.
"""

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('random_data.csv')

    bins = [0, 30, 60, 100]
    labels = ['1-30', '31-60', '61-100']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    age_group_counts = df['Age Group'].value_counts().sort_index()

    age_group_percentage = age_group_counts / len(df) * 100

    plt.figure(figsize=(10, 7))
    plt.pie(age_group_percentage, labels=age_group_percentage.index, autopct='%1.2f%%', startangle=140)
    plt.title('Age Group Distribution')
    plt.show()
