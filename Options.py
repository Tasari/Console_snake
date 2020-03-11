import colorama

# The sizes of the map
size_x = 30
size_y = 30
# Map refresh speed in seconds
speed = 1
# Starting lenght not counting the head
lenght = 4
# Symbols have to be 2 characters and between colorama functions
blank_spot = (
    colorama.Fore.BLACK + colorama.Back.BLACK + " " * 2 + colorama.Style.RESET_ALL
)
fruits = {
    "multiply_fruit_symbol": colorama.Fore.CYAN + "░" * 2 + colorama.Style.RESET_ALL,
    "move_blocking_fruit_symbol": colorama.Fore.YELLOW
    + "░" * 2
    + colorama.Style.RESET_ALL,
    "classic_fruit_symbol": colorama.Fore.RED + "░" * 2 + colorama.Style.RESET_ALL,
    "death_fruit_symbol": colorama.Fore.WHITE + "░" * 2 + colorama.Style.RESET_ALL,
    "random_move_symbol": colorama.Fore.MAGENTA + "░" * 2 + colorama.Style.RESET_ALL,
    "speed_fruit_symbol": colorama.Fore.BLUE + "░" * 2 + colorama.Style.RESET_ALL,
}
impassable_symbols = {
    "border_symbol": colorama.Fore.WHITE + "#" * 2 + colorama.Style.RESET_ALL,
    "snake_symbol": colorama.Fore.GREEN + "█" * 2 + colorama.Style.RESET_ALL,
    "left_border": colorama.Fore.WHITE + " #" + colorama.Style.RESET_ALL,
    "right_border": colorama.Fore.WHITE + "# " + colorama.Style.RESET_ALL,
}
