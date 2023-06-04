def get_char_best_result(half, char):
    best_result = 0
    current = 0
    for ch in half:
        if ch == char:
            current = current + 1
        else:
            best_result = current = max(best_result, current)
            current = 0

    return max(best_result, current)

tickets = [ticket.strip() for ticket in input().split(', ')]
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    if len(ticket) != 20:
        print('invalird ticket')
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]

    best_result = 0
    best_sumbol = ""

    for symbol in symbols:
        left_part_score = get_char_best_result(left_part, symbol)
        right_part_score = get_char_best_result(right_part, symbol)
        overall_result = min(left_part_score, right_part_score)

        if overall_result > best_result:
            best_result = overall_result
            best_symbol = symbol

        is_winning = best_result >= 6
        is_jackpot = is_winning and best_result == 10
        if is_jackpot:
            print(f'ticket "{ticket}" - {best_result}-{best_symbol} Jakpot!')
        elif is_winning:
            print(f'ticket "{ticket}" - {best_result}-{best_symbol}')