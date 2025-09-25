import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def prac4(csv_path=None):
    """Execute Prac 4 - Titanic Survival Prediction"""
    if csv_path:
        # Load & preprocess from your CSV path
        df = pd.read_csv(csv_path)[['Pclass','Gender','Age','Fare','Survived']].dropna()
    else:
        # Create sample titanic-like data as fallback
        import numpy as np
        np.random.seed(42)
        n_samples = 800
        df = pd.DataFrame({
            'Pclass': np.random.choice([1, 2, 3], n_samples),
            'Gender': np.random.choice(['male', 'female'], n_samples),
            'Age': np.random.normal(30, 15, n_samples).clip(1, 80),
            'Fare': np.random.exponential(20, n_samples),
            'Survived': np.random.choice([0, 1], n_samples)
        })
    
    df['Gender'] = df['Gender'].map({'male':0,'female':1}).astype('float32')  # ensure numeric
    X = df[['Pclass','Gender','Age','Fare']].astype('float32').to_numpy()
    y = df['Survived'].astype('float32').to_numpy().reshape(-1,1)

    # Split & scale
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    scaler = StandardScaler().fit(X_tr)
    X_tr, X_te = scaler.transform(X_tr), scaler.transform(X_te)

    # Model
    model = Sequential([Dense(1, 'sigmoid', input_shape=(4,))])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train
    h = model.fit(X_tr, y_tr, epochs=30, batch_size=16, validation_split=0.2, verbose=0)

    # Plot Loss & Accuracy
    plt.figure(figsize=(8,3))
    for i,(k,t) in enumerate([('loss','Loss'), ('accuracy','Accuracy')]):
        plt.subplot(1,2,i+1)
        plt.plot(h.history[k], label='Train')
        plt.plot(h.history['val_'+k], label='Val')
        plt.title(t); plt.legend()
    plt.tight_layout(); plt.show()

    # Evaluate
    l,a = model.evaluate(X_te, y_te, verbose=0)
    print(f"Test Loss: {l:.4f}  |  Test Accuracy: {a:.4f}")
    
    return {
        'model': model,
        'history': h,
        'test_loss': l,
        'test_accuracy': a
    }

# For backward compatibility
titanic_survival_prediction = prac4