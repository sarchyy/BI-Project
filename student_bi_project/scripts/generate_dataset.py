import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of students
n_students = 248

# Generate student data
departments = ['Business', 'CS', 'Engineering', 'Mathematics']
dept_weights = [0.299, 0.241, 0.240, 0.220]  # Based on your PDF data

data = {
    'student_id': range(1, n_students + 1),
    'student_name': [f'Student_{i}' for i in range(1, n_students + 1)],
    'department': np.random.choice(departments, n_students, p=dept_weights),
    'enrollment_year': np.random.choice(['2021', '2022', '2023', '2024'], n_students),
    'gender': np.random.choice(['M', 'F'], n_students),
}

df = pd.DataFrame(data)

# Generate performance metrics based on department characteristics from PDF
def generate_scores(dept):
    if dept == 'Business':
        attendance = np.random.normal(85, 8, 1)[0]
        midterm = np.random.normal(73.48, 10, 1)[0]
        final_grade = np.random.normal(72.17, 8, 1)[0]
    elif dept == 'CS':
        attendance = np.random.normal(70, 10, 1)[0]
        midterm = np.random.normal(73.52, 10, 1)[0]
        final_grade = np.random.normal(67.25, 9, 1)[0]
    elif dept == 'Engineering':
        attendance = np.random.normal(75, 9, 1)[0]
        midterm = np.random.normal(68.85, 10, 1)[0]
        final_grade = np.random.normal(68.48, 8, 1)[0]
    else:  # Mathematics
        attendance = np.random.normal(72, 10, 1)[0]
        midterm = np.random.normal(68.23, 10, 1)[0]
        final_grade = np.random.normal(69.43, 9, 1)[0]
    
    # Generate other scores with correlation to midterm and attendance
    projects = midterm * 0.8 + np.random.normal(10, 5, 1)[0]
    quizzes = attendance * 0.7 + np.random.normal(15, 5, 1)[0]
    assignments = (midterm + attendance) / 2 * 0.9 + np.random.normal(5, 3, 1)[0]
    final_score = final_grade * 1.2 + np.random.normal(0, 5, 1)[0]
    
    # Clip values to realistic ranges
    return {
        'attendance_rate': np.clip(attendance, 0, 100),
        'midterm_score': np.clip(midterm, 0, 100),
        'final_score': np.clip(final_score, 0, 100),
        'projects_score': np.clip(projects, 0, 100),
        'quizzes_avg': np.clip(quizzes, 0, 100),
        'assignments_avg': np.clip(assignments, 0, 100),
        'final_grade': np.clip(final_grade, 0, 100)
    }

# Apply score generation
performance_data = df['department'].apply(generate_scores).apply(pd.Series)
df = pd.concat([df, performance_data], axis=1)

# Calculate total score
df['total_score'] = (
    df['midterm_score'] * 0.25 +
    df['final_score'] * 0.35 +
    df['projects_score'] * 0.20 +
    df['quizzes_avg'] * 0.10 +
    df['assignments_avg'] * 0.10
)

# Add semester and date information
df['semester'] = 'Fall 2024'
df['academic_year'] = '2024/2025'
df['last_updated'] = datetime.now().strftime('%Y-%m-%d')

# Create pass/fail status (below 60 is fail)
df['status'] = df['final_grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')

# Save to CSV
df.to_csv('/home/claude/student_bi_project/data/student_performance.csv', index=False)

print(f"Generated {n_students} student records")
print(f"\nDataset shape: {df.shape}")
print(f"\nDepartment distribution:")
print(df['department'].value_counts())
print(f"\nAverage metrics:")
print(df[['attendance_rate', 'midterm_score', 'final_grade']].mean())
print(f"\nPass/Fail ratio:")
print(df['status'].value_counts())
