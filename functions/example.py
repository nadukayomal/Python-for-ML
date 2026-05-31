def assign_marks(mark):
    if mark >= 75:
        mark = 'A'
    elif mark >= 55:
        mark = "B"
    else:
        mark = "c-"
    return mark

get_mark = assign_marks(40)
print(get_mark)
