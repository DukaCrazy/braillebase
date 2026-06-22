
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

