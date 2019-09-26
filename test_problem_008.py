from pytest import mark

from problem_009 import find_pythagorean_triplet_summing_up_to


@mark.parametrize("n, triplet", [
    (3 + 4 + 5, (3, 4, 5)),
    (20 + 21 + 29, (20, 21, 29)),
    (37 + 684 + 685, (37, 684, 685)),
])
def test_tripled(n, triplet):
    assert find_pythagorean_triplet_summing_up_to(n) == triplet
