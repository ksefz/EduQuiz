import json
from quiz_saintek import main as quiz_menu  # ✅ pastikan file kamu bernama quiz_saintek.py

# ==========================
# FUNGSI LOGIN / REGISTER
# ==========================

def load_users():
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)

def register():
    print("\n=== REGISTER ===")
    users = load_users()
    username = input("Masukkan username baru: ")
    if any(u["username"] == username for u in users):
        print("❌ Username sudah digunakan.")
        return None
    password = input("Masukkan password: ")
    users.append({"username": username, "password": password})
    save_users(users)
    print("✅ Akun berhasil dibuat!")
    return username

def login():
    print("\n=== LOGIN ===")
    users = load_users()
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for u in users:
        if u["username"] == username and u["password"] == password:
            print(f"✅ Login berhasil! Selamat datang, {username} 👋")
            return username
    print("❌ Username atau password salah.")
    return None

# ==========================
# MENU UTAMA
# ==========================

def menu_utama(username):
    while True:
        print(f"\n=== MENU UTAMA (User: {username}) ===")
        print("1. Quiz Saintek TKA")
        print("2. History (Coming Soon)")
        print("3. Leaderboard (Coming Soon)")
        print("0. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            quiz_menu()  # ✅ Memanggil fitur quiz saintek
        elif pilihan == "2":
            print("\n📜 Fitur History sedang dalam pengembangan...")
        elif pilihan == "3":
            print("\n🏆 Fitur Leaderboard sedang dalam pengembangan...")
        elif pilihan == "0":
            print("👋 Logout berhasil. Sampai jumpa lagi!")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi.")

# ==========================
# PROGRAM UTAMA
# ==========================

def main():
    print("=== SELAMAT DATANG DI PROGRAM QUIZ SAINTEK CLI ===")

    while True:
        print("\n1. Login")
        print("2. Register")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username = login()
            if username:
                menu_utama(username)
        elif pilihan == "2":
            username = register()
            if username:
                menu_utama(username)
        elif pilihan == "0":
            print("Terima kasih telah menggunakan program ini! 👋")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
