import matplotlib.pyplot as plt

# Model names
models = [
    "CNN",
    "MobileNetV2",
    "MobileNetV2 + Augmentation"
]

# Test accuracy
test_accuracy = [
    98,
    100,
    100
]

# External image performance
external_accuracy = [
    40,
    60,
    80
]

# Create the graph
plt.figure(figsize=(9, 5))

# Plot test accuracy
plt.plot(
    models,
    test_accuracy,
    marker="o",
    label="Test Accuracy"
)

# Plot external image performance
plt.plot(
    models,
    external_accuracy,
    marker="o",
    label="External Image Performance"
)

# Add labels
plt.xlabel("Model")
plt.ylabel("Accuracy (%)")

# Add title
plt.title("Model Performance Comparison")

# Show legend
plt.legend()

# Add grid
plt.grid(True)

# Save the graph
plt.savefig(
    "results/model_comparison.png"
)

# Display the graph
plt.show()