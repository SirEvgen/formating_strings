class Team1:
    def __init__(self, name1="Мастера Кода", team1=5, tasks1=42, time1=1895.5):
        self.name1 = name1
        self.team1 = team1
        self.tasks1 = tasks1
        self.time1 = time1
        super().__init__()

    def result_challenge1(self):
        print('В команде %(name)s участников %(team)s' % {'name': self.name1, 'team': self.team1})
        print('Команда {team} решила задач: {tasks}'.format(team=self.name1, tasks=self.tasks1))


class Team2:
    def __init__(self, name2="Волшебники Исключений", team2=6, tasks2=40, time2=2234.3):
        self.name2 = name2
        self.team2 = team2
        self.tasks2 = tasks2
        self.time2 = time2

    def result_challenge2(self):
        print('В команде %(name)s участников %(team)s' % {'name': self.name2, 'team': self.team2})
        print('Команда {team} решила задачи за {time}'.format(team=self.name2, time=self.time2))


class OverallResult(Team1, Team2):

    def result_overall(self):
        print(f'Команды решили {self.tasks1} и {self.tasks2} задач')
        if self.tasks1 > self.tasks2 and self.time1 <= self.time2:
            print(f'Результат битвы: победа команды {self.name1}')
        else:
            print(f'Результат битвы: победа команды {self.name2}')
        print(f'Сегодня было решено {self.tasks1 + self.tasks2} задач, в среднем по {round((self.time1 / 
                                                self.tasks1) + (self.time2 / self.tasks2), 2)}'
                                                f' секунды на задачу')


team_1 = Team1()
team_2 = Team2()
res_ov = OverallResult()
team_1.result_challenge1()
team_2.result_challenge2()
res_ov.result_overall()
