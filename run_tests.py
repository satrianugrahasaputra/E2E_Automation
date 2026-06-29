import os
import subprocess
import webbrowser
from dotenv import load_dotenv

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print("=" * 60)
    print("   AUTOMATION TESTING MANAGER - PYTHON + PLAYWRIGHT")
    print("=" * 60)
    
    # 1. Ask for URL
    current_url = os.getenv("BASE_URL", "http://localhost:8000")
    print(f"URL Default Saat Ini: {current_url}")
    new_url = input("Masukkan URL website baru (Tekan ENTER untuk pakai default): ").strip()
    
    if new_url:
        target_url = new_url
        # Update .env file
        with open(".env", "r") as f:
            lines = f.readlines()
        
        with open(".env", "w") as f:
            for line in lines:
                if line.startswith("BASE_URL="):
                    f.write(f"BASE_URL={target_url}\n")
                else:
                    f.write(line)
        print(f"🚀 URL berhasil diubah menjadi: {target_url}\n")
    else:
        target_url = current_url
        print(f" menggunakan URL default: {target_url}\n")

    # 2. Select Test Suite
    print("-" * 60)
    print("Pilih modul test yang ingin Anda jalankan:")
    print("1. Login Test (DDT - Mendukung SauceDemo, Jateng OTS, & Lokal)")
    print("2. Checkout E2E Test (Mendukung SauceDemo & Lokal)")
    print("3. Form Submission Test (Hanya website Lokal)")
    print("4. Register Account Test (Hanya website Lokal)")
    print("5. Jalankan SEMUA Test Case")
    print("-" * 60)
    
    choice = input("Pilih menu (1-5): ").strip()
    
    test_command = []
    
    if choice == "1":
        test_command = ["tests/test_login.py"]
    elif choice == "2":
        test_command = ["tests/test_checkout.py"]
    elif choice == "3":
        test_command = ["tests/test_form.py"]
    elif choice == "4":
        test_command = ["tests/test_register.py"]
    elif choice == "5":
        test_command = []  # Runs everything
    else:
        print("Pilihan tidak valid. Menjalankan semua test.")
        test_command = []

    # 3. Headed or Headless
    print("\nApakah Anda ingin melihat proses test secara visual (browser terbuka)?")
    print("1. Ya (Headed)")
    print("2. Tidak (Headless - Lebih Cepat)")
    headed_choice = input("Pilih (1-2): ").strip()
    
    # Use python interpreter in venv
    pytest_path = os.path.join("venv", "Scripts", "pytest.exe")
    if not os.path.exists(pytest_path):
        pytest_path = "pytest" # Fallback to global
        
    cmd = [pytest_path, "-v"]
    if test_command:
        cmd.extend(test_command)
        
    if headed_choice == "1":
        cmd.append("--headed")
        
    print(f"\n⚡ Menjalankan perintah: {' '.join(cmd)}")
    print("Mohon tunggu, robot sedang bekerja...\n")
    
    # Run the pytest command
    subprocess.run(cmd)
    
    # 4. Open report
    report_path = os.path.abspath("reports/report.html")
    if os.path.exists(report_path):
        print("\n🎉 Pengujian selesai! Membuka HTML Report di browser Anda...")
        webbrowser.open(f"file:///{report_path}")
    else:
        print("\n Gagal menemukan file laporan HTML.")

if __name__ == "__main__":
    load_dotenv()
    main()
