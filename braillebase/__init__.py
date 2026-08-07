"""BrailleBase - a complete and extensible Unicode Braille processing library.

The :class:`BrailleBase` class provides the core engine: a registry of
letter -> braille-cell mappings, full Unicode braille table access
(U+2800-U+283F), text translation into braille, and structured output
formats (JSON, CSV, XML, YAML, Markdown, HTML, plain text).

Language-specific subclasses ship the actual letter tables. ``bbe``
implements the English (UEB-style) grade-1 mapping; more languages can be
added by subclassing :class:`BrailleBase` and registering mappings with
:meth:`BrailleBase.append_multiple_braille_letters`.
"""

__version__ = "0.2.0"

__all__ = ["BrailleBase", "bbe"]


class BrailleBase:
    # map: __letter_brailles[letter: str]  = braille_list} 
    # map: __letter_special_braille_rules_uppercase[letter: str]  = special_braille_list} 


#   self.__letter_brailles: dict[str, list[str]]
#   self.__letter_special_braille_rules_uppercase: dict[str, list[str]]
#   self.__letter_special_braille_rules_CJK: dict[str, list[str]]
#   self.__letter_special_braille_rules_RTL: dict[str, list[str]]
#   self.__braille_to_index: dict[str, int]

#   self.__BrailleList: list[str]
#   self.__BinaryList: list[list[int]]
#   self.__BinaryStringList: list[str]
#   self.__UnicodeList: list[str]
#   self.__DotCountList: list[int]
#   self.__DotNumberingList: list[list[int]]
#   self.__DotNumberingStringList: list[str]
#   self.__ReverseBrailleList: list[str]

#   self.__braille_rules_uppercase: str
#   self.__braille_rules_lowcase: str
#   self.__braille_rules_CJK: str
#   self.__braille_rules_RTL: str

    #0000
    def __init__(self):
        """
        0000
        """
        self.__token_size = 12

        self.__letter_brailles: dict[str, list[str]] = {}
        #rules uppercase
        self.__letter_special_braille_rules_uppercase: dict[str, list[str]] = {}
        self.setting_braille_rules_uppercase("⠠", "⠠")
        #rules CJK: China, Japan, Korea
        self.__letter_special_braille_rules_CJK: dict[str, list[str]] = {}
        self.setting_braille_rules_CJK("")
        #rules RTL: Right-to-Left
        self.__letter_special_braille_rules_RTL: dict[str, list[str]] = {}
        self.setting_braille_rules_RTL("")

        self.__constructor_map_braille()
        self.__constructor_map_spaces()
        self.__constructor_all_table()
        
