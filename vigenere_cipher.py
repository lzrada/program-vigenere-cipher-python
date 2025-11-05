# --- Fungsi enkripsi ---
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for ch in plaintext:
        if ch.isalpha():  # hanya huruf A-Z
            p = ord(ch) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))
            key_index += 1
        else:
            ciphertext += ch  # spasi/tanda baca tetap
    return ciphertext


# --- Fungsi dekripsi ---
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0
    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')
            p = (c - k + 26) % 26
            plaintext += chr(p + ord('A'))
            key_index += 1
        else:
            plaintext += ch
    return plaintext


# --- Fungsi utama (menu interaktif) ---
def main():
    while True:
        print("\n===============================")
        print("     PROGRAM VIGENÈRE CHIPER")
        print("===============================")
        print("1. Enkripsi Teks")
        print("2. Dekripsi Teks")
        print("3. Keluar")
        print("===============================")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            teks = input("\nMasukkan teks yang ingin dienkripsi: ")
            key = input("Masukkan kunci (key): ")
            hasil = vigenere_encrypt(teks, key)
            print(f"\nHasil Enkripsi : {hasil}")

        elif pilihan == "2":
            teks = input("\nMasukkan teks yang ingin didekripsi: ")
            key = input("Masukkan kunci (key): ")
            hasil = vigenere_decrypt(teks, key)
            print(f"\nHasil Dekripsi : {hasil}")

        elif pilihan == "3":
            print("\nTerima kasih telah menggunakan program ini! 👋")
            break

        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")


# --- Jalankan program ---
if __name__ == "__main__":
    main()