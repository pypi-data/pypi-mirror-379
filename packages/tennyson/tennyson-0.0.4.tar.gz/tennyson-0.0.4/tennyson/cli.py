import click
import tennyson.password

@click.group()
def main():
    """
    CLI tools for tennyson
    """
    pass


@main.command()
def password():
    for p in tennyson.password.for_display_passwords():
        print(p)

@main.command()
def math_quiz():
    import random
    import math
    while True:
        a = math.ceil((10 * random.random())**2)
        b = math.ceil((10 * random.random())**2)
        op = random.choice(['*', '/'])
        if op == '*':
            c = a * b
        if op == '/':
            c = a / b
        print(f'{a} {op} {b}')
        input()
        print(f'{c}')
        input()
