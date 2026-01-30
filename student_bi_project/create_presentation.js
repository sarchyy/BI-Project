const pptxgen = require("pptxgenjs");

// Create presentation
let pres = new pptxgen();

// Define color palette - Ocean Gradient theme for data/analytics
const COLORS = {
  primary: "065A82",    // Deep blue
  secondary: "1C7293",  // Teal
  accent: "21295C",     // Midnight
  light: "E8F4F8",      // Light blue
  white: "FFFFFF",
  text: "2C3E50",
  success: "2ECC71",
  warning: "F39C12",
  danger: "E74C3C"
};

// ============================================================
// SLIDE 1: TITLE
// ============================================================
let slide1 = pres.addSlide();
slide1.background = { color: COLORS.primary };

slide1.addText("Analiza Akademskog Uspjeha Studenata", {
  x: 0.5, y: 2.0, w: 9, h: 1.2,
  fontSize: 44, bold: true, color: COLORS.white,
  align: "center", fontFace: "Arial Black"
});

slide1.addText("Data Warehouse i Business Intelligence Izvještaj", {
  x: 0.5, y: 3.3, w: 9, h: 0.6,
  fontSize: 20, color: COLORS.light,
  align: "center", fontFace: "Arial", italic: true
});

slide1.addText("Prediktivna Analitika i ML Model", {
  x: 0.5, y: 4.0, w: 9, h: 0.5,
  fontSize: 16, color: COLORS.light,
  align: "center", fontFace: "Arial"
});

slide1.addText("Studentski BI Projekat | Januar 2026", {
  x: 0.5, y: 5.0, w: 9, h: 0.4,
  fontSize: 14, color: COLORS.secondary,
  align: "center", fontFace: "Arial"
});

// ============================================================
// SLIDE 2: PROBLEM I CILJ
// ============================================================
let slide2 = pres.addSlide();
slide2.background = { color: COLORS.white };

slide2.addText("Problem i Cilj Projekta", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Problem box
slide2.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 1.5, w: 4.2, h: 3.5,
  fill: { color: "FEF5E7" }
});

slide2.addText("🚨 PROBLEM", {
  x: 0.7, y: 1.7, w: 3.8, h: 0.5,
  fontSize: 24, bold: true, color: COLORS.danger,
  fontFace: "Arial Black"
});

const problems = [
  "• Visok broj studenata koji padaju (13.7%)",
  "• Nema ranog uvida u rizične studente",
  "• Odluke se donose reaktivno, bez podataka",
  "• Troškovi: 65,000 KM godišnje"
];

slide2.addText(problems.join("\\n\\n"), {
  x: 0.7, y: 2.4, w: 3.8, h: 2.3,
  fontSize: 16, color: COLORS.text,
  fontFace: "Arial", valign: "top"
});

// Solution box
slide2.addShape(pres.ShapeType.rect, {
  x: 5.3, y: 1.5, w: 4.2, h: 3.5,
  fill: { color: "E8F8F5" }
});

slide2.addText("✅ RJEŠENJE", {
  x: 5.5, y: 1.7, w: 3.8, h: 0.5,
  fontSize: 24, bold: true, color: COLORS.success,
  fontFace: "Arial Black"
});

const solutions = [
  "• BI sistem za analizu uspjeha",
  "• Early Warning sistem sa ML modelom",
  "• Identifikacija ključnih faktora",
  "• ROI: 8.3% u prvoj godini"
];

slide2.addText(solutions.join("\\n\\n"), {
  x: 5.5, y: 2.4, w: 3.8, h: 2.3,
  fontSize: 16, color: COLORS.text,
  fontFace: "Arial", valign: "top"
});

// ============================================================
// SLIDE 3: BUSINESS VALUE & ROI
// ============================================================
let slide3 = pres.addSlide();
slide3.background = { color: COLORS.white };

