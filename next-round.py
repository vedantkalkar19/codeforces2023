def round(_people, benchmark):
    input_str = input()
    count = 0
    marks = list(map(int, input_str.split()))
    k = marks[benchmark - 1]
    for x in marks:
        if x >= k and x > 0:
            count += 1
    return count


def main():
    first_input = input()
    better_input = list(map(int, first_input.split()))
    people = better_input[0]
    benchmark = better_input[1]

    result = round(people, benchmark)
    print(result)


if __name__ == "__main__":
    main()
