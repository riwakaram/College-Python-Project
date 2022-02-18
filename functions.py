def readFromCSVFile(filename):
    import csv
    import numpy as np

    with open(filename, newline='') as csvfile:
        temp = list(csv.reader(csvfile))

    a = np.array(temp)
    return a


def printFormattedTable(wcups):
    row, col = wcups.shape
    year, country, winner, runup, third, fourth, goals, teams, matches, attendance = wcups[0]
    print("{:<6}{:<14}{:<12}{:<17}{:<14}{:<17}{:<15}{:<18}{:<17}{:<13}".format(year, country, winner,
                                                                               runup, third, fourth,
                                                                               goals, teams, matches,
                                                                               attendance))
    for i in range(0, 140):
        print('-', end='')
    print()
    for i in range(1, row):
        year, country, winner, runup, third, fourth, goals, teams, matches, attendance = wcups[i]
        print("{:<6}{:<14}{:<12}{:<17}{:<14}{:<17}{:>11}{:>18}{:>17}{:>14}".format(year, country, winner,
                                                                                   runup, third, fourth,
                                                                                   goals, teams, matches,
                                                                                   attendance))


def removeDotsFromAttendance(attendance):
    a = attendance[1:, 9]

    for i in range(0, 3):
        temp = a[i]
        t = temp.split('.')
        a[i] = t[0] + t[1]

    temp = a[3]
    t = temp.split('.')
    a[3] = t[0] + t[1] + t[2]

    for i in range(4, 7):
        temp = a[i]
        t = temp.split('.')
        a[i] = t[0] + t[1]

    for i in range(7, 20):
        temp = a[i]
        t = temp.split('.')
        a[i] = t[0] + t[1] + t[2]

    return a


def convertToIntegerList(l):
    a_list = list(l)
    a_list = [int(i) for i in a_list]
    return a_list


def plotAttendanceVersusYears(wcups, attendance):
    years = wcups[1:, 0]
    attendance_int = convertToIntegerList(attendance)
    from matplotlib import pylab
    pylab.plot(years, attendance_int, 'r')
    pylab.plot(years, attendance_int, 'ko')
    pylab.xticks(rotation=90)
    import numpy as np
    pylab.yticks(np.arange(0, 4.5 * 1e6, 0.3 * 1e6))
    pylab.ylabel('Attendance (in million)')
    pylab.grid()
    pylab.title('Attendance Throughout The Years')
    pylab.savefig('Attendance.pdf')
    pylab.show()


def polyFitAndInterpAttendance(wcups, attendance):
    years = wcups[1:, 0]
    temp1 = convertToIntegerList(attendance)
    temp2 = convertToIntegerList(years)

    import numpy as np
    a = np.array(temp1)
    y = np.array(temp2)
    z = np.polyfit(y, a, 3)
    p = np.poly1d(z)
    ys = [p(x) for x in y]

    from matplotlib import pylab
    figure, axis = pylab.subplots(2, 2)
    figure.suptitle('Attendance: Polynomial Fitting and Interpolation Graphs', fontsize=16)
    axis[0, 0].plot(y, a, 'ro')
    axis[0, 0].set_title('Data')
    axis[0, 1].plot(y, ys, 'k')
    axis[0, 1].set_title('Fitted Curve')
    from scipy.interpolate import interp1d
    f1 = interp1d(y, a, kind='linear')
    axis[1, 0].plot(y, f1(y), 'g--')
    axis[1, 0].set_title('Linear Interpolation')
    f2 = interp1d(y, a, kind='cubic')
    axis[1, 1].plot(y, f2(y), 'y-.')
    axis[1, 1].set_title('Cubic Interpolation')
    pylab.tight_layout()
    figure.subplots_adjust(top=0.88)
    pylab.savefig('PolyFitAndInterpAttendance.pdf')
    pylab.show()


def plotGoalsScoredVersusYears(wcups):
    years = wcups[1:, 0]
    goals = wcups[1:, 6]
    goals_list = convertToIntegerList(goals)
    from matplotlib import pylab
    pylab.plot(years, goals_list, 'r')
    pylab.plot(years, goals_list, 'ko')
    pylab.xticks(rotation=90)
    import numpy as np
    pylab.yticks(np.arange(70, 175, 5))
    pylab.ylabel('Goals Scored')
    pylab.grid()
    pylab.title('Goals Scored Throughout The Years')
    pylab.savefig('GoalsScored.pdf')
    pylab.show()


