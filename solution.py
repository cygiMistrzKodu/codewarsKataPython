def rental_car_cost(d):
    normal_rental_cost = d * 40

    if 3 < d < 7:
        return normal_rental_cost - 20

    if d < 7:
        return normal_rental_cost

    if d >= 7:
        return normal_rental_cost - 50
