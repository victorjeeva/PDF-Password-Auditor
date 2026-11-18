
import itertools
import string

def generate_wordlist():
    words = [
        "password", "admin", "welcome",
        "hello", "student", "cybersecurity",
        "testing", "sample", "mypassword"
    ]

    numbers = ["123", "1234", "12345", "2026"]

    output_file = "test_wordlist.txt"
    count = 0

    with open(output_file, "w") as file:
        for word in words:
            for number in numbers:
                for candidate in [
                    word + number,
                    word.capitalize() + number,
                    word.upper() + number
                ]:
                    file.write(candidate + "\n")
                    count += 1

    print("Wordlist generated successfully!")
    print("Total entries:", count)
    print("Saved to:", output_file)

generate_wordlist()
