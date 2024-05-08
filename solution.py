def tribonacci(signature, n):

    tribonacci_sequence = []
    for i in range(0, n):

        if i < 3:
            tribonacci_sequence.append(signature[i])
        else:
            next_number = tribonacci_sequence[i - 3] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 1]
            tribonacci_sequence.append(next_number)

    return tribonacci_sequence
