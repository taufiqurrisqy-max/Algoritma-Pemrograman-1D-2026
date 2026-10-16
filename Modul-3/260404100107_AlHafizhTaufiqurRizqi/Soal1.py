total_penumpang = 0
pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = float(input("Masukkan jarak (0 untuk selesai): "))

    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    total_penumpang += 1

    if total_penumpang % 5 == 0:
        tarif = tarif * 0.5

    pendapatan += tarif
    total_jarak += jarak

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

    print("Tarif:", tarif)

print("Jumlah penumpang:", total_penumpang)
print("Total pendapatan: Rp", pendapatan)
print("Jarak terjauh:", jarak_terjauh, "km")

if total_penumpang > 0:
    print("Rata-rata jarak:", total_jarak / total_penumpang, "km")
else:
    print("Belum ada penumpang")
