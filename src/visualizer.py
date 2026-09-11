import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

def generate_report(csv_path):
    print(f"Generating report from {csv_path}...")
    
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # Ensure the score is a number (Fixes the isfinite TypeError)
    df['anxiety_score'] = pd.to_numeric(df['anxiety_score'], errors='coerce').fillna(0)
    
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))
    
    # Draw the anxiety line
    sns.lineplot(x='timestamp', y='anxiety_score', data=df, color='crimson', linewidth=2)
    
    # Highlight high anxiety zones in red
    plt.fill_between(df['timestamp'], df['anxiety_score'], 40, 
                     where=(df['anxiety_score'] > 40), 
                     color='red', alpha=0.3, interpolate=True, label='High Anxiety Zone')
    
    plt.title("Student Anxiety Analysis - Post-Exam Report", fontsize=16, fontweight='bold')
    plt.xlabel("Exam Timestamp", fontsize=12)
    plt.ylabel("Anxiety Score (0-100)", fontsize=12)
    plt.ylim(0, 100)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    plt.legend(loc='upper right')
    
    plt.tight_layout()
    
    # Save graph image using the same name as the CSV
    graph_filename = csv_path.replace('.csv', '.png')
    plt.savefig(graph_filename)
    print(f"Report saved as an image to {graph_filename}")
    
    # plt.show()

# Fallback if someone runs this script manually
if __name__ == "__main__":
    print("Please provide a CSV path to generate a report.")