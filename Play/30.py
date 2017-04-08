dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(input):
    return (map(lambda x: dict[x.lower()], input))


print(translate(["merry", "new"]))