import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv('personal_data.csv')

# Perform data analysis and visualization
def analyze_personal_data():
    # Summary statistics
    print("Summary Statistics:")
    print(data.describe())

    # Age distribution
    plt.hist(data['Age'], bins=20)
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.title('Age Distribution')
    plt.show()

    # Education level
    education_counts = data['Education'].value_counts()
    plt.bar(education_counts.index, education_counts.values)
    plt.xlabel('Education Level')
    plt.ylabel('Count')
    plt.title('Education Level Distribution')
    plt.xticks(rotation=45)
    plt.show()

    # Monthly income vs. years of experience
    plt.scatter(data['Years of Experience'], data['Monthly Income'])
    plt.xlabel('Years of Experience')
    plt.ylabel('Monthly Income')
    plt.title('Monthly Income vs. Years of Experience')
    plt.show()

    # Correlation heatmap
    corr = data.corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.title('Correlation Heatmap')
    plt.show()

# Call the analysis function
analyze_personal_data()
