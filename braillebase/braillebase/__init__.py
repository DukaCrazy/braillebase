
class BrailleBasea:  
    # map: __letter_brailles[letter: str]  = braille_list} 
    # map: __letter_special_braille_rules_uppercase[letter: str]  = special_braille_list} 


#   self.__letter_brailles: dict[str, list[str]]
#   self.__letter_special_braille_rules_uppercase: dict[str, list[str]]
#   self.__letter_special_braille_rules_CJK: dict[str, list[str]]
#   self.__letter_special_braille_rules_RTL: dict[str, list[str]]
#   self.__BrailleIndex: dict[str, int]

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
        #Tokenize
        self.configure_token(12)

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

        #Constructor Initializate
        self.__constructor_all_table()
        self.__constructor_output()
        self.__constructor_map_braille()

        #Output

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
    

    #0001-FA
    def append_multiple_braille_letters(self, letter_braillelist_pattern: list):
        """
        0001-F
        Registers multiple letter-to-braille mappings at once. Each entry is validated and added individually.

        default: 0
        rules_uppercase: 1
        CJK: 2
        RTL: 3
        """
        if not isinstance(letter_braillelist_pattern, list):
            raise TypeError("Invalid: append_multiple_braille_letters - #0001-F")

        for index in letter_braillelist_pattern:
            self.append_braille_letter(index[0], index[1], index[2])

    #0001-FB IO Version
    def append_braille_letter_IO(self, target_data_path: str):
        from braillebaseinout import read_file
        self.append_multiple_braille_letters(read_file(target_data_path))

            
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

        return self.__BrailleIndex[braille]
  
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
                self.__ReverseBrailleList[idx],
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
        """
        return self.__BrailleBaseOutputString.output_all_json(self.confidence_test(text))
    
    #0005-B
    def output_all_csv(self, text: str) -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_csv(self.confidence_test(text))

    #0005-C
    def output_all_xml(self, text: str) -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_xml(self.confidence_test(text))

    #0005-D
    def output_all_yaml(self, text: str) -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_yaml(self.confidence_test(text))
    
    #0005-E
    def output_all_markdown(self, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_markdown(self.confidence_test(text), self.translate_text_to_braille(text), self.translate_text_to_reverse_braille(text), text, footer)
    
    #0005-F
    def output_all_html(self, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_html(self.confidence_test(text), self.translate_text_to_braille(text), self.translate_text_to_reverse_braille(text), text, footer)

    #0005-GA
    def output_all_txt(self, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        """
        return self.__BrailleBaseOutputString.output_all_txt(self.confidence_test(text), self.translate_text_to_braille(text), self.translate_text_to_reverse_braille(text), text, footer)
    
    #0005-GB
    def output_binary_txt(self, text: str) -> str:
        """
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
        max_len = self._token_size  

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
        self._token_size = token_size
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

        self.__BrailleIndex = {
        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63
    }

    def __constructor_output(self):
        from braillebaseoutputstring import BrailleBaseOutputString
        self.__BrailleBaseOutputString = BrailleBaseOutputString(self.__BrailleList, self.__BinaryList, self.__BinaryStringList, self.__UnicodeList, self.__DotCountList, self.__DotNumberingList, self.__DotNumberingStringList, self.__ReverseBrailleList, self.__BrailleIndex)

    def __constructor_map_braille(self):
        from braillebaseuniversalset import BrailleBaseBniversalSet
        self.append_multiple_braille_letters(BrailleBaseBniversalSet.braille_base_universal_set())