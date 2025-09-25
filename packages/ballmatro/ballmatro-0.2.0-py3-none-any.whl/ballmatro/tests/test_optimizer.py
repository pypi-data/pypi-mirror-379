import pytest

from ballmatro.card import Card
from ballmatro.optimizer import brute_force_optimize
from ballmatro.score import Score

test_data = [
    (
        [Card('3♦')],
        Score(input=[Card('3♦')], played=[Card('3♦')])
    ),
    (
        [Card(txt='K♥x'), Card(txt='A♥x')],
        Score(input=[Card(txt='K♥x'), Card(txt='A♥x')], played=[Card(txt='A♥x')])
    ),
    (
        [Card('2♥'), Card('3♦')],
        Score(input=[Card('2♥'), Card('3♦')], played=[Card('3♦')])
    ),
    (
        [Card('2♥'), Card('2♥'), Card('3♦')],
        Score(input=[Card('2♥'), Card('2♥'), Card('3♦')], played=[Card('2♥'), Card('2♥')])
    ),
    (
        [Card('2♥'), Card('2♥'), Card('3♦'), Card('3♦'), Card('A♣')],
        Score(input=[Card('2♥'), Card('2♥'), Card('3♦'), Card('3♦'), Card('A♣')], played=[Card('2♥'), Card('2♥'), Card('3♦'), Card('3♦')])
    ),
    (
        [Card('3♥'), Card('3♦'), Card('3♠'), Card('A♣')],
        Score(input=[Card('3♥'), Card('3♦'), Card('3♠'), Card('A♣')], played=[Card('3♥'), Card('3♦'), Card('3♠')])
    ),
    (
        [Card('3♥'), Card('3♦'), Card('3♠'), Card('A♦'), Card('A♠'), Card('2♥'), Card('2♥')],
        Score(input=[Card('3♥'), Card('3♦'), Card('3♠'), Card('A♦'), Card('A♠'), Card('2♥'), Card('2♥')], played=[Card('3♥'), Card('3♦'), Card('3♠'), Card('A♦'), Card('A♠')])
    ),
    (
        [Card('2♥'), Card('2♥'), Card('3♥'), Card('5♥'), Card('8♥'), Card('J♥')],
        Score(input=[Card('2♥'), Card('2♥'), Card('3♥'), Card('5♥'), Card('8♥'), Card('J♥')], played=[Card('2♥'), Card('3♥'), Card('5♥'), Card('8♥'), Card('J♥')])
    ),
    (
        [Card('2♥'), Card('3♦'), Card('4♠'), Card('5♦'), Card('6♠'), Card('3♦'), Card('3♦')],
        Score(input=[Card('2♥'), Card('3♦'), Card('4♠'), Card('5♦'), Card('6♠'), Card('3♦'), Card('3♦')], played=[Card('2♥'), Card('3♦'), Card('4♠'), Card('5♦'), Card('6♠')])
    ),
    (
        [Card('2♥'), Card('4♥'), Card('3♥'), Card('3♦'), Card('3♠'), Card('3♣'), Card('A♥')],
        Score(input=[Card('2♥'), Card('4♥'), Card('3♥'), Card('3♦'), Card('3♠'), Card('3♣'), Card('A♥')], played=[Card('3♥'), Card('3♦'), Card('3♠'), Card('3♣')])
    ),
    (
        [Card('2♥'), Card('3♥'), Card('4♥'), Card('5♠'), Card('5♥'), Card('6♥'), Card('7♠')],
        Score(input=[Card('2♥'), Card('3♥'), Card('4♥'), Card('5♠'), Card('5♥'), Card('6♥'), Card('7♠')], played=[Card('2♥'), Card('3♥'), Card('4♥'), Card('5♥'), Card('6♥')])
    ),
    (
        [],
        Score(input=[], played=[])
    ),
    (
        [Card("🂿 Banned Red: Played cards of red suit (♥, ♦) will be ignored in poker hand determination and scoring"), Card('2♥'), Card('3♥'), Card('4♥')],
        Score(input=[Card("🂿 Banned Red: Played cards of red suit (♥, ♦) will be ignored in poker hand determination and scoring"), Card('2♥'), Card('3♥'), Card('4♥')], played=[])
    ),
    (
        [Card('6♥x'), Card('4♦x'), Card('6♣+'), Card('K♠+'), Card('A♠+'), Card('Q♠'), Card('Q♠+'), Card('Q♥x')],
        Score(input=[Card('6♥x'), Card('4♦x'), Card('6♣+'), Card('K♠+'), Card('A♠+'), Card('Q♠'), Card('Q♠+'), Card('Q♥x')], played=[Card('Q♠'), Card('Q♠+'), Card('Q♥x'), Card('6♥x'), Card('6♣+')])
    )
]

@pytest.mark.parametrize("cards, expected_score_info", test_data)
def test_brute_force_optimize(cards, expected_score_info):
    """The brute force optimizer can find the best hand for a number of cards"""
    opt = brute_force_optimize(cards)
    assert opt.score == expected_score_info.score
    assert opt.chips == expected_score_info.chips
    assert opt.multiplier == expected_score_info.multiplier
    assert sorted(opt.input) == sorted(expected_score_info.input)
    assert sorted(opt.played) == sorted(expected_score_info.played)
