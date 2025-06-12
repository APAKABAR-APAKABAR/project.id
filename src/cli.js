const fs = require('fs');
const { runFile, runCode } = require('./interpreter');
const { translate } = require('./translator');

const args = process.argv.slice(2);
const version = '1.0.0';

if (args.length === 0) {
    console.log('Bahasa .id - Bahasa pemrograman dengan sintaks bahasa Indonesia');
    console.log('Penggunaan:');
    console.log('  node src/cli.js run <file.id>        Jalankan file .id');
    console.log('  node src/cli.js translate <file.id>  Terjemahkan ke JavaScript');
    console.log('  node src/cli.js --version           Tampilkan versi');
    process.exit(0);
}

const command = args[0];
const file = args[1];

if (command === '--version') {
    console.log(`Bahasa .id v${version}`);
    process.exit(0);
}

if (command === 'run') {
    if (!file) {
        console.error('Harap masukkan nama file .id');
        process.exit(1);
    }
    if (!file.endsWith('.id')) {
        console.error('File harus berekstensi .id');
        process.exit(1);
    }
    if (!fs.existsSync(file)) {
        console.error(`File ${file} tidak ditemukan`);
        process.exit(1);
    }
    runFile(file);
} else if (command === 'translate') {
    if (!file) {
        console.error('Harap masukkan nama file .id');
        process.exit(1);
    }
    if (!file.endsWith('.id')) {
        console.error('File harus berekstensi .id');
        process.exit(1);
    }
    if (!fs.existsSync(file)) {
        console.error(`File ${file} tidak ditemukan`);
        process.exit(1);
    }
    const code = fs.readFileSync(file, 'utf-8');
    const translated = translate(code);
    console.log(translated);
} else {
    console.error('Perintah tidak dikenal. Gunakan: run, translate, atau --version');
    process.exit(1);
      }
