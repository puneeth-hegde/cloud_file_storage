# ☁️ Cloud File Storage System (AWS S3 + Python + Streamlit)

A secure **cloud-based file storage system** built with **AWS S3, Python (boto3), SQLite authentication, and Streamlit UI**.  
This project allows users to **sign up, log in, upload, download, view, and delete files securely** using AWS S3, with real-time logs and `.env` for key security.

---

## 🔑 **Key Features**
✅ User Authentication (Signup/Login via SQLite)  
✅ Secure AWS S3 Storage (Private Bucket)  
✅ File Upload, Download, View, Delete Options  
✅ Logs all file operations for auditing  
✅ Secure `.env` file for AWS keys (secure) 
✅ Streamlit UI with multi-page navigation (Login → Dashboard)  

---

## 🛠️ **Tech Stack**
- **Frontend/UI**: Streamlit
- **Backend**: Python
- **Authentication**: SQLite
- **Cloud Storage**: AWS S3 (Boto3 SDK)
- **Key Management**: `.env` with `python-dotenv`

---

## 🚀 **Project Setup Guide**

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/<your-username>/cloud-file-storage.git
cd cloud-file-storage
```

---

### 2️⃣ **Create a Virtual Environment**
```bash
python -m venv .venv
.\.venv\Scripts\activate    # Windows
source .venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

Dependencies include:
- streamlit  
- boto3  
- sqlite3 (built-in)  
- python-dotenv  

---

## 🔧 **AWS Setup**

### Step 1: Create AWS Account (Free Tier)
- Sign up at [https://aws.amazon.com/free](https://aws.amazon.com/free).
- Log in to **AWS Management Console**.

### Step 2: Create S3 Bucket
1. Go to **AWS Console → S3 → Create Bucket**  
2. Bucket Name: `cloud-file-storage-<your-name>`  
3. Region: Choose nearest (e.g., `ap-south-1` for India)  
4. Uncheck "Block all public access" (if you want testing access)  
5. Keep private (recommended for production).  

### Step 3: Create IAM User & Keys
1. Go to **AWS → IAM → Users → Add User**
2. Username: `cloud-storage-user`
3. **Access type:** Programmatic access
4. Permissions: Attach **`AmazonS3FullAccess`**
5. Finish & Download **Access Key ID** and **Secret Key**.

---

## 🔒 **Secure AWS Keys with `.env`**
Create a `.env` file in your project folder:
```
AWS_ACCESS_KEY=your-access-key
AWS_SECRET_KEY=your-secret-key
BUCKET_NAME=cloud-file-storage- 'yourname'
```

**Important:** Add `.env` to `.gitignore` (already included).  
✅ This prevents accidental key leaks to GitHub.

---

## ▶️ **How to Run**
Run the app locally:
```bash
streamlit run app.py
```
- Open in browser: [http://localhost:8501](http://localhost:8501)  
- Login/Signup → Dashboard → Upload/Download/Delete files.

---

## 📂 **Project Structure**
```
cloud_file_storage/
│
├── app.py            # Main Streamlit app (login + dashboard)
├── app1.py           # Demo UI app (no AWS)
├── auth.py           # Authentication (SQLite DB)
├── s3_utils.py       # AWS S3 upload/download logic
├── users.db          # Auto-created SQLite DB (ignored in git)
├── .env              # AWS credentials (ignored in git)
├── .gitignore        # Ignores .env, venv, DB, logs
├── requirements.txt   # Dependencies
└── README.md         # Documentation
```

---

## 🖼️ **Screenshots 
1. **Login Page**  
2. **Signup Page**  
3. **Dashboard (Upload/Download)**  
![Login Page](https://raw.githubusercontent.com/puneeth-hegde/cloud-file-storage/image.png)
![Dashboard](https://raw.githubusercontent.com/puneeth-hegde/cloud-file-storage/image1.png)
---

## 🔍 **How It Works**
1. User **signs up** (stored in `users.db`).
2. On login → Dashboard appears.
3. Upload file → Sent to AWS S3 bucket.
4. Download/Delete/View operations fetch directly from S3.
5. All operations logged in `logs.txt`.


---

## 📌 **Key Learnings**
- Cloud storage integration using **AWS S3 + Boto3**
- Secure credential handling with `.env`
- Building full-stack Streamlit apps
- Authentication using **SQLite**

---

## 🔮 **Future Enhancements**
- File versioning in S3
- Role-based access (admin/user)
- Deploy app online (Streamlit Cloud/EC2)
- Add email alerts on uploads

---

## 🏷️ **License**
This project is licensed under MIT License.

---

## 👤 **Author**
**Puneeth Hegde**  
Email: puneethgshegde@gmail.com  
GitHub: [puneeth-hegde](https://github.com/puneeth-hegde)

---
