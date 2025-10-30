week = {
    "pn": "poniedziałek",
    "wt": "wtorek",
    "sr": "środa",
    "cz": "czwartek",
    "pt": "piątek",
    "so": "sobota",
    "ni": "niedziela"
}
pory_dnia = {
    "r": "rano",
    "w": "wieczor"
}

def prepare_day_slice(slic):
    if "-" in slic:
        days = slic.split("-")
        week_days = list(week.keys())
        return {week[day] for day in week_days[week_days.index(days[0]):week_days.index(days[1]) + 1]}
    else:

        return [week[slic]]
