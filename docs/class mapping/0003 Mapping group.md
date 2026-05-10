# ---------------------------------------- Mapping group (0003) ----------------------------------------

## 0003-A
Component: get_braille_to_index(braille)

Input:
    - braille: str

Output:
    - int (index 0–63)

Errors:
    - KeyError if braille is not a valid key in the internal mapping dict

Responsibilities:
    - Map a single braille Unicode character to its numeric index
    - Provide constant‑time lookup for braille → index conversion

Dependencies:
    - Internal static dictionary braille_to_index

Behavior:
    - Pure function
    - No mutation
    - Deterministic
## 0003-B
Component: get_braille_list_to_index_list(braille_list)

Input:
    - braille_list: list[str]

Output:
    - list[int] (indices 0–63)

Errors:
    - KeyError if any braille symbol is invalid
    - Any errors raised by get_braille_to_index

Responsibilities:
    - Convert a list of braille symbols into their corresponding indices
    - Apply get_braille_to_index to each element

Dependencies:
    - get_braille_to_index (static mapping)

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic