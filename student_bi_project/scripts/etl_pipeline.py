"""
ETL Pipeline for Student Performance Data Warehouse
Author: Your Name
Date: January 2026

This script demonstrates a complete ETL (Extract, Transform, Load) process
for student academic performance data.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3  # Using SQLite for demonstration (can be replaced with PostgreSQL)

class StudentDataETL:
    """
    ETL Pipeline for Student Performance Data
    """
    
    def __init__(self, source_file, db_path):
        self.source_file = source_file
        self.db_path = db_path
        self.conn = None
        
    def extract(self):
        """
        EXTRACT: Load data from source CSV file
        """
        print("=" * 60)
        print("STEP 1: EXTRACT - Loading data from source")
        print("=" * 60)
        
        df = pd.read_csv(self.source_file)
        print(f"✓ Loaded {len(df)} records from {self.source_file}")
        print(f"✓ Columns: {', '.join(df.columns)}")
        
        return df
    
    def transform(self, df):
        """
        TRANSFORM: Clean and transform data
        """
        print("\n" + "=" * 60)
        print("STEP 2: TRANSFORM - Cleaning and transforming data")
        print("=" * 60)
        
        # Check for missing values
        null_counts = df.isnull().sum()
        print(f"✓ Null values check: {null_counts[null_counts > 0].to_dict() if null_counts.sum() > 0 else 'No nulls found'}")
        
        # Handle missing values (if any)
        df = df.fillna({
            'attendance_rate': df['attendance_rate'].mean(),
            'midterm_score': df['midterm_score'].mean(),
            'final_score': df['final_score'].mean()
        })
        
        # Data validation: Ensure scores are in valid range (0-100)
        score_columns = ['attendance_rate', 'midterm_score', 'final_score', 
                        'projects_score', 'quizzes_avg', 'assignments_avg', 'final_grade']
        
        for col in score_columns:
            df[col] = df[col].clip(0, 100)
        
        print(f"✓ Validated score ranges (0-100)")
        
        # Create risk categories based on attendance and midterm
        df['risk_category'] = df.apply(self._calculate_risk, axis=1)
        print(f"✓ Created risk categories")
        
        # Create performance tier
        df['performance_tier'] = pd.cut(df['final_grade'], 
                                       bins=[0, 60, 70, 80, 100],
                                       labels=['Failing', 'Satisfactory', 'Good', 'Excellent'])
        print(f"✓ Created performance tiers")
        
        # Standardize department names
        df['department'] = df['department'].str.strip().str.title()
        
        print(f"✓ Transformation complete: {len(df)} records ready for loading")
        
        return df
    
    def _calculate_risk(self, row):
        """
        Calculate risk category based on attendance and midterm score
        """
        if row['attendance_rate'] < 60 or row['midterm_score'] < 60:
            return 'High Risk'
        elif row['attendance_rate'] < 75 or row['midterm_score'] < 70:
            return 'Medium Risk'
        else:
            return 'Low Risk'
    
    def load(self, df):
        """
        LOAD: Load transformed data into Data Warehouse
        """
        print("\n" + "=" * 60)
        print("STEP 3: LOAD - Loading data into Data Warehouse")
        print("=" * 60)
        
        # Connect to SQLite database (Data Warehouse)
        self.conn = sqlite3.connect(self.db_path)
        print(f"✓ Connected to database: {self.db_path}")
        
        # Create Star Schema tables
        self._create_schema()
        
        # Load Dimension Tables
        self._load_dim_student(df)
        self._load_dim_department(df)
        self._load_dim_semester(df)
        
        # Load Fact Table
        self._load_fact_performance(df)
        
        print(f"\n✓ ETL Pipeline completed successfully!")
        print(f"✓ Total records loaded: {len(df)}")
        
        self.conn.close()
        
    def _create_schema(self):
        """
        Create Star Schema in the Data Warehouse
        """
        cursor = self.conn.cursor()
        
        # Dimension: Student
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_student (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT,
                enrollment_year TEXT,
                gender TEXT,
                status TEXT
            )
        """)
        
        # Dimension: Department
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_department (
                department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                department_name TEXT UNIQUE,
                department_code TEXT
            )
        """)
        
        # Dimension: Semester
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dim_semester (
                semester_id INTEGER PRIMARY KEY AUTOINCREMENT,
                semester_name TEXT,
                academic_year TEXT
            )
        """)
        
        # Fact: Student Performance
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fact_student_performance (
                performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                department_id INTEGER,
                semester_id INTEGER,
                attendance_rate REAL,
                midterm_score REAL,
                final_score REAL,
                projects_score REAL,
                quizzes_avg REAL,
                assignments_avg REAL,
                total_score REAL,
                final_grade REAL,
                risk_category TEXT,
                performance_tier TEXT,
                last_updated DATE,
                FOREIGN KEY (student_id) REFERENCES dim_student(student_id),
                FOREIGN KEY (department_id) REFERENCES dim_department(department_id),
                FOREIGN KEY (semester_id) REFERENCES dim_semester(semester_id)
            )
        """)
        
        self.conn.commit()
        print("✓ Star Schema created (4 tables: 3 dimensions + 1 fact)")
        
    def _load_dim_student(self, df):
        """Load Student Dimension"""
        dim_student = df[['student_id', 'student_name', 'enrollment_year', 'gender', 'status']].drop_duplicates()
        dim_student.to_sql('dim_student', self.conn, if_exists='replace', index=False)
        print(f"  ✓ Loaded dim_student: {len(dim_student)} records")
        
    def _load_dim_department(self, df):
        """Load Department Dimension"""
        departments = df['department'].unique()
        dim_dept = pd.DataFrame({
            'department_name': departments,
            'department_code': [d[:3].upper() for d in departments]
        })
        dim_dept.to_sql('dim_department', self.conn, if_exists='replace', index=False)
        print(f"  ✓ Loaded dim_department: {len(dim_dept)} records")
        
    def _load_dim_semester(self, df):
        """Load Semester Dimension"""
        dim_semester = df[['semester', 'academic_year']].drop_duplicates()
        dim_semester.columns = ['semester_name', 'academic_year']
        dim_semester.to_sql('dim_semester', self.conn, if_exists='replace', index=False)
        print(f"  ✓ Loaded dim_semester: {len(dim_semester)} records")
        
    def _load_fact_performance(self, df):
        """Load Fact Table"""
        # Get department IDs
        dept_map = pd.read_sql("SELECT rowid as department_id, department_name FROM dim_department", self.conn)
        df = df.merge(dept_map, left_on='department', right_on='department_name', how='left')
        
        # Get semester IDs
        sem_map = pd.read_sql("SELECT rowid as semester_id, semester_name FROM dim_semester", self.conn)
        df = df.merge(sem_map, left_on='semester', right_on='semester_name', how='left')
        
        fact_cols = ['student_id', 'department_id', 'semester_id', 'attendance_rate',
                    'midterm_score', 'final_score', 'projects_score', 'quizzes_avg',
                    'assignments_avg', 'total_score', 'final_grade', 'risk_category',
                    'performance_tier', 'last_updated']
        
        fact_performance = df[fact_cols]
        fact_performance.to_sql('fact_student_performance', self.conn, if_exists='replace', index=False)
        print(f"  ✓ Loaded fact_student_performance: {len(fact_performance)} records")


def main():
    """
    Main ETL execution
    """
    print("\n" + "🔄 STUDENT PERFORMANCE DATA WAREHOUSE - ETL PIPELINE 🔄".center(60))
    print("=" * 60)
    
    # Initialize ETL
    etl = StudentDataETL(
        source_file='/home/claude/student_bi_project/data/student_performance.csv',
        db_path='/home/claude/student_bi_project/data/student_dw.db'
    )
    
    # Execute ETL Pipeline
    df = etl.extract()
    df_transformed = etl.transform(df)
    etl.load(df_transformed)
    
    print("\n" + "=" * 60)
    print("ETL PIPELINE SUMMARY")
    print("=" * 60)
    print(f"Source: CSV file")
    print(f"Target: SQLite Data Warehouse (Star Schema)")
    print(f"Status: ✓ SUCCESS")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
