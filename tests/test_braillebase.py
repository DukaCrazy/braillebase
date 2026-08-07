"""Tests for the braillebase package.

Covers the registry, mapping, translate, and output groups, plus the
English ``bbe`` subclass and the regression fixes:
  - ``__token_size`` initialization (was shadowed by ``configure_token = 12``)
  - reverse-braille index in ``translate_text_to_full_list``
  - well-formed HTML tables in ``output_all_html``
"""
import json
import xml.etree.ElementTree as ET

import pytest

import braillebase
from braillebase import BrailleBase, bbe


class TestConstructor:
    def test_instantiate_base(self):
        bb = BrailleBase()
        assert bb is not None

    def test_token_size_defaults_to_12(self):
        bb = BrailleBase()
        assert bb._BrailleBase__token_size == 12

    def test_configure_token_changes_size(self):
        bb = BrailleBase()
        bb.configure_token(5)
        assert bb._BrailleBase__token_size == 5

    def test_configure_token_validation(self):
        bb = BrailleBase()
        with pytest.raises(TypeError):
            bb.configure_token("12")
        with pytest.raises(ValueError):
            bb.configure_token(0)

    def test_translate_does_not_crash(self):
        # Regression: every translate method used to raise AttributeError
        # because __token_size was never initialized.
        bb = bbe()
        assert bb.translate_text_to_braille("a") == ["⠁"]

    def test_base_registers_all_64_cells(self):
        bb = BrailleBase()
        assert len(bb.get_registered_letters()) == 86


class TestRegistry:
    def test_append_and_get(self):
        bb = BrailleBase()
        bb.append_braille_letter("x", ["⠭"])
        assert bb.get_brailles_with_letter("x") == ["⠭"]

    def test_append_overwrites(self):
        bb = BrailleBase()
        bb.append_braille_letter("x", ["⠭"])
        bb.append_braille_letter("x", ["⠮"])
        assert bb.get_brailles_with_letter("x") == ["⠮"]

    def test_append_invalid_letter_type(self):
        bb = BrailleBase()
        with pytest.raises(TypeError):
            bb.append_braille_letter(1, ["⠁"])

    def test_append_empty_letter(self):
        bb = BrailleBase()
        with pytest.raises(ValueError):
            bb.append_braille_letter("", ["⠁"])

    def test_append_invalid_braille_list_type(self):
        bb = BrailleBase()
        with pytest.raises(TypeError):
            bb.append_braille_letter("x", "⠭")

    def test_append_invalid_braille_item(self):
        bb = BrailleBase()
        with pytest.raises(TypeError):
            bb.append_braille_letter("x", [1])
        with pytest.raises(ValueError):
            bb.append_braille_letter("x", ["a"])
        with pytest.raises(ValueError):
            bb.append_braille_letter("x", ["\u2840"])

    def test_get_unregistered_raises(self):
        bb = BrailleBase()
        with pytest.raises(KeyError):
            bb.get_brailles_with_letter("zz")

    def test_has_letter(self):
        bb = BrailleBase()
        assert bb.has_letter("⠁")
        assert not bb.has_letter("zz")

    def test_remove_letter(self):
        bb = BrailleBase()
        bb.append_braille_letter("x", ["⠭"])
        assert bb.remove_letter("x") is True
        assert not bb.has_letter("x")
        assert bb.remove_letter("x") is False

    def test_edit_braille_letter(self):
        bb = BrailleBase()
        bb.append_braille_letter("x", ["⠭"])
        bb.edit_braille_letter("x", ["⠮"])
        assert bb.get_brailles_with_letter("x") == ["⠮"]

    def test_edit_unregistered_raises(self):
        bb = BrailleBase()
        with pytest.raises(KeyError):
            bb.edit_braille_letter("zz", ["⠁"])

    def test_append_multiple(self):
        bb = BrailleBase()
        bb.append_multiple_braille_letters({"x": ["⠭"], "y": ["⠽"]})
        assert bb.get_brailles_with_letter("x") == ["⠭"]
        assert bb.get_brailles_with_letter("y") == ["⠽"]

    def test_append_multiple_invalid_type(self):
        bb = BrailleBase()
        with pytest.raises(TypeError):
            bb.append_multiple_braille_letters([("x", ["⠭"])])

    def test_special_rules_types(self):
        bb = BrailleBase()
        bb.append_braille_letter("Q", ["⠟"], 1)
        assert bb.has_letter("Q", 1)
        assert "Q" in bb.get_registered_letters(1)


