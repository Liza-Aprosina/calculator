# калькулятор

import math

from .errors import error


def tokenize(expr):
    tok = []
    i = 0

    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1
            continue
        if c in "+-*/":
            tok.append(c)
            i += 1
            continue
        if "0" <= c <= "9" or c == ".":
            j = i
            dots = 0
            digits = 0
            while i < len(expr) and ("0" <= expr[i] <= "9" or expr[i] == "."):
                if expr[i] == ".":
                    dots += 1
                else:
                    digits += 1
                i += 1
            if dots > 1 or digits == 0:
                raise error("Неверная запись числа")
            tok.append(expr[j:i])
            continue
        raise error(f"Недопустимый символ: {c}")

    return tok


def validate(tok):
    if not tok:
        raise error("Пустое выражение")

    nums = []
    ops = []
    i = 0

    while i < len(tok):
        sign = 1
        while i < len(tok) and tok[i] in "+-":
            if tok[i] == "-":
                sign = -sign
            i += 1

        if i == len(tok) or tok[i] in "+-*/":
            raise error("Пропущен операнд")

        num = sign * float(tok[i])
        if not math.isfinite(num):
            raise error("Слишком большое число")
        nums.append(num)
        i += 1

        if i < len(tok):
            if tok[i] not in "+-*/":
                raise error("Пропущен оператор")
            ops.append(tok[i])
            i += 1
            if i == len(tok):
                raise error("Пропущен операнд")

    return nums, ops


def calculate(expr):
    nums, ops = validate(tokenize(expr))
    total = 0.0
    cur = nums[0]

    for op, num in zip(ops, nums[1:]):
        if op == "+":
            total += cur
            cur = num
        elif op == "-":
            total += cur
            cur = -num
        elif op == "*":
            cur *= num
        else:
            if num == 0:
                raise error("Деление на ноль")
            cur /= num
        if not math.isfinite(cur) or not math.isfinite(total):
            raise error("Слишком большое число")

    res = total + cur
    if not math.isfinite(res):
        raise error("Слишком большое число")
    return res
