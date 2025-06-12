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
node src/cli.js examples/hello.id
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

## 👥 Kontribusi

Kami membuka kontribusi dari siapa pun:

- Tambahkan fitur baru
- Perbaiki bug
- Tambahkan contoh atau dokumentasi

### Jalankan pengembangan lokal

```bash
git clone https://github.com/APAKABAR-APAKABAR/project.id
cd project.id
node src/cli.js examples/hello.id
```

---

## 📄 Lisensi

Proyek ini berada di bawah lisensi **MIT** — silakan gunakan dan modifikasi sesuai kebutuhan.

---

**Bahasa kita, kode kita.** 🇮🇩
