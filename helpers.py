def definition_cleanup(definition):
    front_index, end_index = 0, len(definition) - 1
    offset = 2
    while definition[front_index] == " " or definition[end_index] == " ":
        front_index += 1
        end_index -= 1
    res = definition[front_index + offset:end_index + 1]
    return res