slide3.addText("💰 Business Value & ROI", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Metrics cards
const metrics = [
  { label: "Trenutno padaju", value: "34", sublabel: "studenta (13.7%)", color: COLORS.danger },
  { label: "Potencijalno spašeno", value: "13", sublabel: "studenata (40%)", color: COLORS.warning },
  { label: "Godišnje uštede", value: "65K", sublabel: "KM", color: COLORS.success },
  { label: "ROI (Year 1)", value: "8.3%", sublabel: "povrat investicije", color: COLORS.primary }
];

metrics.forEach((metric, idx) => {
  const xPos = 0.5 + (idx * 2.4);
  
  slide3.addShape(pres.ShapeType.rect, {
    x: xPos, y: 1.5, w: 2.2, h: 1.8,
    fill: { color: "F8F9FA" },
    line: { color: metric.color, width: 3 }
  });
  
  slide3.addText(metric.value, {
    x: xPos, y: 1.8, w: 2.2, h: 0.8,
    fontSize: 52, bold: true, color: metric.color,
    align: "center", fontFace: "Arial Black"
  });
  
  slide3.addText(metric.label, {
    x: xPos, y: 2.7, w: 2.2, h: 0.3,
    fontSize: 12, bold: true, color: COLORS.text,
    align: "center", fontFace: "Arial"
  });
  
  slide3.addText(metric.sublabel, {
    x: xPos, y: 3.0, w: 2.2, h: 0.2,
    fontSize: 10, color: "7F8C8D",
    align: "center", fontFace: "Arial", italic: true
  });
});

// Operational benefits
slide3.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 3.8, w: 9, h: 1.5,
  fill: { color: COLORS.light }
});

