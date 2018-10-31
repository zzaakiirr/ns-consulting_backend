def get_total_votes_count(poll, choices):
    total_votes_count = 0
    for choice in choices:
        total_votes_count += choice.votes
    return total_votes_count


def update_percents(poll):
    choices = poll.choice_set.all()
    total_votes_count = get_total_votes_count(poll, choices)
    total_percentage = 0
    max_percentage_choice = None

    for choice in choices:
        if not max_percentage_choice:
            max_percentage_choice = choice

        choice.percent = round(choice.votes / total_votes_count * 100)
        choice.save()

        total_percentage += choice.percent
        if choice.percent > max_percentage_choice.percent:
            max_percentage_choice = choice

    change_total_percentage_to_100(max_percentage_choice, total_percentage)


def change_total_percentage_to_100(max_percentage_choice, total_percentage):
    if total_percentage == 98:
        max_percentage_choice.percent += 2
    elif total_percentage == 99:
        max_percentage_choice.percent += 1
    elif total_percentage == 101:
        max_percentage_choice.percent -= 1
    elif total_percentage == 102:
        max_percentage_choice.percent -= 2
    max_percentage_choice.save()
