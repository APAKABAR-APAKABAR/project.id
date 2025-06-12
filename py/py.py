import re
import sys
import os
import subprocess
import ast

# 🔑 Kamus kata kunci Bahasa Indonesia → Python
kata_kunci = {
    "fungsi": "def",
    "jika": "if",
    "lain jika": "elif",
    "lain": "else",
    "untuk": "for",
    "selama": "while",
    "dalam": "in",
    "tidak": "not",
    "dan": "and",
    "atau": "or",
    "benar": "True",
    "salah": "False",
    "keluar": "exit",
    "kembali": "return",
    "cetak": "print",
    "panjang": "len",
    "jangkauan": "range",
    "pecah": "split",
    "gabung": "join",
    "ubah_angka": "int",
    "ubah_teks": "str",
    "ubah_desimal": "float",
    "bulatkan": "round",
    "tambah": "append",
    "sisipkan": "insert",
    "hapus": "remove",
    "ambil": "pop",
    "urutkan": "sort",
    "balikkan": "reverse",
    "jumlahkan": "sum",
    "min": "min",
    "max": "max",
    "buka_berkas": "open",
    "baca_baris": "readline",
    "baca_semua": "read",
    "tulis": "write",
    "tutup": "close",
    "impor": "import",
    "dari": "from",
    "sebagai": "as",
    "coba": "try",
    "kecuali": "except",
    "akhirnya": "finally",
    "angkat": "raise",
    "kelas": "class",
    "pass": "pass",
    "lanjutkan": "continue",
    "berhenti": "break",
    "nama_utama": "__name__ == '__main__'"
}

# Pola tambahan untuk sintaks khusus
pola_tambahan = {
    # potong(x, a, b) → x[a:b]
    r'potong\s*\(\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^)]+)\s*\)': r'\1[\2:\3]',
    # ambil_dari(x, i) → x[i]
    r'ambil_dari\s*\(\s*([^,]+)\s*,\s*([^)]+)\s*\)': r'\1[\2]',
    # ulang(x, n) → [x for _ in range(n)]
    r'ulang\s*\(\s*([^,]+)\s*,\s*([^)]+)\s*\)': r'[\1 for _ in range(\2)]'
}

def translate_line(baris):
    # Simpan string dan komentar untuk melindunginya dari penggantian
    string_matches = []
    comment_matches = []
    
    # Tangani string (baik ' maupun ")
    def simpan_string(match):
        string_matches.append(match.group(0))
        return f"__STRING_{len(string_matches)-1}__"
    
    baris = re.sub(r'"[^"]*"|\'[^\']*\'', simpan_string, baris)
    
    # Tangani komentar (# sampai akhir baris)
    comment_match = re.search(r'#.*$', baris)
    if comment_match:
        comment_matches.append(comment_match.group(0))
        baris = baris.replace(comment_match.group(0), f"__COMMENT_{len(comment_matches)-1}__")
    
    # Terapkan pola tambahan
    for pola, pengganti in pola_tambahan.items():
        baris = re.sub(pola, pengganti, baris)
    
    # Ganti kata kunci
    for indo, py in kata_kunci.items():
        baris = re.sub(rf'\b{indo}\b', py, baris)
    
    # Kembalikan string
    for i, string in enumerate(string_matches):
        baris = baris.replace(f"__STRING_{i}__", string)
    
    # Kembalikan komentar
    for i, comment in enumerate(comment_matches):
        baris = baris.replace(f"__COMMENT_{i}__", comment)
    
    return baris

def validate_syntax(kode):
    try:
        ast.parse(kode)
        return True
    except SyntaxError as e:
        print(f"[!] Kesalahan sintaks: {e}")
        return False

def transpile(file_input):
    if not os.path.exists(file_input):
        print(f"[x] File tidak ditemukan: {file_input}")
        sys.exit(1)
    
    with open(file_input, 'r', encoding='utf-8') as f:
        baris_id = f.readlines()
    
    baris_py = [translate_line(baris) for baris in baris_id]
    
    # Validasi sintaks sebelum menyimpan
    kode_hasil = ''.join(baris_py)
    if not validate_syntax(kode_hasil):
        print("[x] Transpiler gagal: Kode hasil tidak valid.")
        sys.exit(1)
    
    nama_py = file_input.replace('.id', '.py')
    with open(nama_py, 'w', encoding='utf-8') as f:
        f.writelines(baris_py)
    
    print(f"[✓] Berhasil: {file_input} → {nama_py}")
    return nama_py

def jalankan(nama_py):
    try:
        subprocess.run(["python", nama_py], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Gagal menjalankan {nama_py}:\n{e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: python id_ke_py.py <file.id>")
        sys.exit(1)
    
    nama_file = sys.argv[1]
    hasil = transpile(nama_file)
    jalankan(hasil)
