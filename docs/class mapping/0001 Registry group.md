# ---------------------------------------- Registry group (0001) 
## 0001-A
Component: append_braille_letter(letter, braille_list)

Input:
    - letter: str
    - braille_list: list[str]

Output:
    - None

Errors:
    - TypeError if letter is not str
    - ValueError if letter is empty
    - TypeError or ValueError from __validate_braille_list

Responsibilities:
    - Validate input type and non‑emptiness of letter
    - Validate braille_list structure and contents
    - Register or overwrite the mapping letter → braille_list

Dependencies:
    - __validate_braille_list (internal validator)
    - __letter_brailles (internal dict)

Behavior:
    - Mutates internal state
    - Overwrites existing mappings
    - Deterministic

## 0001-B
Component: get_brailles_with_letter(letter)

Input:
    - letter: str

Output:
    - list[str] (braille symbols)

Errors:
    - KeyError if letter not registered

Responsibilities:
    - Validate existence
    - Retrieve mapping
    - Provide safe access

Dependencies:
    - __letter_brailles (internal dict)
    - Validation ensured by registry methods

Behavior:
    - Pure accessor
    - No mutation
    - Deterministic

## 0001-C
Component: has_letter(letter)

Input:
    - letter: str

Output:
    - bool (True if registered, False otherwise)

Errors:
    - None (safe lookup; does not raise exceptions)

Responsibilities:
    - Check whether a given letter exists in the internal mapping
    - Provide a fast boolean lookup for registry validation

Dependencies:
    - __letter_brailles (internal dict)

Behavior:
    - Pure check
    - No mutation
    - Deterministic

## 0001-D
Component: remove_letter(letter)

Input:
    - letter: str

Output:
    - bool (True if removed, False otherwise)

Errors:
    - None (does not raise exceptions for missing letters)

Responsibilities:
    - Check if letter exists in the mapping
    - Remove the entry if present
    - Indicate success or failure

Dependencies:
    - __letter_brailles (internal dict)

Behavior:
    - Mutates internal state
    - Safe removal (no error on missing key)
    - Deterministic

## 0001-E
Component: get_registered_letters()

Input:
    - None

Output:
    - list[str] (all registered letters)

Errors:
    - None (safe retrieval; does not raise exceptions)

Responsibilities:
    - Return a list of all keys currently stored in the internal mapping
    - Provide visibility into which letters are registered

Dependencies:
    - __letter_brailles (internal dict)

Behavior:
    - Pure retrieval
    - No mutation
    - Deterministic

## 0001-F
Component: append_multiple_braille_letters(mapping)

Input:
    - mapping: dict[str, list[str]]

Output:
    - None

Errors:
    - TypeError if mapping is not a dict
    - Any errors raised by append_braille_letter for invalid entries

Responsibilities:
    - Validate that mapping is a dictionary
    - Iterate through all entries
    - Delegate validation and registration to append_braille_letter
    - Register multiple mappings in sequence

Dependencies:
    - append_braille_letter (internal registry method)
    - __letter_brailles (internal dict)

Behavior:
    - Mutates internal state
    - Overwrites existing mappings when necessary
    - Deterministic

## 0001-G
Component: edit_braille_letter(letter, new_braille_list)

Input:
    - letter: str
    - new_braille_list: list[str]

Output:
    - None

Errors:
    - KeyError if the letter is not registered in the internal mapping
    - TypeError or ValueError if new_braille_list fails validation
      (raised by __validate_braille_list)

Responsibilities:
    - Modify the braille list associated with an already‑registered letter
    - Validate the new braille list before applying the update
    - Ensure registry integrity by preventing invalid braille assignments

Dependencies:
    - __letter_brailles (internal dict)
    - __validate_braille_list (internal validation method)

Behavior:
    - Mutates internal state (updates mapping entry)
    - Deterministic
    - Does not create new letters; only edits existing ones