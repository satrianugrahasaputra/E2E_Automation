# Python + Playwright E2E Web Automation Testing Framework

Framework ini dibangun menggunakan **Python 3.11+** dan **Playwright** untuk melakukan pengujian Web End-to-End secara scalable, cepat, dan mudah dipelihara. Framework ini menggunakan metodologi **Page Object Model (POM)** dan mendukung **Data-Driven Testing (DDT)**.

## 🚀 Fitur Utama

- **Page Object Model (POM):** Pemisahan logic navigasi/aksi halaman dengan definisi locator secara modular.
- **Data-Driven Testing (DDT):** Menggunakan data eksternal bertipe JSON (untuk login) dan CSV via Pandas (untuk registrasi).
- **Auto Logging (Loguru):** Mencatat setiap aktivitas pengetesan ke terminal dan file arsip log secara terstruktur.
- **Auto Capture Failure Screenshot:** Otomatis menangkap screenshot halaman ketika ada test case yang gagal, lalu menyimpannya ke folder `screenshots/` dan mengintegrasikannya ke HTML report.
- **Video Recording:** Merekam seluruh sesi test case ke dalam folder `videos/`.
- **HTML Report (pytest-html):** Menghasilkan laporan pengetesan interaktif di `reports/report.html`.
- **Mock Local E-Commerce Site:** Aplikasi web premium bawaan lokal untuk testing yang stabil, cepat, dan anti-flaky di CI/CD.
- **CI/CD Integration:** Otomatis menjalankan automation testing menggunakan **GitHub Actions** setiap kali ada kode yang di-push atau Pull Request.

---

## 🛠️ Teknologi & Library

- **Core:** Python 3.11+, Pytest (Test Runner), Playwright (Web Automation)
- **Reporting:** pytest-html
- **Logging:** Loguru
- **Data DDT:** Pandas (membaca CSV), JSON
- **Data Dummy:** Faker (untuk data form dinamis)
- **Excel:** openpyxl (support load data dari spreadsheet)

---

## 📂 Struktur Project

```text
E2E-Automation/
├── .github/workflows/
│   └── playwright.yml   # Konfigurasi CI/CD GitHub Actions
├── data/
│   ├── login_data.json  # Data DDT untuk Login
│   ├── register_data.csv# Data DDT untuk Registrasi
│   └── sample_cv.txt    # File dummy untuk test upload
├── demo_site/           # Mock website lokal untuk pengujian
│   ├── login.html
│   ├── register.html
│   ├── form.html
│   ├── index.html
│   ├── cart.html
│   └── checkout.html
├── locators/            # Pemisah locator dari logic (POM)
│   ├── login_locators.py
│   ├── register_locators.py
│   ├── form_locators.py
│   └── checkout_locators.py
├── pages/               # Page Objects (Logic & Assertion)
│   ├── base_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── form_page.py
│   └── checkout_page.py
├── reports/             # Folder output HTML Report & Log File
├── screenshots/         # Folder output Screenshot saat test gagal
├── videos/              # Folder output Video rekaman testing
├── utils/
│   └── logger.py        # Pengaturan Loguru
├── conftest.py          # Fixtures global & hooks screenshot/video
├── pytest.ini           # Konfigurasi utama Pytest runner
├── requirements.txt     # Daftar dependensi Python
├── .env                 # Konfigurasi environment (url, credentials)
└── README.md
```

---

## 💻 Cara Install & setup

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/satrianugrahasaputra/E2E_Automation.git
   cd E2E_Automation
   ```

2. **Buat dan aktifkan Virtual Environment:**
   - **Windows:**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependensi & browser binaries:**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Konfigurasi Environment:**
   Salin `.env.example` menjadi `.env` lalu sesuaikan isinya jika dibutuhkan.
   ```bash
   cp .env.example .env
   ```

---

## 🎯 Cara Menjalankan Test

1. **Jalankan seluruh test case (Headless mode):**
   ```bash
   pytest
   ```

2. **Jalankan test case tertentu:**
   ```bash
   pytest tests/test_login.py
   ```

3. **Jalankan test case dengan browser terlihat (Headed mode):**
   ```bash
   pytest --headed
   ```

---

## 📊 Contoh Report, Screenshot & Video

Setelah menjalankan pengujian:
- **HTML Report** dapat dilihat di: [reports/report.html](file:///d:/E2E-Automation/reports/report.html)
- **Video Recording** disimpan di folder: `videos/`
- **Screenshots (pada kegagalan)** disimpan di folder: `screenshots/` dan otomatis tersemat di HTML Report.