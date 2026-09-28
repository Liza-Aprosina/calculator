# команды из терминала

import argparse
import sys
from collections.abc import Sequence

from .calculator import calculate
from .converter import convert
from .errors import error


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="toolkit")
    cmds = parser.add_subparsers(dest="cmd", required=True)

    calc_p = cmds.add_parser("calc", help="вычислить выражение")
    calc_p.add_argument("expr", help="выражение в кавычках")

    conv_p = cmds.add_parser("convert", help="перевести величину")
    conv_p.add_argument("value", type=float)
    conv_p.add_argument("--from", dest="src", required=True)
    conv_p.add_argument("--to", dest="dst", required=True)

    args = parser.parse_args(argv)

    try:
        if args.cmd == "calc":
            res = calculate(args.expr)
        else:
            res = convert(args.value, args.src, args.dst)
    except error as err:
        print(f"Ошибка: {err}", file=sys.stderr)
        return 2

    print(res)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
