import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

def prac3(csv_path=None):
    """Execute Prac 3 - Iris Classification"""
    if csv_path:
        # Load data from provided CSV path (your original code)
        df = pd.read_csv(csv_path)
        X = df.iloc[:, :4].astype("float32").to_numpy()  # ensure float32
        y = LabelEncoder().fit_transform(df.iloc[:, 4])  # convert string labels to integers
        y = to_categorical(y, 3).astype("float32")       # one-hot encoding
    else:
        # Use sklearn's built-in iris dataset as fallback
        from sklearn.datasets import load_iris
        iris = load_iris()
        X = iris.data.astype("float32")
        y = to_categorical(iris.target, 3).astype("float32")

    # Train/Val/Test split (60/20/20)
    X_t, X_test, y_t, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, test_size=0.25, stratify=y_t, random_state=42)

    # Build model
    model = Sequential([
        Dense(16, activation="relu", input_shape=(4,)),
        Dense(12, activation="relu"),
        Dense(3, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    # Train
    h = model.fit(X_train, y_train, epochs=30, batch_size=16, validation_data=(X_val, y_val), verbose=0)

    # Plots
    plt.figure(figsize=(8,3))
    for i,(k,t) in enumerate([("loss","Loss"), ("accuracy","Accuracy")]):
        plt.subplot(1,2,i+1)
        plt.plot(h.history[k], label="Train")
        plt.plot(h.history["val_"+k], label="Val")
        plt.title(t); plt.legend()
    plt.tight_layout(); plt.show()

    # Evaluate
    l,a = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {l:.4f}  |  Test Accuracy: {a:.4f}")
    
    return {
        'model': model,
        'history': h,
        'test_loss': l,
        'test_accuracy': a
    }

# For backward compatibility
iris_classification = prac3