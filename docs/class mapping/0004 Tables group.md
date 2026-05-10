# ---------------------------------------- Tables group (0004)
## 0004-A
Component: braille_list()

Input:
    - None

Output:
    - list[str] (64 braille Unicode characters in U+2800–U+283F order)

Errors:
    - None

Responsibilities:
    - Provide the full ordered Unicode braille table
    - Serve as the canonical reference list for all braille outputs

Dependencies:
    - None (static, hardcoded list)

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-B
Component: get_binary_list()

Input:
    - None

Output:
    - list[list[int]] (64 arrays of 6 bits)

Errors:
    - None

Responsibilities:
    - Generate binary arrays representing each braille cell (0–63)
    - Encode each index as a 6‑bit list of integers

Dependencies:
    - Python formatting (f"{i:06b}")

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-C
Component: get_binary_string_list()

Input:
    - None

Output:
    - list[str] (64 binary strings of length 6)

Errors:
    - None

Responsibilities:
    - Generate binary string representations for all braille indices (0–63)

Dependencies:
    - Python formatting (f"{i:06b}")

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-D
Component: get_unicode_list()

Input:
    - None

Output:
    - list[str] (64 Unicode hex codes for U+2800–U+283F)

Errors:
    - None

Responsibilities:
    - Generate the Unicode hexadecimal representation for each braille cell
    - Provide a canonical mapping index → Unicode code

Dependencies:
    - Python formatting (f"{0x2800 + i:04x}")

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-E
Component: get_dot_count()

Input:
    - None

Output:
    - list[int] (dot counts for each braille cell)

Errors:
    - None

Responsibilities:
    - Count the number of active dots (1–6) for each braille index
    - Provide a fast lookup table for dot density

Dependencies:
    - Python bin() and count("1")

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-F
Component: get_dot_numbering_list()

Input:
    - None

Output:
    - list[list[int]] (active dot numbers for each braille cell)

Errors:
    - None

Responsibilities:
    - Determine which dot positions (1–6) are active for each braille index
    - Produce educational‑friendly dot numbering lists

Dependencies:
    - Bitwise operations (i >> d) & 1

Behavior:
    - Pure function
    - No mutation
    - Deterministic

## 0004-G
Component: get_dot_numbering_string_list()

Input:
    - None

Output:
    - list[str] (hyphen‑separated active dot numbers for each braille cell)

Errors:
    - None

Responsibilities:
    - Convert each dot‑numbering list into a hyphen‑joined string
    - Provide an educational‑friendly representation of active dot positions

Dependencies:
    - get_dot_numbering_list (static method)

Behavior:
    - Pure function
    - No mutation
    - Deterministic