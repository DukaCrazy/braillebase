class BrailleBase:
    # map: __letter_brailles[letter: str]  = braille_list} 
    # map: __letter_specialBraille_rules01[letter: str]  = specialBraille_list} 


#   self.__letter_brailles: dict[str, list[str]]
#   self.__letter_specialBraille_rules01: dict[str, list[str]]
#   self.__letter_specialBraille_rules_CJK: dict[str, list[str]]
#   self.__braille_to_index: dict[str, int]

#   self.__BrailleList: list[str]
#   self.__BinaryList: list[list[int]]
#   self.__BinaryStringList: list[str]
#   self.__UnicodeList: list[str]
#   self.__DotCountList: list[int]
#   self.__DotNumberingList: list[list[int]]
#   self.__DotNumberingStringList: list[str]

#   self.__braille_rules_uppercase: str
#   self.__braille_rules_lowcase: str
#   self.__braille_rules_CJK: str

    #0000
    def __init__(self):
        self.__letter_brailles: dict[str, list[str]] = {}
        #rules 01
        self.__letter_specialBraille_rules01: dict[str, list[str]] = {}
        self.setting_braille_rules01("⠠", "⠠")
        #rules CJK: China, Japan, Korea
        self.__letter_specialBraille_rules_CJK: dict[str, list[str]] = {}
        self.setting_braille_rules_CJK("")

        self.__constructor_map_braille()
        self.__constructor_map_spaces()
        self.__constructor_all_table()
        
#---------------------------------------- Registry group (0001) ----------------------------------------
    #0001-AA
    def append_braille_letter(self, letter: str, braille_list: list):
        """
        Registers a letter and its associated braille list. If the letter already exists, its mapping is overwritten.
        """
        if not isinstance(letter, str):
            raise TypeError("letter must be a string")

        if len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)

        self.__letter_brailles[letter] = braille_list

    #0001-AB
    def append_special_braille_lettr_rules01(self, letter: str, braille_list: list):
        """
        """
        if not isinstance(letter, str):
            raise TypeError("letter must be a string")

        if len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)

        self.__letter_brailles[letter] = braille_list
        self.__letter_specialBraille_rules01[letter] = braille_list


    #0001-AC
    def append_special_braille_lettr_rules_CJK(self, letter: str, braille_list: list):
        """
        Adds Chinese, Japanese, and Korean characters to the CJK list.
        """
        if not isinstance(letter, str):
            raise TypeError("letter must be a string")

        if len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)

        self.__letter_brailles[letter] = braille_list
        self.__letter_specialBraille_rules_CJK[letter] = braille_list

    #0001-B
    def get_brailles_with_letter(self, letter: str):
        """
        This method is the core of the application: it receives a letter* and returns the list of braille symbols associated with it. 
        If the letter* is not registered, an error is raised.
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")
        return self.__letter_brailles[letter]

    #0001-CA
    def has_letter(self, letter: str) -> bool:
        """
        Checks whether the given letter is registered in the internal mapping. Returns True or False.
        """
        return letter in self.__letter_brailles
    
    #0001-CB
    def has_letter_specialBraille_rules01(self, letter: str) -> bool:
        """
        """
        return letter in self.__letter_specialBraille_rules01
    
    #0001-CC
    def has_letter_specialBraille_rules_CJK(self, letter: str) -> bool:
        """
        """
        return letter in self.__letter_specialBraille_rules_CJK

    #0001-D
    def remove_letter(self, letter: str):
        """
        Removes the given letter from the internal mapping. Returns True if the letter existed and was removed, otherwise returns False.
        """
        if letter in self.__letter_brailles:
            del self.__letter_brailles[letter]
            return True
        return False


    #0001-EA
    def get_registered_letters(self):
        """
        Returns a list containing all letters currently registered in the internal mapping.
        """
        return list(self.__letter_brailles.keys())
    
    #0001-EB
    def get_registered_letters_specialBraille_Rules01(self):
        """
        """
        return list(self.__letter_specialBraille_rules01.keys())
    
    #0001-EC
    def get_registered_letters_specialBraille_rules_CJK(self):
        """
        """
        return list(self.__letter_specialBraille_rules_CJK.keys())

    #0001-F
    def append_multiple_braille_letters(self, mapping: dict):
        """
        Registers multiple letter-to-braille mappings at once. Each entry is validated and added individually.
        """
        if not isinstance(mapping, dict):
            raise TypeError("mapping must be a dict")

        for letter, braille_list in mapping.items():
            self.append_braille_letter(letter, braille_list)

    #0001-G
    def edit_braille_letter(self, letter: str, new_braille_list: list):
        """
        Edits the braille list associated with the given letter. Raises an error if the letter is not registered.
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")

        self.__validate_braille_list(new_braille_list)

        self.__letter_brailles[letter] = new_braille_list

