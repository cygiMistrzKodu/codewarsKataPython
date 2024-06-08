import statistics


def get_grade(s1, s2, s3):
    mean_scores = statistics.mean([s1, s2, s3])

    if 90 <= mean_scores <= 100:
        return "A"

    if 80 <= mean_scores < 90:
        return "B"

    if 70 <= mean_scores < 80:
        return "C"

    if 60 <= mean_scores < 70:
        return "D"

    if 0 <= mean_scores < 60:
        return "F"
