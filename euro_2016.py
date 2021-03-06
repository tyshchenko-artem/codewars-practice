def uefa_euro_2016(teams, scores):
    if scores[0] > scores[1]:
        return "At match {0} - {1}, {0} won !".format(teams[0], teams[1])
    elif scores[0] < scores[1]:
        return "At match {0} - {1}, {1} won !".format(teams[0], teams[1])
    elif scores[0] == scores[1]:
        return "At match {0} - {1}, teams played draw".format(teams[0], teams[1])

#test
print(uefa_euro_2016(['Germany', 'Ukraine'], [2, 0]))
print(uefa_euro_2016(['Belgium', 'Italy'], [0, 2]))
print(uefa_euro_2016(['Republic of Ireland', 'Sweden'], [0, 0]))