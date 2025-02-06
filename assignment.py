def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(value):
    return "Greater" if value > 10 else "Less or Equal"

def loop_sum(n):
    return sum(range(1, n + 1))

def list_operations(lst):
    return sum(lst), max(lst), min(lst)

def dict_operations(students):
    return {name for name, score in students.items() if score > 80}

def set_operations(set1, set2):
    return set(set1) & set(set2)

def arithmetic_ops(a, b):
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b
    }

def logical_ops(a, b):
    return {
        "and": a and b,
        "or": a or b,
        "not_a": not a,
        "not_b": not b
    }

def bitwise_ops(a, b):
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }
