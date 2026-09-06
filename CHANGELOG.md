
## 2026/9/6 - Version 0.2.9 Sumary
- Update to the logic that processes uppercase and lowercase characters.
  
## 2026/8/30 - Version 0.2.7 Sumary
- dependence logic update

## 2026/8/19 - Version 0.2.6 Sumary
### Improvements in Rule Generation
- Updated rule‑generation methods, increasing translation accuracy for characters, symbols, and numbers.
- Refined internal algorithms for detecting and applying special rules, reducing ambiguities and improving consistency across modules.
### Enhancements to Internal Methods
- Improved the behavior of confidence_test, making output analysis more predictable and better aligned with the translation pipeline.
- Optimized tokenize_text, ensuring more stable segmentation and compatibility with new token sets.
### New Rules for Special Symbols
- Added dedicated rules for translating special symbols, enabling braille generation for icons, markers, and graphical elements.
- Expanded mathematical sub‑rules, extending support for new operators, indicators, and numeric structures.

        Old >> def prepare_number_braille(self, text: str) -> str:
        New >> def prepare_number_braille(self, tokens: list[str]) -> list[str]:

        Old >> def prepare_special_braille_rules_uppercase(self, text: str) -> str:
        New >> def prepare_special_braille_rules_uppercase(self, tokens: list[str]) -> list[str]:

        Old >> def prepare_special_braille_rules_CJK(self, text: str) -> str:
        New >> def prepare_special_braille_rules_CJK(self, tokens: list[str]) -> list[str]:

        Old >> def prepare_special_braille_rules_RTL(self, text: str) -> str:
        New >> def prepare_special_braille_rules_RTL(self, tokens: list[str]) -> list[str]:

        New >> def prepare_special_braille_rules_simbol(self, tokens: list[str]) -> list[str]:
  
## 2026/8/16 - Version 0.2.4 Sumary
### Architecture Updates
- Centralization of common data:  
- All universal symbols — such as numbers, Roman letters, and other elements shared across multiple languages — are now registered directly in the BrailleBase superclass.
- Language‑specific subclasses no longer duplicate these entries and instead inherit the unified core set automatically.
### Updates to multiple‑append methods
`def append_braille_letter_IO(target_data_path: str):`
- Support for external files:  
- The multiple‑append methods have been updated to allow registering new symbols directly from CSV, JSON, or XML files.
- Dynamic table updates:
- The internal database can now be updated by calling native library methods that process these external files, making maintenance simpler and more automated.

        # Braille Base IO
        Reader for JSON, XML, and CSV formats.

        ## Input Examples
        JSON example:
        ```json
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
        XML example:
        ```xml
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
        CSV example:
        ```csv
        a,"⠁,⠁",0
        b,"⠟,⠟,⠟",0
        ```
        ## Output Example

        [('a', ['⠁', '⠁'], 0), ('b', ['⠟', '⠟', '⠟'], 0)]

## 2026/08/11 - Version 0.1.5 Summary
### Added
- Full implementation of the BrailleBaseOutput module, responsible for generating multiple output formats based on the data processed by braillebase.
### New export methods:
- output_all_json — detailed JSON structure generation.
- output_all_csv — tabular CSV export.
- output_all_xml — formatted and validated XML output.
- output_all_yaml — clean and readable YAML output.
- output_all_markdown — Markdown documentation with organized sections.
- output_all_html — HTML rendering with tables and a standardized layout.
- output_all_txt — plain text output, ideal for logs and quick inspection.
### Improved
- Complete separation of heavy formatting logic, removing duplication and reducing coupling with the main module.
- Standardization of output fields (index, braille, binary, numbering, unicode, reverse).
- Ensured consistency across all formats, including cross‑validation of Unicode and reverse braille cells.
- Enhanced readability of all outputs with consistent indentation and clear data organization.

## 2026/08/02 - Version 0.1.4 Summary
- Adjustments to the token size definition caused a bug that was not detected in the testing environment but was noticed after the version was released. The inconsistency has been fixed.

## 2026/08/02 - Version 0.1.3 Summary
- Fixed internal bugs.
- Added new output methods.
- Configurable token size.
    *def configure_token(self, token_size: int)
        **This method defines the maximum size of each item identified by the tokenization method.

## 2026/07/20 - Version 0.1.2 Summary
- Bug fix for the [translate_text_to_reverse braille()] method.
- Update to the HTML generator method [output_all_html()].

## 2026/07/13 - Version 0.1.1 Summary
- Edition of the base reverse Braille.
- Definition of the base architecture.

## 2026/06/22 - Version 0.0.15 Summary
- Invocation of the special append methods via the simple append method using the third argument.

## 2026/06/22 - Version 0.0.14 Summary
- Separating the RTL module for languages like Arabic, Hebrew, and Persian.
- Specific rules for uppercase Latin letters.
- Spelling fix in method names: lettr -> letter

## 2026/06/14 - Version 0.0.13 Summary
- Scope Optimization for Latin Characters: Updated internal variables within the methods responsible for parsing and validating Latin alphabet rules.
- Modularization and Isolation of the CJK Block: Segregated the processing pipeline for CJK languages (Chinese, Japanese, and Korean). 
- This behavior was isolated from both the generic rules_02 method and the non-special character flow, ensuring exclusive and specialized handling for this linguistic group.
Code Refactoring and Cleanup: Removed structural redundancies to improve system readability and maintainability.
- Performance Optimization: Updated the methods responsible for managing Braille character lists and their respective dependencies, reducing computational overhead.

## 2026/06/07 — Version 0.0.12 Summary
- Updated documentation.
- Updated dependence/     def __constructor_all_table(self): [brailletable 1.0.0 -> brailletable 1.0.1].
- New paramether in Prepare Special 01: Roma Letter/    def setting_braille_rules01(self, braille_uppercase: str, braille_lowercase: str): [Only Uppercase -> Uppercase and Lowercase]

## 2026/05/17 — Version 0.0.8 Summary
- 1) Mapping group (0003) Add: def get_index_to_braille(self, index: int) -> str: 0003-C
- 2) All class members became instance members
- Constructor Add: def __constructor_all_table(self):
- a) Tables group (0004): All methods of group 4 receive the private lists.

## 2026/05/13 — Version 0.0.7 Summary
- Improved support for Latin letters compared to previous versions.

## 2026/05/10 — Version 0.0.6 Summary
- Updated documentation.
- Fixed internal bugs.
- Added new output methods.

## 2026/05/08 — Version 0.0.5 Summary
- Added automatic registration of all 64 Unicode braille cells as default keys in the internal map.
- Added support for handling text that contains numbers (using the number‑processing method we implemented).
- Updated and expanded documentation to reflect the new initialization behavior and numeric‑handling support.
  
  <img src="./img/logo.png" alt="Logo" width="500" height="493">
