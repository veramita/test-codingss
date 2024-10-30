import random

def tebak_angka():
    while True:
        angkaRahasia = random.randint(1, 10)
        jumlahTebakan = 0
        
        print("Selamat datang di Permainan Tebak Angka!")
        print("Saya telah memilih angka antara 1 dan 10. Coba tebak!")

        while True:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlahTebakan += 1
            
            if tebakan < angkaRahasia:
                print("Tebakan terlalu rendah.")
            elif tebakan > angkaRahasia:
                print("Tebakan terlalu tinggi.")
            else:
                print(f"Selamat! Anda menebak angka {angkaRahasia} dengan benar!")
                print(f"Jumlah tebakan Anda: {jumlahTebakan}")
                break

        lagi = input("Apakah Anda ingin bermain lagi? (ya/tidak): ")
        if lagi.lower() != 'ya':
            print("Terima kasih telah bermain!")
            break

tebak_angka()