#---------------------------------------- Registry group (0001) ----------------------------------------
    #-----Append----------------------------------------------------------------------------------------
    #0001-AA
    def append_braille_letter(self, letter: str, braille_list: list, type = 0):
        """
        0001-AA
        Registers a letter and its associated braille list. If the letter already exists, its mapping is overwritten.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """

        if not isinstance(letter, str):
            raise TypeError("letter must be a string")
        elif len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)
        self.__letter_brailles[letter] = braille_list

        match type:
            case 1:
                self.__letter_special_braille_rules_uppercase[letter] = braille_list
            case 2:
                self.__letter_special_braille_rules_CJK[letter] = braille_list
            case 3:
                self.__letter_special_braille_rules_RTL[letter] = braille_list

    #-----Get-------------------------------------------------------------------------------------------
    #0001-B
    def get_brailles_with_letter(self, letter: str):
        """
        0001-B
        This method is the core of the application: it receives a letter* and returns the list of braille symbols associated with it. 
        If the letter* is not registered, an error is raised.
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")
        

        return self.__letter_brailles[letter]

    #-----Has-------------------------------------------------------------------------------------------
    #0001-CA
    def has_letter(self, letter: str, type = 0) -> bool:
        """
        0001-CA
        Checks whether the given letter is registered in the internal mapping. Returns True or False.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
        match type:
            case 0:
                return letter in self.__letter_brailles
            case 1:
                return letter in self.__letter_special_braille_rules_uppercase
            case 2:
                return letter in self.__letter_special_braille_rules_CJK
            case 3:
                return letter in self.__letter_special_braille_rules_RTL

    #-----Remove----------------------------------------------------------------------------------------
    #0001-D
    def remove_letter(self, letter: str, type = 0) -> bool:
        """
        0001-D
        Removes the given letter from the internal mapping. Returns True if the letter existed and was removed, otherwise returns False.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
        if letter in self.__letter_brailles:
            del self.__letter_brailles[letter]

            match type:                 
                case 1:
                    if letter in self.__letter_special_braille_rules_uppercase:
                        del  self.__letter_special_braille_rules_uppercase[letter]
                case 2:
                    if letter in self.__letter_special_braille_rules_CJK:
                        del  self.__letter_special_braille_rules_CJK[letter]
                case 3:
                    if letter in self.__letter_special_braille_rules_RTL:
                        del  self.__letter_special_braille_rules_RTL[letter]
    
            return True
        return False

    #-----Get Registered--------------------------------------------------------------------------------
    #0001-EA
    def get_registered_letters(self, type = 0):
        """
        0001-EA
        Returns a list containing all letters currently registered in the internal mapping.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
    
        match type:    
            case 0:
                return list(self.__letter_brailles.keys())             
            case 1:
                return list(self.__letter_special_braille_rules_uppercase.keys())
            case 2:
                return list(self.__letter_special_braille_rules_CJK.keys())
            case 3:
                return list(self.__letter_special_braille_rules_RTL.keys())
    

    #0001-F
    def append_multiple_braille_letters(self, mapping: dict, type = 0):
        """
        0001-F
        Registers multiple letter-to-braille mappings at once. Each entry is validated and added individually.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
        if not isinstance(mapping, dict):
            raise TypeError("mapping must be a dict")

        for letter, braille_list in mapping.items():
            self.append_braille_letter(letter, braille_list)
            match type:                
                case 1:
                    self.append_braille_letter(letter, braille_list, 1)
                case 2:
                    self.append_braille_letter(letter, braille_list, 2)
                case 3:
                    self.append_braille_letter(letter, braille_list, 3)
            

    #0001-G
    def edit_braille_letter(self, letter: str, new_braille_list: list, type = 0):
        """
        0001-G
        Edits the braille list associated with the given letter. Raises an error if the letter is not registered.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")

        self.__validate_braille_list(new_braille_list)
        self.__letter_brailles[letter] = new_braille_list

        match type:                
            case 1:
                self.__letter_special_braille_rules_uppercase[letter] = new_braille_list
            case 2:
                self.__letter_special_braille_rules_CJK[letter] = new_braille_list
            case 3:
                self.__letter_special_braille_rules_RTL[letter] = new_braille_list

#---------------------------------------- Mapping group (0003) ----------------------------------------
    #0003-A
    def get_braille_to_index(self, braille: str) -> int:
        """
        0003-A
        Receives a character (string), which must be a valid braille symbol, 
        and returns an integer (int) that represents its position in the Unicode braille table (U+2800 to U+283F).

        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63
        """

        return self.__braille_to_index[braille]
  
    #0003-C
    def get_index_to_braille(self, index: int) -> str:
        """
        0003-C
        """
        return self.__BrailleList[index]
    
    #0003-B
    def get_braille_list_to_index_list(self, braille_list: list[str]) -> list[int]:
        """
        0003-B
        Receives multiple characters (strings), each of which must be a valid braille symbol, and returns a list of integers (int), 
        where each value represents the position of the corresponding symbol in the Unicode braille table (U+2800 to U+283F).
         """
        return [self.get_braille_to_index(b) for b in braille_list]
    

