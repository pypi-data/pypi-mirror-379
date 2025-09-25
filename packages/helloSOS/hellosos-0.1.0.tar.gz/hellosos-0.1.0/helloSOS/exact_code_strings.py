# Prac 1 - Neural Network Visualization
PRAC1_CODE = '''# Prac 1
import matplotlib.pyplot as plt
import numpy as np

layers = [4, 8, 3]  # input, hidden, output
fig, ax = plt.subplots(); ax.axis("off")

for i, n in enumerate(layers):
    y = np.linspace(0, 1, n)
    for yy in y: ax.add_patch(plt.Circle((i, yy), 0.03, color="skyblue", ec="black"))
    if i < len(layers)-1:
        y_next = np.linspace(0, 1, layers[i+1])
        for y1 in y:
            for y2 in y_next: ax.plot([i, i+1], [y1, y2], "k-", lw=0.5)

ax.set_title("4-8-3 Neural Network")
plt.show()'''

# Prac 3 - Iris Classification
PRAC3_CODE = '''# Prac 3
import pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

df = pd.read_csv(r"iris.csv")
X = df.iloc[:, :4].astype("float32").to_numpy()  
y = LabelEncoder().fit_transform(df.iloc[:, 4])  
y = to_categorical(y, 3).astype("float32")       

X_t, X_test, y_t, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_t, y_t, test_size=0.25, stratify=y_t, random_state=42)

model = Sequential([
    Dense(16, activation="relu", input_shape=(4,)),
    Dense(12, activation="relu"),
    Dense(3, activation="softmax")
])
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

h = model.fit(X_train, y_train, epochs=30, batch_size=16, validation_data=(X_val, y_val), verbose=0)

plt.figure(figsize=(8,3))
for i,(k,t) in enumerate([("loss","Loss"), ("accuracy","Accuracy")]):
    plt.subplot(1,2,i+1)
    plt.plot(h.history[k], label="Train")
    plt.plot(h.history["val_"+k], label="Val")
    plt.title(t); plt.legend()
plt.tight_layout(); plt.show()

l,a = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Loss: {l:.4f}  |  Test Accuracy: {a:.4f}")'''

# Prac 4 - Titanic Survival Prediction
PRAC4_CODE = '''# prac 4
import pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

df = pd.read_csv(r"titanic.csv")[['Pclass','Gender','Age','Fare','Survived']].dropna()
df['Gender'] = df['Gender'].map({'male':0,'female':1}).astype('float32')  # ensure numeric
X = df[['Pclass','Gender','Age','Fare']].astype('float32').to_numpy()
y = df['Survived'].astype('float32').to_numpy().reshape(-1,1)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
scaler = StandardScaler().fit(X_tr)
X_tr, X_te = scaler.transform(X_tr), scaler.transform(X_te)

model = Sequential([Dense(1, 'sigmoid', input_shape=(4,))])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

h = model.fit(X_tr, y_tr, epochs=30, batch_size=16, validation_split=0.2, verbose=0)

plt.figure(figsize=(8,3))
for i,(k,t) in enumerate([('loss','Loss'), ('accuracy','Accuracy')]):
    plt.subplot(1,2,i+1)
    plt.plot(h.history[k], label='Train')
    plt.plot(h.history['val_'+k], label='Val')
    plt.title(t); plt.legend()
plt.tight_layout(); plt.show()

l,a = model.evaluate(X_te, y_te, verbose=0)
print(f"Test Loss: {l:.4f}  |  Test Accuracy: {a:.4f}")'''

# Prac 5 - MNIST CNN Classification
PRAC5_CODE = '''# Prac 5
import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from tensorflow.keras.utils import to_categorical

# Load CSV
df = pd.read_csv(r"mnist_train.csv")

X = df.iloc[:,1:].apply(pd.to_numeric, errors='coerce').fillna(0).astype('float32').values
X = X.reshape(-1,28,28,1)/255.0

y = pd.to_numeric(df.iloc[:,0], errors='coerce').fillna(0).astype(int)
y = to_categorical(y, num_classes=10)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=np.argmax(y,1), random_state=42
)

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
print(f"Test Loss: {loss:.4f} | Test Accuracy: {acc:.4f}")'''

