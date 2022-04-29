from random import randint


def get_user_number():
    """Get number from user input.

    Check if it is proper number.

    Try until user give proper number.
    """
    while True:
        try:
            user_number = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number!")

    return user_number


def get_draw_number():
    """Get draw number from computer.

    Compare computer number with user number until user guesses computer number.

    Give instruction "Too small" or "Too big".

    Inform user when win with communicate: "You win!"
    """
    draw_number = randint(1, 100)
    given_number = get_user_number()
    while draw_number != given_number:
        if draw_number > given_number:
            print("To small!")
        elif draw_number < given_number:
            print("To big!")
        given_number = get_user_number()
    print("You win!")


if __name__ == '__main__':
    get_draw_number()
