def calculate_happiness(date):
    while len(date) > 1:
        total = sum(int(digit) for digit in date)
        date = str(total)
    return date


input_file_name = "input.txt"
output_file_name = "output.txt"

with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
    for line in input_file:
        date = line.strip()
        happiness_number = calculate_happiness(date)
        output_file.write(happiness_number + "\n")

print("Щасливість дат обчислена та збережена у файлі", output_file_name)
