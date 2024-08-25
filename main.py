import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        # Создаем бегунов с разными скоростями
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        # Выводим результаты после всех тестов
        for key in sorted(cls.all_results.keys()):
            finishers = cls.all_results[key]
            formatted_output = ', '.join(f"{place}: {runner}" for place, runner in finishers.items())
            print(f"{{{formatted_output}}}")

    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(results[len(results)].name, "Ник")  # Проверяем, что Ник последний

    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(results[len(results)].name, "Ник")  # Проверяем, что Ник последний

    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nik)
        results = tournament.start()
        self.all_results[len(self.all_results) + 1] = results
        self.assertEqual(results[len(results)].name, "Ник")  # Проверяем, что Ник последний


# Запуск тестов
if __name__ == '__main__':
    unittest.main()