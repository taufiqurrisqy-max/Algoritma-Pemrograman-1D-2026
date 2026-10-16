penerima = []
jumlah_penuh = 0

for i in range(10):
    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        break

    print("\nMahasiswa ke-", i + 1)
    nama = input("Nama: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat IPK.")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan > 5000000:
        print("Tidak memenuhi syarat penghasilan.")
        continue

    if penghasilan <= 3000000:
        jenis = "Beasiswa penuh"
        jumlah_penuh += 1
    else:
        jenis = "Beasiswa sebagian"

    penerima.append([nama, jenis])
    print("Status:", jenis)

print("\n--- DAFTAR PENERIMA BEASISWA ---")
for data in penerima:
    print(data[0], "-", data[1])
