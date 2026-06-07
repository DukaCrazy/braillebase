
## 2026/06/07 — Version 0.0.10 Summary
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

