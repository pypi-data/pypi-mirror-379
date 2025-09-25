import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def prac8(csv_path=None):
    """Execute Prac 8 - MNIST Denoising Autoencoder"""
    if csv_path:
        # --- Load & preprocess ---
        df = pd.read_csv(csv_path)
        X = df.drop('label', axis=1).values / 255.0
    else:
        # Use Keras built-in MNIST dataset as fallback
        from tensorflow.keras.datasets import mnist
        (X_train_full, _), (X_test_full, _) = mnist.load_data()
        
        # Combine and flatten
        X = np.concatenate([X_train_full, X_test_full])
        X = X.reshape(-1, 784) / 255.0
    
    X_noisy = np.clip(X + np.random.normal(0,0.4,X.shape), 0, 1)
    X_train, X_test, Xn_train, Xn_test = tts(X, X_noisy, test_size=0.2, random_state=42)

    # --- Denoising Autoencoder ---
    model = Sequential([
        Input((784,)), Dense(128,'relu'), Dense(64,'relu'), Dense(32,'relu'),
        Dense(64,'relu'), Dense(128,'relu'), Dense(784,'sigmoid')
    ])
    model.compile('adam','binary_crossentropy')

    # --- Train ---
    hist = model.fit(Xn_train, X_train, validation_data=(Xn_test, X_test), epochs=10, verbose=0)

    # --- Plot Loss ---
    plt.plot(hist.history['loss'], label='Train')
    plt.plot(hist.history['val_loss'], label='Val')
    plt.title("Denoising Autoencoder Loss"); plt.xlabel("Epoch"); plt.ylabel("Loss")
    plt.legend(); plt.grid(True); plt.show()

    # --- Visualize Noisy → Denoised → Original ---
    decoded = model.predict(Xn_test[:5])
    fig, axs = plt.subplots(3,5,figsize=(12,6))
    for i in range(5):
        axs[0,i].imshow(Xn_test[i].reshape(28,28), cmap='gray'); axs[0,i].axis('off')
        axs[1,i].imshow(decoded[i].reshape(28,28), cmap='gray'); axs[1,i].axis('off')
        axs[2,i].imshow(X_test[i].reshape(28,28), cmap='gray'); axs[2,i].axis('off')
    axs[0,0].set_title("Noisy"); axs[1,0].set_title("Denoised"); axs[2,0].set_title("Original")
    plt.suptitle("Denoising Autoencoder Results"); plt.tight_layout(); plt.show()
    
    return {
        'model': model,
        'history': hist,
        'X_test': X_test,
        'Xn_test': Xn_test,
        'decoded': decoded
    }

# For backward compatibility
mnist_denoising_autoencoder = prac8