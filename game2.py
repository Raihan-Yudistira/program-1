import os
import random

def main():
    secret_word = "Carieta 68"
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6
    
    # Buat display dengan underscore
    display = ""
    for char in secret_word:
        if char == " ":
            display += " "
        else:
            display += "_ "
    
    print("=" * 50)
    print("SELAMAT DATANG DI GAME TEBAK KATA!")
    print("=" * 50)
    print(f"\nKata rahasia: {display}")
    print(f"Kesempatan salah: {max_attempts - wrong_attempts}")
    print()
    
    while wrong_attempts < max_attempts:
        # Tampilkan status
        display = ""
        for char in secret_word:
            if char == " ":
                display += " "
            elif char.lower() in guessed_letters:
                display += char + " "
            else:
                display += "_ "
        
        print(f"Kata: {display}")
        print(f"Huruf yang ditebak: {', '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
        print(f"Kesempatan salah tersisa: {max_attempts - wrong_attempts}/{max_attempts}")
        print()
        
        # Cek apakah sudah menang
        is_won = True
        for char in secret_word:
            if char != " " and char.lower() not in guessed_letters:
                is_won = False
                break
        
        if is_won:
            print("=" * 50)
            print(f"🎉 SELAMAT! Anda menang! Kata rahasia adalah: {secret_word}")
            print("=" * 50)
            break
        
        # Input pemain
        guess = input("Tebak satu huruf atau seluruh kata: ").strip()
        
        if not guess:
            print("❌ Silakan masukkan huruf atau kata!\n")
            continue
        
        # Cek apakah menebak seluruh kata
        if len(guess) > 1:
            if guess.lower() == secret_word.lower():
                print(f"🎉 SELAMAT! Anda menang! Kata rahasia adalah: {secret_word}")
                print("=" * 50)
                break
            else:
                print(f"❌ Kata '{guess}' salah!")
                wrong_attempts += 1
                print()
                continue
        
        # Cek apakah huruf valid
        if not guess.isalpha():
            print("❌ Silakan masukkan huruf!\n")
            continue
        
        guess_lower = guess.lower()
        
        # Cek apakah sudah ditebak
        if guess_lower in guessed_letters:
            print(f"⚠️  Anda sudah menebak huruf '{guess}'!\n")
            continue
        
        guessed_letters.add(guess_lower)
        
        # Cek apakah huruf ada di kata
        if guess_lower in secret_word.lower():
            print(f"✅ Benar! Huruf '{guess}' ada di kata!")
        else:
            print(f"❌ Salah! Huruf '{guess}' tidak ada di kata!")
            wrong_attempts += 1
        
        print()
    
    # Jika kalah
    if wrong_attempts >= max_attempts:
        print("=" * 50)
        print(f"😢 GAME OVER! Anda kalah!")
        print(f"Kata rahasia adalah: {secret_word}")
        print("=" * 50)

if __name__ == "__main__":
    main()
