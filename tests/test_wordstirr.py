"""
Testing base fuctions of the package.
"""

import pytest
from pytest_mock import MockerFixture

from wordstirr import wordstirr


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "abc"),
        ("abcd", "acbd"),
        ("abcde", "adcbe"),
        ("а", "а"),
        ("аб", "аб"),
        ("абв", "абв"),
        ("абвг", "авбг"),
        ("абвгд", "агвбд"),
    ],
)
def test_process_word_correct_input_correct_output(
    mocker: MockerFixture, test_input: str, expected: str
) -> None:
    mocker.patch("random.shuffle", side_effect=list.reverse)
    assert wordstirr._process_word(test_input) == expected


#  def test_tokenize():
#  test_input = """\
#  Test string, for testing text-tokenizer. Some words... More words?!
#  Слова для проверки юникода. <Some-random_text># 3 lines in total ->
#  there's nothing special; Just some more "text".  End."""
#
#  estimated_output = [
#  "Test",
#  " ",
#  "string",
#  ", ",
#  "for",
#  " ",
#  "testing",
#  " ",
#  "text",
#  "-",
#  "tokenizer",
#  ". ",
#  "Some",
#  " ",
#  "words",
#  "... ",
#  "More",
#  " ",
#  "words",
#  "?!\n",
#  "Слова",
#  " ",
#  "для",
#  " ",
#  "проверки",
#  " ",
#  "юникода",
#  ". <",
#  "Some",
#  "-",
#  "random",
#  "_",
#  "text",
#  "># 3 ",
#  "lines",
#  " ",
#  "in",
#  " ",
#  "total",
#  " ->\n",
#  "there",
#  "'",
#  "s",
#  " ",
#  "nothing",
#  " ",
#  "special",
#  "; ",
#  "Just",
#  " ",
#  "some",
#  " ",
#  "more",
#  ''' "''',
#  "text",
#  """".  """,
#  "End",
#  ".",
#  ]
#
#  assert list(wordstirr._tokenize(test_input)) == estimated_output


def test_stirr_text(mocker: MockerFixture) -> None:
    mocker.patch("random.shuffle", side_effect=list.reverse)

    test_input = """\
Test string, for testing text-tokenizer. Some words... More words?!
Слова для проверки юникода. <Some-random_text># 3 lines in total ->
there's nothing special; Just some more "text".  End."""

    estimated_output = """\
Tset snirtg, for tnitseg txet-tezinekor. Smoe wdros... Mroe wdros?!
Свола для пкревори юдокина. <Smoe-rodnam_txet># 3 lenis in tatol ->
trehe's nnihtog saicepl; Jsut smoe mroe "txet".  End."""

    assert wordstirr.text_stirr(test_input) == estimated_output
