# Braille Base (braillebase)
- pypi install braillebase
- version 0.3.0

        Braille Base is an open-source project licensed under the MIT License, designed to offer ease of use for beginners and flexibility for professionals, while prioritizing accuracy, performance, and simplicity in text-to-Braille translation.

In general, official **Braille standards** share the same Braille cells for Roman and Greek alphabet letters, as well as numbers. For this reason, Braille Base uses the **BrailleBaseUniversalSet**, which provides a predefined collection of shared Braille characters across languages.

## Registry Group (0001)
<p>Each language has its own rules for Braille transcription. These may include phonetic, syllabic, direct character-to-Braille translation, or other specialized transcription rules.
<br><br>
Therefore, a static character set alone may not be sufficient. API users must also be able to register new characters, edit existing entries, and remove them when necessary.
<br><br>
To support this flexibility, the Braille Base API provides several methods for managing character lists. The following section introduces the methods available in this group.
</p>

### Group Identification
        The methods in this group include an argument called collection, which determines which map the operation will target. Each value corresponds to a specific group, as described below:

<p>
<h4>0 — Default</h4>
The central registry and translation base of Braille Base. All records are stored in this group. The other groups act as auxiliary rule-identification mechanisms, allowing the engine to determine in advance which processing rules should be applied to each character or expression.
<h4>1 — Uppercase</h4>
Used to register uppercase letters, allowing the engine to identify when translation requires the application of an uppercase indicator.
<h4>2 — Syllabic</h4>
Used to register characters and writing systems that follow syllabic rules, such as Hiragana, Jamul, and Pinyin.
<h4>3 — RTL</h4>
Used to register languages whose writing systems follow a right-to-left (RTL) direction.
<h4>4 — Symbol</h4>
Used to register symbols, characters, and special expressions that take priority over all other interpretation rules. It allows complete expressions to be recognized as a single translation unit, preventing their individual characters from being interpreted separately.
</p>

### Registry Group Constants
```python
        bbDEFAULT = 0
        bbUPPERCASE = 1
        bbSYLLABIC = 2
        bbRTL = 3
        bbSYMBOL = 4
```

        As described earlier, registry groups are identified by indices ranging from 0 to 4. However, there is no need to memorize these values. Braille Base exposes predefined constants that map directly to each registry group. For example, use bbUPPERCASE instead of 1.

- In practice, both the numeric identifier and its corresponding constant can be used interchangeably when registering or editing Braille entries. However, using constants is recommended because it improves code readability and makes maintenance easier.

```python
from braillebase import BrailleBase

class BrailleBaseMyLanguage(BrailleBase):
    def __init__(self):

        self.append_braille_letter("CH", ["⠡"], bbUPPERCASE) 
        self.append_braille_letter("SH", ["⠩"], bbUPPERCASE) 
        self.append_braille_letter("TH", ["⠹"], 1) 
        self.append_braille_letter("WH", ["⠱"], 1)
        self.append_braille_letter("あ", ["⠁"],bbSYLLABIC) 
        self.append_braille_letter("い", ["⠃"],bbSYLLABIC) 
        self.append_braille_letter("う", ["⠉"],2) 

        self.edit_braille_letter("え", ["⠋"],bbSYLLABIC)
        self.edit_braille_letter("お", ["⠊"],2)
```

- The methods in Registry Group (0001) are intuitive and self-explanatory. Nevertheless, the following section provides a brief overview of each method signature.
```python
        Registers a new letter and its Braille representation. Return: None
        def append_braille_letter(self, letter: str, braille_list: list, collection = bbDEFAULT):​‌
```
```python
        Retrieves all Braille cells associated with a letter. Return: list
        def get_brailles_with_letter(self, letter: str):​‌
```
```python
        Checks whether a letter is registered. Return: bool
        def has_letter(self, letter: str, collection = bbDEFAULT) -> bool:​‌
```
```python
        Removes a registered letter. Return: bool (True if removed)
        def remove_letter(self, letter: str, collection = bbDEFAULT) -> bool:​‌
```
```python
        Returns all registered letters from a group. Return: list
        def get_registered_letters(self, collection = bbDEFAULT):​‌
```
```python
        Registers multiple letters at once. Return: None
        def append_multiple_braille_letters(self, letter_braillelist_pattern: list):​‌
```
```python
        Imports letter registrations from a data source. Return: None
        def append_braille_letter_IO(self, target_data_path: str):​‌
```
```python
        Updates the Braille representation of a registered letter. Return: None
        def edit_braille_letter(self, letter: str, new_braille_list: list, collection = bbDEFAULT):
```
### append_braille_letter_IO
- The append_braille_letter_IO method accepts only one argument, which is the path to the file containing the data. The API supports only three data formats: JSON, XML, and CSV.

