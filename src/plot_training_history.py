import matplotlib.pyplot as plt

# Model 3 training results
epochs = range(1, 11)

train_accuracy = [
    82.71, 95.43, 98.43, 98.00, 99.00,
    98.86, 99.14, 98.86, 99.43, 99.00
]

validation_accuracy = [
    97.33, 97.33, 98.67, 98.67, 99.33,
    99.33, 98.67, 99.33, 99.33, 99.33
]

train_loss = [
    0.3931, 0.1293, 0.0736, 0.0675, 0.0502,
    0.0470, 0.0360, 0.0405, 0.0288, 0.0294
]

validation_loss = [
    0.1375, 0.0611, 0.0461, 0.0478, 0.0278,
    0.0296, 0.0399, 0.0237, 0.0232, 0.0225
]


# -------------------------
# Accuracy graph
# -------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    epochs,
    train_accuracy,
    marker="o",
    label="Training Accuracy"
)

plt.plot(
    epochs,
    validation_accuracy,
    marker="o",
    label="Validation Accuracy"
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.title("Training and Validation Accuracy")
plt.legend()
plt.grid(True)

plt.savefig(
    "models/augmented_accuracy.png"
)

plt.show()


# -------------------------
# Loss graph
# -------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    epochs,
    train_loss,
    marker="o",
    label="Training Loss"
)

plt.plot(
    epochs,
    validation_loss,
    marker="o",
    label="Validation Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training and Validation Loss")
plt.legend()
plt.grid(True)

plt.savefig(
    "models/augmented_loss.png"
)

plt.show()