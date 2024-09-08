import pandas as pd
from datetime import datetime


def calculate_bet_cost(bet_name: str, bet_size: int, number_draws: int):
    """Calculate the bet amount

    Args:
        bet_name (str): post name.
        bet_size (int): total numbers.
        number_draws (int): number of moves.

    Returns:
        The value of the play
    """
    cost = 0

    if bet_name == "duplasena":
        match bet_size:
            case 6:
                cost = 2.5 * number_draws
            case 7:
                cost = 17.5 * number_draws
            case 8:
                cost = 70 * number_draws
            case 9:
                cost = 210 * number_draws
            case 10:
                cost = 525 * number_draws
            case 11:
                cost = 1155 * number_draws
            case 12:
                cost = 2310 * number_draws
            case 13:
                cost = 4290 * number_draws
            case 14:
                cost = 7507.5 * number_draws
            case 15:
                cost = 12512.5 * number_draws

    elif bet_name == "lotofacil":
        match bet_size:
            case 15:
                cost = 3 * number_draws
            case 16:
                cost = 48 * number_draws
            case 17:
                cost = 408 * number_draws
            case 18:
                cost = 2448 * number_draws
            case 19:
                cost = 11628 * number_draws
            case 20:
                cost = 46512 * number_draws

    elif bet_name == "megasena":
        match bet_size:
            case 6:
                cost = 5 * number_draws
            case 7:
                cost = 35 * number_draws
            case 8:
                cost = 140 * number_draws
            case 9:
                cost = 420 * number_draws
            case 10:
                cost = 1050 * number_draws
            case 11:
                cost = 2310 * number_draws
            case 12:
                cost = 4620 * number_draws
            case 13:
                cost = 8580 * number_draws
            case 14:
                cost = 15015 * number_draws
            case 15:
                cost = 25025 * number_draws

    elif bet_name == "quina":
        match bet_size:
            case 5:
                cost = 2.5 * number_draws
            case 6:
                cost = 15 * number_draws
            case 7:
                cost = 52.5 * number_draws
            case 8:
                cost = 140 * number_draws
            case 9:
                cost = 315 * number_draws
            case 10:
                cost = 630 * number_draws
            case 11:
                cost = 1155 * number_draws
            case 12:
                cost = 1980 * number_draws
            case 13:
                cost = 3217.5 * number_draws
            case 14:
                cost = 5005 * number_draws
            case 15:
                cost = 7507.5 * number_draws

    return f"R$ {cost:.2f}".replace(".", ",")


def save_data(data: dict, path):
    """Generates a table and saves the data to the specified path.

    Args:
        data (dict): Dictionary for table generation.
        path (_type_): Path to save the table.
    """
    df = pd.DataFrame(data)
    df.to_excel(f"{path}{(datetime.now().strftime('%d-%m-%Y %H-%M-%S'))}.xlsx")
