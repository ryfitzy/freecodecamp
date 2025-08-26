def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_number_list = []
    second_number_list = []
    operator_list = []

    for problem in problems:
        operator_index = problem.find('+')
        if operator_index == -1:
            operator_index = problem.find('-')

        if operator_index == -1:
            return "Error: Operator must be '+' or '-'."

        operator_list.append(problem[operator_index])
        first_number = problem[:operator_index - 1]
        second_number = problem[operator_index + 2:]

        if not first_number.isnumeric() or not second_number.isnumeric():
            return 'Error: Numbers must only contain digits.'

        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_number_list.append(first_number)
        second_number_list.append(second_number)

    print(first_number_list, second_number_list, operator_list)

    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for i in range(len(problems)):
        first_number = first_number_list[i]
        second_number = second_number_list[i]
        problem_length = max(len(first_number), len(second_number)) + 2 

        first_line += (problem_length - len(first_number)) * ' ' + first_number
        second_line += operator_list[i] + (problem_length - len(second_number) - 1) * ' ' + second_number
        third_line += problem_length * '-'

        if show_answers:
            total = ""
            if operator_list[i] == '+':
                total = str(int(first_number) + int(second_number))
            else:
                total = str(int(first_number) - int(second_number))
            fourth_line += (problem_length - len(total)) * ' ' + total

        
        if i == len(problems) - 1:
            first_line += '\n'
            second_line += '\n'
            if show_answers:
                third_line += '\n'
        else:
            first_line += 4 * ' '
            second_line += 4 * ' '
            third_line += 4 * ' '
            if show_answers:
                fourth_line += 4 * ' '

    return first_line + second_line + third_line + fourth_line

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 - 3801"], True))


