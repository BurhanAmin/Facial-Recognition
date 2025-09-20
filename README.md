# Facial-Recognition
# Siamese Neural Network for Facial Recognition

This project implements a **Siamese Neural Network** for facial recognition, inspired by **Nicholas Renotte’s tutorial**.  
The model is designed to compare two input images and determine whether they belong to the same person or not.

---

## 📌 Overview
A Siamese Network learns to differentiate between pairs of inputs by computing a similarity score.  
In this project:
- Each image is passed through a **convolutional embedding network** that generates a 4096-dimensional feature vector.
- A **custom L1 Distance layer** computes the absolute difference between two embeddings.
- A **Dense sigmoid classifier** outputs the probability that the two images represent the same identity.

---

## 🏗️ Model Architecture
- **Input**: Two images of size `100x100x3`
- **Embedding Network**:
  - Conv2D → MaxPooling → Conv2D → MaxPooling → Conv2D → MaxPooling
  - Flatten + Dense(4096, activation='sigmoid')
- **Distance Layer**: L1 Distance (absolute difference)
- **Classifier**: Dense(1, activation='sigmoid')

---

## ⚙️ Training
- Dataset structured into positive and negative pairs.
- Model trained with **Binary Crossentropy loss**.
- Optimizer: **Adam**.
- Evaluation: Accuracy on unseen validation image pairs.

---
📚 Acknowledgments
This project was built following Nicholas Renotte’s Siamese Network tutorial on YouTube.
Huge thanks to him for providing an excellent walkthrough and explanation of the concepts.

📜 License

This project is for educational purposes.
If you use this code or build upon it, please give credit to both this repository and Nicholas Renotte’s original tutorial

