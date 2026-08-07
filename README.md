# BrailleBase
### pip install braillebase
## Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.

## Features
- Full Unicode Braille block support (U+2800–U+283F), all 64 cells
- Letter → braille registry with validation (append, edit, remove, query)
- Text translation to braille cells, indices, binary, Unicode, dot counts, numbering
- Reverse braille (write side) output
- Structured output formats: JSON, CSV, XML, YAML, Markdown, HTML, plain text
- Extensible: subclass `BrailleBase` and register your own letter tables
- Ships with `bbe`, the English (UEB-style) grade-1 table

## English
```python
from braillebase import bbe

bb = bbe()
print(bb.output_braille_txt("Library Developed to Handle Simple and Complex Braille 2026"))
```
Output: ⠠⠇⠊⠃⠗⠁⠗⠽⠀⠠⠙⠑⠧⠑⠇⠕⠏⠑⠙⠀⠞⠕⠀⠠⠓⠁⠝⠙⠇⠑⠀⠠⠎⠊⠍⠏⠇⠑⠀⠁⠝⠙⠀⠠⠉⠕⠍⠏⠇⠑⠭⠀⠠⠃⠗⠁⠊⠇⠇⠑⠀⠼⠃⠚⠃⠋

The English subclass handles capitals (⠠), number signs (⠼), digits and common punctuation automatically. Other languages are planned as `bbj` (Japanese), `bbp` (Portuguese), `bba` (Arabic) and `bbv` (Vietnamese); the base class is language-neutral and ready for them.

## Base class
The core engine works on any registered mapping. Braille cells always map to themselves, so you can mix raw braille with translated text:

```python
from braillebase import BrailleBase

bb = BrailleBase()
print(bb.get_braille_to_index("⠃"))   # 3
print(bb.get_index_to_braille(3))     # ⠃
```

Register your own table:

```python
from braillebase import BrailleBase

bb = BrailleBase()
bb.append_braille_letter("x", ["⠭"])
print(bb.output_braille_txt("x"))     # ⠭
```

## Confidence Test Method
```python
from braillebase import bbe

bb = bbe()
print(bb.confidence_test("Braille"))
```
- Output: {0: ['⠠', ['⠠']], 1: ['B', ['⠃']], 2: ['r', ['⠗']], 3: ['a', ['⠁']], 4: ['i', ['⠊']], 5: ['l', ['⠇']], 6: ['l', ['⠇']], 7: ['e', ['⠑']]}

## Running the tests
```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
```

  <img src="./img/logo.png" alt="Logo" width="500" height="493">
