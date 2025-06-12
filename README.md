## V > 0.1
---

# 🇮🇩 .id - Bahasa Pemrograman Indonesia

**.id** adalah bahasa pemrograman eksperimental yang menggunakan Bahasa Indonesia sebagai sintaks utama. Dibangun dengan JavaScript (Node.js), `.id` bertujuan untuk membuat pemrograman lebih mudah dipahami oleh penutur bahasa Indonesia.

---

## ✨ Fitur Utama

- Sintaks full Bahasa Indonesia (seperti `jika`, `selama`, `fungsi`, dll)
- Interpreter berbasis Node.js
- Mendukung fungsi, class, modul, dan asynchronous
- Contoh kode tersedia di folder `examples/`

---

## 🧪 Contoh Kode

### `hello.id`

```id
fungsi sapa(nama) {
    biar pesan = "Halo, " + nama;
    jika (nama === "Dunia") {
        kembalikan pesan + "!";
    } lain {
        kembalikan pesan + ", apa kabar?";
    }
}
cetak(sapa("Dunia"));
```

---

### `loops.id`

```id
fungsi hitung() {
    untuk (biar i = 1; i <= 5; i++) {
        cetak("Angka: " + i);
    }
    biar j = 0;
    selagi (j < 3) {
        cetak("Perulangan selagi: " + j);
        j++;
    }
}
hitung();
```

---

### `async.id`

```id
tak_sinkron fungsi ambilData() {
    coba {
        biar respons = tunggu ambil("https://api.example.com/data");
        kembalikan respons;
    } tangkap (kesalahan) {
        cetak("Error: " + kesalahan.pesan);
        kembalikan kosong;
    }
}
tak_sinkron fungsi utama() {
    biar data = tunggu ambilData();
    cetak(data);
}
utama();
```

---

### `classes.id`

```id
kelas Manusia {
    fungsi konstruktor(nama, umur) {
        ini.nama = nama;
        ini.umur = umur;
    }
    fungsi perkenalan() {
        kembalikan "Saya " + ini.nama + ", umur " + ini.umur + " tahun.";
    }
}
biar budi = baru Manusia("Budi", 25);
cetak(budi.perkenalan());
```

---

### `modules.id`

```ekspor fungsi tambah(a, b) {
    kembalikan a + b;
}

ekspor kelas Kalkulator {
    fungsi kali(a, b) {
        kembalikan a * b;
    }
}

biar angka = [1, 2, 3, 4];
biar kuadrat = angka.peta(x => x * x);
biar genap = angka.saring(x => x % 2 === 0);
biar jumlah = angka.kurangi((sum, x) => sum + x, 0);

cetak(kuadrat); // Output: [1, 4, 9, 16]
cetak(genap);   // Output: [2, 4]
cetak(jumlah);  // Output: 10
```

---

### `web.id`

```id
jika (typeof window !== "tak_ada") {
    fungsi ubahTeks() {
        biar elemen = document.getElementById("demo");
        elemen.innerHTML = "Halo dari Bahasa .id!";
    }
    window.onload = ubahTeks;
}
```

---

## ▶️ Menjalankan Kode

### 1. Install Node.js (jika belum)

- [Download Node.js](https://nodejs.org)

### 2. Jalankan file `.id`

```bash
node js/cli.js js.id/hello.id
```

---

## 🛠️ Perintah Dasar

| Bahasa Indonesia   | Arti Internasional  |
|--------------------|---------------------|
| `tulis`            | `console.log`       |
| `jika`, `selainnya`, `akhir` | `if`, `else`, `end` |
| `selama`           | `while`             |
| `fungsi`           | `function`          |
| `kelas`            | `class`             |
| `tunggu`           | `await`             |
| `impor`            | `import`            |
| `kembali`          | `return`            |
| `baru`             | `new`               |
| `ini`              | `this`              |
| `akhir`            | `res.end()`         |

---

### Jalankan pengembangan lokal

```bash
git clone https://github.com/APAKABAR-APAKABAR/project.id
cd project.id
node js/cli.js js.py/hello.id
```

---

# Transpiler Python Bahasa Indonesia

Transpiler ini mengubah kode Python yang ditulis dengan kata kunci dan pola berbahasa Indonesia (file berekstensi `.id`) menjadi kode Python standar (file berekstensi `.py`) yang dapat dijalankan oleh interpreter Python. Tujuannya adalah mempermudah pemrograman bagi pengguna yang lebih nyaman dengan bahasa Indonesia, terutama pemula, sambil tetap menjaga kompatibilitas dengan Python standar.

## Fitur
- **Terjemahan Kata Kunci**: Mengubah kata kunci seperti `jika` menjadi `if`, `cetak` menjadi `print`, `untuk` menjadi `for`, dll.
- **Pola Khusus**:
  - `potong(x, a, b)` → `x[a:b]` (slicing).
  - `ambil_dari(x, i)` → `x[i]` (indexing).
  - `ulang(x, n)` → `[x for _ in range(n)]` (mengulang nilai x sebanyak n kali).
- **Proteksi String dan Komentar**: Kata kunci dalam string atau komentar tidak diubah (misalnya, `cetak("jika")` tetap menghasilkan `"jika"`).
- **Validasi Sintaks**: Memastikan kode hasil transpiler valid menggunakan `ast.parse`.
- **Error Handling**: Menyediakan pesan error yang jelas jika file tidak ditemukan atau ada kesalahan sintaks.
- **Encoding UTF-8**: Mendukung karakter khusus dalam kode.

## Prasyarat
- Python 3.x terinstal.
- Modul standar Python: `re`, `sys`, `os`, `subprocess`, `ast`.

## Instalasi
1. Salin kode transpiler di bawah ini ke file bernama `id_ke_py.py`.
2. Simpan di direktori proyek Anda.
3. Pastikan Python terinstal dan dapat dijalankan dari terminal.

---

## 🧪 Contoh Kode

### `hello.id`

```id
def sapa(nama):
    print("Halo", nama)
    return nama

if __name__ == '__main__':
    sapa("Budi")
```

---

### `kalkulator.id`

```id
fungsi tambah(a, b):
    kembali a + b

fungsi kurang(a, b):
    kembali a - b

fungsi kali(a, b):
    kembali a * b

fungsi bagi(a, b):
    jika b == 0:
        cetak("Tidak bisa dibagi dengan nol!")
        kembali 0
    kembali a / b

jika nama_utama:
    cetak("=== KALKULATOR SEDERHANA ===")
    cetak("Pilih operasi: tambah / kurang / kali / bagi")

    operasi = input("Operasi: ")
    angka1 = ubah_desimal(input("Masukkan angka pertama: "))
    angka2 = ubah_desimal(input("Masukkan angka kedua: "))

    jika operasi == "tambah":
        hasil = tambah(angka1, angka2)
    jika operasi == "kurang":
        hasil = kurang(angka1, angka2)
    jika operasi == "kali":
        hasil = kali(angka1, angka2)
    jika operasi == "bagi":
        hasil = bagi(angka1, angka2)

    cetak("Hasil:", hasil)
```

---

### Jalankan pengembangan lokal

```bash
git clone https://github.com/APAKABAR-APAKABAR/project.id
cd project.id
node py/py.py py.id/hello.id
```

---

---

**Bahasa kita, kode kita.** 🇮🇩
