from random import sample


def generate_numbers_duplasena(number_draws: int = 1, betsize: int = 6):
    """Generates doublesena games according to the established parameters.

    Args:
        number_draws (int, optional): Receives the number of moves. Defaults to 1.
        betsize (int, optional): Receives the number of numbers. Defaults to 6.

    Returns:
        dict: returns a dictionary with all computed moves.
    """
    bet = {}

    for value in range(1, number_draws + 1):
        play = sample(range(1, 51), betsize)
        bet[f"Sorteio {value}"] = play

    return bet


def generate_numbers_lotofacil(number_draws: int = 1, betsize: int = 15):
    """Generates lotofacil games according to the established parameters.

    Args:
        number_draws (int, optional): Receives the number of moves. Defaults to 1.
        betsize (int, optional): Receives the number of numbers. Defaults to 6.

    Returns:
        dict: returns a dictionary with all computed moves.
    """
    bet = {}

    for value in range(1, number_draws + 1):
        play = sample(range(1, 26), betsize)
        bet[f"Sorteio {value}"] = play

    return bet


def generate_numbers_megasena(number_draws: int = 1, betsize: int = 6):
    """Generates megasena games according to the established parameters.

    Args:
        number_draws (int, optional): Receives the number of moves. Defaults to 1.
        betsize (int, optional): Receives the number of numbers. Defaults to 6.

    Returns:
        dict: returns a dictionary with all computed moves.
    """
    bet = {}

    for value in range(1, number_draws + 1):
        play = sample(range(1, 61), betsize)
        bet[f"Sorteio {value}"] = play

    return bet


def generate_numbers_quina(number_draws: int = 1, betsize: int = 5):
    """Generates quina games according to the established parameters.

    Args:
        number_draws (int, optional): Receives the number of moves. Defaults to 1.
        betsize (int, optional): Receives the number of numbers. Defaults to 6.

    Returns:
        dict: returns a dictionary with all computed moves.
    """
    bet = {}

    for value in range(1, number_draws + 1):
        play = sample(range(1, 81), betsize)
        bet[f"Sorteio {value}"] = play

    return bet