#---------------------------------------- Translate group (0002) ----------------------------------------
   #0002-A
    def translate_text_to_braille(self, text: str) -> list:
        """
        0002-A
        The method expects a string as an argument — the text to be translated into braille.
        Each character is converted into braille.
        This is the main method of the translate group.
        The entire text is processed and converted into a list of braille symbols, which will later be transformed into a list of indices.
        All methods in the translate group are fully dependent on translate_text_to_braille(text: str).
        """

        tokens = self.confidence_test(text)

        result = []
        for iToken in range(0, len(tokens)):
            brailles = self.get_brailles_with_letter(tokens[iToken][0])
            result.extend(brailles)

        return result

    #0002-B
    def translate_text_to_index(self, textBraille: str) -> list:
        """
        Translates the input text into a list of braille indices. Each character may expand into multiple braille cells.
        """
        brailles = self.translate_text_to_braille(textBraille)
        return self.get_braille_list_to_index_list(brailles)
    
    #0002-C
    def translate_text_to_binary_string(self, text: str) -> list:
        """
        Translates the input text into a list of 6-bit binary strings representing each braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__BinaryStringList[i] for i in indices]
    
    #0002-D
    def translate_text_to_binary_list(self, text: str) -> list:
        """
        Translates the input text into a list of 6-bit binary arrays representing each braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__BinaryList[i] for i in indices]
    
    #0002-E
    def translate_text_to_unicode(self, text: str) -> list:
        """
        Translates the input text into a list of Unicode code representations for each braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__UnicodeList[i] for i in indices]
    
    #0002-F
    def translate_text_to_dot_count(self, text: str) -> list:
        """
        Translates the input text into a list containing the dot count of each braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__DotCountList[i] for i in indices]

    #0002-G
    def translate_text_to_numbering_string(self, text: str) -> list:
        """
        Translates the input text into a list of numbering strings, each indicating the active dot positions of every braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__DotNumberingStringList[i] for i in indices]
    
    #0002-H
    def translate_text_to_numbering_list(self, text: str) -> list:
        """
        Translates the input text into a list of numbering lists, each containing the active dot positions of every braille cell.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__DotNumberingList[i] for i in indices]
    
    #0002-I
    def translate_text_to_full_list(self, text: str) -> list:
        """
        Translates the input text into a full list of braille-related data.  
        Each entry contains: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)

        result = []

        for idx in range(len(indices)):
            i = indices[idx]
            result.append([
                brailles[idx],
                i,
                self.__BinaryStringList[i],
                self.__BinaryList[i],
                self.__UnicodeList[i],
                self.__DotCountList[i],
                self.__DotNumberingStringList[i],
                self.__DotNumberingList[i],
                self.__ReverseBrailleList[i],
            ])
        return result
    

    #0002-J
    def translate_text_to_reverse_braille(self, textBraille: str) -> list:
        """
        Translates the input text into a list of Reverse Braille.
        """
        brailles = self.translate_text_to_braille(textBraille)
        indices = self.get_braille_list_to_index_list(brailles)
        return [self.__ReverseBrailleList[i] for i in reversed(indices)]
    
#---------------------------------------- Output group (0005) ----------------------------------------

    #0005-A
    def output_all_json(self, text: str) -> str:
        """
        Generates a JSON array containing all braille-related data for each character in the input text.  
        Each entry includes: original letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import json

        result = []

        brailles_map = self.confidence_test(text)

        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)

                result.append({
                    "index": key,
                    "Letter": braille_list[0],

                    "Braille": self.__BrailleList[idx],
                    "Binary": self.__BinaryStringList[idx],
                    "Numbering": self.__DotNumberingStringList[idx],
                    "Unicode":  "U+" + self.__UnicodeList[idx],

                    "ReverseBraille": self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    "ReverseBinary": self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    "ReverseNumbering": self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    "ReverseUnicode": "U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]
                })

        return json.dumps(result, ensure_ascii=False, indent=4)
        

    #0005-B
    def output_all_csv(self, text: str) -> str:
        """
        Generates a CSV string containing all braille-related data for each character in the input text.  
        Each row includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import csv
        import io

        output = io.StringIO()
        writer = csv.writer(output)

        writer.writerow([
            "index",
            "Letter",

            "Braille",
            "Binary",
            "Numbering",
            "Unicode",

            "ReverseBraille",
            "ReverseBinary",
            "ReverseNumbering",
            "ReverseUnicode",
        ])


        brailles_map = self.confidence_test(text)

        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)

                writer.writerow([
                    key,
                    braille_list[0],

                    self.__BrailleList[idx],
                    self.__BinaryStringList[idx],
                    self.__DotNumberingStringList[idx],
                    "U+" + self.__UnicodeList[idx],

                    self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])],
                    "U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]
                ])

        return output.getvalue()

    #0005-C
    def output_all_xml(self, text: str) -> str:
        """
        Generates a formatted XML string containing all braille-related data for each character in the input text.  
        Each <item> node includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import xml.etree.ElementTree as ET
        import xml.dom.minidom as minidom

        root = ET.Element("braille_output")

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            item = ET.SubElement(root, "item")
            ET.SubElement(item, "braille").text = self.__BrailleList[idx]
            ET.SubElement(item, "index").text = str(idx)
            ET.SubElement(item, "binary_string").text = self.__BinaryStringList[idx]
            ET.SubElement(item, "binary_list").text = str(self.__BinaryList[idx])
            ET.SubElement(item, "unicode").text = self.__UnicodeList[idx]
            ET.SubElement(item, "dot_count").text = str(self.__DotCountList[idx])
            ET.SubElement(item, "numbering_string").text = self.__DotNumberingStringList[idx]
            ET.SubElement(item, "numbering_list").text = str(self.__DotNumberingList[idx])
            ET.SubElement(item, "reverse_braille").text = self.__ReverseBrailleList[idx]

        rough_xml = ET.tostring(root, encoding="utf-8")
        reparsed = minidom.parseString(rough_xml)
        return reparsed.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8")

    #0005-D
    def output_all_yaml(self, text: str) -> str:
        """
        Generates a YAML-formatted string containing all braille-related data for each character in the input text.  
        Each entry includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            lines.append(f"- braille: \"{self.__BrailleList[idx]}\"")
            lines.append(f"  index: {idx}")
            lines.append(f"  binary_string: \"{self.__BinaryStringList[idx]}\"")
            lines.append(f"  binary_list: {self.__BinaryList[idx]}")
            lines.append(f"  unicode: \"{self.__UnicodeList[idx]}\"")
            lines.append(f"  dot_count: {self.__DotCountList[idx]}")
            lines.append(f"  numbering_string: \"{self.__DotNumberingStringList[idx]}\"")
            lines.append(f"  numbering_list: {self.__DotNumberingList[idx]}")
            lines.append(f"  reverse_braille: \"{self.__ReverseBrailleList[idx]}\"")
            lines.append("")

        return "\n".join(lines)

    #0005-E
    def output_all_markdown(self, text: str) -> str:
        """
        Generates a Markdown-formatted string containing all braille-related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            lines.append(f"## Braille {count}")
            lines.append(f"- **Braille:** {self.__BrailleList[idx]}")
            lines.append(f"- **Index:** {idx}")
            lines.append(f"- **Binary:** `{self.__BinaryStringList[idx]}`")
            lines.append(f"- **Binary List:** {self.__BinaryList[idx]}")
            lines.append(f"- **Unicode:** {self.__UnicodeList[idx]}")
            lines.append(f"- **Dot Count:** {self.__DotCountList[idx]}")
            lines.append(f"- **Numbering:** {self.__DotNumberingStringList[idx]}")
            lines.append(f"- **Numbering List:** {self.__DotNumberingList[idx]}")
            lines.append(f"- **Reverse Braille:** {self.__ReverseBrailleList[idx]}")
            lines.append("")

            count += 1

        return "\n".join(lines)
    
    #0005-F
    def output_all_html(self, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        Generates an HTML-formatted string containing all braille-related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []
        brailles_map = self.confidence_test(text)

        lines.append('<!DOCTYPE html>')
        lines.append('<html>')
        lines.append('<head>')
        lines.append('  <meta charset="UTF-8">')
        lines.append('  <title>Braille Base - HTML Generate</title>')
        lines.append('  <style>')
        lines.append('    table {      border-collapse: collapse;      width: 400px;      font-family: sans-serif;    }')
        lines.append('    td {      border: 1px solid #000;      padding: 6px 10px;    }')
        lines.append('    .cell-letter {      font-size: 48px;      text-align: center;      vertical-align: middle;      width: 100px;    }')
        lines.append('  </style>')
        lines.append('</head>')
        lines.append('<body>')

        lines.append('<div class="text-output">')
        lines.append('<h2>Text</h2>')
        lines.append(f'<p>{text}</p>')
        lines.append('</div>')

        lines.append('<div class="read-braille-output">')
        lines.append('<h2>Read Braille</h2>')
        lines.append(f'<p>{self.translate_text_to_braille(text)}</p>')
        lines.append('</div>')

        lines.append('<div class="read-braille-output">')
        lines.append('<h2>Write Braille</h2>')
        lines.append(f'<p>{self.translate_text_to_reverse_braille(text)}</p>')
        lines.append('</div>')

        lines.append('<div class="braille-table-output">')

        for key, braille_list in brailles_map.items():
            lines.append(f'    <h3>Letter {key}</h3>')
            lines.append('<table>')

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)
                rev_idx = self.__BrailleList.index(self.__ReverseBrailleList[idx])

                lines.append('      <tr>')
                lines.append(f'        <td class="cell-letter" rowspan="10">{braille_list[0]}</td>')
                lines.append('        <td colspan="2"><b>Read Braille</b></td>')
                lines.append('      </tr>')
                lines.append(f'      <tr>    <td>Braille:</td><td>{self.__BrailleList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Binary:</td><td>{self.__BinaryStringList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Numbering:</td><td>{self.__DotNumberingStringList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Unicode:</td><td>U+{self.__UnicodeList[idx]}</td>  </tr>')
                #Reverse Braille
                lines.append('      <tr>')
                lines.append('        <td colspan="2"><b>Write Braille</b></td>')
                lines.append('      </tr>')
                lines.append(f'      <tr>    <td>Braille:</td><td>{self.__BrailleList[rev_idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Binary:</td><td>{self.__BinaryStringList[rev_idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Numbering:</td><td>{self.__DotNumberingStringList[rev_idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Unicode:</td><td>U+{self.__UnicodeList[rev_idx]}</td>  </tr>')

            lines.append('</table>')
            lines.append('<br>')

                
        lines.append('</div>')
        lines.append(f'<footer><p>{footer}</p></footer>')
        lines.append('</body>')
        lines.append('</html>')

        return "\n".join(lines)

    #0005-GA
    def output_all_txt(self, text: str) -> str:
        """
        Generates a plain text string containing all braille-related data for each character in the input text.  
        Each block includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            lines.append(f"Braille {count}")
            lines.append(f"Braille: {self.__BrailleList[idx]}")
            lines.append(f"Index: {idx}")
            lines.append(f"Binary: {self.__BinaryStringList[idx]}")
            lines.append(f"Binary List: {self.__BinaryList[idx]}")
            lines.append(f"Unicode: {self.__UnicodeList[idx]}")
            lines.append(f"Dot Count: {self.__DotCountList[idx]}")
            lines.append(f"Numbering: {self.__DotNumberingStringList[idx]}")
            lines.append(f"Numbering List: {self.__DotNumberingList[idx]}")
            lines.append(f"Reverse Braille: {self.__ReverseBrailleList[idx]}")
            lines.append("-" * 40)
            lines.append("")

            count += 1

        return "\n".join(lines)

    #0005-GB
    def output_binary_txt(self, text: str) -> str:
        """
        Generates a plain text string containing only the binary strings of each braille cell derived from the input text.
        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)                    
            lines.append(self.__BinaryStringList[idx])

        return "\n".join(lines)
 
    #0005-GCA
    def output_braille_txt(self, text: str) -> str:
        """

        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)
            lines.append(self.__BrailleList[idx])

        return "".join(lines)
    
    #0005-GCB
    def output_reverse_braille_txt(self, text: str) -> str:
        """

        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        for braille_cell in reversed(brailles):
            idx = self.__BrailleList.index(braille_cell)
            lines.append(self.__ReverseBrailleList[idx])

        return "".join(lines)
    
    #----------------------------Internal logic of exceptions-------------------------------
    def __validate_braille_list(self, braille_list: list):
        """
        Internal method that validates a list of braille symbols.  
        Ensures the value is a list, that each item is a string, and that every string is a valid Unicode braille character (U+2800-U+283F).
        """
        if not isinstance(braille_list, list):
            raise TypeError("braille_list must be a list")

        for b in braille_list:
            if not isinstance(b, str):
                raise TypeError("each braille item must be a string")
            if not ("\u2800" <= b <= "\u283F"):
                raise ValueError(f"invalid braille character: {b}")
            
    #----------------------------Internal logic for braille number processing---------------------------
    def prepare_number_braille(self, text: str) -> str:
        """
        """
        result = []
        previous = False

        for ch in text:
            isnum = ch.isdigit()

            if isnum and not previous:
                result.append("⠼")

            result.append(ch)
            previous = isnum

        return "".join(result)
    
    #----------------------------Prepare Special 01: Roma Letter---------------------------

    def prepare_special_braille_rules_uppercase(self, text: str) -> str:
        result = []
        text_size = len(text)

        for iLetter in range(text_size):
            previous_letter = text[iLetter - 1] if iLetter > 0 else None
            current_letter = text[iLetter]
            next_letter = text[iLetter + 1] if iLetter < text_size - 1 else None

            has_previous_letter = previous_letter in self.__letter_special_braille_rules_uppercase if previous_letter else False
            has_current_letter = current_letter in self.__letter_special_braille_rules_uppercase
            has_next_letter = next_letter in self.__letter_special_braille_rules_uppercase if next_letter else False

            if not has_previous_letter and has_current_letter and has_next_letter:
                result.append(self.__braille_rules_uppercase)
                result.append(self.__braille_rules_uppercase)

            elif  not has_previous_letter and has_current_letter and not has_next_letter:
                result.append(self.__braille_rules_uppercase)


            if has_previous_letter and has_current_letter and not has_next_letter:
                result.append(current_letter)
                result.append(self.__braille_rules_lowcase)
            else:
                result.append(current_letter)

        return "".join(result)
    
    def setting_braille_rules_uppercase(self, braille_uppercase: str, braille_lowercase: str):
        self.__braille_rules_uppercase = braille_uppercase
        self.__braille_rules_lowcase = braille_lowercase

    #----------------------------Prepare Special 02---------------------------
    
    def prepare_special_braille_rules_CJK(self, text: str) -> str:
        result = []
        previous = False

        for ch in text:
            is_special = ch in self.__letter_special_braille_rules_CJK

            if is_special and not previous:
                result.append(self.__braille_rules_CJK)

            result.append(ch)
            previous = is_special

        return "".join(result)
    
    def setting_braille_rules_CJK(self, braille: str):
        self.__braille_rules_CJK = braille

    #----------------------------Prepare Special 02---------------------------
    
    def prepare_special_braille_rules_RTL(self, text: str) -> str:
        result = []
        previous = False

        for ch in text:
            is_special = ch in self.__letter_special_braille_rules_RTL

            if is_special and not previous:
                result.append(self.__braille_rules_RTL)

            result.append(ch)
            previous = is_special

        return "".join(result)
    
    def setting_braille_rules_RTL(self, braille: str):
        self.__braille_rules_RTL = braille

    #----------------------------Token---------------------------

    def tokenize_text(self, text: str) -> list[str]:
        tokens = []
        i = 0
        max_len = self.__token_size  

        while i < len(text):
            matched = False

            for size in range(max_len, 0, -1):
                chunk = text[i:i+size]

                if chunk in self.__letter_brailles:
                    tokens.append(chunk)
                    i += len(chunk)
                    matched = True
                    break

            if not matched:
                raise KeyError(f"letter '{text[i]}' not registered")

        return tokens
    
    #    def tokenize_text(self, text: str) -> list[str]:
    def confidence_test(self, text: str) -> dict:
        iToken = 0

        text = self.prepare_number_braille(text)
        text = self.prepare_special_braille_rules_uppercase(text)
        text = self.prepare_special_braille_rules_CJK(text)
        text = self.prepare_special_braille_rules_RTL(text)

        tokens = self.tokenize_text(text)
        result = {}
        for token in tokens:
            brailles = self.get_brailles_with_letter(token)
            result[iToken] = [token, brailles]

            iToken+=1
        return result

    def configure_token(self, token_size: int):
        """
        Sets the maximum token length used by :meth:`tokenize_text`.

        The tokenizer tries the longest registered mapping first, so this
        value must be at least as large as the longest multi-cell braille
        mapping (e.g. a two-cell quote mark). Defaults to 12.
        """
        if not isinstance(token_size, int) or isinstance(token_size, bool):
            raise TypeError("token_size must be an integer")
        if token_size < 1:
            raise ValueError("token_size must be >= 1")
        self.__token_size = token_size
        #----------------------------Constructor ---------------------------

    def __constructor_all_table(self):
        from brailletable import BrailleTable

        self.__BrailleList: list[str] = BrailleTable.braille_list() #A
        self.__BinaryList: list[list[int]] = BrailleTable.binary_list() #B
        self.__BinaryStringList: list[str] = BrailleTable.binary_string_list() #C
        self.__UnicodeList: list[str] = BrailleTable.unicode_list() #D
        self.__DotCountList: list[int] = BrailleTable.dot_count() #E
        self.__DotNumberingList: list[list[int]]  = BrailleTable.dot_numbering_list() #F
        self.__DotNumberingStringList: list[str] = BrailleTable.dot_numbering_string_list() #G
        self.__ReverseBrailleList: list[str] = BrailleTable.reverse_braille_list() #H

        self.__braille_to_index = {
        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63
    }

    def __constructor_map_braille(self):
        braille_map = {

        "⠀": ["\u2800"],
        "⠁": ["⠁"],
        "⠂": ["⠂"],
        "⠃": ["⠃"],
        "⠄": ["⠄"],
        "⠅": ["⠅"],
        "⠆": ["⠆"],
        "⠇": ["⠇"],
        "⠈": ["⠈"],
        "⠉": ["⠉"],
        "⠊": ["⠊"],
        "⠋": ["⠋"],
        "⠌": ["⠌"],
        "⠍": ["⠍"],
        "⠎": ["⠎"],
        "⠏": ["⠏"],
        "⠐": ["⠐"],
        "⠑": ["⠑"],
        "⠒": ["⠒"],
        "⠓": ["⠓"],
        "⠔": ["⠔"],
        "⠕": ["⠕"],
        "⠖": ["⠖"],
        "⠗": ["⠗"],
        "⠘": ["⠘"],
        "⠙": ["⠙"],
        "⠚": ["⠚"],
        "⠛": ["⠛"],
        "⠜": ["⠜"],
        "⠝": ["⠝"],
        "⠞": ["⠞"],
        "⠟": ["⠟"],
        "⠠": ["⠠"],
        "⠡": ["⠡"],
        "⠢": ["⠢"],
        "⠣": ["⠣"],
        "⠤": ["⠤"],
        "⠥": ["⠥"],
        "⠦": ["⠦"],
        "⠧": ["⠧"],
        "⠨": ["⠨"],
        "⠩": ["⠩"],
        "⠪": ["⠪"],
        "⠫": ["⠫"],
        "⠬": ["⠬"],
        "⠭": ["⠭"],
        "⠮": ["⠮"],
        "⠯": ["⠯"],
        "⠰": ["⠰"],
        "⠱": ["⠱"],
        "⠲": ["⠲"],
        "⠳": ["⠳"],
        "⠴": ["⠴"],
        "⠵": ["⠵"],
        "⠶": ["⠶"],
        "⠷": ["⠷"],
        "⠸": ["⠸"],
        "⠹": ["⠹"],
        "⠺": ["⠺"],
        "⠻": ["⠻"],
        "⠼": ["⠼"],
        "⠽": ["⠽"],
        "⠾": ["⠾"],
        "⠿": ["⠿"]
        }
        self.append_multiple_braille_letters(braille_map)

    def __constructor_map_spaces(self):
        spaces = {
            # whitespace
            "\u0020": ["\u2800"],  # SPACE
            "\u1680": ["\u2800"],
            "\u180E": ["\u2800"],
            "\u2000": ["\u2800"],
            "\u2001": ["\u2800"],
            "\u2002": ["\u2800"],
            "\u2003": ["\u2800"],
            "\u2004": ["\u2800"],
            "\u2005": ["\u2800"],
            "\u2006": ["\u2800"],
            "\u2007": ["\u2800"],
            "\u2008": ["\u2800"],
            "\u2009": ["\u2800"],
            "\u200A": ["\u2800"],
            "\u200B": ["\u2800"],
            "\u200C": ["\u2800"],
            "\u200D": ["\u2800"],
            "\u202F": ["\u2800"],
            "\u205F": ["\u2800"],
            "\u2060": ["\u2800"],
            "\u3000": ["\u2800"],
            "\uFEFF": ["\u2800"],

            #"\u00A0": ["⠀"],      # NBSP
            #"\t": ["⠄"],   # TAB
            #"\n": ["\n"]
        }

        self.append_multiple_braille_letters(spaces)


