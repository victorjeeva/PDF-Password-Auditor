
import pikepdf
import os

def crack_pdf():
    print("\n===== PDF PASSWORD AUDITOR =====")

    pdf_path = input("Enter PDF file path: ").strip('"')
    wordlist_path = input("Enter wordlist path: ").strip('"')

    if not os.path.isfile(pdf_path):
        print("PDF file not found!")
        return

    if not os.path.isfile(wordlist_path):
        print("Wordlist file not found!")
        return

    print("\nStarting password audit...\n")

    attempts = 0

    try:
        with open(wordlist_path, "r", encoding="utf-8",
                  errors="ignore") as file:

            for password in file:
                password = password.strip()

                if not password:
                    continue

                attempts += 1

                try:
                    with pikepdf.open(
                        pdf_path,
                        password=password
                    ):
                        print("\n[+] PASSWORD FOUND!")
                        print("[+] Password:", password)
                        print("[+] Attempts:", attempts)
                        return

                except pikepdf.PasswordError:
                    print(f"[-] Attempt {attempts}: Incorrect")

        print("\n[-] Password not found in wordlist.")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    crack_pdf()
