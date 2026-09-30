import matplotlib.pyplot as plt
import seaborn as sns

# Confusion matrix values
cm = [
    [75, 0],
    [0, 75]
]

# Class names
class_names = [
    "Modern",
    "Traditional"
]

# Create the heatmap
plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)

# Add labels
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")

# Add title
plt.title("Confusion Matrix - MobileNetV2 with Augmentation")

# Save the image
plt.savefig(
    "results/confusion_matrix_augmented.png"
)

# Display the image
plt.show()