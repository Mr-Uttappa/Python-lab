
Here’s the **step‑by‑step checklist** you can note down to push your local repo to GitHub successfully:

---

## 📝 Steps to Push Local Repo to GitHub

### 1. Initialize Git (only once per project)
```bash
git init
```

### 2. Configure your Git identity (only once per machine)
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```
👉 Use the same email linked to your GitHub account.

### 3. Stage your files
```bash
git add .
```

### 4. Commit your changes
```bash
git commit -m "Initial commit"
```

### 5. Connect your local repo to GitHub
```bash
git remote add origin https://github.com/Uttappa-k/Python-lab.git
```

### 6. Push your code
```bash
git branch -M main
git push -u origin main
```

---

## 🔑 Authentication
- When prompted:
  - **Username** → `Uttappa-k`  
  - **Password** → paste your **Personal Access Token (PAT)**  
- Or use the **“Sign in with browser”** option in the GitHub pop‑up window.

---

## ⚡ Optional (to avoid re‑entering PAT every time)
```bash
git config --global credential.helper store
```
👉 After this, Git will remember your credentials.

---

✅ Once done, your code will appear in your GitHub repo.  

Would you like me to also give you the **SSH setup steps** so you can skip tokens and browser login entirely in the future? That’s the smoother long‑term workflow.