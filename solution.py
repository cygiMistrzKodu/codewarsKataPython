def final_grade(exam, projects):
    match (exam, projects):
        case (e, p) if e > 90 or p > 10:
            return 100
        case (e, p) if e > 75 and p >= 5:
            return 90
        case (e, p) if e > 50 and p >= 2:
            return 75
        case _:
            return 0
