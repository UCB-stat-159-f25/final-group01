import matplotlib.pyplot as plt
import seaborn as sns
import os

def setup_plot_style(style="whitegrid", context="notebook", figsize=(14, 6)):
    """
    Sets the global plotting style for consistent figures across the project.
    
    Args:
        style (str): Seaborn style ('whitegrid', 'darkgrid', etc.)
        context (str): Scale of elements ('paper', 'notebook', 'talk', 'poster')
        figsize (tuple): Default figure size (width, height)
    """
    # Set the seaborn style
    sns.set_style(style)
    sns.set_context(context)
    
    # Update global matplotlib parameters for better readability
    plt.rcParams.update({
        'figure.figsize': figsize,
        'axes.titlesize': 16,
        'axes.labelsize': 14,
        'xtick.labelsize': 12,
        'ytick.labelsize': 12,
        'legend.fontsize': 12,
        'figure.dpi': 600
    })
    print("Plotting style set to global defaults.")

def save_figure(filename, directory="../figures", dpi=300):
    """
    Saves the current figure to a specified directory.
    
    Args:
        filename (str): Name of the file (e.g., 'inflation_trend.png')
        directory (str): Folder to save in. Defaults to '../figures'.
        dpi (int): Resolution for the saved image.
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # Create full path
    path = os.path.join(directory, filename)
    
    # Save with tight bounding box to prevent cutting off labels
    plt.savefig(path, dpi=dpi, bbox_inches='tight')
    print(f"Figure saved to: {path}")