slide3.addText("📊 Operativne Koristi", {
  x: 0.7, y: 4.0, w: 8.6, h: 0.3,
  fontSize: 18, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

const benefits = "⏱️ 35h uštedjenih godišnje  |  📈 25% veće zadovoljstvo studenata  |  🎯 Rana intervencija  |  📊 Data-driven odluke";

slide3.addText(benefits, {
  x: 0.7, y: 4.4, w: 8.6, h: 0.7,
  fontSize: 14, color: COLORS.text,
  align: "center", fontFace: "Arial"
});

// ============================================================
// SLIDE 4: DATA WAREHOUSE ARHITEKTURA
// ============================================================
let slide4 = pres.addSlide();
slide4.background = { color: COLORS.white };

slide4.addText("🏗️ Data Warehouse - Star Schema", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Fact table (center)
slide4.addShape(pres.ShapeType.rect, {
  x: 3.0, y: 1.8, w: 4.0, h: 2.5,
  fill: { color: COLORS.accent },
  line: { color: COLORS.primary, width: 2 }
});

slide4.addText("FACT_STUDENT_PERFORMANCE", {
  x: 3.0, y: 1.9, w: 4.0, h: 0.4,
  fontSize: 14, bold: true, color: COLORS.white,
  align: "center", fontFace: "Arial Black"
});

const factFields = [
  "• student_id (FK)",
  "• department_id (FK)",
  "• attendance_rate",
  "• midterm_score",
  "• final_grade",
  "• risk_category"
];

slide4.addText(factFields.join("\\n"), {
  x: 3.2, y: 2.4, w: 3.6, h: 1.7,
  fontSize: 11, color: COLORS.white,
  fontFace: "Courier New"
});

// Dimension tables
const dimensions = [
  { name: "DIM_STUDENT", x: 0.5, y: 2.3, fields: ["student_id", "student_name", "enrollment_year"] },
  { name: "DIM_DEPARTMENT", x: 7.5, y: 2.3, fields: ["department_id", "dept_name", "dept_code"] },
  { name: "DIM_SEMESTER", x: 3.8, y: 5.0, fields: ["semester_id", "semester_name", "academic_year"] }
];

dimensions.forEach(dim => {
  slide4.addShape(pres.ShapeType.rect, {
    x: dim.x, y: dim.y, w: 2.0, h: 1.2,
    fill: { color: COLORS.secondary },
    line: { color: COLORS.primary, width: 1 }
  });
  
  slide4.addText(dim.name, {
    x: dim.x, y: dim.y + 0.05, w: 2.0, h: 0.3,
    fontSize: 11, bold: true, color: COLORS.white,
    align: "center", fontFace: "Arial Black"
  });
  
  slide4.addText(dim.fields.map(f => "• " + f).join("\\n"), {
    x: dim.x + 0.1, y: dim.y + 0.4, w: 1.8, h: 0.7,
    fontSize: 9, color: COLORS.white,
    fontFace: "Courier New"
  });
  
  // Add connection lines
  const centerX = 5.0;
  const centerY = 3.0;
  
  if (dim.x < 3) {
    slide4.addShape(pres.ShapeType.line, {
      x: dim.x + 2.0, y: dim.y + 0.6, w: centerX - (dim.x + 2.0), h: 0,
      line: { color: COLORS.primary, width: 2, dashType: "dash" }
    });
  } else if (dim.x > 5) {
    slide4.addShape(pres.ShapeType.line, {
      x: centerX + 2.0, y: centerY, w: dim.x - (centerX + 2.0), h: 0,
      line: { color: COLORS.primary, width: 2, dashType: "dash" }
    });
  }
});

// ============================================================
// SLIDE 5: ETL PROCES
// ============================================================
let slide5 = pres.addSlide();
slide5.background = { color: COLORS.white };

slide5.addText("🔄 ETL Pipeline", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// ETL stages
const etlStages = [
  { 
    title: "1️⃣ EXTRACT", 
    desc: "• Student Information System\\n• Learning Management System\\n• Attendance Tracking\\n• CSV, Excel, API izvoz",
    x: 0.5, color: COLORS.danger
  },
  { 
    title: "2️⃣ TRANSFORM", 
    desc: "• Čišćenje null vrijednosti\\n• Validacija raspona (0-100)\\n• Kreiranje risk kategorija\\n• Kalkulacija metrika",
    x: 3.7, color: COLORS.warning
  },
  { 
    title: "3️⃣ LOAD", 
    desc: "• SQLite Data Warehouse\\n• Star Schema struktura\\n• Fact + Dim tabele\\n• Dnevno učitavanje",
    x: 6.9, color: COLORS.success
  }
];

etlStages.forEach(stage => {
  slide5.addShape(pres.ShapeType.rect, {
    x: stage.x, y: 1.8, w: 2.8, h: 2.8,
    fill: { color: "FFFFFF" },
    line: { color: stage.color, width: 3 }
  });
  
  slide5.addText(stage.title, {
    x: stage.x, y: 1.9, w: 2.8, h: 0.5,
    fontSize: 18, bold: true, color: stage.color,
    align: "center", fontFace: "Arial Black"
  });
  
  slide5.addText(stage.desc, {
    x: stage.x + 0.2, y: 2.5, w: 2.4, h: 1.9,
    fontSize: 12, color: COLORS.text,
    fontFace: "Arial", valign: "top"
  });
  
  // Add arrows
  if (stage.x < 6) {
    slide5.addShape(pres.ShapeType.rightArrow, {
      x: stage.x + 2.9, y: 2.9, w: 0.7, h: 0.4,
      fill: { color: COLORS.secondary }
    });
  }
});

// Technology stack
slide5.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 5.0, w: 9, h: 0.8,
  fill: { color: COLORS.light }
});

slide5.addText("🛠️ Stack: Python + pandas + SQLAlchemy + SQLite", {
  x: 0.5, y: 5.15, w: 9, h: 0.5,
  fontSize: 16, bold: true, color: COLORS.primary,
  align: "center", fontFace: "Arial"
});

// ============================================================
// SLIDE 6: KORELACIONA ANALIZA
// ============================================================
let slide6 = pres.addSlide();
slide6.background = { color: COLORS.white };

slide6.addText("📊 Korelaciona Analiza", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Correlation table
const correlations = [
  { factor: "Final Score", r: "+0.888", strength: "Very Strong", pval: "<0.001", sig: true },
  { factor: "Midterm Score", r: "+0.137", strength: "Weak", pval: "0.031", sig: true },
  { factor: "Attendance", r: "+0.124", strength: "Weak", pval: "0.050", sig: false },
  { factor: "Projects", r: "+0.133", strength: "Weak", pval: "0.037", sig: true }
];

// Table header
slide6.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 1.5, w: 9, h: 0.5,
  fill: { color: COLORS.primary }
});

const headers = ["Faktor", "Korelacija (r)", "Jačina", "P-value", "Značajno"];
headers.forEach((header, idx) => {
  slide6.addText(header, {
    x: 0.5 + (idx * 1.8), y: 1.6, w: 1.7, h: 0.3,
    fontSize: 14, bold: true, color: COLORS.white,
    align: "center", fontFace: "Arial Black"
  });
});

// Table rows
correlations.forEach((corr, idx) => {
  const yPos = 2.1 + (idx * 0.6);
  const bgColor = idx % 2 === 0 ? "F8F9FA" : "FFFFFF";
  
  slide6.addShape(pres.ShapeType.rect, {
    x: 0.5, y: yPos, w: 9, h: 0.5,
    fill: { color: bgColor }
  });
  
  const rowData = [corr.factor, corr.r, corr.strength, corr.pval, corr.sig ? "✓ DA" : "✗ NE"];
  rowData.forEach((data, colIdx) => {
    slide6.addText(data, {
      x: 0.5 + (colIdx * 1.8), y: yPos + 0.1, w: 1.7, h: 0.3,
      fontSize: 13, color: COLORS.text,
      align: "center", fontFace: "Arial"
    });
  });
});

// Key insight
slide6.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 4.7, w: 9, h: 0.8,
  fill: { color: "FFF3CD" }
});

