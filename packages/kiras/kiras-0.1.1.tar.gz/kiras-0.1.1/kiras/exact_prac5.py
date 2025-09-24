import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.utils import to_categorical

def prac5(csv_path=None):
    """Execute Prac 5 - MNIST CNN Classification"""
    if csv_path:
        # Load CSV from your path
        df = pd.read_csv(csv_path)
        
        # Ensure all feature columns are numeric
        X = df.iloc[:,1:].apply(pd.to_numeric, errors='coerce').fillna(0).astype('float32').values
        X = X.reshape(-1,28,28,1)/255.0
        
        # Ensure labels are numeric
        y = pd.to_numeric(df.iloc[:,0], errors='coerce').fillna(0).astype(int)
        y = to_categorical(y, num_classes=10)
    else:
        # Use Keras built-in MNIST dataset as fallback
        from tensorflow.keras.datasets import mnist
        (X_train_full, y_train_full), (X_test_full, y_test_full) = mnist.load_data()
        
        # Combine train and test for our own split
        X = np.concatenate([X_train_full, X_test_full])
        y = np.concatenate([y_train_full, y_test_full])
        
        X = X.reshape(-1,28,28,1).astype('float32') / 255.0
        y = to_categorical(y, num_classes=10)

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=np.argmax(y,1), random_state=42
    )

    # Build CNN
    model = Sequential([
        Input(shape=(28,28,1), dtype='float32'),
        Conv2D(32,3,activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(64,'relu'),
        Dense(10,'softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train
    h = model.fit(X_train, y_train, epochs=5, batch_size=128, validation_split=0.2)

    # Plot
    plt.figure(figsize=(10,4))
    for k in ['loss','val_loss','accuracy','val_accuracy']:
        plt.plot(h.history[k], label=k)
    plt.legend(); plt.grid(True); plt.show()

    # Evaluate
    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss:.4f} | Test Accuracy: {acc:.4f}")
    
    return {
        'model': model,
        'history': h,
        'test_loss': loss,
        'test_accuracy': acc
    }

# For backward compatibility
mnist_cnn_classification = prac5