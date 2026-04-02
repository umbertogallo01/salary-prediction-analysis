import matplotlib.pyplot as plt
import seaborn as sns

def plot_salary_distribution(df, target_col):
    plt.figure()
    sns.histplot(df[target_col], kde=True)
    plt.title("Salary Distribution")
    plt.xlabel(target_col)
    plt.ylabel("Frequency")
    plt.show()