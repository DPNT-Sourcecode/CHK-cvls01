import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute('a', 'b') == 4
        print('Done')


