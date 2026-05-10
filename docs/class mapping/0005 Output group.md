# ---------------------------------------- Output group (0005)
## 0005-A
Component: output_all_json(text)

Input:
    - text: str

Output:
    - str (JSON‑formatted string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Build a list of dictionaries with full braille metadata
    - Serialize the result into a JSON string

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list
    - json.dumps

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-B
Component: output_all_csv(text)

Input:
    - text: str

Output:
    - str (CSV‑formatted string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Write rows into a CSV structure
    - Convert the CSV buffer into a string

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list
    - csv.writer
    - io.StringIO

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-C
Component: output_all_xml(text)

Input:
    - text: str

Output:
    - str (formatted XML string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list
    - Any XML serialization errors from ElementTree or minidom

Responsibilities:
    - Collect all braille‑related data for each character
    - Build an XML tree with <item> nodes
    - Serialize and pretty‑format the XML output

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list
    - xml.etree.ElementTree
    - xml.dom.minidom

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-D
Component: output_all_yaml(text)

Input:
    - text: str

Output:
    - str (YAML‑formatted string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Write YAML entries manually (no external YAML library)
    - Preserve indentation and formatting consistency

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-E
Component: output_all_markdown(text)

Input:
    - text: str

Output:
    - str (Markdown‑formatted string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Generate a Markdown section for each braille cell
    - Format fields using Markdown headings and lists

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-F
Component: output_all_html(text)

Input:
    - text: str

Output:
    - str (HTML‑formatted string)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Generate HTML blocks (<div>, <p>, <span>) for each braille cell
    - Ensure valid HTML structure for embedding in web pages

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-GA
Component: output_all_txt(text)

Input:
    - text: str

Output:
    - str (plain text with full braille metadata)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Collect all braille‑related data for each character
    - Produce a human‑readable plain‑text block for each braille cell
    - Include separators and line breaks for clarity

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - braille_list
    - get_binary_string_list
    - get_binary_list
    - get_unicode_list
    - get_dot_count
    - get_dot_numbering_string_list
    - get_dot_numbering_list

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic

## 0005-GB
Component: output_binary_string_txt(text)

Input:
    - text: str

Output:
    - str (plain text containing only binary strings)

Errors:
    - KeyError if any character in text is not registered
    - Any errors raised by get_brailles_with_letter
    - Any errors raised by get_braille_list_to_index_list

Responsibilities:
    - Convert text into braille symbols
    - Convert braille symbols into indices
    - Output only the 6‑bit binary strings, one per line

Dependencies:
    - get_brailles_with_letter
    - get_braille_list_to_index_list
    - get_binary_string_list

Behavior:
    - Pure output generation
    - No mutation
    - Deterministic