# 11 c -> f, 12 f -> c
# 21EUR, 22UAH, 23USD ----> RUB
# 31kg -> pound, 32pound -> kg

def unit_converter(convert: int, value: int) -> str:
    if convert == 11:
        return f"{value} °C is equal to {(value*1.8)+32} °F"
    elif convert == 12:
        return f"{value} °F is equal to {(value-32)*0.5556} °C"
    elif convert == 21:
        return f"{value} EUR is equal to {value*86.93} RUB"
    elif convert == 22:
        return f"{value} UAH is equal to {value*2.72} RUB"
    elif convert == 23:
        return f"{value} USD is equal to {value*77.37} RUB"
    elif convert == 31:
        return f"{value} Pound is equal to {value*0.453592} kg"
    elif convert == 32:
        return f"{value} kg is equal to {value*2.2046} Pound"
    else:
        return f"I don't understand"


print(unit_converter(11,12))




