# Tugas Besar IF2124 Teori Bahasa Formal dan Otomata - Parserah
### Parser Bahasa JavaScript (Node.js)
## Table Of Contents
* [Project Description](#Project-Description)
* [Directory](#directory)
* [Usage](#usage)
* [Screenshots](#screenshots)
* [Pembagian Tugas](#Pembagian-Tugas)

## Project Description
Dalam proses pembuatan program dari sebuah bahasa menjadi instruksi yang dapat dieksekusi oleh mesin, terdapat pemeriksaan sintaks bahasa atau parsing yang dibuat oleh programmer untuk memastikan program dapat dieksekusi tanpa menghasilkan error. Parsing ini bertujuan untuk memastikan instruksi yang dibuat oleh programmer mengikuti aturan yang sudah ditentukan oleh bahasa tersebut. Baik bahasa berjenis interpreter maupun compiler, keduanya pasti melakukan pemeriksaan sintaks. Perbedaannya terletak pada apa yang dilakukan setelah proses pemeriksaan (kompilasi/compile) tersebut selesai dilakukan.

Dibutuhkan grammar bahasa dan algoritma parser untuk melakukan parsing. Sudah sangat banyak grammar dan algoritma yang dikembangkan untuk menghasilkan compiler dengan performa yang tinggi. Terdapat CFG, CNF-e, CNF+e, 2NF, 2LF, dll untuk grammar yang dapat digunakan, dan terdapat LL(0), LL(1), CYK, Earley’s Algorithm, LALR, GLR, Shift-reduce, SLR, LR(1), dll untuk algoritma yang dapat digunakan untuk melakukan parsing.

Pada tugas besar ini, implementasikan parser untuk JavaScript (Node.js) untuk beberapa statement dan sintaks bawaan JavaScript.

## Directory
```bash
├───src
│   ├───CFG
│   │   ├───CFG.txt
│   |   └───GrammarReader.py
│   ├───CodeSplitter
│   │   ├───codeSplitter.py
│   |   └───tesCodeSplitter.py
│   ├───CYK
│   |   └───cyk.py
│   └───FA
│       ├───checkExpression.py
|       ├───tesCheckVariable.py
|       ├───tesCheckExpression.py
│       └───checkVariable.py
├───docs
│   └───Laporan.pdf
├───testcase
|   ├───inputAcc.js
|   ├───inputReject.js
|   ├───kasus3.js
|   ├───kasus4.js
|   ├───kasus5.js
|   ├───kasus6.js
|   ├───kasus7.js
|   ├───kasus8.js
|   ├───kasus9.js
|   ├───kasus10.js
|   ├───testCodeSplitter.txt
|   ├───testExpNotValid.txt
|   ├───testExpValid.js
|   ├───testVarNotValid.js
|   ├───testVarValid.js
|   ├───TEST.txt
|   ├───TEST1.txt
|   ├───TEST2.txt
|   ├───TEST3.txt
|   ├───TEST4.txt
│   └───test.js
├───main.py
└───README.md
```
## Usage
- Clone or download the repository
    > 
        git clone https://github.com/maikeljh/TubesTBFOParserah.git
- Run main.py file inside src
- Put your javascript file inside folder testcase
- Type your javascript filename in program

## Screenshots
### User Interface
![Screenshot_2188](https://user-images.githubusercontent.com/87570374/203948527-6a3af707-3ee9-4215-bfe9-229167806a87.png)
![Screenshot_2189](https://user-images.githubusercontent.com/87570374/203948539-14d6e6bd-0ca5-4386-b856-9279c5137f2f.png)
![Screenshot_2190](https://user-images.githubusercontent.com/87570374/203948544-9cea72e0-816c-4c6e-85b1-194f46d15cb6.png)
![Screenshot_2191](https://user-images.githubusercontent.com/87570374/203948548-4c760955-cd65-4563-8062-81f955405d95.png)
![Screenshot_2192](https://user-images.githubusercontent.com/87570374/203948553-ccdda22a-63aa-47f6-b12b-a137b1177f9e.png)

## Pembagian Tugas
| NIM | Nama | Tugas |
|-----|------|-------|
|13521124|Michael Jonathan Halim|Main Program, FA, CYK, Debugging (Keseluruhan), Laporan|
|13521143|Raynard Tanadi|Code Splitter, Eliminate Useless Variable, Convert CFG to CNF, Debugging (Keseluruhan), Laporan|
|13521148|Johannes Lee|Membuat CFG, Baca CFG, Eliminasi E production, Eliminasi Unit production, Debugging (Keseluruhan), Laporan|

