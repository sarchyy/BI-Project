"""
Correlation Analysis and Statistical Insights
Student Performance Data Warehouse BI Project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import sqlite3

class CorrelationAnalysis:
    """
    Statistical analysis and correlation insights
    """
    
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        
    def load_data(self):
        """Load data from Data Warehouse"""
        query = """
        SELECT 
            f.*,
            d.department_name,
            s.student_name,
            s.enrollment_year
        FROM fact_student_performance f
        JOIN dim_student s ON f.student_id = s.student_id
        JOIN dim_department d ON f.department_id = d.rowid
        """
        return pd.read_sql(query, self.conn)
    
    def calculate_correlations(self, df):
        """
        Calculate correlation coefficients between key metrics
        """
        print("=" * 70)
        print("CORRELATION ANALYSIS - Key Performance Indicators".center(70))
        print("=" * 70)
        
        # Select numerical columns
        metrics = ['attendance_rate', 'midterm_score', 'final_score', 
                  'projects_score', 'quizzes_avg', 'assignments_avg', 'final_grade']
        
        correlation_matrix = df[metrics].corr()
        
        # Key correlations with final grade
        final_grade_corr = correlation_matrix['final_grade'].sort_values(ascending=False)
        
        print("\n📊 CORRELATION WITH FINAL GRADE (sorted by strength):")
        print("-" * 70)
        for metric, corr_value in final_grade_corr.items():
            if metric != 'final_grade':
                strength = self._interpret_correlation(abs(corr_value))
                print(f"  {metric:20s}: r = {corr_value:+.3f}  ({strength})")
        
        # Statistical significance tests
        print("\n" + "=" * 70)
        print("STATISTICAL SIGNIFICANCE TESTS (p-value < 0.05 = significant)")
        print("=" * 70)
        
        # Test correlation between attendance and final grade
        corr_att, p_att = stats.pearsonr(df['attendance_rate'], df['final_grade'])
        print(f"\n✓ Attendance vs Final Grade:")
        print(f"  Correlation: r = {corr_att:.3f}")
        print(f"  P-value: {p_att:.6f} {'✓ SIGNIFICANT' if p_att < 0.05 else '✗ Not significant'}")
        
        # Test correlation between midterm and final grade
        corr_mid, p_mid = stats.pearsonr(df['midterm_score'], df['final_grade'])
        print(f"\n✓ Midterm vs Final Grade:")
        print(f"  Correlation: r = {corr_mid:.3f}")
        print(f"  P-value: {p_mid:.6f} {'✓ SIGNIFICANT' if p_mid < 0.05 else '✗ Not significant'}")
        
        return correlation_matrix
    
    def _interpret_correlation(self, r):
        """Interpret correlation strength"""
        if r > 0.7:
            return "Very Strong"
        elif r > 0.5:
            return "Strong"
        elif r > 0.3:
            return "Moderate"
        elif r > 0.1:
            return "Weak"
        else:
            return "Very Weak"
    
    def department_analysis(self, df):
        """
        Analyze performance by department
        """
        print("\n" + "=" * 70)
        print("DEPARTMENT-LEVEL ANALYSIS")
        print("=" * 70)
        
        dept_stats = df.groupby('department_name').agg({
            'final_grade': ['mean', 'std', 'min', 'max'],
            'attendance_rate': 'mean',
            'midterm_score': 'mean',
            'student_id': 'count'
        }).round(2)
        
        dept_stats.columns = ['Avg Grade', 'Std Dev', 'Min', 'Max', 'Avg Attendance', 'Avg Midterm', 'N Students']
        
        print("\n" + dept_stats.to_string())
        
        # Risk distribution by department
        print("\n" + "=" * 70)
        print("RISK DISTRIBUTION BY DEPARTMENT")
        print("=" * 70)
        
        risk_dist = pd.crosstab(df['department_name'], df['risk_category'], normalize='index') * 100
        print("\n" + risk_dist.round(1).to_string())
        
    def business_insights(self, df):
        """
        Generate actionable business insights
        """
        print("\n" + "=" * 70)
        print("💡 ACTIONABLE BUSINESS INSIGHTS")
        print("=" * 70)
        
        # 1. Early Warning: Students at risk
        high_risk = df[df['risk_category'] == 'High Risk']
        print(f"\n1. EARLY WARNING SYSTEM:")
        print(f"   • {len(high_risk)} students ({len(high_risk)/len(df)*100:.1f}%) are HIGH RISK")
        print(f"   • Average attendance: {high_risk['attendance_rate'].mean():.1f}%")
        print(f"   • Average midterm: {high_risk['midterm_score'].mean():.1f}")
        print(f"   💡 ACTION: Immediate intervention needed (tutoring, counseling)")
        
        # 2. Attendance impact
        low_attendance = df[df['attendance_rate'] < 70]
        avg_grade_low_att = low_attendance['final_grade'].mean()
        avg_grade_high_att = df[df['attendance_rate'] >= 80]['final_grade'].mean()
        grade_diff = avg_grade_high_att - avg_grade_low_att
        
        print(f"\n2. ATTENDANCE IMPACT:")
        print(f"   • Students with <70% attendance: avg grade = {avg_grade_low_att:.1f}")
        print(f"   • Students with ≥80% attendance: avg grade = {avg_grade_high_att:.1f}")
        print(f"   • Difference: {grade_diff:.1f} points ({grade_diff/avg_grade_low_att*100:.1f}% improvement)")
        print(f"   💡 ACTION: Implement attendance monitoring system")
        
        # 3. Midterm as predictor
        failed_midterm = df[df['midterm_score'] < 60]
        pct_failed_final = (failed_midterm['final_grade'] < 60).sum() / len(failed_midterm) * 100
        
        print(f"\n3. MIDTERM AS EARLY PREDICTOR:")
        print(f"   • Students who failed midterm (<60): {len(failed_midterm)}")
        print(f"   • Of those, {pct_failed_final:.1f}% also failed final exam")
        print(f"   💡 ACTION: Post-midterm intervention program")
        
        # 4. Department-specific recommendations
        print(f"\n4. DEPARTMENT-SPECIFIC NEEDS:")
        dept_avg = df.groupby('department_name')['final_grade'].mean().sort_values()
        for dept, avg in dept_avg.items():
            if avg < 68:
                print(f"   • {dept}: avg = {avg:.1f} → Need curriculum review & support")
            elif avg > 71:
                print(f"   • {dept}: avg = {avg:.1f} → Share best practices")
        
        # 5. ROI Calculation
        print(f"\n5. BUSINESS VALUE / ROI:")
        total_students = len(df)
        failing_students = (df['final_grade'] < 60).sum()
        potential_saves = int(failing_students * 0.4)  # 40% reduction with intervention
        cost_per_student = 5000  # KM
        total_savings = potential_saves * cost_per_student
        
        print(f"   • Current failing students: {failing_students} ({failing_students/total_students*100:.1f}%)")
        print(f"   • Potential students saved (40% reduction): {potential_saves}")
        print(f"   • Financial impact: {total_savings:,} KM annually")
        print(f"   • System cost: 50,000 KM one-time + 10,000 KM/year")
        print(f"   • ROI: {(total_savings-60000)/60000*100:.1f}% in Year 1")
        
    def save_visualizations(self, df, correlation_matrix):
        """
        Create and save visualizations
        """
        print("\n" + "=" * 70)
        print("Generating visualizations...")
        print("=" * 70)
        
        # Set style
        sns.set_style("whitegrid")
        
        # 1. Correlation Heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                   fmt='.2f', linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Correlation Matrix - Student Performance Metrics', fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.savefig('/home/claude/student_bi_project/visualizations/correlation_heatmap.png', dpi=300)
        print("  ✓ Saved: correlation_heatmap.png")
        
        # 2. Attendance vs Final Grade Scatter
        plt.figure(figsize=(10, 6))
        for dept in df['department_name'].unique():
            dept_data = df[df['department_name'] == dept]
            plt.scatter(dept_data['attendance_rate'], dept_data['final_grade'], 
                       label=dept, alpha=0.6, s=50)
        
        # Add regression line
        z = np.polyfit(df['attendance_rate'], df['final_grade'], 1)
        p = np.poly1d(z)
        plt.plot(df['attendance_rate'], p(df['attendance_rate']), "r--", alpha=0.8, linewidth=2)
        
        plt.xlabel('Attendance Rate (%)', fontsize=12)
        plt.ylabel('Final Grade', fontsize=12)
        plt.title('Attendance vs Final Grade (with regression line)', fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('/home/claude/student_bi_project/visualizations/attendance_vs_grade.png', dpi=300)
        print("  ✓ Saved: attendance_vs_grade.png")
        
        # 3. Risk Category Distribution
        plt.figure(figsize=(10, 6))
        risk_counts = df['risk_category'].value_counts()
        colors = {'Low Risk': '#2ecc71', 'Medium Risk': '#f39c12', 'High Risk': '#e74c3c'}
        bars = plt.bar(risk_counts.index, risk_counts.values, 
                      color=[colors[x] for x in risk_counts.index])
        
        plt.xlabel('Risk Category', fontsize=12)
        plt.ylabel('Number of Students', fontsize=12)
        plt.title('Student Risk Distribution - Early Warning System', fontsize=14, fontweight='bold')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}\n({height/len(df)*100:.1f}%)',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.savefig('/home/claude/student_bi_project/visualizations/risk_distribution.png', dpi=300)
        print("  ✓ Saved: risk_distribution.png")
        
        plt.close('all')


def main():
    """
    Main analysis execution
    """
    print("\n" + "📊 CORRELATION ANALYSIS & BUSINESS INSIGHTS 📊".center(70))
    
    # Initialize analysis
    analysis = CorrelationAnalysis('/home/claude/student_bi_project/data/student_dw.db')
    
    # Load data
    df = analysis.load_data()
    
    # Run analyses
    correlation_matrix = analysis.calculate_correlations(df)
    analysis.department_analysis(df)
    analysis.business_insights(df)
    analysis.save_visualizations(df, correlation_matrix)
    
    print("\n" + "=" * 70)
    print("✓ Analysis complete! Check /visualizations folder for charts")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
