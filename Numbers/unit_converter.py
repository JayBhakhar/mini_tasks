# 11 c -> f, 12 f -> c
# 21EUR, 22UAH, 23USD ----> RUB
# 31kg -> pound, 32pound -> kg

def convert_unit(frm: str, to: str, value: int) -> str:
    frm, to = frm.lower(), to.lower()
    proper_combinations = [
        ['celsius', 'fahrenheit'],
        ['kg', 'pound']
    ]

    is_valid = False
    for proper_comb in proper_combinations:
        if frm and to in proper_comb and frm != to:
            is_valid = True
            break

    if not is_valid:
        return "invalid combination"

    if frm == proper_combinations[0][0] and to == proper_combinations[0][1]:
        return f"{value} °C is equal to {celsius_to_fahrenheit(value)} °F"

    if frm == proper_combinations[0][1] and to == proper_combinations[0][0]:
        return f"{value} °F is equal to {fahrenheit_to_celsius(value)} °C"

    if frm == proper_combinations[1][0] and to == proper_combinations[1][1]:
        return f"{value} Kg is equal to {kg_to_pound(value)} Pound"

    if frm == proper_combinations[1][1] and to == proper_combinations[1][0]:
        return f"{value} Pound is equal to {pound_to_kg(value)} Kg"


def celsius_to_fahrenheit(val):
    return (val * 1.8) + 32


def fahrenheit_to_celsius(val):
    return (val - 32) * 0.5556


def kg_to_pound(val):
    return val*2.20462


def pound_to_kg(val):
    return val*0.453592


print(convert_unit('celsius', 'fahrenheit', 12))
print(convert_unit('fahrenheit', 'celsius', 50))
print(convert_unit('kg', 'pound', 71))
print(convert_unit('pound', 'kg', 200))


