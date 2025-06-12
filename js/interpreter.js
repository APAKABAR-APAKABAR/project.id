const fs = require('fs');
const vm = require('vm');
const path = require('path');
const { translate } = require('./translator');

function runCode(code, filename) {
    try {
        const translatedCode = translate(code);
        const context = {
            console,
            require,
            process,
            Buffer,
            setTimeout,
            setInterval,
            clearTimeout,
            clearInterval,
            __dirname: path.dirname(filename),
            __filename: filename
        };
        vm.createContext(context);
        vm.runInContext(translatedCode, context, { filename });
        return { success: true };
    } catch (error) {
        return { success: false, error: error.message };
    }
}

function runFile(inputFile) {
    try {
        const code = fs.readFileSync(inputFile, 'utf-8');
        const result = runCode(code, inputFile);
        if (result.success) {
            console.log(`Berhasil menjalankan ${inputFile}`);
        } else {
            console.error(`Error saat menjalankan ${inputFile}: ${result.error}`);
        }
    } catch (error) {
        console.error(`Error membaca file ${inputFile}: ${error.message}`);
    }
}

module.exports = { runCode, runFile };