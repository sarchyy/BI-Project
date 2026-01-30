# 📦 GitHub Setup Instructions

## Šta treba da pushuješ na GitHub?

Evo tačno šta ide na GitHub i šta NE:

### ✅ ŠTA PUSHUJ (sve ovo je spremno):

```
student_bi_project/
├── scripts/                    ✅ PUSH (Python kod)
│   ├── generate_dataset.py
│   ├── etl_pipeline.py
│   ├── correlation_analysis.py
│   └── ml_prediction_model.py
│
├── docs/                       ✅ PUSH (Dokumentacija)
│   └── star_schema.mermaid
│
├── visualizations/             ✅ PUSH (Slike grafikona)
│   ├── correlation_heatmap.png
│   ├── attendance_vs_grade.png
│   ├── risk_distribution.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
│
├── README.md                   ✅ PUSH (Glavni README)
├── PRESENTATION_GUIDE.md       ✅ PUSH (Vodič za odbranu)
├── requirements.txt            ✅ PUSH (Python dependencies)
├── .gitignore                  ✅ PUSH (Git config)
├── create_presentation.js      ✅ PUSH (Prezentacija kod)
└── Student_BI_Project_Complete.pptx  ✅ PUSH (Prezentacija)
```

### ❌ ŠTA NE PUSHUJ:

```
data/                          ❌ NE PUSH (veliki fajlovi, .gitignore ih ignoriše)
├── student_performance.csv
├── student_dw.db
└── predictions.csv

models/                        ❌ NE PUSH (veliki .pkl fajlovi)
├── logistic_regression_model.pkl
└── scaler.pkl
```

---

## 🚀 Korak-po-korak GitHub Upload

### **KORAK 1: Kreiraj GitHub Repository**

1. Idi na https://github.com
2. Klikni "New repository" (zeleno dugme)
3. Popuni:
   - **Repository name**: `student-bi-project`
   - **Description**: "Complete BI solution for student academic performance analysis with ML predictions"
   - **Public** ili **Private** (tvoj izbor)
   - ❌ **NE** checkuj "Initialize with README" (već imaš README.md)
4. Klikni "Create repository"

### **KORAK 2: Upload kroz GitHub Web Interface (NAJLAKŠE)**

**Opcija A: Drag & Drop (ako imaš manje od 100 fajlova)**

1. Na stranici repozitorijuma, klikni "uploading an existing file"
2. Selektuj SVE fajlove iz `/mnt/user-data/outputs/student_bi_project/` folder-a
3. **ISKLJUČI**: `data/` i `models/` foldere
4. Povuci fajlove na GitHub stranicu
5. Dodaj commit message: "Initial commit - Complete BI project"
6. Klikni "Commit changes"

**Opcija B: Kroz Git Command Line (ako znaš git)**

```bash
# U terminalu, idi u folder projekta
cd student_bi_project

# Inicijalizuj git
git init

# Dodaj sve fajlove (gitignore će automatski ignorisati data/ i models/)
git add .

# Komituj
git commit -m "Initial commit - Complete BI project"

# Dodaj remote (zamijeni USERNAME sa svojim username-om)
git remote add origin https://github.com/USERNAME/student-bi-project.git

# Push na GitHub
git push -u origin main
```

---

## 📝 Šta će ljudi vidjeti na GitHub-u?

Kada otvore tvoj projekat, vidjeće:

1. **README.md** sa:
   - Business problem
   - ROI kalkulacija
   - Star Schema diagram
   - Korelaciona analiza
   - ML model performanse
   - Vizualizacije

2. **Kod u `scripts/`**:
   - `generate_dataset.py` - kako generišeš podatke
   - `etl_pipeline.py` - kompletan ETL proces
   - `correlation_analysis.py` - statistička analiza
   - `ml_prediction_model.py` - ML model

3. **Vizualizacije** u `visualizations/`:
   - Korelaciona heatmap
   - Scatter plot attendance vs grade
   - Risk distribution
   - Confusion matrix
   - ROC kriva

4. **Dokumentacija**:
   - `PRESENTATION_GUIDE.md` - vodič za odbranu
   - `star_schema.mermaid` - database dijagram

---

## 🎓 GitHub kao Portfolio

Ovo je **idealan projekat za portfolio** jer pokazuje:

✅ **Data Engineering**: ETL pipeline, Data Warehouse, Star Schema
✅ **Data Analysis**: Statistika, korelacije, p-values
✅ **Machine Learning**: Logistic regression, feature engineering
✅ **Business Acumen**: ROI kalkulacija, actionable insights
✅ **Documentation**: Kompletan README, code comments
✅ **Visualizations**: Professional charts & graphs

---

## 📊 Kako testirati kod?

Ako neko hoće da pokrene tvoj projekat:

```bash
# Clone repository
git clone https://github.com/USERNAME/student-bi-project.git
cd student-bi-project

# Install dependencies
pip install -r requirements.txt

# Run pipeline
python scripts/generate_dataset.py
python scripts/etl_pipeline.py
python scripts/correlation_analysis.py
python scripts/ml_prediction_model.py
```

---

## 💡 BONUS: GitHub Repository Description

Kada kreiras repo, stavi ovu description:

```
📊 Complete Business Intelligence solution for student academic success analysis. 
Features: ETL pipeline, Data Warehouse (Star Schema), Statistical correlation 
analysis, ML predictions (Logistic Regression), and actionable insights. 
ROI: 8.3% in Year 1.

Tech: Python, pandas, SQLite, scikit-learn, matplotlib, seaborn
```

---

## 🏷️ GitHub Topics (Tags)

Dodaj ove topics na tvoj repo (settings → topics):

```
business-intelligence
data-warehouse
machine-learning
etl-pipeline
student-analytics
predictive-analytics
python
data-science
star-schema
logistic-regression
```

---

## ✅ Checklist prije push-a

- [ ] Provjeri da `.gitignore` ignoriše `data/` i `models/`
- [ ] Provjeri da sve vizualizacije postoje u `visualizations/`
- [ ] Provjeri da `README.md` izgleda dobro (preview na GitHub-u)
- [ ] Dodaj LICENSE file (MIT je ok)
- [ ] Provjeri da svi Python scripti rade bez greške
- [ ] Provjeri da `requirements.txt` ima sve dependencies

---

## 🤝 Dodavanje LICENSE (opcionalno ali preporučeno)

Kreiraj fajl `LICENSE` sa MIT licencom:

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

**GOTOVO! Tvoj projekat je spreman za GitHub! 🎉**
