def zero_fuel(distance_to_pump, mpg, fuel_left):
    miles_will_go = fuel_left * mpg
    if distance_to_pump <= miles_will_go:
        return True

    return False
