import matplotlib.pyplot as plt
import json

# Example language composition data
# (Replace with actual data from your repository)
languages = {
    'JavaScript': 45,
    'HTML': 25,
    'CSS': 15,
    'Python': 10,
    'Other': 5
}

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 8))
colors = ['#F1E05A', '#E34C26', '#563D7C', '#3572A5', '#CCCCCC']
wedges, texts, autotexts = ax.pie(languages.values(), 
                                     labels=languages.keys(), 
                                     autopct='%1.1f%%',
                                     colors=colors,
                                     startangle=90,
                                     textprops={'fontsize': 12, 'weight': 'bold'})

# Enhance the appearance
ax.set_title('Repository Language Composition', fontsize=16, weight='bold', pad=20)

# Save as image
plt.savefig('language_composition.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'language_composition.png'")
plt.show()
