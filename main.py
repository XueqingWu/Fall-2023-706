# class TryTesting(TestCase):
#     def test_always_passes(self):
#         self.assertTrue(5 == 5)


def func(x):
    count = 0
    for i in x:
        count += 1
    return count
