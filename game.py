# Aplikasi game secret nuber

secret_number = 777

guess_number = int(input("Masukkan angka:"))

while guess_number != secret_number:
    print("tebakan salah, silakan coba lagi")
    guess_number = int(input("Masukkan angka:"))

print("Selamat....Anda Benar!!!")
print("Kode ini saya buat di codespace")