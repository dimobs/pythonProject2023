def naughty_or_nice_list(santa_list, *args, **kwargs):
    nice_list, naughty_list = [], []
    results = []

    def place_kid():
        if len(kids) == 1:
            nice_list.append(kids[0][1]) if type_kids == "Nice" else naughty_list.append(kids[0][1])
            santa_list.remove(kids[0])

    for data in args:
        num, type_kids = data.split("-")
        kids = [info for info in santa_list if info[0] == int(num)]
        place_kid()

    for k, v in kwargs.items():
        kids = [info for info in santa_list if info[1] == k]
        place_kid()

    if nice_list:
        results.append(f"Nice: {', '.join(nice_list)}")
    if naughty_list:
        results.append(f"Naughty: {', '.join(naughty_list)}")
    if santa_list:
        results.append(f"Not found: {', '.join(k[1] for k in santa_list)}")

    return "\n".join(results)



print(naughty_or_nice_list(
    [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ],
    "3-Nice", "1-Naughty",
    Amy="Nice", Katy="Naughty", ))