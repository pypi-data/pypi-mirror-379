# ❤️ LoveLang

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](../../issues)  
[![GitHub stars](https://img.shields.io/github/stars/CodeGoura/lovelang.svg?style=social)](https://github.com/CodeGoura/lovelang/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/CodeGoura/lovelang.svg?style=social)](https://github.com/CodeGoura/lovelang/network/members)  

LoveLang is a fun, Hinglish-based toy programming language written in Python.  
It is inspired by BhaiLang but created with its own flavor of **pyaar (love)** ❤️.

- Hinglish keywords (`bolo`, `suno`, `agartum`, `nehito`…)
- Easy to run (pure Python, no external dependencies)
- Great for learning how interpreters work
- Open to community contributions ✨

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/CodeGoura/lovelang.git
cd lovelang
```

### 2. Run a LoveLang file
```bash
python lovelang.py examples/hello.pyr
```

### 3. File extension
All LoveLang files use `.pyr`.

---

## 📝 Syntax Keywords

| LoveLang Keyword | Meaning (English)   |
|------------------|---------------------|
| `suno`           | input               |
| `bolo`           | print               |
| `agartum`        | if                  |
| `nehito`         | else                |
| `jabtak`         | while               |
| `thodaroko`      | continue            |
| `miltehe`        | break               |
| `trust`          | pass                |
| `dilse`          | function definition |
| `lautjao`        | return              |
| `lovetrue`       | true                |
| `lovefalse`      | false               |

---

## 💡 Example Programs

### Hello World
```pyr
bolo("Hello doston, Welcome to LoveLang ❤️");
```

### Input / Output
```pyr
naam = suno("Apna naam batao: ");
bolo("Hi", naam, "- nice to meet you!");
```

### Conditionals
```pyr
x = 10;
agartum (x > 5) {
    bolo("x bada hai");
} nehito {
    bolo("x chhota hai");
}
```

### Loops
```pyr
i = 0;
jabtak (i < 5) {
    i = i + 1;
    agartum (i == 3) { thodaroko; }
    bolo("Count:", i);
    agartum (i == 4) { miltehe; }
}
```

### Functions
```pyr
dilse add(a, b) {
    lautjao a + b;
}
bolo("2 + 3 =", add(2, 3));
```

---

## ⚡ Error Handling

- **Syntax Errors**: Show line + column with caret pointer.  
- **Runtime Errors**:  
  - Undefined variable  
  - Division by zero  
  - Argument count mismatch  
  - Function not found  

Example:
```pyr
bolo(x);   # RuntimeError: Undefined variable 'x'
```

---

## 📂 Project Structure
```
lovelang/
│── lovelang.py       # Interpreter
│── examples/         # Sample .pyr programs
│── docs/             # Syntax & grammar docs
│── README.md         # This file
```

---

## 🤝 How to Contribute

LoveLang is open source and we welcome your contributions!

1. Fork this repo
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/lovelang.git
   cd lovelang
   ```
3. Create a feature branch:
   ```bash
   git checkout -b feature-new-keyword
   ```
4. Add your changes (new Hinglish keywords, syntax, bug fixes, docs…)
5. Commit and push:
   ```bash
   git commit -m "Add new keyword: dilkaro"
   git push origin feature-new-keyword
   ```
6. Open a Pull Request 🎉

---

## 📌 Roadmap

- [ ] Add **for-loops** (maybe `jabtaklove`?)  
- [ ] Add **lists/arrays** support  
- [ ] Build an **interactive REPL** (`python lovelang.py` without file)  
- [ ] More built-in string functions  
- [ ] Error messages with suggestions ("Did you mean `nehito`?")  
- [ ] Community-driven Hinglish keywords ❤️  

---

## 👤 Author
**[Gourahari (CodeGoura)](https://github.com/CodeGoura)**  

---

## 📜 License
This project is open source under the **MIT License**.
