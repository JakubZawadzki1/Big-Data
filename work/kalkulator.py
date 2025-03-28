from collections import defaultdict

def count_numbers(file_path):
    with open(file_path, 'r') as f:
        return len(f.readlines())

def is_sorted(file_path):
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    return numbers == sorted(numbers)

def count_occurrences(file_path):
    occurrences = defaultdict(int) 
    with open(file_path, 'r') as f:
        for line in f:
            number = int(line.strip())
            occurrences[number] += 1
    return occurrences

# Pełne ścieżki do plików
file1 = "/home/u335780/Pulpit/bigdata/work/6_1.dat"
file2 = "/home/u335780/Pulpit/bigdata/data.dat"


count1 = count_numbers(file1)
count2 = count_numbers(file2)

if count1 == count2:
    print("Pliki mają taką samą liczbę liczb:", count1)
else:
    print("Pliki mają różną liczbę liczb:", count1, "i", count2)


if is_sorted(file1):
    print("Plik 6_1.dat jest posortowany.")
else:
    print("Plik 6_1.dat NIE jest posortowany.")

# Liczenie wystąpień każdej liczby
occurrences = count_occurrences(file1)

# Wyświetlenie kilku przykładowych wyników
print("\nLiczba wystąpień poszczególnych liczb:")
for number, count in sorted(occurrences.items())[:10]:  # Wyświetlamy 10 pierwszych liczb
    print(f"Liczba {number} występuje {count} razy.")