#---------------------------------------- English subclass (bbe) ----------------------------------------

class bbe(BrailleBase):
    """
    English (UEB-style grade 1) braille engine.

    Ships the standard English letter table: a-z, A-Z, digits 0-9 and
    common punctuation. Uppercase letters are marked with the capital
    sign (U+2800 block ``⠠``) and digit runs with the number sign
    (``⠼``), following the rules already implemented in the base class.
    """

    def __init__(self):
        super().__init__()

        letters = {
            "a": ["\u2801"], "b": ["\u2803"], "c": ["\u2809"], "d": ["\u2819"],
            "e": ["\u2811"], "f": ["\u280B"], "g": ["\u281B"], "h": ["\u2813"],
            "i": ["\u280A"], "j": ["\u281A"], "k": ["\u2805"], "l": ["\u2807"],
            "m": ["\u280D"], "n": ["\u281D"], "o": ["\u2815"], "p": ["\u280F"],
            "q": ["\u281F"], "r": ["\u2817"], "s": ["\u280E"], "t": ["\u281E"],
            "u": ["\u2825"], "v": ["\u2827"], "w": ["\u283A"], "x": ["\u282D"],
            "y": ["\u283D"], "z": ["\u2835"],
        }
        self.append_multiple_braille_letters(letters)

        # Uppercase letters reuse the lowercase cells; the capital sign is
        # inserted by prepare_special_braille_rules_uppercase (type=1).
        uppercase = {ch.upper(): cells for ch, cells in letters.items()}
        self.append_multiple_braille_letters(uppercase, 1)

        # Digits: 1-9, 0 map to the a-j cells, prefixed by the number sign
        # (⠼) which the base class inserts automatically.
        digits = {
            "1": ["\u2801"], "2": ["\u2803"], "3": ["\u2809"], "4": ["\u2819"],
            "5": ["\u2811"], "6": ["\u280B"], "7": ["\u281B"], "8": ["\u2813"],
            "9": ["\u280A"], "0": ["\u281A"],
        }
        self.append_multiple_braille_letters(digits)

        # Common punctuation (single-cell and the two-cell quote mark).
        punctuation = {
            ".": ["\u2832"], ",": ["\u2802"], "?": ["\u2826"], "!": ["\u2816"],
            "'": ["\u2804"], ";": ["\u2806"], ":": ["\u2812"], "-": ["\u2824"],
            "(": ["\u2836"], ")": ["\u2836"], "\"": ["\u2810", "\u2826"],
        }
        self.append_multiple_braille_letters(punctuation)
