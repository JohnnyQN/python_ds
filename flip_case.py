def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
to_swap_lower = to_swap.lower()
to_swap_upper = to_swap.upper()

result = []

for char in phrase:
    if char == to_swap_lower:
        result.append(char.upper())
    elif char == to_swap_upper:
        result.append(char.lower())
    else:
        result.append(char)

return ''.join(result)