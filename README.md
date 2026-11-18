# PDF Password Auditor 🔐

A Python-based PDF Password Auditing Tool developed using the **pikepdf** library. This project demonstrates dictionary-based password auditing on PDF files for educational purposes and authorized security testing.

## 📌 Project Overview

PDF Password Auditor is a Python tool designed to test candidate passwords against password-protected PDF documents.

It uses a user-provided wordlist to check whether a candidate password can open an authorized test PDF.

## 🚀 Features

- PDF password auditing using pikepdf
- Dictionary-based password testing
- Custom wordlist support
- Password attempt counter
- Password match detection
- Error handling for invalid files
- Separate wordlist generation utility

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| pikepdf | PDF password verification |
| itertools | Combination generation |
| string | Character sets |
| TXT files | Wordlist storage |

## 📂 Project Structure

```text
PDF-Password-Auditor/
│
├── pdf_password_auditor.py
├── wordlist_generator.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/victorjeevea/PDF-Password-Auditor.git
```

**Step 2: Navigate to the project directory**

```bash
cd PDF-Password-Auditor
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the PDF auditing tool:

```bash
python pdf_password_auditor.py
```

Provide:
1. The path to your authorized test PDF.
2. The path to your prepared password wordlist.

The tool checks candidate passwords and reports whether a matching password is found.

## 🔍 How It Works

1. The user provides a password-protected PDF.
2. The user provides a wordlist containing candidate passwords.
3. Python reads the candidates one by one.
4. pikepdf attempts to open the PDF using each candidate.
5. The tool reports a match or indicates that no password was found.

## ⚠️ Limitations

- Dictionary-based auditing only checks passwords present in the supplied wordlist.
- Password recovery is not guaranteed.
- Very large wordlists can require significant processing time.
- The tool does not bypass PDF encryption.

## 🔒 Ethical Disclaimer

This project is developed strictly for educational purposes, cybersecurity learning, and authorized security testing.

Use this tool only on PDF documents that you own or have explicit permission to audit.

The developer is not responsible for unauthorized use.

## 👨‍💻 Developer

**Jeevanantham K**

Cybersecurity Student | Python | Ethical Hacking | Security Tools

GitHub: https://github.com/victorjeevea

---

⭐ If you find this project useful, consider giving the repository a star!
