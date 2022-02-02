def convert_unit(frm: str, to: str, value: float) -> float:
    frm, to = frm.lower(), to.lower()

    if frm == 'celsius' and to == 'fahrenheit':
        return round((value * 1.8) + 32, 2)

    if frm == 'fahrenheit' and to == 'celsius':
        return round((value - 32) * 0.5556, 2)

    if frm == 'kg' and to == 'pound':
        return round(value * 2.20462, 3)

    if frm == 'pound' and to == 'kg':
        return round(value * 0.453592, 3)

    raise AttributeError("Unknown units")


def conversion_result(frm: str, to: str, value: float) -> str:
    return f"{value} {frm} is equal to {convert_unit(frm, to, value)} {to}"
