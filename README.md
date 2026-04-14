# Horus - User Management System

Aplikasi full-stack untuk manajemen user dengan backend Flask dan frontend Vue.js. Sistem ini mencakup fitur pendaftaran, login, dan CRUD operations untuk data pengguna dengan autentikasi JWT.

## 📋 Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Struktur Folder](#struktur-folder)
- [Prasyarat Instalasi](#prasyarat-instalasi)
- [Panduan Instalasi Lengkap](#panduan-instalasi-lengkap)
- [Konfigurasi Environment](#konfigurasi-environment)
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
- **SQLite/PostgreSQL** - Database
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
│   ├── .env                      # Environment variables (buat sendiri)
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
- **SQLite** (default, sudah include dengan Python)
- Atau **PostgreSQL** (optional, jika ingin menggunakan PostgreSQL)

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

# Atau install satu per satu (jika ingin tahu apa yang di-install):
pip install Flask==2.3.0
pip install Flask-SQLAlchemy==3.0.0
pip install Flask-Migrate==4.0.0
pip install Flask-JWT-Extended==4.4.0
pip install Flask-CORS==4.0.0
pip install python-dotenv==1.0.0
```

**Dependencies yang diperlukan:**
- Flask - Web framework
- Flask-SQLAlchemy - Database ORM
- Flask-Migrate - Database migrations
- Flask-JWT-Extended - JWT authentication
- Flask-CORS - CORS handling
- python-dotenv - Environment variables

#### 2d. Setup Database

```bash
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

# Atau lebih detail:
npm install vue@3.4.21
npm install vue-router@4.3.0
npm install axios@1.6.8
npm install vite@5.2.8 --save-dev
npm install @vitejs/plugin-vue@5.0.4 --save-dev
```

---

## ⚙️ Konfigurasi Environment

### Backend Configuration

Buat file `.env` di folder `backend/` dengan konten berikut:

```bash
# Backend .env file
# backend/.env

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Database Configuration
# Untuk SQLite (default):
DATABASE_URL=sqlite:///app.db

# Atau untuk PostgreSQL:
# DATABASE_URL=postgresql://username:password@localhost:5432/horus_db

# JWT Configuration
SECRET_KEY=your-secret-key-here-change-this-in-production
JWT_SECRET_KEY=your-jwt-secret-key-here-change-this-in-production

# Server Configuration
SERVER_PORT=5000
SERVER_HOST=0.0.0.0
```

### Frontend Configuration (Optional)

Sesuaikan `vite.config.js` jika diperlukan proxy API:

```javascript
// frontend/vite.config.js
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      }
    }
  }
})
```

---

## ▶️ Menjalankan Project

### Menjalankan Backend

```bash
# Navigate ke folder backend (jika belum)
cd backend

# Pastikan virtual environment sudah aktif (lihat Step 2b)
# Jika belum, jalankan:
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
  "username": "samueldevops",
  "email": "samuel@example.com",
  "password": "password123",
  "nama": "Samuel"
}

Response (201 Created):
{
  "message": "User berhasil didaftarkan",
  "user": {
    "id": 1,
    "username": "samueldevops",
    "email": "samuel@example.com",
    "nama": "Samuel"
  }
}
```

### 2. Login User

```
POST /users/login
Content-Type: application/json

Request Body:
{
  "username": "samueldevops",
  "password": "password123"
}

Response (200 OK):
{
  "message": "Login berhasil",
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "samueldevops",
    "email": "samuel@example.com"
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
      "username": "samueldevops",
      "email": "samuel@example.com",
      "nama": "Samuel"
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
  "nama": "Samuel Devops Updated",
  "email": "samuel.new@example.com"
}

Response (200 OK):
{
  "message": "User berhasil diupdate",
  "user": {
    "id": 1,
    "username": "samueldevops",
    "email": "samuel.new@example.com",
    "nama": "Samuel Devops Updated"
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
   - Body (JSON):
     ```json
     {
       "username": "testuser",
       "email": "test@example.com",
       "password": "testpass123",
       "nama": "Test User"
     }
     ```

2. **Login**
   - Method: POST
   - URL: http://localhost:5000/users/login
   - Body (JSON):
     ```json
     {
       "username": "testuser",
       "password": "testpass123"
     }
     ```
   - Copy `access_token` dari response

3. **Get Users**
   - Method: GET
   - URL: http://localhost:5000/users
   - Headers: `Authorization: Bearer <paste_token_dari_step_2>`

4. **Update User**
   - Method: PUT
   - URL: http://localhost:5000/users/1
   - Headers: `Authorization: Bearer <token>`
   - Body (JSON):
     ```json
     {
       "nama": "Test User Updated",
       "email": "test.updated@example.com"
     }
     ```

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

#### Error Database: "sqlite3.OperationalError: no such table"
```bash
# Solusi: Jalankan migrasi database
cd backend
flask db upgrade

# Atau buat ulang:
rm app.db  # Hapus database lama
flask db upgrade
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

#### Ingin reset database
```bash
cd backend

# Hapus file database
rm app.db

# Hapus migrasi (optional)
rm -rf migrations/versions/*

# Buat migrasi baru
flask db migrate -m "Initial migration"
flask db upgrade
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

1. **Development vs Production**: Konfigurasi di `.env` adalah untuk development. Untuk production, gunakan environment variables yang lebih aman.

2. **Secret Key**: Ubah `SECRET_KEY` dan `JWT_SECRET_KEY` di `.env` dengan string random yang panjang untuk production.

3. **Database**: Default menggunakan SQLite. Untuk production, disarankan menggunakan PostgreSQL.

4. **CORS**: Backend sudah dikonfigurasi untuk menerima request dari frontend dengan CORS yang tepat.

5. **JWT Token**: Token JWT valid selama waktu tertentu. Implementasi refresh token bisa ditambahkan untuk security lebih baik.

---

## 🤝 Support

Jika ada pertanyaan atau issue, silakan:
- Cek bagian Troubleshooting di atas
- Review error message dengan teliti
- Periksa kembali langkah instalasi
- Pastikan semua dependencies sudah terinstall

---

## 📄 License

Proyek ini dibuat untuk keperluan pembelajaran dan testing.

---

**Last Updated**: April 2026
