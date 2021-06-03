def parse(path):
    customRules = []
    with open(path) as fp:
        for _, line in enumerate(fp):
            customRules.append(line)
    return customRules