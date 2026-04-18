def load_passwords(file_path, limit=50000):
    passwords = []
    with open(file_path, 'r', encoding='latin-1') as f:
        for i, line in enumerate(f):
            pwd = line.strip()
            if pwd:  # avoid empty lines
                passwords.append(pwd)
            if i >= limit:
                break
    return passwords


if __name__ == "__main__":
    sample = load_passwords("data/rockyou.txt", limit=10)
    print(sample)