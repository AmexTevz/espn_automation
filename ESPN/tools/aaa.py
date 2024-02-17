import random

teams = 'Napoli, Genoa,Valencia, Manchester United, Newcastle United, Borussia Dortmund, Atalanta'.split(',')
team_list = random.sample(teams,3)

for i in team_list:
    print(i.strip())

for i in team_list:
    print(i)