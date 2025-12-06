b = float(input("Masukkan nilai b: "))
a = float(input("Masukkan nilai a: "))
v = float(input("Masukkan nilai v: "))

hasil = (b - 10) / (2 * (1 - (a / (2 * v**2))))
print("Hasil perhitungan adalah:", hasil) 

def hitung_rumus(b, a, v, nama="Stefanus", lokasi="Pondok Aren"):
    try:
        hasil = (b - 10) / (2 * (1 - (a / (2 * v**2))))
        print(f"Halo {nama} dari {lokasi}!")
        print(f"Hasil perhitungan rumus adalah: {hasil:.2f}")
    except ZeroDivisionError:
        print("Terjadi pembagian dengan nol. Pastikan nilai v tidak nol.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
b = float(input("Masukkan nilai b: "))
a = float(input("Masukkan nilai a: "))
v = float(input("Masukkan nilai v: "))

hitung_rumus(b, a, v)