```json
JSON
[
    {
        "letter": "a",
        "braille": "⠁,⠁",
        "pattern": 0
    },
    {
        "letter": "b",
        "braille": "⠟,⠟,⠟",
        "pattern": 0
    }
]
```

```xml
XML
<?xml version="1.0" encoding="utf-8"?>
<braille_append>
    <item>
        <letter>a</letter>
        <braille>⠁,⠁</braille>
        <pattern>0</pattern>
    </item>

    <item>
        <letter>b</letter>
        <braille>⠟,⠟,⠟</braille>
        <pattern>0</pattern>
    </item>
</braille_append>
```
```csv
CSV
a,"⠁,⠁",0
b,"⠟,⠟,⠟",0
```
- The file data does not contain a header. You must provide the character, the Braille representation, and the group using its numeric identifier, following the format demonstrated in the examples. The group field cannot be omitted, so make sure to specify the correct group for each entry.
- For more information on how to create JSON, XML, or CSV files, please refer directly to the BrailleBaseIO documentation.

# documentation under development.# Braille Base
# Old Doc

- <b>BrailleBase is an algorithm developed in Python with the goal of making Braille accessible to both blind and sighted individuals.

- Its architecture was designed to be intuitive, easy to understand, and simple to manipulate, allowing any developer to explore, transform, and integrate Braille data without complexity.</b>

## 1) Introduction
### BrailleBase is divided into X parts.
### Register Letters and Characters
<b>The first part of BrailleBase is responsible for registering letters, characters, symbols, icons, and other elements.
The registration methods are organized into four sets:</b>

**General** — where all items are registered: letters, numbers, uppercase and lowercase characters, punctuation, and other elements.

**Uppercase** — stores all uppercase items of the registered language.

**CJK** — registers phonetic alphabets such as Pinyin, Katakana, Hangul, and other East Asian writing systems.

**RTL** — stores alphabets that are written and read from right to left.

The Uppercase, CJK, and RTL sets are also added to the General set.
Therefore:

**General = {General[0], Uppercase[1], CJK[2], RTL[3]}**

```python
from braillebase import BrailleBase

class BrailleBaseExemple(BrailleBase):
        def __init__(self):
        super().__init__()
        #Uppercase / Lowercase Rules
        self.setting_braille_rules_uppercase("⠠", "⠠⠄")
        #General
        self.append_braille_letter("a", ["⠁"]) 
        self.append_braille_letter("b", ["⠃"]) 
        self.append_braille_letter("c", ["⠉"]) 
        #Upper
        self.append_braille_letter("A", ["⠁"],1) 
        self.append_braille_letter("B", ["⠃"],1) 
        self.append_braille_letter("C", ["⠉"],1) 
        #CJK
        self.append_braille_letter("あ", ["⠁"],2)
        self.append_braille_letter("い", ["⠃"],2)
        self.append_braille_letter("う", ["⠉"],2)
        self.append_braille_letter("え", ["⠋"],2) 
        self.append_braille_letter("お", ["⠊"],2)
        #RTL
        self.append_braille_letter("ا", ["⠁"], 3) 
        self.append_braille_letter("ب", ["⠃"], 3) 
        self.append_braille_letter("ت", ["⠞"], 3) 
        self.append_braille_letter("ث", ["⠹"], 3) 
        self.append_braille_letter("ج", ["⠚"], 3)
        #Other A
        self.append_braille_letter("⠼", ["⠼"])
        self.append_braille_letter("1", ["⠁"]) 
        self.append_braille_letter("2", ["⠃"])
        #Other B
        self.append_braille_letter(".", ["⠲"])
        self.append_braille_letter(",", ["⠂"]) 
        self.append_braille_letter(";", ["⠆"])
        #Other C
        self.append_braille_letter("[ch]", ["⠡"])
        self.append_braille_letter("[sh]", ["⠩"])
        self.append_braille_letter("[th]", ["⠹"]) 
        #Other D
        self.append_braille_letter("[OW]", ["⠪"], 1)
        self.append_braille_letter("[AR]", ["⠜"], 1)
        self.append_braille_letter("[ING]", ["⠬"], 1) 
        #Other E
        self.append_braille_letter("$", ["⠈", "⠎"])
        self.append_braille_letter("¢", ["⠈", "⠉"])
        self.append_braille_letter("¥", ["⠈", "⠽"])
        self.append_braille_letter("€", ["⠈", "⠑"])
```

