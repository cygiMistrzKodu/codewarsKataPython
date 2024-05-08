def open_or_senior(data):
    membership = []
    for member in data:
        age = member[0]
        handicap = member[1]

        if age >= 55 and handicap > 7:
            membership.append("Senior")
        else:
            membership.append("Open")

    return membership