def polyFitAndInterpGoals(wcups):
    years = wcups[1:, 0]
    goals = wcups[1:, 6]
    temp1 = convertToIntegerList(goals)
    temp2 = convertToIntegerList(years)

    import numpy as np
    a = np.array(temp1)
    y = np.array(temp2)
    z = np.polyfit(y, a, 3)
    p = np.poly1d(z)
    ys = [p(x) for x in y]

    from matplotlib import pylab
    figure, axis = pylab.subplots(2, 2)
    figure.suptitle('Goals Scored: Polynomial Fitting and Interpolation Graphs', fontsize=16)
    axis[0, 0].plot(y, a, 'ro')
    axis[0, 0].set_title('Data')
    axis[0, 1].plot(y, ys, 'k')
    axis[0, 1].set_title('Fitted Curve')
    from scipy.interpolate import interp1d
    f1 = interp1d(y, a, kind='linear')
    axis[1, 0].plot(y, f1(y), 'g--')
    axis[1, 0].set_title('Linear Interpolation')
    f2 = interp1d(y, a, kind='cubic')
    axis[1, 1].plot(y, f2(y), 'y-.')
    axis[1, 1].set_title('Cubic Interpolation')
    pylab.tight_layout()
    figure.subplots_adjust(top=0.88)
    pylab.savefig('PolyFitAndInterpGoals.pdf')
    pylab.show()


def plotQualifiedTeamsVersusYears(wcups):
    years = wcups[1:, 0]
    teams = wcups[1:, 7]
    teams_list = convertToIntegerList(teams)
    from matplotlib import pylab
    pylab.plot(years, teams_list, 'r')
    pylab.plot(years, teams_list, 'ko')
    pylab.xticks(rotation=90)
    import numpy as np
    pylab.yticks(np.arange(12, 36, 2))
    pylab.ylabel('Qualified Teams')
    pylab.grid()
    pylab.title('Number of Qualified Teams Throughout The Years')
    pylab.savefig('QualifiedTeams.pdf')
    pylab.show()


def plotMatchesPlayedVersusYears(wcups):
    years = wcups[1:, 0]
    matches = wcups[1:, 8]
    matches_list = convertToIntegerList(matches)
    from matplotlib import pylab
    pylab.plot(years, matches_list, 'r')
    pylab.plot(years, matches_list, 'ko')
    pylab.xticks(rotation=90)
    import numpy as np
    pylab.yticks(np.arange(17, 64, 2))
    pylab.ylabel('Matches Played')
    pylab.grid()
    pylab.title('Number of Matches Played Throughout The Years')
    pylab.savefig('MatchesPlayed.pdf')
    pylab.show()


def convertToStringList(l):
    a_list = list(l)
    a_list = [str(i) for i in a_list]
    return a_list


def plotWinsByCountry(wcups):
    wins_list = convertToStringList(wcups[1:, 2])

    uru_wins = wins_list.count('Uruguay')
    ita_wins = wins_list.count('Italy')
    ger_wins = wins_list.count('Germany FR') + wins_list.count('Germany')
    braz_wins = wins_list.count('Brazil')
    eng_wins = wins_list.count('England')
    arg_wins = wins_list.count('Argentina')
    fra_wins = wins_list.count('France')
    spa_wins = wins_list.count('Spain')

    countries = ['Uruguay', 'Italy', 'Germany', 'Brazil', 'England', 'Argentina', 'France', 'Spain']
    wins = [uru_wins, ita_wins, ger_wins, braz_wins, eng_wins, arg_wins, fra_wins, spa_wins]

    from matplotlib import pylab
    pylab.stem(countries, wins)
    pylab.ylabel('Number of Wins')
    import numpy as np
    pylab.yticks(np.arange(0, 6, 1))
    pylab.xticks(rotation=90)
    pylab.tight_layout()
    pylab.title('Number of Wins by Country', y=0.98)
    pylab.savefig('WinsByCountry.pdf', bbox_inches='tight')
    pylab.show()


def plotRunnerUpsByCountry(wcups):
    runnerups_list = convertToStringList(wcups[1:, 3])

    arg_runnerups = runnerups_list.count('Argentina')
    cze_runnerups = runnerups_list.count('Czechoslovakia')
    hun_runnerups = runnerups_list.count('Hungary')
    braz_runnerups = runnerups_list.count('Brazil')
    swe_runnerups = runnerups_list.count('Sweden')
    ger_runnerups = runnerups_list.count('Germany FR') + runnerups_list.count('Germany')
    ita_runnerups = runnerups_list.count('Italy')
    neth_runnerups = runnerups_list.count('Netherlands')
    fra_runnerups = runnerups_list.count('France')

    countries = ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Sweden', 'Germany', 'Italy', 'Netherlands',
                 'France']
    runnerups = [arg_runnerups, cze_runnerups, hun_runnerups, braz_runnerups, swe_runnerups, ger_runnerups,
                 ita_runnerups,
                 neth_runnerups, fra_runnerups]

    from matplotlib import pylab
    pylab.stem(countries, runnerups)
    pylab.ylabel('Number of Runner-Up Occurrences')
    import numpy as np
    pylab.yticks(np.arange(0, 6, 1))
    pylab.xticks(rotation=90)
    pylab.tight_layout()
    pylab.title('Number of Runner-Up Occurrences by Country ', y=0.98)
    pylab.savefig('RunnerUpsByCountry.pdf', bbox_inches='tight')
    pylab.show()


