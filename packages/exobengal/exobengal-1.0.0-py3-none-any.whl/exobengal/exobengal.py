import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Dropout

import warnings
warnings.filterwarnings("ignore")

# ---------------------------------------------------
# Setup paths
# ---------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR.parent / "models"
DATA_DIR = BASE_DIR.parent / "data"
MODELS_DIR.mkdir(parents=True, exist_ok=True)


class ExoParams:
    def __init__(self, period=None, prad=None, teq=None, srad=None,
                 slog_g=None, steff=None, impact=None, duration=None, depth=None):
        self.period = period
        self.prad = prad
        self.teq = teq
        self.srad = srad
        self.slog_g = slog_g
        self.steff = steff
        self.impact = impact
        self.duration = duration
        self.depth = depth

    def to_feature_list(self):
        return [
            self.period,
            self.prad,
            self.teq,
            self.srad,
            self.slog_g,
            self.steff,
            self.impact,
            self.duration,
            self.depth,
        ]


class DetectExoplanet:
    def __init__(self,
                 rf_model_path=str(MODELS_DIR / "random_forest_classifier.pkl"),
                 cnn_model_path=str(MODELS_DIR / "cnn_model.h5"),
                 knn_model_path=str(MODELS_DIR / "knn_model.pkl"),
                 scaler_path=str(MODELS_DIR / "scaler.pkl"),
                 imputer_path=str(MODELS_DIR / "imputer.pkl")):

        self.model_path = rf_model_path
        self.cnn_path = cnn_model_path
        self.knn_model_path = knn_model_path
        self.scaler_path = scaler_path
        self.imputer_path = imputer_path

        self.model = None
        self.cnn_model = None
        self.knn_model = None
        self.scaler = None
        self.imputer = None

    # ---------------- ESI ----------------
    def calculate_esi(self, koi_prad, koi_teq):
        r_earth = 1.0
        t_earth = 288
        radius_score = 1 - abs(koi_prad - r_earth) / (koi_prad + r_earth)
        temp_score = 1 - abs(koi_teq - t_earth) / (koi_teq + t_earth)
        esi = (radius_score * temp_score) ** 0.5
        return round(esi, 3)

    # ---------------- Helper ----------------
    def _prepare_input(self, input_data):
        """Convert ExoParams to feature array and fill missing values"""
        if isinstance(input_data, ExoParams):
            features = input_data.to_feature_list()
        else:
            features = input_data
        features = [0 if x is None else x for x in features]  # fill missing with 0
        input_array = np.array(features).reshape(1, -1)
        if self.imputer is not None:
            input_array = self.imputer.transform(input_array)
        if self.scaler is not None:
            input_array = self.scaler.transform(input_array)
        return input_array

    # ---------------- Random Forest ----------------
    def train_random_forest(self, data_path=str(DATA_DIR / "cumulative_2025.09.20_12.15.37.csv")):
        koi_table = pd.read_csv(data_path, skiprows=1, delimiter=",", comment="#")
        koi_table['koi_insol'] = ((koi_table['koi_steff'] / 5778) ** 4) * (koi_table['koi_srad'] ** 2) / (koi_table['koi_period'] ** (4 / 3))

        features = ["koi_period", "koi_prad", "koi_teq", "koi_srad", "koi_slogg",
                    "koi_steff", "koi_impact", "koi_duration", "koi_depth"]
        koi_table["label"] = koi_table["koi_disposition"].map(
            {"CONFIRMED": 1, "FALSE POSITIVE": 0, "CANDIDATE": 1})

        self.imputer = SimpleImputer(strategy='mean')
        koi_table[features] = self.imputer.fit_transform(koi_table[features])
        joblib.dump(self.imputer, self.imputer_path)

        koi_table = koi_table.dropna(subset=["label"])
        X = koi_table[features]
        y = koi_table["label"]

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        joblib.dump(self.scaler, self.scaler_path)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42)

        param_grid = {'n_estimators': [50, 100, 200],
                      'max_depth': [None, 10, 20],
                      'min_samples_split': [2, 5, 10]}
        model = RandomForestClassifier(random_state=42)
        grid_search = GridSearchCV(model, param_grid, cv=3,
                                   scoring='roc_auc', n_jobs=-1)
        grid_search.fit(X_train, y_train)
        self.model = grid_search.best_estimator_
        joblib.dump(self.model, self.model_path)

        # Evaluate
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Random Forest Confusion Matrix')
        plt.show()
        auc_roc = roc_auc_score(y_test, self.model.predict_proba(X_test)[:, 1])
        print(f"AUC-ROC: {auc_roc:.2f}")

    def load_rf_model(self):
        self.model = joblib.load(self.model_path)
        self.scaler = joblib.load(self.scaler_path)
        self.imputer = joblib.load(self.imputer_path)

    def random_forest(self, input_data):
        if self.model is None:
            self.load_rf_model()
        input_array = self._prepare_input(input_data)
        prediction = self.model.predict(input_array)[0]
        probability = self.model.predict_proba(input_array)[0][1]
        label = "Planet" if prediction == 1 else "Not a Planet"

        result = {"prediction": label, "probability": float(probability)}
        if label == "Planet":
            result["ESI"] = self.calculate_esi(input_array[0][1], input_array[0][2])
            print(f"Prediction: {label}, Probability: {probability:.2f}, ESI: {result['ESI']}")
        else:
            print(f"Prediction: {label}, Probability: {probability:.2f}")
        return result

    # ---------------- CNN ----------------
    def train_cnn(self, data_path=str(DATA_DIR / "cumulative_2025.09.20_12.15.37.csv")):
        koi_table = pd.read_csv(data_path, skiprows=1, delimiter=",", comment="#")
        koi_table['koi_insol'] = ((koi_table['koi_steff'] / 5778) ** 4) * (koi_table['koi_srad'] ** 2) / (koi_table['koi_period'] ** (4 / 3))
        features = ["koi_period", "koi_prad", "koi_teq", "koi_srad", "koi_slogg",
                    "koi_steff", "koi_impact", "koi_duration", "koi_depth"]
        koi_table["label"] = koi_table["koi_disposition"].map(
            {"CONFIRMED": 1, "FALSE POSITIVE": 0, "CANDIDATE": 1})

        self.imputer = SimpleImputer(strategy='mean')
        koi_table[features] = self.imputer.fit_transform(koi_table[features])
        joblib.dump(self.imputer, self.imputer_path)
        koi_table = koi_table.dropna(subset=["label"])

        X = koi_table[features]
        y = koi_table["label"]

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        joblib.dump(self.scaler, self.scaler_path)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42, stratify=y)

        model = Sequential([
            Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
            Dropout(0.3),
            Dense(32, activation="relu"),
            Dropout(0.3),
            Dense(16, activation="relu"),
            Dense(1, activation="sigmoid")
        ])
        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
        model.fit(X_train, y_train, epochs=50, batch_size=32,
                  validation_data=(X_test, y_test), verbose=1)

        self.cnn_model = model
        model.save(self.cnn_path)
        print(f"CNN model saved to {self.cnn_path}")

    def load_cnn(self):
        self.cnn_model = load_model(self.cnn_path)
        self.scaler = joblib.load(self.scaler_path)
        self.imputer = joblib.load(self.imputer_path)

    def cnn(self, input_data):
        if self.cnn_model is None:
            self.load_cnn()
        input_array = self._prepare_input(input_data)
        probability = self.cnn_model.predict(input_array)[0][0]
        label = "Planet" if probability > 0.6 else "Not a Planet"
        result = {"prediction": label, "probability": float(probability)}
        if label == "Planet":
            result["ESI"] = self.calculate_esi(input_array[0][1], input_array[0][2])
        return result

    # ---------------- kNN ----------------
    def train_knn(self, data_path=str(DATA_DIR / "cumulative_2025.09.20_12.15.37.csv")):
        koi_table = pd.read_csv(data_path, skiprows=1, delimiter=",", comment="#")
        koi_table['koi_insol'] = ((koi_table['koi_steff'] / 5778) ** 4) * (koi_table['koi_srad'] ** 2) / (koi_table['koi_period'] ** (4 / 3))
        features = ["koi_period", "koi_prad", "koi_teq", "koi_srad", "koi_slogg",
                    "koi_steff", "koi_impact", "koi_duration", "koi_depth"]
        koi_table["label"] = koi_table["koi_disposition"].map(
            {"CONFIRMED": 1, "FALSE POSITIVE": 0, "CANDIDATE": 1})

        self.imputer = SimpleImputer(strategy='mean')
        koi_table[features] = self.imputer.fit_transform(koi_table[features])
        joblib.dump(self.imputer, self.imputer_path)
        koi_table = koi_table.dropna(subset=["label"])

        X = koi_table[features]
        y = koi_table["label"]

        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        joblib.dump(self.scaler, self.scaler_path)

        X_train, X_test, y_train, y_test = train_test_split(
            X_scaled, y, test_size=0.2, random_state=42, stratify=y)

        self.knn_model = KNeighborsClassifier(n_neighbors=5)
        self.knn_model.fit(X_train, y_train)
        joblib.dump(self.knn_model, self.knn_model_path)
        print(f"kNN model saved to {self.knn_model_path}")

    def load_knn(self):
        self.knn_model = joblib.load(self.knn_model_path)
        self.scaler = joblib.load(self.scaler_path)
        self.imputer = joblib.load(self.imputer_path)

    def knn(self, input_data):
        if self.knn_model is None:
            self.load_knn()
        input_array = self._prepare_input(input_data)
        probability = self.knn_model.predict_proba(input_array)[0][1]
        label = "Planet" if probability >= 0.6 else "Not a Planet"
        result = {"prediction": label, "probability": float(probability)}
        if label == "Planet":
            result["ESI"] = self.calculate_esi(input_array[0][1], input_array[0][2])
        return result