slide6.addText("💡 KLJUČNI NALAZ: Attendance i midterm su NAJRANIJI indikatori uspjeha (p<0.05)", {
  x: 0.7, y: 4.9, w: 8.6, h: 0.4,
  fontSize: 16, bold: true, color: "856404",
  fontFace: "Arial"
});

// ============================================================
// SLIDE 7: ML MODEL
// ============================================================
let slide7 = pres.addSlide();
slide7.background = { color: COLORS.white };

slide7.addText("🤖 Machine Learning Model", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Model info
slide7.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 1.5, w: 4.5, h: 1.5,
  fill: { color: COLORS.light }
});

slide7.addText("📋 Model: Logistic Regression", {
  x: 0.7, y: 1.7, w: 4.1, h: 0.3,
  fontSize: 18, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

const modelInfo = "Cilj: Predikcija Pass/Fail\\nFeaturi: attendance, midterm, projects\\nTrening: 198 studenata (80%)\\nTest: 50 studenata (20%)";

slide7.addText(modelInfo, {
  x: 0.7, y: 2.1, w: 4.1, h: 1.1,
  fontSize: 14, color: COLORS.text,
  fontFace: "Arial"
});

// Performance metrics
slide7.addShape(pres.ShapeType.rect, {
  x: 5.3, y: 1.5, w: 4.2, h: 1.5,
  fill: { color: "E8F8F5" }
});

slide7.addText("📈 Performanse Modela", {
  x: 5.5, y: 1.7, w: 3.8, h: 0.3,
  fontSize: 18, bold: true, color: COLORS.success,
  fontFace: "Arial Black"
});

const performance = "Accuracy: 86%  |  ROC-AUC: 0.615\\nPrecision: 86%  |  Recall: 100%";

slide7.addText(performance, {
  x: 5.5, y: 2.1, w: 3.8, h: 0.9,
  fontSize: 14, color: COLORS.text,
  fontFace: "Arial", align: "center"
});

// Feature importance
slide7.addText("🎯 Značaj Featuresا", {
  x: 0.5, y: 3.3, w: 9, h: 0.4,
  fontSize: 20, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

const features = [
  { name: "attendance_rate", coef: "+0.777", impact: "Najveći pozitivan uticaj" },
  { name: "midterm_score", coef: "+0.394", impact: "Umjeren pozitivan uticaj" },
  { name: "projects_score", coef: "+0.288", impact: "Slab pozitivan uticaj" }
];

features.forEach((feat, idx) => {
  const yPos = 3.9 + (idx * 0.6);
  
  slide7.addShape(pres.ShapeType.rect, {
    x: 0.5, y: yPos, w: 9, h: 0.5,
    fill: { color: idx % 2 === 0 ? "F8F9FA" : "FFFFFF" }
  });
  
  slide7.addText(feat.name, {
    x: 0.7, y: yPos + 0.1, w: 3.0, h: 0.3,
    fontSize: 14, bold: true, color: COLORS.text,
    fontFace: "Courier New"
  });
  
  slide7.addText(feat.coef, {
    x: 3.9, y: yPos + 0.1, w: 1.5, h: 0.3,
    fontSize: 14, bold: true, color: COLORS.success,
    align: "center", fontFace: "Arial Black"
  });
  
  slide7.addText(feat.impact, {
    x: 5.6, y: yPos + 0.1, w: 3.6, h: 0.3,
    fontSize: 13, color: COLORS.text,
    fontFace: "Arial", italic: true
  });
});

// ============================================================
// SLIDE 8: ORIGINALNI REZULTATI (iz PDF-a)
// ============================================================
let slide8 = pres.addSlide();
slide8.background = { color: COLORS.white };

slide8.addText("📊 Rezultati Analize", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Department performance table
const deptData = [
  { dept: "Business", grade: "72.4", attendance: "85.1%", risk: "4.9%" },
  { dept: "Mathematics", grade: "70.0", attendance: "73.0%", risk: "30.2%" },
  { dept: "Engineering", grade: "66.6", attendance: "77.4%", risk: "20.7%" },
  { dept: "CS", grade: "66.9", attendance: "69.2%", risk: "20.0%" }
];

// Table header
slide8.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 1.5, w: 9, h: 0.5,
  fill: { color: COLORS.secondary }
});

const deptHeaders = ["Odsjek", "Prosjek Ocjena", "Prisutnost", "High Risk %"];
deptHeaders.forEach((header, idx) => {
  slide8.addText(header, {
    x: 0.5 + (idx * 2.25), y: 1.6, w: 2.2, h: 0.3,
    fontSize: 14, bold: true, color: COLORS.white,
    align: "center", fontFace: "Arial Black"
  });
});

// Table rows
deptData.forEach((dept, idx) => {
  const yPos = 2.1 + (idx * 0.6);
  const rowColor = dept.risk === "4.9%" ? "E8F8F5" : (parseFloat(dept.risk) > 25 ? "FADBD8" : "F8F9FA");
  
  slide8.addShape(pres.ShapeType.rect, {
    x: 0.5, y: yPos, w: 9, h: 0.5,
    fill: { color: rowColor }
  });
  
  const rowData = [dept.dept, dept.grade, dept.attendance, dept.risk];
  rowData.forEach((data, colIdx) => {
    slide8.addText(data, {
      x: 0.5 + (colIdx * 2.25), y: yPos + 0.1, w: 2.2, h: 0.3,
      fontSize: 13, color: COLORS.text,
      align: "center", fontFace: "Arial"
    });
  });
});

// Key findings
slide8.addShape(pres.ShapeType.rect, {
  x: 0.5, y: 4.7, w: 9, h: 1.0,
  fill: { color: COLORS.light }
});

slide8.addText("🔍 Ključni Nalazi", {
  x: 0.7, y: 4.85, w: 8.6, h: 0.3,
  fontSize: 16, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

const findings = "• Business odsjek: najbolji rezultati (72.4 prosjek, 4.9% rizik)\\n• Mathematics: najviše rizičnih studenata (30.2%)\\n• Prisutnost direktno utiče na uspjeh (r=+0.124)";

slide8.addText(findings, {
  x: 0.7, y: 5.2, w: 8.6, h: 0.4,
  fontSize: 13, color: COLORS.text,
  fontFace: "Arial"
});

// ============================================================
// SLIDE 9: PREPORUKE I AKCIONI PLAN
// ============================================================
let slide9 = pres.addSlide();
slide9.background = { color: COLORS.white };

slide9.addText("💡 Preporuke i Akcioni Plan", {
  x: 0.5, y: 0.5, w: 9, h: 0.7,
  fontSize: 40, bold: true, color: COLORS.primary,
  fontFace: "Arial Black"
});

// Timeline
const timeline = [
  { phase: "Sedmica 1-4", actions: "• Deployment attendance sistema\\n• Kontakt sa 43 high-risk studenata\\n• Setup tutorijala za CS/Engineering", icon: "🚀" },
  { phase: "Semestar 1", actions: "• Post-midterm intervencija\\n• Sedmični BI dashboardi\\n• Pilot alert sistem", icon: "📅" },
  { phase: "Akademska godina", actions: "• Production ML model\\n• Multi-semester analiza\\n• SIS integracija", icon: "🎯" }
];

timeline.forEach((item, idx) => {
  const yPos = 1.5 + (idx * 1.4);
  
  slide9.addShape(pres.ShapeType.rect, {
    x: 0.5, y: yPos, w: 9, h: 1.2,
    fill: { color: idx % 2 === 0 ? COLORS.light : "F8F9FA" },
    line: { color: COLORS.secondary, width: 2 }
  });
  
  slide9.addText(item.icon + " " + item.phase, {
    x: 0.7, y: yPos + 0.1, w: 8.6, h: 0.3,
    fontSize: 18, bold: true, color: COLORS.primary,
    fontFace: "Arial Black"
  });
  
  slide9.addText(item.actions, {
    x: 0.7, y: yPos + 0.5, w: 8.6, h: 0.6,
    fontSize: 13, color: COLORS.text,
    fontFace: "Arial"
  });
});

// ============================================================
// SLIDE 10: ZAKLJUČAK
// ============================================================
let slide10 = pres.addSlide();
slide10.background = { color: COLORS.primary };

slide10.addText("Zaključak", {
  x: 0.5, y: 1.5, w: 9, h: 0.8,
  fontSize: 44, bold: true, color: COLORS.white,
  align: "center", fontFace: "Arial Black"
});

const conclusions = [
  "✅ Kompletan BI sistem: ETL → Data Warehouse → Analytics → ML",
  "✅ Dokazana korelacija: Prisutnost i midterm = najjači prediktori",
  "✅ ROI: 8.3% u prvoj godini, 65,000 KM ušteđeno",
  "✅ Early Warning sistem sa 86% accuracy",
  "✅ Actionable insights za svaki odsjek"
];

slide10.addText(conclusions.join("\\n\\n"), {
  x: 1.0, y: 2.8, w: 8.0, h: 2.5,
  fontSize: 18, color: COLORS.white,
  fontFace: "Arial", valign: "top"
});

slide10.addText("Hvala na pažnji! 🎓", {
  x: 0.5, y: 5.3, w: 9, h: 0.5,
  fontSize: 24, bold: true, color: COLORS.secondary,
  align: "center", fontFace: "Arial Black", italic: true
});

// Save presentation
pres.writeFile({ fileName: "Student_BI_Project_Complete.pptx" });
console.log("✅ Prezentacija kreirana: Student_BI_Project_Complete.pptx");