def plotThirdsByCountry(wcups):
    thirds_list = convertToStringList(wcups[1:, 4])

    USA_thirds = thirds_list.count('USA')
    ger_thirds = thirds_list.count('Germany FR') + thirds_list.count('Germany')
    braz_thirds = thirds_list.count('Brazil')
    swe_thirds = thirds_list.count('Sweden')
    aus_thirds = thirds_list.count('Austria')
    fra_thirds = thirds_list.count('France')
    chi_thirds = thirds_list.count('Chile')
    por_thirds = thirds_list.count('Portugal')
    pol_thirds = thirds_list.count('Poland')
    ita_thirds = thirds_list.count('Italy')
    cro_thirds = thirds_list.count('Croatia')
    tur_thirds = thirds_list.count('Turkey')
    neth_thirds = thirds_list.count('Netherlands')

    countries = ['USA', 'Germany', 'Brazil', 'Sweden', 'Austria', 'France', 'Chile', 'Portugal',
                 'Poland', 'Italy', 'Croatia', 'Turkey', 'Netherlands']
    thirds = [USA_thirds, ger_thirds, braz_thirds, swe_thirds, aus_thirds, fra_thirds, chi_thirds, por_thirds,
              pol_thirds,
              ita_thirds, cro_thirds, tur_thirds, neth_thirds]

    from matplotlib import pylab
    pylab.stem(countries, thirds)
    pylab.ylabel('Number of Third Place Occurrences')
    import numpy as np
    pylab.yticks(np.arange(0, 6, 1))
    pylab.xticks(rotation=90)
    pylab.tight_layout()
    pylab.title('Number of Third Place Occurrences by Country ', y=0.98)
    pylab.savefig('ThirdsByCountry.pdf', bbox_inches='tight')
    pylab.show()


def plotFourthsByCountry(wcups):
    fourths_list = convertToStringList(wcups[1:, 5])

    yugo_fourths = fourths_list.count('Yugoslavia')
    aus_fourths = fourths_list.count('Austria')
    swe_fourths = fourths_list.count('Sweden')
    spa_fourths = fourths_list.count('Spain')
    uru_fourths = fourths_list.count('Uruguay')
    ger_fourths = fourths_list.count('Germany FR') + fourths_list.count('Germany')
    SU_fourths = fourths_list.count('Soviet Union')
    braz_fourths = fourths_list.count('Brazil')
    ita_fourths = fourths_list.count('Italy')
    fra_fourths = fourths_list.count('France')
    belg_fourths = fourths_list.count('Belgium')
    eng_fourths = fourths_list.count('England')
    bulg_fourths = fourths_list.count('Bulgaria')
    neth_fourths = fourths_list.count('Netherlands')
    KR_fourths = fourths_list.count('Korea Republic')
    por_fourths = fourths_list.count('Portugal')

    countries = ['Yugoslavia', 'Austria', 'Sweden', 'Spain', 'Uruguay', 'Germany', 'Soviet Union', 'Brazil',
                 'Italy', 'France', 'Belgium', 'England', 'Bulgaria', 'Netherlands', 'Korea Republic', 'Portugal']
    fourths = [yugo_fourths, aus_fourths, swe_fourths, spa_fourths, uru_fourths, ger_fourths, SU_fourths, braz_fourths,
               ita_fourths, fra_fourths, belg_fourths, eng_fourths, bulg_fourths, neth_fourths, KR_fourths, por_fourths]

    from matplotlib import pylab
    pylab.stem(countries, fourths)
    pylab.ylabel('Number of Fourth Place Occurrences')
    import numpy as np
    pylab.yticks(np.arange(0, 4, 1))
    pylab.xticks(rotation=90)
    pylab.tight_layout()
    pylab.title('Number of Fourth Place Occurrences by Country ', y=0.98)
    pylab.savefig('FourthsByCountry.pdf', bbox_inches='tight')
    pylab.show()
