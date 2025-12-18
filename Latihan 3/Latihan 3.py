nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")
valid = True
# Validasi nama (hanya huruf dan spasi)
if not nama.replace(" ", "").isalpha():
    print("❌ Nama harus hanya berisi huruf")
    valid = False
# Validasi nomor telepon (hanya angka)
if not telepon.isdigit():
    print("❌ Nomor telepon harus hanya berisi angka")
    valid = False
# Validasi email (harus ada @ dan .)
if "@" not in email or "." not in email:
    print("❌ Email tidak valid")
    valid = False
if valid:
    print("✅ Data pendaftaran valid")
