# ---------------------------------------- Translate group (0002)
## 0002-A
Component: translate_text_to_braille(text)

Input:
    - text: str

Output:
    - list[str] (braille symbols)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by prepare_number_braille
    - Any errors raised by get_brailles_with_letter

Responsibilities:
    - Preprocess text for numeric braille rules
    - Convert each character into its corresponding braille list
    - Flatten all braille lists into a single output list

Dependencies:
    - prepare_number_braille (numeric preprocessing)
    - get_brailles_with_letter (registry lookup)
    - __letter_brailles (indirectly)

Behavior:
    - Mutates nothing (pure transformation)
    - Expands characters into 1..N braille cells
    - Deterministic

## 0002-B
Component: translate_text_to_index(textBraille)

Input:
    - textBraille: str

Output:
    - list[int] (braille indices)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into their numeric indices
    - Serve as the numeric translation layer for downstream methods

Dependencies:
    - translate_text_to_braille (primary dependency)
    - get_braille_list_to_index_list (static mapping)
    - __letter_brailles (indirectly)

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-C
Component: translate_text_to_binary_string(text)

Input:
    - text: str

Output:
    - list[str] (6‑bit binary strings)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to 6‑bit binary strings

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_binary_string_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-D
Component: translate_text_to_binary_list(text)

Input:
    - text: str

Output:
    - list[list[int]] (6‑bit binary arrays)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to 6‑bit binary arrays

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_binary_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-E
Component: translate_text_to_unicode(text)

Input:
    - text: str

Output:
    - list[str] (Unicode hex codes)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to Unicode hexadecimal strings

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_unicode_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-F
Component: translate_text_to_dot_count(text)

Input:
    - text: str

Output:
    - list[int] (dot counts)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to dot counts (1–6)

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_dot_count

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-G
Component: translate_text_to_numbering_string(text)

Input:
    - text: str

Output:
    - list[str] (hyphen‑separated dot numbers)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to numbering strings (e.g., "1-3-5")

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_dot_numbering_string_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-H
Component: translate_text_to_numbering_list(text)

Input:
    - text: str

Output:
    - list[list[int]] (dot numbers)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Map indices to lists of active dot numbers

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_dot_numbering_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic

## 0002-I
Component: translate_text_to_full_list(text)

Input:
    - text: str

Output:
    - list[list[Any]] (full braille data per cell)

Errors:
    - KeyError if any character is not registered
    - Any errors raised by translate_text_to_braille
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Aggregate all braille‑related data into a single structure:
        [braille, index, binary_string, binary_list,
         unicode, dot_count, numbering_string, numbering_list]

Dependencies:
    - translate_text_to_braille
    - get_braille_list_to_index_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list

Behavior:
    - Pure transformation
    - No mutation
    - Deterministic