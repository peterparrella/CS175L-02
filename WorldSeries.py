#Peter Parrella
#CS175L-02
#WorldSeries

    # Open the WorldSeriesWinner.txt file and read all the lines
with open('WorldSeriesWinners.txt', 'r') as f:
    lines = f.readlines()

# Create a dictionary to store the team names and the number of times they won
team_wins = {}
for line in lines:
    team = line.strip()
    if team not in team_wins:
        team_wins[team] = 1
    else:
        team_wins[team] += 1

# Ask the user to enter a team name or quit
while True:
    team = input("Enter the name of the team or Quit: ")
    if team.lower() == "quit":
        break
    if team in team_wins:
        print(f"The {team} won the World Series {team_wins[team]} times between 1903 and 2009")
    else:
        print("Team not found")
        
