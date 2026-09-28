# переводчик

import math

from .errors import error

LEN = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
MASS = {"g": 0.001, "kg": 1.0}
TEMP = {"c", "f", "k"}


def convert(v, pred, sled):
    pred = pred.lower()
    sled = sled.lower()

    if not math.isfinite(v):
        raise error("Неверное числовое значение")
    if pred not in LEN and pred not in MASS and pred not in TEMP:
        raise error(f"Неизвестная единица: {pred}")
    if sled not in LEN and sled not in MASS and sled not in TEMP:
        raise error(f"Неизвестная единица: {sled}")

    if pred in LEN and sled in LEN:
        res = v * LEN[pred] / LEN[sled]
    elif pred in MASS and sled in MASS:
        res = v * MASS[pred] / MASS[sled]
    elif pred in TEMP and sled in TEMP:
        if pred == "c":
            k = v + 273.15
        elif pred == "f":
            k = (v + 459.67) * 5 / 9
        else:
            k = v

        if k < 0:
            raise error("Температура ниже абсолютного нуля")
        if sled == "c":
            res = k - 273.15
        elif sled == "f":
            res = k * 9 / 5 - 459.67
        else:
            res = k
    else:
        raise error("Несовместимые единицы")

    if not math.isfinite(res):
        raise error("Слишком большое число")
    return float(res)
