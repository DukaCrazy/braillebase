# Braille Base (braillebase)
- pypi install braillebase
- version 0.3.3

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

## Translate Group (0002)
Before using the **Translate Group (0002)**, it is important to understand the conversion rules applied by the system, how text tokenization works, and the relationship between the available *collection*s and output formats.

<p>
<b>Collections function as sets.</b>

self.__letter_brailles: dict[str, list[str]] is the main set.

self.__letter_special_braille_rules_symbol, self.__letter_special_braille_rules_uppercase, self.__letter_special_braille_rules_syllabic, and self.__letter_special_braille_rules_rtl are its subsets.

In other words, all data registered in the subsets is also registered in the main set. For example:
</p>

```
Default {
    Uppercase {},
    Syllabic {},
    RTL {},
    Symbol {},
    other data...
}
```
- Therefore, the main set contains all available entries, while each subset contains only the data related to its respective category.

- The tokenization process is performed through the tokenize_text() method.

- During tokenization, the system always attempts to match the longest registered token at the current position in the text. The maximum token length is defined through the configure_token() method.

- Token recognition is always performed using the main collection (self.__letter_brailles). Because all entries from the special collections are also registered in the main collection, tokenization is not affected by the selected collection. Collections are applied only after token recognition, during the conversion process.

        After tokenization, each token is analyzed individually following a specific sequence of collections.

        The Symbol collection is checked first. Elements belonging to this group do not use special grammatical rules. When a match is found, its value is used directly, without the application of additional indicators.

        Next, the Uppercase collection is analyzed. Unlike the previous group, this collection may require the application of grammatical indicators. The rules vary depending on the configured language. In some languages, the indicator changes according to the number of consecutive uppercase letters; in others, it may also be necessary to apply a lowercase termination indicator after a sequence of uppercase letters.

        The Syllabic and RTL collections are then checked. At present, these groups do not apply special rules during the conversion process. Their primary purpose is to organize entries according to their specific characteristics. However, their existence allows dedicated rules to be implemented in the future without requiring structural changes to the system.

        Finally, the Numeric rule is applied, which is responsible for inserting the numeric indicator whenever required.

        As a result, only the Uppercase and Numeric collections use special indicators during the conversion process, while the remaining collections are primarily intended for data organization and categorization.

- Finally, after all rules and indicators have been applied, the tokens stored in the list are converted into Braille.

- Unlike the previous stages, the conversion process does not apply grammatical rules or special handling. Each token is used directly as a lookup key in the dictionary, returning its corresponding Braille value.

- **Note:** if a key is not registered in the dictionary, an exception will be raised.

