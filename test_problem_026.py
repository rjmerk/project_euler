from pytest import mark

from problem_026 import recurring_cycle_length


@mark.parametrize('d, cycle_length', [
    (3, 1),
    (6, 1),
    (7, 6),
    (9, 1),
])
def test_recurring_cycle_length(d, cycle_length):
    assert recurring_cycle_length(d) == cycle_length


