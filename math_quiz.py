import random


def function_A(min, max):
    """
    Gives a Random integer b/n min_value and max_value.
    """
    return random.randint(min, max)


def function_B():
    """
    Gives a random arithmetic operator from '+', '-', or '*'.
    Returns:
        str: A randomly chosen operator.
    """
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    """
    Creates a math problem and calculates the correct solution.

    Args:
        n1 = first num
        n2 = second num
        operator = Arithmetic Operation from function_B
    Returns:
        tuple: A string showing the math problem and the correct answer as an integer.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    #Runs a simple math quiz game where the user is asked to solve math problems and is scored on it.
    s = 0
    #t_q = 3.14159265359 -> Needs to be integer
    t_q = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = function_A(1, 10); n2 = function_A(1, 5); o = function_B()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
