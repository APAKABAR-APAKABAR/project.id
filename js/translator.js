const keywordMap = {
    'fungsi': 'function',
    'biar': 'let',
    'tetap': 'const',
    'variabel': 'var',
    'jika': 'if',
    'lain': 'else',
    'jika_lain': 'else if',
    'untuk': 'for',
    'selagi': 'while',
    'kembalikan': 'return',
    'benar': 'true',
    'salah': 'false',
    'kosong': 'null',
    'tak_ada': 'undefined',
    'kelas': 'class',
    'baru': 'new',
    'ini': 'this',
    'tak_sinkron': 'async',
    'tunggu': 'await',
    'coba': 'try',
    'tangkap': 'catch',
    'lempar': 'throw',
    'cetak': 'console.log',
    'ekspor': 'export',
    'impor': 'import',
    'bawaan': 'default',
    'sebagai': 'as',
    'dari': 'from',
    'peta': 'map',
    'kurangi': 'reduce',
    'saring': 'filter'
};

function translate(code) {
    let result = code;
    for (const [idKeyword, jsKeyword] of Object.entries(keywordMap)) {
        const regex = new RegExp(`\\b${idKeyword}\\b`, 'g');
        result = result.replace(regex, jsKeyword);
    }
    return result;
}

module.exports = { translate, keywordMap };