def count_numbers(file_path):
    with open(file_path, 'r') as f:
        return len(f.readlines())

def is_sorted(file_path):
    with open(file_path, 'r') as f:
        previous_number = None
        for line in f:
            current_number = int(line.strip())
            if previous_number is not None and current_number < previous_number:
                return False
            previous_number = current_number
    return True

def count_occurrences(file_path):
    occurrences = {} 
    with open(file_path, 'r') as f:
        for line in f:
            number = int(line.strip())
            if number in occurrences:
                occurrences[number] += 1
            else:
                occurrences[number] = 1
    return occurrences


file1 = "/home/u335780/Pulpit/bigdata/work/6_1.dat"
file2 = "/home/u335780/Pulpit/bigdata/data.dat"


count1 = count_numbers(file1)
count2 = count_numbers(file2)


if count1 == count2:
    print("Pliki mają taką samą liczbę liczb:", count1)
else:
    print("Pliki mają różną liczbę liczb:", count2, "i", count1)

if is_sorted(file1):
    print("Plik 6_1.dat jest posortowany.")
else:
    print("Plik 6_1.dat NIE jest posortowany.")


occurrences = count_occurrences(file1)


print("\nLiczba wystąpień poszczególnych liczb:")
for number, count in sorted(occurrences.items())[:10]: 
    print(f"Liczba {number} występuje {count} razy.")
