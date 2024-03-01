department_counts = {}

with open('info.txt', 'r') as file:
    for line in file:
        info = line.strip().split()

        department_number = info[-1].split('-')[0]
        bonus = int(info[-2])
        if bonus >= 0:
            if department_number in department_counts:
                department_counts[department_number] += 1
            else:
                department_counts[department_number] = 1

for department, count in department_counts.items():
    print(f"Bo'lim {department}")
