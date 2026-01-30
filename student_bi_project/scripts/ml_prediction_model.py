"""
Machine Learning Model for Student Success Prediction
Logistic Regression Model to predict Pass/Fail
"""

import pandas as pd
import numpy as np
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

class StudentSuccessPredictor:
    """
    ML Model to predict student success based on early indicators
    """
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.model = None
        self.scaler = StandardScaler()
        
    def load_data(self):
        """Load data from Data Warehouse"""
        conn = sqlite3.connect(self.db_path)
        query = """
        SELECT 
            attendance_rate,
            midterm_score,
            projects_score,
            quizzes_avg,
            assignments_avg,
            final_grade,
            CASE WHEN final_grade >= 60 THEN 1 ELSE 0 END as pass
        FROM fact_student_performance
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    
    def prepare_features(self, df):
        """
        Prepare features for ML model
        Using EARLY indicators only (available before final exam)
        """
        # Features: Only data available BEFORE final exam
        feature_columns = [
            'attendance_rate',
            'midterm_score',
            'projects_score',
            'quizzes_avg',
            'assignments_avg'
        ]
        
        X = df[feature_columns]
        y = df['pass']  # 1 = Pass, 0 = Fail
        
        return X, y, feature_columns
    
    def train_model(self, X, y):
        """
        Train Logistic Regression model
        """
        print("=" * 70)
        print("MACHINE LEARNING MODEL TRAINING".center(70))
        print("=" * 70)
        
        # Split data (80% train, 20% test)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        print(f"\n📊 Dataset Split:")
        print(f"   Training set: {len(X_train)} students")
        print(f"   Testing set: {len(X_test)} students")
        
        # Standardize features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train Logistic Regression
        print(f"\n🤖 Training Logistic Regression Model...")
        self.model = LogisticRegression(random_state=42, max_iter=1000)
        self.model.fit(X_train_scaled, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test_scaled)
        y_pred_proba = self.model.predict_proba(X_test_scaled)[:, 1]
        
        # Evaluate
        print(f"\n✓ Model trained successfully!")
        
        return X_train_scaled, X_test_scaled, y_train, y_test, y_pred, y_pred_proba
    
    def evaluate_model(self, X_test, y_test, y_pred, y_pred_proba, feature_columns):
        """
        Evaluate model performance
        """
        print("\n" + "=" * 70)
        print("MODEL PERFORMANCE EVALUATION")
        print("=" * 70)
        
        # Accuracy
        accuracy = accuracy_score(y_test, y_pred)
        print(f"\n📈 Overall Accuracy: {accuracy:.2%}")
        
        # ROC-AUC Score
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"📈 ROC-AUC Score: {roc_auc:.3f}")
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_pred)
        print(f"\n📊 Confusion Matrix:")
        print(f"                  Predicted")
        print(f"                Fail    Pass")
        print(f"   Actual Fail    {cm[0,0]:3d}     {cm[0,1]:3d}")
        print(f"          Pass    {cm[1,0]:3d}     {cm[1,1]:3d}")
        
        # Classification Report
        print(f"\n📋 Detailed Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))
        
        # Feature Importance
        print(f"\n🎯 Feature Importance (Logistic Regression Coefficients):")
        feature_importance = pd.DataFrame({
            'Feature': feature_columns,
            'Coefficient': self.model.coef_[0]
        }).sort_values('Coefficient', ascending=False)
        
        for idx, row in feature_importance.iterrows():
            impact = "↑ Increases pass probability" if row['Coefficient'] > 0 else "↓ Decreases pass probability"
            print(f"   {row['Feature']:20s}: {row['Coefficient']:+.3f}  {impact}")
        
    def predict_at_risk_students(self, threshold=0.5):
        """
        Identify students at risk of failing
        """
        print("\n" + "=" * 70)
        print("🚨 EARLY WARNING: AT-RISK STUDENT IDENTIFICATION")
        print("=" * 70)
        
        # Load all current students
        df = self.load_data()
        X, _, feature_columns = self.prepare_features(df)
        X_scaled = self.scaler.transform(X)
        
        # Predict probabilities
        probabilities = self.model.predict_proba(X_scaled)[:, 1]  # Probability of passing
        df['pass_probability'] = probabilities
        df['prediction'] = (probabilities >= threshold).astype(int)
        
        # Identify at-risk students (probability < 50%)
        at_risk = df[df['pass_probability'] < threshold].copy()
        at_risk = at_risk.sort_values('pass_probability')
        
        print(f"\n🔴 Students at HIGH RISK of failing (pass probability < {threshold*100:.0f}%):")
        print(f"   Total: {len(at_risk)} students ({len(at_risk)/len(df)*100:.1f}%)")
        
        if len(at_risk) > 0:
            print(f"\n   Top 10 highest risk students:")
            print(f"   {'Student':<10} {'Attendance':<12} {'Midterm':<10} {'Pass Prob':<12} {'Risk Level'}")
            print("   " + "-" * 65)
            
            for idx, row in at_risk.head(10).iterrows():
                risk_level = "🔴 CRITICAL" if row['pass_probability'] < 0.3 else "🟠 HIGH"
                print(f"   Student {idx+1:<3}  {row['attendance_rate']:6.1f}%      "
                      f"{row['midterm_score']:6.1f}    {row['pass_probability']:6.1%}      {risk_level}")
        
        # Save predictions
        df.to_csv('/home/claude/student_bi_project/data/predictions.csv', index=False)
        print(f"\n✓ Predictions saved to: predictions.csv")
        
        return at_risk
    
    def save_visualizations(self, X_test, y_test, y_pred, y_pred_proba):
        """
        Create visualizations for model evaluation
        """
        print("\n" + "=" * 70)
        print("Generating model visualizations...")
        print("=" * 70)
        
        # 1. Confusion Matrix Heatmap
        cm = confusion_matrix(y_test, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                   xticklabels=['Fail', 'Pass'], 
                   yticklabels=['Fail', 'Pass'])
        plt.title('Confusion Matrix - Student Success Prediction', fontweight='bold')
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        plt.tight_layout()
        plt.savefig('/home/claude/student_bi_project/visualizations/confusion_matrix.png', dpi=300)
        print("  ✓ Saved: confusion_matrix.png")
        
        # 2. ROC Curve
        from sklearn.metrics import roc_curve
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='darkorange', lw=2, 
                label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curve - Model Performance', fontweight='bold')
        plt.legend(loc="lower right")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('/home/claude/student_bi_project/visualizations/roc_curve.png', dpi=300)
        print("  ✓ Saved: roc_curve.png")
        
        plt.close('all')
    
    def save_model(self):
        """Save trained model for deployment"""
        joblib.dump(self.model, '/home/claude/student_bi_project/models/logistic_regression_model.pkl')
        joblib.dump(self.scaler, '/home/claude/student_bi_project/models/scaler.pkl')
        print(f"\n✓ Model saved to: /models/logistic_regression_model.pkl")


def main():
    """
    Main execution
    """
    print("\n" + "🤖 PREDICTIVE ANALYTICS - STUDENT SUCCESS PREDICTION 🤖".center(70))
    
    # Initialize predictor
    predictor = StudentSuccessPredictor('/home/claude/student_bi_project/data/student_dw.db')
    
    # Load and prepare data
    df = predictor.load_data()
    X, y, feature_columns = predictor.prepare_features(df)
    
    # Train model
    X_train, X_test, y_train, y_test, y_pred, y_pred_proba = predictor.train_model(X, y)
    
    # Evaluate
    predictor.evaluate_model(X_test, y_test, y_pred, y_pred_proba, feature_columns)
    
    # Identify at-risk students
    at_risk = predictor.predict_at_risk_students(threshold=0.5)
    
    # Save visualizations
    predictor.save_visualizations(X_test, y_test, y_pred, y_pred_proba)
    
    # Save model
    predictor.save_model()
    
    print("\n" + "=" * 70)
    print("✓ ML Pipeline complete!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
