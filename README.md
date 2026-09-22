# Kalkulator Biaya Hotel

Script Python sederhana buat ngitung total biaya nginap di hotel berdasarkan jenis kamar dan lama menginap.

## Cara pakai

```bash
python hotel.py
```

Nanti bakal diminta input:
- Jenis kamar (`standar` atau `deluxe`)
- Tanggal check-in
- Tanggal check-out

Lama menginap dihitung otomatis dari selisih tanggal checkout dan checkin, terus dikaliin sama harga kamar per malam.

## Harga kamar

| Jenis kamar | Harga/malam |
|---|---|
| Standar | Rp200.000 |
| Deluxe | Rp350.000 |

Kalau jenis kamar diketik selain dua itu (typo atau apa aja), total biayanya bakal keitung 0. Ini belum ada validasi input, jadi hati-hati aja.

## Contoh output

```
==== Data pemesanan hotel ====
Jenis kamar: deluxe
Tanggal checkin: 10
Tanggal checkout: 13
Lamanya menginap di hotel: 3
Total biaya nginap: 1050000
```

## Catatan

- Input jenis kamar gak case-sensitive ("Deluxe", "DELUXE", "deluxe" semua kebaca sama).
- Tanggal checkin/checkout diinput sebagai angka biasa (bukan format tanggal beneran), jadi cuma dianggap sebagai hari ke-berapa.
