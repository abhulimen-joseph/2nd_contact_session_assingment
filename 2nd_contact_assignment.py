with open('text.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if ":" in line:
            key, value = line.split(":", 1)
            print(f"{key.strip()}: {value.strip()}")