class TestMapping:
    def test_get_braille_to_index(self):
        bb = BrailleBase()
        assert bb.get_braille_to_index("⠀") == 0
        assert bb.get_braille_to_index("⠁") == 1
        assert bb.get_braille_to_index("⠿") == 63

    def test_index_to_braille(self):
        bb = BrailleBase()
        assert bb.get_index_to_braille(0) == "⠀"
        assert bb.get_index_to_braille(63) == "⠿"

    def test_roundtrip_all_64(self):
        bb = BrailleBase()
        for i in range(64):
            assert bb.get_braille_to_index(bb.get_index_to_braille(i)) == i

    def test_list_to_index_list(self):
        bb = BrailleBase()
        assert bb.get_braille_list_to_index_list(["⠁", "⠃"]) == [1, 3]


class TestTranslate:
    def test_text_to_braille(self):
        bb = bbe()
        assert bb.translate_text_to_braille("a") == ["⠁"]
        assert bb.translate_text_to_braille("Hi") == ["⠠", "⠓", "⠊"]

    def test_text_to_index(self):
        bb = bbe()
        assert bb.translate_text_to_index("Hi") == [32, 19, 10]

    def test_text_to_binary_string(self):
        bb = bbe()
        assert bb.translate_text_to_binary_string("Hi") == [
            "100000", "010011", "001010",
        ]

    def test_text_to_binary_list(self):
        bb = bbe()
        assert bb.translate_text_to_binary_list("Hi") == [
            [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, 0],
        ]

    def test_text_to_unicode(self):
        bb = bbe()
        assert bb.translate_text_to_unicode("Hi") == ["2820", "2813", "280a"]

    def test_text_to_dot_count(self):
        bb = bbe()
        assert bb.translate_text_to_dot_count("Hi") == [1, 3, 2]

    def test_text_to_numbering_string(self):
        bb = bbe()
        assert bb.translate_text_to_numbering_string("Hi") == [
            "6", "1-2-5", "2-4",
        ]

    def test_text_to_numbering_list(self):
        bb = bbe()
        assert bb.translate_text_to_numbering_list("Hi") == [
            [6], [1, 2, 5], [2, 4],
        ]

    def test_text_to_full_list(self):
        bb = bbe()
        full = bb.translate_text_to_full_list("Hi")
        assert len(full) == 3
        # Regression: reverse braille must use the braille index, not the
        # loop position. Reverse of ⠠ (index 32) is ⠄, not ⠀.
        assert full[0][-1] == "⠄"
        assert full[1][-1] == "⠚"
        assert full[2][-1] == "⠑"

    def test_reverse_braille(self):
        bb = bbe()
        assert bb.translate_text_to_reverse_braille("Hi") == ["⠑", "⠚", "⠄"]


