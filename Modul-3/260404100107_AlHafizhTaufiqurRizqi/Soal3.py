nama_list = []
nilai_list = []
kategori_list = []

for i in range(10):
    print("\nMahasiswa ke-", i + 1)
    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    nilai = tugas * 0.3 + uts * 0.3 + uas * 0.4

    if nilai >= 85:
        kategori = "A"
    elif nilai >= 75:
        kategori = "B"
    elif nilai >= 60:
        kategori = "C"
    elif nilai >= 50:
        kategori = "D"
    else:
        kategori = "E"

    nama_list.append(nama)
    nilai_list.append(nilai)
    kategori_list.append(kategori)

    print("Nilai akhir:", round(nilai, 2))
    print("Kategori:", kategori)

tertinggi = max(nilai_list)
terendah = min(nilai_list)
rata_rata = sum(nilai_list) / len(nilai_list)

print("\n--- HASIL AKHIR KELAS ---")

for i in range(10):
    print(nama_list[i], "-", round(nilai_list[i], 2),
          "-", kategori_list[i])

print("Nilai tertinggi:", nama_list[nilai_list.index(tertinggi)],
      "-", round(tertinggi, 2))
print("Nilai terendah:", nama_list[nilai_list.index(terendah)],
      "-", round(terendah, 2))
print("Rata-rata kelas:", round(rata_rata, 2))