# Prac 7 - Banknote Authentication
PRAC7_CODE = '''# prac 7 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

df = pd.read_csv(r"banknote.csv")
df = df.apply(lambda col: pd.to_numeric(col, errors='coerce')).dropna()  # remove non-numeric

X = df.iloc[:, :-1].to_numpy(dtype=np.float32)
y = df.iloc[:, -1].to_numpy(dtype=np.float32).reshape(-1,1)

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
sc = StandardScaler().fit(X_tr)
X_tr, X_te = sc.transform(X_tr), sc.transform(X_te)

model = Sequential([
    Input(shape=(X_tr.shape[1],)),
    Dense(10, activation='relu'),
    Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

h = model.fit(X_tr, y_tr, epochs=30, batch_size=16, validation_split=0.2, verbose=0)

plt.figure(figsize=(10,4))
for i, (k, t) in enumerate([('loss','Loss'), ('accuracy','Accuracy')]):
    plt.subplot(1,2,i+1)
    plt.plot(h.history[k], label='train')
    plt.plot(h.history['val_'+k], label='val')
    plt.title(t)
    plt.legend()
plt.tight_layout()
plt.show()

loss, acc = model.evaluate(X_te, y_te, verbose=0)
print(f"Test Loss: {loss:.4f} | Test Accuracy: {acc:.4f}")'''

# Prac 8 - MNIST Denoising Autoencoder
PRAC8_CODE = '''# prac 8
import numpy as np, pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tts
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

df = pd.read_csv(r"mnist_train.csv")
X = df.drop('label', axis=1).values / 255.0
X_noisy = np.clip(X + np.random.normal(0,0.4,X.shape), 0, 1)
X_train, X_test, Xn_train, Xn_test = tts(X, X_noisy, test_size=0.2, random_state=42)

model = Sequential([
    Input((784,)), Dense(128,'relu'), Dense(64,'relu'), Dense(32,'relu'),
    Dense(64,'relu'), Dense(128,'relu'), Dense(784,'sigmoid')
])
model.compile('adam','binary_crossentropy')

hist = model.fit(Xn_train, X_train, validation_data=(Xn_test, X_test), epochs=10, verbose=0)

plt.plot(hist.history['loss'], label='Train')
plt.plot(hist.history['val_loss'], label='Val')
plt.title("Denoising Autoencoder Loss"); plt.xlabel("Epoch"); plt.ylabel("Loss")
plt.legend(); plt.grid(True); plt.show()

decoded = model.predict(Xn_test[:5])
fig, axs = plt.subplots(3,5,figsize=(12,6))
for i in range(5):
    axs[0,i].imshow(Xn_test[i].reshape(28,28), cmap='gray'); axs[0,i].axis('off')
    axs[1,i].imshow(decoded[i].reshape(28,28), cmap='gray'); axs[1,i].axis('off')
    axs[2,i].imshow(X_test[i].reshape(28,28), cmap='gray'); axs[2,i].axis('off')
axs[0,0].set_title("Noisy"); axs[1,0].set_title("Denoised"); axs[2,0].set_title("Original")
plt.suptitle("Denoising Autoencoder Results"); plt.tight_layout(); plt.show()'''

# Dictionary for easy access
CODE_DICT = {
    'prac1': PRAC1_CODE,
    'prac3': PRAC3_CODE,
    'prac4': PRAC4_CODE,
    'prac5': PRAC5_CODE,
    'prac7': PRAC7_CODE,
    'prac8': PRAC8_CODE
}

def get_code(prac_name):
    """
    Get the source code for a specific practical.
    
    Args:
        prac_name (str): Name of the practical ('prac1', 'prac3', 'prac4', 'prac5', 'prac7', 'prac8')
    
    Returns:
        str: The source code as a string
    
    Example:
        code = get_code('prac1')
        print(code)
    """
    prac_name = prac_name.lower()
    if prac_name in CODE_DICT:
        return CODE_DICT[prac_name]
    else:
        available = ', '.join(CODE_DICT.keys())
        raise ValueError(f"Unknown prac_name '{prac_name}'. Available: {available}")

def get_all_codes():
    """
    Get all source codes as a dictionary.
    
    Returns:
        dict: Dictionary with prac names as keys and source codes as values
    
    Example:
        all_codes = get_all_codes()
        for name, code in all_codes.items():
            print(f"=== {name.upper()} ===")
            print(code)
            print()
    """
    return CODE_DICT.copy()

def save_code_to_file(prac_name, filename):
    """
    Save a specific practical's code to a file.
    
    Args:
        prac_name (str): Name of the practical
        filename (str): Output filename
    
    Example:
        save_code_to_file('prac1', 'neural_network_viz.py')
    """
    code = get_code(prac_name)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Code for {prac_name} saved to {filename}")

def print_code(prac_name):
    """
    Print the source code for a specific practical with formatting.
    
    Args:
        prac_name (str): Name of the practical
    
    Example:
        print_code('prac1')
    """
    code = get_code(prac_name)
    print(f"=== {prac_name.upper()} - SOURCE CODE ===")
    print(code)
    print("=" * 50)

def execute_code(prac_name):
    """
    Execute the code for a specific practical.
    WARNING: This will execute the code directly!
    
    Args:
        prac_name (str): Name of the practical
    
    Example:
        execute_code('prac1')  # This will run the neural network visualization
    """
    code = get_code(prac_name)
    print(f"Executing {prac_name.upper()}...")
    exec(code)