<b>BrailleBase allows you to register or edit braille directly through the instantiated object.
Since characters are stored in internal dictionaries, any new registration using an existing key automatically replaces the previous value.
This makes it possible to add, correct, or update letters, symbols, and tokens at any point during execution, without recreating the class or reinitializing the system.</b>

### Convert Text To Braille
<b>BrailleBase is the superclass that centralizes all the logic for processing, organizing, and analyzing Braille databases.
All subclasses inherit this logic and provide different output formats.</b>

#### A)
BrailleBase supports multiple output formats, including:
<b>
- JSON - `output_all_json(txt)`
- CSV - `output_all_csv(txt)`
- XML - `output_all_xml(txt)`
- YAML - `output_all_yaml(txt)`
- Markdown - `output_all_markdown(txt)`
- HTML - `output_all_html(txt)`
- TXT - `output_all_txt(txt)`
</b>

<b>The sequence of data provided in each set is: index, letter, braille, binary, numbering list, unicode, reverse braille, reverse binary, reverse numbering, reverse unicode.</b>

For example, the braille ⠓ produces the following output:

- **Braille:** ⠓
- **Numbering:** 1-2-5.
- **Binary:** 010011
- **Unicode:** U+2813
- **Reverse Braille:** ⠚
- **Reverse Numbering:** 2-4-5
- **Reverse Binary:** 011010
- **Reverse Unicode:** U+281a

#### B)
Additionally, the class provides different types of Braille output:

**I Love Braille!**

`output_braille_txt(txt)`

“Standard Braille — this is the traditional braille used for tactile reading.
Each cell represents the raised dots exactly as they would be perceived by the fingers. `⠠⠊⠀⠠⠇⠕⠧⠑⠀⠠⠃⠗⠁⠊⠇⠇⠑⠖`

`output_braille_txt(txt)`

Reverse Braille — this is the mirrored version of standard braille.
This format corresponds to braille writing, meaning the arrangement of dots as they appear when embossed or punched, before being read by touch. `⠲⠊⠸⠸⠑⠈⠺⠘⠄⠀⠊⠼⠪⠸⠄⠀⠑⠄`

`output_binary_txt(txt)`

Binary corresponding to each Braille symbol: a string containing a number from 0 to 63 in binary, representing each dot position used in that specific braille cell, where 0 means no dot and 1 means a raised dot.

#### C)
At the core of the class is the `confidence_test` method, considered the ‘brain’ of BrailleBase.
This method analyzes the provided sentence, identifies the most appropriate token, and returns a list of braille cells in the correct order, representing the final conversion sequence.

```python
from braillebaseenglish import *

bbe = BrailleBaseEnglish()
# Complete output
print(bbe.output_all_json("insert any text"))
print(bbe.output_all_csv("insert any text"))
print(bbe.output_all_xml("insert any text"))
print(bbe.output_all_yaml("insert any text"))
print(bbe.output_all_markdown("insert any text", "insert any footer"))
print(bbe.output_all_html("insert any text", "insert any footer"))
print(bbe.output_all_txt("insert any text", "insert any footer"))
# Simple output
print(bbe.output_braille_txt("insert any text"))
print(bbe.output_reverse_braille_txt("insert any text"))
print(bbe.output_binary_txt("insert any text"))
# Confidence test
print(bbe.confidence_test("insert any text"))
```

---

-> pip install braillebase 0.2.9

Other
-> pip install braille 
        -> Japanese, Portuguese, English, Arabic, Viet


## 2) Objective and motivation
- The goal is to create a tool capable of translating more complex texts and expressions using simple methods, so that even a beginner in programming can use it and develop their own tools.

- In addition to providing a character‑to‑Braille translation engine, BrailleBase offers classes with a pre‑registered database, allowing the user to simply download it and start using it. This makes it easy to create new translation rules, register new items, and much more.

- Beyond the code itself, BrailleBase will soon allow users to access Braille from other countries simply by calling a method. When sighted people study new languages, the first thing they are introduced to is the alphabet of the target language. With the pre‑registered characters, the user only needs to know which class to call — for example, BrailleBaseEnglish — and insert the character or sentence as the method argument. The Braille output will be generated automatically, along with its metadata if needed.

<b>I Love</b>
⠠⠊⠀⠠⠇⠕⠧⠑
6
2‑4

6
1‑2‑3
1‑3‑5
1‑2‑3‑6
1‑5
