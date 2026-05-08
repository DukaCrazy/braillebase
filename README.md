📘 BrailleBase — Internal Architecture Overview (EN)
BrailleBase is organized into numbered functional groups, each responsible for a specific part of the internal logic.
This modular structure improves readability, maintainability, scalability, and multilingual documentation.
Below is the official description of each group.

<span style="color:red">📌 Observation Note
We are continuously working to improve our application.
Version 0.0.5 is already capable of handling text that contains numbers, as long as those characters are properly registered in the system.
We are currently updating and expanding our documentation to make the usage of the library clearer.
In version 0.1.0, known issues — such as map keys longer than two characters — will have been fully resolved.
For questions, suggestions, or issue reports, please reach out through the GitHub Issues section.
Your feedback is essential to help us improve this project.</span>


0001 Registry → registers letters and braille mappings
0002 Translate → converts text into braille and indices
0003 Mapping → maps braille ↔ indices
0004 Tables → provides fixed internal tables
0005 Output → exports processed data

🧩 0001 — Registry group
Manages the internal registry of characters and their associated braille mappings.
Main functions
- append_braille_letter
Registers a letter and its braille list. Overwrites the mapping if the letter already exists.
- get_brailles_with_letter
Returns the braille list associated with a registered letter.
- has_letter
Checks whether a letter is registered.
- remove_letter
Removes a letter from the internal registry.
Group responsibility
This group acts as the class’s internal database.
No translation happens without going through this registry.

🔤 0002 — Translate group
Responsible for converting text into braille and then into numeric indices.
Main functions
- translate_text_to_braille
Converts each character into one or more braille cells.
Includes number preprocessing (⠼).
- translate_text_to_index
Converts a list of braille symbols into a list of indices (0–63).
Group responsibility
This is the core translation engine.
All text passes through this group before being exported or processed further.

🔁 0003 — Mapping group
Provides direct mappings between:
- braille → index
- list of braille symbols → list of indices
Main functions
- get_braille_to_index
Returns the Unicode braille index (U+2800–U+283F).
- get_braille_list_to_index_list
Converts an entire list of braille symbols into indices.
Group responsibility
This is the mathematical core of the library.
No numeric conversion happens outside this group.

📚 0004 — Tables group
Contains fixed internal tables used as reference structures.
Main functions
- braille_list
Returns the full list of 64 Unicode braille symbols.
- get_binary_list
Returns 64 arrays of 6 bits (binary representation of braille).
- get_binary_string_list
Returns 64 binary strings of 6 bits.
Group responsibility
Provides base structures for conversions, validation, and output formatting.

📤 0005 — Output group
Responsible for formatting and exporting processed data.
Main functions
- output_all_json
Exports text, braille, and indices in JSON format.
Group responsibility
This is the final layer of the library.
Everything that leaves BrailleBase goes through this group.
