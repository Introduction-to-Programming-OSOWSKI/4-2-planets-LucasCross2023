def planets(p):
    if p == "mercury":
        return 1
    if p == "venus":
        return 2
    if p == "earth":
        return 3
    if p == "mars":
        return 4
    if p == "jupiter":
        return 5
    if p == "saturn":
        return 6
    if p == "uranus":
        return 7
    if p == "neptune":
        return 8
    else:
        return (p) + (" is not a planet")

print(planets("mercury"))
