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
tulis "Halo Dunia"
```

---

### `loops.id`

```id
angka = 1
selama (angka <= 5) {
  tulis "Angka: " + angka
  angka = angka + 1
}
```

---

### `async.id`

```id
fungsi tunggu(ms) {
  kembali baru Janji((selesai) => {
    aturWaktu(() => selesai(), ms)
  })
}

fungsi utama() {
  tulis "Mulai"
  tunggu tunggu(1000)
  tulis "Selesai setelah 1 detik"
}

utama()
```

---

### `classes.id`

```id
kelas Orang {
  fungsi __init__(nama) {
    ini.nama = nama
  }

  fungsi sapa() {
    tulis "Halo, saya " + ini.nama
  }
}

orang = baru Orang("Budi")
orang.sapa()
```

---

### `modules.id`

File: `examples/utils.id`
```id
fungsi tambah(a, b) {
  kembali a + b
}

ekspor tambah
```

File: `examples/modules.id`
```id
impor { tambah } dari "./utils.id"

tulis tambah(3, 4)
```

---

### `web.id`

```id
impor http dari "http"

server = http.buatServer((req, res) => {
  res.statusKode = 200
  res.setHeader("Content-Type", "text/plain")
  res.akhir("Halo dari server .id")
})

server.dengar(3000, () => {
  tulis "Server berjalan di http://localhost:3000"
})
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
