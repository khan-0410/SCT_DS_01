import matplotlib.pyplot as plt

# Sample data based on the image in your task
age_groups = ['0 to 20 Years', '21 to 64 Years', '65+ Years']
population_millions = [512, 807, 98]  # in millions
percentages = [36.1, 57.0, 6.9]

# Create bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(age_groups, population_millions, color=['gold', 'deepskyblue', 'orchid'])

# Add labels
for i, bar in enumerate(bars):
    height = bar.get_height()
    label = f'{population_millions[i]}M\n({percentages[i]}%)'
    plt.text(bar.get_x() + bar.get_width()/2, height + 10, label, ha='center', fontsize=12)

# Titles and axes
plt.title("India's Population Distribution by Age in 2022", fontsize=14)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Population (in millions)", fontsize=12)

# Save the chart
plt.tight_layout()
plt.savefig("age_distribution_chart.png")  # This will save the chart
plt.show()
