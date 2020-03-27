OPERATORS = ["+", "-", "/", "*"];
CONDITIONS = ["<", ">", "="];
import operator

ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul, "=": operator.eq,
       "<": operator.lt, ">": operator.gt}


def calculate(operationStr):
    operations = operationStr.split(" ")
    tmp_g, tmp_d = None, None;
    for c in operations:
        if c == ' ':
            continue;
        if c not in OPERATORS and c not in CONDITIONS:
            if tmp_g is None:
                tmp_g = int(c);
            else:
                tmp_d = int(c);
        else:
            tmp_g = ops[c](tmp_g, tmp_d);
    return tmp_g;

print(calculate("12 4 - 2 * 16 ="))
