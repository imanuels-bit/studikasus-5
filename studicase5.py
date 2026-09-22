def hitungjumlah(jKamar, lNginap):
    jKamar = jKamar.lower()
    if jKamar == "standar":
        byr = 200000
    elif jKamar == "deluxe":
        byr = 350000
    else:
        byr = 0
    return byr * lNginap

jKamar = input("Masukkan jenis kamar:")
chekcin = int(input("Masukkan tanggal checkin:"))
checkout = int(input("Masukkan tanggal check out:"))
lNginap = checkout - chekcin
total = hitungjumlah(jKamar, lNginap)
print("==== Data pemesanan hotel ====")
print("Jenis kamar:", jKamar)
print("Tanggal checkin:", chekcin)
print("Tanggal checkout:", checkout)
print("Lamanya menginap di hotel:", lNginap)
print("Total biaya nginap:", total)