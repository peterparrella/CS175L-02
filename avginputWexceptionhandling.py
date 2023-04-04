#CS175L-02
#Peter Parrella
#AverageFromInput W/ Exception Handling

import sys

def read_values(filename):
    values = []
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, start=1):
                try:
                    value = float(line.strip())
                except ValueError:
                    print(f"Error: invalid input on line {line_num} in file '{filename}'", file=sys.stderr)
                    sys.exit(1)
                values.append(value)
    except IOError:
        print(f"Error: could not read from file '{filename}'", file=sys.stderr)
        sys.exit(1)
    return values

def calculate_average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)

def print_average(average, num_values):
    print(f"Read in {num_values} number(s)")
    for i, value in enumerate(values, start=1):
        total = sum(values[:i])
        print(f"Current number is: {value:8.2f} Total is: {total:8.2f}")
    print(f"Average: {average:8.1f}")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    values = read_values(filename)
    average = calculate_average(values)
    print_average(average, len(values))

if __name__ == '__main__':
    main()