#---------------------------------------- Mapping group (0003) ----------------------------------------
    #0003-A
    def get_braille_to_index(self, braille: str) -> int:
        """
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
        return self.__BrailleList[index]
    
    #0003-B
    def get_braille_list_to_index_list(self, braille_list: list[str]) -> list[int]:
        """
        Receives multiple characters (strings), each of which must be a valid braille symbol, and returns a list of integers (int), 
        where each value represents the position of the corresponding symbol in the Unicode braille table (U+2800 to U+283F).
         """
        return [self.get_braille_to_index(b) for b in braille_list]
    

#---------------------------------------- Translate group (0002) ----------------------------------------
   #0002-A
    def translate_text_to_braille(self, text: str) -> list:
        """
        The method expects a string as an argument — the text to be translated into braille.
        Each character is converted into braille.
        This is the main method of the translate group.
        The entire text is processed and converted into a list of braille symbols, which will later be transformed into a list of indices.
        All methods in the translate group are fully dependent on translate_text_to_braille(text: str).
        """
        text = self.prepare_number_braille(text)
        #apply rules 1
        text = self.prepare_special_braille_rules01(text)
        #apply rules 2
        text = self.prepare_special_braille_rules_CJK(text)
        tokens = self.tokenize_text(text)

        result = []
        for token in tokens:
            brailles = self.get_brailles_with_letter(token)
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
                self.__DotNumberingList[i]
            ])
        return result
#---------------------------------------- Output group (0005) ----------------------------------------

    #0005-A
    def output_all_json(self, text: str) -> str:
        """
        Generates a JSON array containing all braille-related data for each character in the input text.  
        Each entry includes: original letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import json

        result = []


        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            result.append({
                "braille": self.__BrailleList[idx],
                "index": idx,
                "binary_string": self.__BinaryStringList[idx],
                "binary_list": self.__BinaryList[idx],
                "unicode": self.__UnicodeList[idx],
                "dot_count": self.__DotCountList[idx],
                "numbering_string": self.__DotNumberingStringList[idx],
                "numbering_list": self.__DotNumberingList[idx]
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
            "letter",
            "braille",
            "index",
            "binary_string",
            "binary_list",
            "unicode",
            "dot_count",
            "numbering_string",
            "numbering_list"
        ])


        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            writer.writerow([
                "",
                self.__BrailleList[idx],
                idx,
                self.__BinaryStringList[idx],
                str(self.__BinaryList[idx]),
                self.__UnicodeList[idx],
                self.__DotCountList[idx],
                self.__DotNumberingStringList[idx],
                str(self.__DotNumberingList[idx])
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
            lines.append("")

            count += 1

        return "\n".join(lines)
    
    #0005-F
    def output_all_html(self, text: str) -> str:
        """
        Generates an HTML-formatted string containing all braille-related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        lines.append('<div class="braille-output">')

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)

            lines.append(f'  <section class="braille-item">')
            lines.append(f'    <h2>Braille {count}</h2>')
            lines.append('    <ul>')
            lines.append(f'      <li><strong>Braille:</strong> {self.__BrailleList[idx]}</li>')
            lines.append(f'      <li><strong>Index:</strong> {idx}</li>')
            lines.append(f'      <li><strong>Binary:</strong> <code>{self.__BinaryStringList[idx]}</code></li>')
            lines.append(f'      <li><strong>Binary List:</strong> {self.__BinaryList[idx]}</li>')
            lines.append(f'      <li><strong>Unicode:</strong> {self.__UnicodeList[idx]}</li>')
            lines.append(f'      <li><strong>Dot Count:</strong> {self.__DotCountList[idx]}</li>')
            lines.append(f'      <li><strong>Numbering:</strong> {self.__DotNumberingStringList[idx]}</li>')
            lines.append(f'      <li><strong>Numbering List:</strong> {self.__DotNumberingList[idx]}</li>')
            lines.append('    </ul>')
            lines.append('  </section>')

            count += 1

        lines.append('</div>')

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
 
    #0005-GC
    def output_braille_txt(self, text: str) -> str:
        """

        """
        lines = []

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = self.__BrailleList.index(braille_cell)
            lines.append(self.__BrailleList[idx])

        return "".join(lines)

    #0005-GD
    def output_braille_map_txt(self, text: str) -> str:
        """

        """
        mapping = self.confidence_test(text)
        lines = []
        for token, brailles in mapping.items():
            lines.append(f"{token}: {''.join(brailles)}")
        return "\n".join(lines)
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

    def prepare_special_braille_rules01(self, text: str) -> str:
        result = []
        text_size = len(text)

        for iLetter in range(text_size):
            previous_letter = text[iLetter - 1] if iLetter > 0 else None
            current_letter = text[iLetter]
            next_letter = text[iLetter + 1] if iLetter < text_size - 1 else None

            has_previous_letter = previous_letter in self.__letter_specialBraille_rules01 if previous_letter else False
            has_current_letter = current_letter in self.__letter_specialBraille_rules01
            has_next_letter = next_letter in self.__letter_specialBraille_rules01 if next_letter else False

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
    
    def setting_braille_rules01(self, braille_uppercase: str, braille_lowercase: str):
        self.__braille_rules_uppercase = braille_uppercase
        self.__braille_rules_lowcase = braille_lowercase

    #----------------------------Prepare Special 02---------------------------
    
    def prepare_special_braille_rules_CJK(self, text: str) -> str:
        result = []
        previous = False

        for ch in text:
            is_special = ch in self.__letter_specialBraille_rules_CJK

            if is_special and not previous:
                result.append(self.__braille_rules_CJK)

            result.append(ch)
            previous = is_special

        return "".join(result)
    
    def setting_braille_rules_CJK(self, braille: str):
        self.__braille_rules_CJK = braille

    #----------------------------Token---------------------------

    def tokenize_text(self, text: str) -> list[str]:
        tokens = []
        i = 0
        max_len = 5  

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
    
    #    def tokenize_text(self, text: str) -> list[str]: #TEST
    def confidence_test(self, text: str) -> dict:
        text = self.prepare_number_braille(text)
        text = self.prepare_special_braille_rules01(text)
        text = self.prepare_special_braille_rules_CJK(text)

        tokens = self.tokenize_text(text)
        result = {}
        for token in tokens:
            brailles = self.get_brailles_with_letter(token)
            result[token] = brailles
        return result

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
