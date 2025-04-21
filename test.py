def calculate_bmi(weight_kg: float, height_m: float) -> float:
    if height_m <= 0:
        raise ValueError("Height must be a positive value greater than 0.")
    return weight_kg / (height_m ** 2)