class TestOutput:
    def test_output_all_json(self):
        bb = bbe()
        data = json.loads(bb.output_all_json("Hi"))
        assert len(data) == 3
        assert data[0]["Letter"] == "⠠"
        assert data[0]["Braille"] == "⠠"
        assert data[0]["Unicode"] == "U+2820"

    def test_output_all_csv(self):
        bb = bbe()
        lines = bb.output_all_csv("Hi").strip().splitlines()
        assert len(lines) == 4
        assert lines[0].startswith("index,Letter")

    def test_output_all_xml(self):
        bb = bbe()
        root = ET.fromstring(bb.output_all_xml("Hi"))
        assert root.tag == "braille_output"
        assert len(root.findall("item")) == 3

    def test_output_all_yaml(self):
        bb = bbe()
        yaml_out = bb.output_all_yaml("Hi")
        assert yaml_out.count("- braille:") == 3

    def test_output_all_markdown(self):
        bb = bbe()
        md = bb.output_all_markdown("Hi")
        assert md.count("## Braille") == 3

    def test_output_all_html_well_formed(self):
        bb = bbe()
        html = bb.output_all_html("Hi")
        # Regression: table rows used to be nested (unclosed <tr>).
        assert html.count("<tr>") == html.count("</tr>")
        assert html.count("</table>") == 3
        assert "Thank you for using Braille Base." in html

    def test_output_all_html_custom_footer(self):
        bb = bbe()
        html = bb.output_all_html("Hi", footer="bye")
        assert "bye" in html

    def test_output_all_txt(self):
        bb = bbe()
        txt = bb.output_all_txt("Hi")
        assert txt.count("-" * 40) == 3

    def test_output_braille_txt(self):
        bb = bbe()
        assert bb.output_braille_txt("Hi") == "⠠⠓⠊"

    def test_output_reverse_braille_txt(self):
        bb = bbe()
        assert bb.output_reverse_braille_txt("Hi") == "⠑⠚⠄"

    def test_output_binary_txt(self):
        bb = bbe()
        assert bb.output_binary_txt("Hi").splitlines() == [
            "100000", "010011", "001010",
        ]


class TestEnglish:
    def test_all_lowercase_letters(self):
        bb = bbe()
        expected = {
            "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
            "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
            "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
            "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
            "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
            "z": "⠵",
        }
        for letter, braille in expected.items():
            assert bb.output_braille_txt(letter) == braille, letter

    def test_uppercase_marked_with_capital_sign(self):
        bb = bbe()
        assert bb.output_braille_txt("A") == "⠠⠁"

    def test_readme_example(self):
        bb = bbe()
        out = bb.output_braille_txt(
            "Library Developed to Handle Simple and Complex Braille 2026"
        )
        expected = (
            "⠠⠇⠊⠃⠗⠁⠗⠽⠀⠠⠙⠑⠧⠑⠇⠕⠏⠑⠙⠀⠞⠕⠀"
            "⠠⠓⠁⠝⠙⠇⠑⠀⠠⠎⠊⠍⠏⠇⠑⠀⠁⠝⠙⠀"
            "⠠⠉⠕⠍⠏⠇⠑⠭⠀⠠⠃⠗⠁⠊⠇⠇⠑⠀⠼⠃⠚⠃⠋"
        )
        assert out == expected

    def test_numbers_get_number_sign(self):
        bb = bbe()
        assert bb.output_braille_txt("2026") == "⠼⠃⠚⠃⠋"

    def test_digits(self):
        bb = bbe()
        for digit, braille in [("1", "⠁"), ("0", "⠚")]:
            assert bb.output_braille_txt(digit).endswith(braille)

    def test_punctuation(self):
        bb = bbe()
        assert bb.output_braille_txt(".") == "⠲"
        assert bb.output_braille_txt(",") == "⠂"
        assert bb.output_braille_txt("?") == "⠦"
        assert bb.output_braille_txt("!") == "⠖"

    def test_space(self):
        bb = bbe()
        assert bb.output_braille_txt(" ") == "⠀"

    def test_custom_letter_registration(self):
        bb = bbe()
        # Z is in the uppercase rules, so the capital sign is added by
        # the preprocessor; the custom cell replaces the default one.
        bb.append_braille_letter("Z", ["⠵"])
        assert bb.output_braille_txt("Z") == "⠠⠵"


class TestConfidence:
    def test_confidence_test(self):
        bb = bbe()
        out = bb.confidence_test("Braille")
        assert out[0] == ["⠠", ["⠠"]]
        assert out[1] == ["B", ["⠃"]]
        assert out[7] == ["e", ["⠑"]]


class TestMetadata:
    def test_version(self):
        assert braillebase.__version__ == "0.2.0"

    def test_all(self):
        assert set(braillebase.__all__) == {"BrailleBase", "bbe"}
