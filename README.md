# Horus - User Management System

Aplikasi full-stack untuk manajemen user dengan backend Flask dan frontend Vue.js. Sistem ini mencakup fitur pendaftaran, login, dan CRUD operations untuk data pengguna dengan autentikasi JWT.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Folder](#struktur-folder)
- [Prasyarat Instalasi](#prasyarat-instalasi)
- [Panduan Instalasi Lengkap](#panduan-instalasi-lengkap)
- [Menjalankan Project](#menjalankan-project)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

---

## ✨ Fitur Utama

- **User Registration**: Pendaftaran user baru dengan validasi data
- **User Login**: Login dengan autentikasi JWT token
- **Get Users**: Mengambil daftar semua user (memerlukan autentikasi)
- **Update User**: Mengupdate data user (memerlukan autentikasi)
- **Delete User**: Menghapus data user (memerlukan autentikasi)
- **CORS Support**: Dukungan Cross-Origin Resource Sharing untuk frontend
- **Database Migration**: Menggunakan Alembic untuk version control database

---

## 🛠️ Teknologi yang Digunakan

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - ORM untuk database
- **Flask-Migrate** - Database migration tool
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - CORS support
- **PostgreSQL** - Database (dengan pgAdmin4)
- **python-dotenv** - Environment variables

### Frontend
- **Node.js 16+**
- **Vue 3** - JavaScript framework
- **Vite** - Build tool dan dev server
- **Vue Router 4** - Client-side routing
- **Axios** - HTTP client
- **ES6+** - Modern JavaScript

---

## 📁 Struktur Folder

```
horus-Samuel-exam/
├── README.md                      # File dokumentasi (file ini)
│
├── backend/                       # Backend Flask
│   ├── requirements.txt          # Python dependencies
│   ├── run.py                    # Entry point aplikasi Flask
│   ├── .env                      # Environment variables (create yourself - NOT in repo)
│   │
│   └── app/
│       ├── __init__.py           # App factory
│       ├── config.py             # Konfigurasi aplikasi
│       ├── extensions.py         # Inisialisasi extensions (db, migrate, jwt, cors)
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py           # Model User (SQLAlchemy)
│       │
│       ├── routes/
│       │   ├── __init__.py
│       │   └── users.py          # API routes untuk user
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   └── user_service.py   # Business logic untuk user
│       │
│       └── utils/
│           ├── __init__.py
│           └── validators.py     # Validasi input data
│
│   └── migrations/               # Database migrations (di-generate oleh Alembic)
│       ├── alembic.ini
│       ├── env.py
│       ├── script.py.mako
│       └── versions/
│           └── 430d7c59069c_init_db_users.py
│
└── frontend/                     # Frontend Vue.js
    ├── package.json             # Node dependencies
    ├── vite.config.js           # Vite configuration
    ├── index.html               # Entry HTML
    │
    ├── public/                  # Static files
    │
    └── src/
        ├── main.js              # Entry point Vue
        ├── App.vue              # Root component
        │
        ├── components/          # Reusable components
        │   ├── SearchBar.vue    # Search component
        │   └── UserTable.vue    # User table component
        │
        ├── views/               # Page components
        │   ├── Login.vue        # Login page
        │   ├── Register.vue     # Register page
        │   ├── Dashboard.vue    # Main dashboard
        │   └── UpdateUser.vue   # Update user page
        │
        ├── router/
        │   └── index.js         # Vue Router configuration
        │
        ├── services/
        │   └── api.js           # Axios API client
        │
        └── store/
            └── auth.js          # Vuex/Pinia auth store
```

---

## 📦 Prasyarat Instalasi

Sebelum memulai, pastikan system anda memiliki:

### Untuk Backend
- **Python 3.8 atau lebih tinggi**
  - Cek versi: `python --version`
  - Download: https://www.python.org/downloads/

- **pip** (Python package manager, biasanya sudah include)
  - Cek: `pip --version`

- **Virtual Environment** (optional tapi recommended)
  - Module `venv` biasanya sudah include dengan Python

### Untuk Frontend
- **Node.js 16 atau lebih tinggi**
  - Cek versi: `node --version`
  - Download: https://nodejs.org/

- **npm** (Node package manager, biasanya sudah include)
  - Cek: `npm --version`

### Untuk Database
- **PostgreSQL 12+** (menggunakan pgAdmin4 untuk management)
  - Download: https://www.postgresql.org/download/
  - pgAdmin4: https://www.pgadmin.org/download/

---

## 🚀 Panduan Instalasi Lengkap

### Step 1: Clone atau Download Project

```bash
# Jika menggunakan git
git clone <repository-url>
cd horus-Samuel-exam

# Atau jika sudah di-download
cd horus-Samuel-exam
```

### Step 2: Instalasi Backend

#### 2a. Buat Virtual Environment (Recommended)

```bash
# Navigate ke folder backend
cd backend

# Buat virtual environment
# Windows:
python -m venv venv

# Linux/Mac:
python3 -m venv venv
```

#### 2b. Aktivasi Virtual Environment

```bash
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

Setelah aktivasi, terminal anda akan menampilkan `(venv)` di awal baris.

#### 2c. Instalasi Dependencies Backend

```bash
# Install semua dependencies dari requirements.txt
pip install -r requirements.txt
```

#### 2d. Setup Environment Variables

Buat file `.env` di folder `backend/` dengan konfigurasi yang diperlukan:
- Database connection string untuk PostgreSQL
- Secret keys untuk JWT
- Flask environment settings

⚠️ **PENTING**: File `.env` harus dibuat secara lokal dan TIDAK di-commit ke repository untuk keamanan.

#### 2e. Setup Database

```bash
# Pastikan database PostgreSQL sudah dibuat di pgAdmin4 atau command line

# Jalankan migrasi database
flask db upgrade

# Atau jika ingin menginisialisasi dari awal:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Step 3: Instalasi Frontend

Buka terminal baru (tab baru), navigate ke folder frontend, lalu:

```bash
# Navigate ke folder frontend
cd frontend

# Instalasi dependencies
npm install
```

---

## ▶️ Menjalankan Project

### Prerequisites
- PostgreSQL service harus sudah berjalan
- Database sudah dibuat dan `.env` sudah dikonfigurasi

### Menjalankan Backend

```bash
# Navigate ke folder backend (jika belum)
cd backend

# Aktivasi virtual environment
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Jalankan Flask development server
python run.py

# Output yang diharapkan:
# WARNING in app.run_with_reloader
#  * Serving Flask app 'app'
#  * Debug mode: on
#  * Running on http://127.0.0.1:5000

# Backend siap di http://localhost:5000
```

### Menjalankan Frontend

Buka terminal baru (jangan tutup terminal backend):

```bash
# Navigate ke folder frontend
cd frontend

# Jalankan Vite development server
npm run dev

# Output yang diharapkan:
#   VITE v5.2.8  ready in 123 ms
#   
#   ➜  Local:   http://localhost:5173/
#   ➜  Press h to show help

# Frontend siap di http://localhost:3000 atau http://localhost:5173
```

### Akses Aplikasi

1. Buka browser dan akses: **http://localhost:3000** (atau port yang ditampilkan di terminal frontend)
2. Backend API tersedia di: **http://localhost:5000**

---

## 🔌 API Endpoints

Semua endpoint dilayani di `http://localhost:5000/users`

### 1. Register User

```
POST /users/register
Content-Type: application/json

Request Body:
{
  "username": "<username>",
  "email": "<email@example.com>",
  "password": "<secure-password>",
  "nama": "<full-name>"
}

Response (201 Created):
{
  "message": "User berhasil didaftarkan",
  "user": {
    "id": 1,
    "username": "<username>",
    "email": "<email@example.com>",
    "nama": "<full-name>"
  }
}
```

### 2. Login User

```
POST /users/login
Content-Type: application/json

Request Body:
{
  "username": "<username>",
  "password": "<secure-password>"
}

Response (200 OK):
{
  "message": "Login berhasil",
  "access_token": "<jwt-token-received>",
  "user": {
    "id": 1,
    "username": "<username>",
    "email": "<email@example.com>"
  }
}
```

### 3. Get All Users (Protected)

```
GET /users
Authorization: Bearer <access_token>

Response (200 OK):
{
  "users": [
    {
      "id": 1,
      "username": "<username>",
      "email": "<email@example.com>",
      "nama": "<full-name>"
    }
  ]
}
```

### 4. Update User (Protected)

```
PUT /users/<id>
Authorization: Bearer <access_token>
Content-Type: application/json

Request Body:
{
  "nama": "<updated-full-name>",
  "email": "<updated-email@example.com>"
}

Response (200 OK):
{
  "message": "User berhasil diupdate",
  "user": {
    "id": 1,
    "username": "<username>",
    "email": "<updated-email@example.com>",
    "nama": "<updated-full-name>"
  }
}
```

### 5. Delete User (Protected)

```
DELETE /users/<id>
Authorization: Bearer <access_token>

Response (200 OK):
{
  "message": "User berhasil dihapus"
}
```

---

## 🧪 Testing dengan Postman/REST Client

### Langkah-langkah Testing:

1. **Registrasi User Baru**
   - Method: POST
   - URL: http://localhost:5000/users/register
   - Gunakan contoh request body dari API Endpoints section di atas

2. **Login**
   - Method: POST
   - URL: http://localhost:5000/users/login
   - Catat `access_token` yang diterima untuk digunakan di endpoint yang dilindungi

3. **Get Users**
   - Method: GET
   - URL: http://localhost:5000/users
   - Headers: `Authorization: Bearer <token_dari_login>`

4. **Update User**
   - Method: PUT
   - URL: http://localhost:5000/users/1
   - Headers: `Authorization: Bearer <token>`
   - Gunakan request body contoh dari API Endpoints section

5. **Delete User**
   - Method: DELETE
   - URL: http://localhost:5000/users/1
   - Headers: `Authorization: Bearer <token>`

---

## 📋 Build untuk Production

### Frontend Build

```bash
# Navigate ke folder frontend
cd frontend

# Build untuk production
npm run build

# Output akan berada di folder dist/
# File ini bisa di-serve oleh backend atau web server lain

# Preview build results (optional)
npm run preview
```

### Backend Preparation

```bash
# Update requirements.txt dengan dependencies yang jelas
pip freeze > requirements.txt

# Atau manual setup production environment variables
# Edit file .env dengan production configuration
```

---

## 🔧 Troubleshooting

### Backend Issues

#### Error: "ModuleNotFoundError: No module named 'flask'"
```bash
# Solusi: Pastikan virtual environment sudah aktif
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Lalu install requirements:
pip install -r requirements.txt
```

#### Error: "CORS" atau error 400 dari frontend
```bash
# Solusi: Pastikan Flask-CORS sudah diinstall dan dikonfigurasi
pip install Flask-CORS

# Di app/__init__.py sudah ada:
# cors.init_app(app)
```

#### Error Database: "Connection refused" atau "FATAL: Ident authentication failed"
```bash
# Solusi: Periksa bahwa:
# 1. PostgreSQL service sudah berjalan
# 2. Database sudah dibuat
# 3. .env memiliki DATABASE_URL yang benar

# Windows: Buka Services dan pastikan PostgreSQL berjalan
# Linux/Mac: sudo systemctl status postgresql
```

#### Port 5000 sudah digunakan
```bash
# Ketemukan process yang menggunakan port 5000
# Windows:
netstat -ano | findstr :5000

# Linux/Mac:
lsof -i :5000

# Atau ubah port di run.py:
# app.run(debug=True, port=5001)  # Ubah port ke 5001
```

### Frontend Issues

#### Error: "npm: command not found"
```bash
# Solusi: Install Node.js dari https://nodejs.org/
# Verify instalasi:
node --version
npm --version
```

#### Error: "port 3000 already in use"
```bash
# Solusi: Ubah port di package.json atau vite.config.js
# Atau jalankan di port lain:
npm run dev -- --port 3001
```

#### CORS Error: "Access to XMLHttpRequest blocked"
```bash
# Solusi: Pastikan backend punya CORS headers yang benar
# Cek api.js di frontend:
const api = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json'
  }
})
```

#### Components tidak tampil atau error "Cannot find module"
```bash
# Solusi: Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### General Issues

#### Database migration error
```bash
# Solusi: Reset database dan migrasi ulang
cd backend

# Jalankan upgrade migrasi
flask db upgrade

# Jika masih error, cek connection string di .env
```

#### Port tidak bisa diakses dari machine lain
```bash
# Di Windows/Linux, ubah HOST di run.py:
# app.run(debug=True, port=5000, host='0.0.0.0')

# Lalu akses dari machine lain dengan:
# http://<your-machine-ip>:5000
```

---

## 📝 Catatan Penting

1. **Environment Variables**: File `.env` HARUS dibuat secara lokal. Jangan pernah push ke repository.

2. **Database**: Gunakan PostgreSQL untuk production. Pastikan service sudah berjalan sebelum menjalankan aplikasi.

3. **CORS Configuration**: Backend sudah dikonfigurasi untuk menerima request dari frontend. Sesuaikan jika diperlukan perubahan.

4. **Virtual Environment**: Selalu aktivasi virtual environment sebelum menjalankan backend untuk menghindari conflict dependencies.

5. **Dependencies**: Update requirements.txt setelah menambah package baru dengan: `pip freeze > requirements.txt`

---

## 🤝 Support

Jika ada pertanyaan atau issue, silakan:
- Cek bagian Troubleshooting di atas
- Review error message dengan teliti
- Periksa kembali langkah instalasi
- Pastikan semua dependencies sudah terinstall
- Verifikasi database sudah berjalan dan dikonfigurasi dengan benar

---

## 📄 License

Proyek ini dibuat untuk keperluan pembelajaran dan testing.

---

**Last Updated**: April 2026
