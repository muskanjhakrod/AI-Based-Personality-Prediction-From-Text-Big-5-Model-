# 🧠 AI-Based Personality Prediction From Text (Big-5 Model)

This project predicts the **Big Five Personality Traits** —
**Agreeableness, Openness, Conscientiousness, Extraversion, Neuroticism**
— from user text using a **fine-tuned BERT model**.

The system takes any writing sample (social media posts, diary entries, messages, etc.) and produces:

✔ Trait Scores (0–100)
✔ “Low / Medium / High” category for each trait
✔ A clean radar chart visualization
✔ A short AI-generated personality summary
✔ A modern Flask + Bootstrap web UI

---

# ✨ Features

### 🔍 **AI Model**

* Fine-tuned `bert-base-uncased`
* Trained on Big-5 Personality dataset
  (`Fatima0923/Automated-Personality-Prediction`)
* Multi-output regression (predicts all 5 traits at once)
* Normalized labels during training → denormalized to 0–100 for UI
* Custom trait interpretation (Low/Medium/High)
* Natural-language summary of personality

### 🎨 **Web UI**

* Flask backend
* Bootstrap UI with custom styling
* Chart.js radar graph for visualization
* Mobile-responsive layout
* Interactive results section

### 🧪 **Live Prediction**

Just type your text → get a full psychological profile.

---

# 🖼 Demo Screenshots

```
screenshots/
    home.png
    result.png
```

### 🏠 Home Screen

![Home screen](screenshots/home.png)

### 📊 Prediction Result

![Prediction](screenshots/result.png)

---

# 📁 Project Structure

```
PersonalityPrediction/
│
├── app.py                     # Flask web server
├── model_utils.py             # BERT model loading + prediction logic
├── requirements.txt           # Dependences for deployment
├── templates/
│     └── index.html           # UI frontend
│
├── screenshots/               # UI images for README
│     ├── home.png
│     └── result.png
│
└── big5-bert-normalized-model/   # (Not included in repo)
```

---

# ⚠️ Model Not Included in GitHub Repo

The fine-tuned BERT model is **too large for GitHub** (>100 MB).
You must download it separately.

### 👉 Download Model Here

**[Click to Download the Model ZIP](https://drive.google.com/drive/folders/1fSCjwg_BRa6LqA5G_dR2NXuZNHJM6Ik4?usp=sharing)**

After downloading:

1. Extract the ZIP
2. Place the folder exactly as:

```
project/
  app.py
  model_utils.py
  big5-bert-normalized-model/
  templates/
```

---

# ▶️ How to Run the Project Locally

### 1️⃣ Clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2️⃣ Create a virtual environment (Python 3.10 recommended)

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download & place the model

Download ZIP → extract → place:

```
big5-bert-normalized-model/
```

next to `app.py`.

### 5️⃣ Start the app

```bash
python app.py
```

### 6️⃣ Open in browser

Visit:

**[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

# 🧠 How the Personality Prediction Works

### 🪄 Step 1 — Text Input

The user enters:

* A message
* Social media post
* Paragraph about themselves
* Multiple sentences

### 🪄 Step 2 — BERT Encoding

Text is tokenized using **AutoTokenizer** from Hugging Face.

### 🪄 Step 3 — Model Prediction

A fine-tuned BERT model outputs **5 continuous values (0–1)**.

### 🪄 Step 4 — Denormalization

Each trait is mapped back to the dataset’s actual scale (0–100 approx).

### 🪄 Step 5 — Levels + Summary

* Scores converted to **Low / Medium / High**
* Generates a personalized description like:

  > “You seem curious and imaginative with a tendency toward emotional sensitivity…”

### 🪄 Step 6 — UI Visualization

Results are shown as:

* A trait list
* A colored level badge
* A radar chart
* A personality summary paragraph

---

# 📊 Big-5 Personality Traits Explained

| Trait                 | Meaning                                  |
| --------------------- | ---------------------------------------- |
| **Openness**          | Imagination, creativity, curiosity       |
| **Conscientiousness** | Organization, responsibility, discipline |
| **Extraversion**      | Sociability, energy, enthusiasm          |
| **Agreeableness**     | Kindness, cooperation, warmth            |
| **Neuroticism**       | Emotional sensitivity, stress response   |

---

# 🛠 Technologies Used

* **Python 3.10**
* **PyTorch**
* **Hugging Face Transformers**
* **Flask**
* **Bootstrap 5**
* **Chart.js**
* **HTML/CSS/Jinja2**

---

# 🌟 Why This Project Is Useful

* Demonstrates NLP + ML + UI integration
* Uses real psychological frameworks
* Great for college projects / viva
* Resume-ready project
* Shows ML deployment + backend/frontend skills
* Educates how language relates to personality
