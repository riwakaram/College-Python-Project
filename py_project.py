import functions

# reading and printing the array
wCups = functions.readFromCSVFile('WorldCups.csv')
functions.printFormattedTable(wCups)

# plot for attendances
attendance = functions.removeDotsFromAttendance(wCups)
functions.plotAttendanceVersusYears(wCups, attendance)
functions.polyFitAndInterpAttendance(wCups, attendance)

# plot for goals scored
functions.plotGoalsScoredVersusYears(wCups)
functions.polyFitAndInterpGoals(wCups)

# plot for qualified teams
functions.plotQualifiedTeamsVersusYears(wCups)

# plot for matches played
functions.plotMatchesPlayedVersusYears(wCups)

# plot for wins
functions.plotWinsByCountry(wCups)

# plot for runner-ups
functions.plotRunnerUpsByCountry(wCups)

# plot for thirds
functions.plotThirdsByCountry(wCups)

# plot for fourths
functions.plotFourthsByCountry(wCups)
