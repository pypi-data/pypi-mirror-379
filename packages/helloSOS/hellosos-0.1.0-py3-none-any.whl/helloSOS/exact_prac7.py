import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

def prac7(csv_path=None):
    """Execute Prac 7 - Banknote Authentication"""
    if csv_path:
        # 1️⃣ Load CSV and force numeric values
        df = pd.read_csv(csv_path)
        df = df.apply(lambda col: pd.to_numeric(col, errors='coerce')).dropna()  # remove non-numeric
    else:
        # Create sample banknote data as fallback
        np.random.seed(42)
        n_samples = 1000
        # Features: variance, skewness, curtosis, entropy
        X_authentic = np.random.multivariate_normal([0, 0, 0, -1], 
                                                   [[1, 0.3, 0.1, 0.2],
                                                    [0.3, 1, 0.2, 0.1],
                                                    [0.1, 0.2, 1, 0.3],
                                                    [0.2, 0.1, 0.3, 1]], 
                                                   n_samples//2)
        X_fake = np.random.multivariate_normal([2, 1, -1, 1], 
                                              [[1.5, 0.2, 0.3, 0.1],
                                               [0.2, 1.2, 0.1, 0.4],
                                               [0.3, 0.1, 1.3, 0.2],
                                               [0.1, 0.4, 0.2, 1.1]], 
                                              n_samples//2)
        
        X_data = np.vstack([X_authentic, X_fake])
        y_data = np.hstack([np.zeros(n_samples//2), np.ones(n_samples//2)])
        
        df = pd.DataFrame(X_data, columns=['variance', 'skewness', 'curtosis', 'entropy'])
        df['class'] = y_data

    # 2️⃣ Split features and target
    X = df.iloc[:, :-1].to_numpy(dtype=np.float32)
    y = df.iloc[:, -1].to_numpy(dtype=np.float32).reshape(-1,1)

    # 3️⃣ Train/test split & scaling
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    sc = StandardScaler().fit(X_tr)
    X_tr, X_te = sc.transform(X_tr), sc.transform(X_te)

    # 4️⃣ Build model
    model = Sequential([
        Input(shape=(X_tr.shape[1],)),
        Dense(10, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # 5️⃣ Train model
    h = model.fit(X_tr, y_tr, epochs=30, batch_size=16, validation_split=0.2, verbose=0)

    # 6️⃣ Plot training curves
    plt.figure(figsize=(10,4))
    for i, (k, t) in enumerate([('loss','Loss'), ('accuracy','Accuracy')]):
        plt.subplot(1,2,i+1)
        plt.plot(h.history[k], label='train')
        plt.plot(h.history['val_'+k], label='val')
        plt.title(t)
        plt.legend()
    plt.tight_layout()
    plt.show()

    # 7️⃣ Evaluate
    loss, acc = model.evaluate(X_te, y_te, verbose=0)
    print(f"Test Loss: {loss:.4f} | Test Accuracy: {acc:.4f}")
    
    return {
        'model': model,
        'history': h,
        'test_loss': loss,
        'test_accuracy': acc
    }

# For backward compatibility
banknote_authentication = prac7