# LAPORAN PRAKTIKUM 9

## Judul Praktikum : Python String

---

 **Nama**   : Naziha Raiqi Aribino<br>
**NIM**    : 312510232<br>
**Kelas**  : TI. 25. A2<br>
**Mata Kuliah** : Pengantar Pemrograman<br>
**Pertemuan ke**: 14<br>

---

## Tujuan Praktikum

1. Memahami konsep dasar string pada bahasa pemrograman Python.
2. Mampu melakukan operasi dasar pada string seperti indexing, slicing, dan manipulasi string.
3. Mampu menggunakan format string pada Python.
4. Mampu membuat program sederhana untuk validasi input menggunakan string.


## DASAR TEORI

String adalah tipe data pada Python yang digunakan untuk menyimpan kumpulan karakter. String dapat diolah menggunakan berbagai operasi seperti pengambilan karakter, pengubahan huruf, penggantian karakter, serta validasi data.


## PRAKTIKUM

### Latihan 1 : Operasi Dasar String

#### Kode Program

```python
txt = "Hello World"

print("1. Jumlah karakter:")
print(len(txt))
print()

print("2. Karakter terakhir:")
print(txt[-1])
print()

print("3. Karakter index ke-2 sampai ke-4:")
print(txt[2:5])
print()

print("4. Hilangkan spasi:")
print(txt.replace(" ", ""))
print()

print("5. Huruf besar:")
print(txt.upper())
print()

print("6. Huruf kecil:")
print(txt.lower())
print()

print("7. Ganti H dengan J:")
print(txt.replace("H", "J"))
```

#### Penjelasan Program

* `len()` digunakan untuk menghitung jumlah karakter.
* Index `-1` digunakan untuk mengambil karakter terakhir.
* Slicing `[2:5]` digunakan untuk mengambil karakter dari index ke-2 sampai ke-4.
* `replace()` digunakan untuk menghapus spasi dan mengganti karakter.
* `upper()` dan `lower()` digunakan untuk mengubah huruf.


### Latihan 2 : Format String

#### Kode Program

```python
umur = 24
txt = "Hello, nama saya john, dan umur saya adalah {} tahun"

print(txt.format(umur))
```

#### Penjelasan Program

Program ini menggunakan fungsi `format()` untuk menyisipkan nilai variabel `umur` ke dalam string.


### Latihan 3 : Studi Kasus Validasi Form Input

#### Kode Program

```python
nama = input("Masukkan nama lengkap: ")
telepon = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

valid = True

if not nama.replace(" ", "").isalpha():
    print("Nama harus hanya berisi huruf")
    valid = False

if not telepon.isdigit():
    print("Nomor telepon harus hanya berisi angka")
    valid = False

if "@" not in email or "." not in email:
    print("Email tidak valid")
    valid = False

if valid:
    print("Data pendaftaran valid")
```

#### Penjelasan Program

* `input()` digunakan untuk menerima data dari pengguna.
* `isalpha()` digunakan untuk memvalidasi nama.
* `isdigit()` digunakan untuk memvalidasi nomor telepon.
* Pengecekan `@` dan `.` digunakan untuk validasi email.

---

## Kesimpulan

Berdasarkan hasil praktikum yang telah dilakukan pada pertemuan ini, dapat disimpulkan bahwa penggunaan tipe data string dalam bahasa pemrograman Python sangat penting dalam pengolahan data berbasis teks. Berbagai operasi string seperti menghitung jumlah karakter, mengambil karakter tertentu, mengubah huruf, serta mengganti karakter dapat dilakukan dengan mudah menggunakan fungsi bawaan Python.<br>

Selain itu, praktikum ini juga menunjukkan bahwa string dapat digunakan untuk memformat output menggunakan metode format() serta untuk melakukan validasi data input pengguna, seperti nama, nomor telepon, dan email. Dengan pemahaman yang baik terhadap konsep string, programmer dapat membuat program yang lebih interaktif, terstruktur, dan meminimalkan kesalahan input. Praktikum ini diharapkan dapat menjadi dasar dalam pengembangan program Python yang lebih kompleks di pertemuan selanjutnya.
