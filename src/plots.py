import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_salary_distribution(df, target_col, save_path=None):
    plt.figure()
    sns.histplot(df[target_col], kde=True)
    plt.title("Distribuzione dei salari")
    plt.xlabel(target_col)
    plt.ylabel("Conteggio")

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()


def plot_correlation_matrix(df, save_path=None):
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Matrice di correlazione")

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()
    

def plot_residuals(y_test, y_pred_test, model_label, save_path=None):
    residuals = y_test - y_pred_test
    plt.figure()
    plt.scatter(y_pred_test, residuals)
    plt.axhline(0, color='red')
    plt.xlabel("Predicted Salary")
    plt.ylabel("Residuals")
    plt.title(f"Residuals Distribution - {model_label}")
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()


def plot_distribution(y_train, y_pred_train, y_test, y_pred_test, model_label, save_path=None):
    fig, ax = plt.subplots(1, 2, figsize=(12,5))

    sns.kdeplot(y_train, color="r", fill=True, label="Actual Value", ax=ax[0])
    sns.kdeplot(y_pred_train, color="b", fill=True, label="Predicted Value", ax=ax[0])
    ax[0].set_title(f"Distribuzione dei salari (Training Set) - {model_label}")
    ax[0].legend()

    sns.kdeplot(y_test, color="r", fill=True, label="Actual Value", ax=ax[1])
    sns.kdeplot(y_pred_test, color="b", fill=True, label="Predicted Value", ax=ax[1])
    ax[1].set_title(f"Distribuzione dei salari (Test Set) - {model_label}")
    ax[1].legend()

    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)

    plt.show()


def plot_predicted_vs_actual(y_train, y_pred_train, y_test, y_pred_test, model_label, save_path=None):
    plt.scatter(y_train, y_pred_train, label="Train")
    plt.scatter(y_test, y_pred_test, label="Test")

    plt.xlabel("Actual Salary Values")
    plt.ylabel("Predicted Salary Values")
    plt.title(f"Actual vs Predicted Salary (Train vs Test) - {model_label}")

    # Creiamo la retta y = x
    min_val = min(min(y_train), min(y_test))
    max_val = max(max(y_train), max(y_test))

    x = np.linspace(min_val, max_val, 100)
    plt.plot(x, x, color='r', linestyle='--')

    plt.tight_layout()
    plt.legend()

    if save_path is not None:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
        
    plt.show()
