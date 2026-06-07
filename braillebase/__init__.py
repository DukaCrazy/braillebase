class BrailleBase:
    # map: __letter_brailles[letter: str]  = braille_list} 
    # map: __letter_specialBraille_rules01[letter: str]  = specialBraille_list} 


#   self.__letter_brailles: dict[str, list[str]]
#   self.__letter_specialBraille_rules01: dict[str, list[str]]
#   self.__letter_specialBraille_rules02: dict[str, list[str]]
#   self.__braille_to_index: dict[str, int]

#   self.__BrailleList: list[str]
#   self.__BinaryList: list[list[int]]
#   self.__BinaryStringList: list[str]
#   self.__UnicodeList: list[str]
#   self.__DotCountList: list[int]
#   self.__DotNumberingList: list[list[int]]
#   self.__DotNumberingStringList: list[str]

#   self.__braille_rules01_a: str
#   self.__braille_rules01_b: str
#   self.__braille_rules02: str

    #0000
    def __init__(self):
        self.__letter_brailles: dict[str, list[str]] = {}
        #rules 01
        self.__letter_specialBraille_rules01: dict[str, list[str]] = {}
        self.setting_braille_rules01("⠠", "⠠")
        #rules 02
        self.__letter_specialBraille_rules02: dict[str, list[str]] = {}
        self.setting_braille_rules02("⠰")

        self.__constructor_map_braille()
        self.__constructor_map_spaces()
        self.__constructor_all_table()

        self.abc()

#---------------------------------------- Registry group (0001) ----------------------------------------
    #0001-AA
    def append_braille_letter(self, letter: str, braille_list: list):
        """
        EN
        Registers a letter and its associated braille list. If the letter already exists, its mapping is overwritten.

        JP
        文字と対応する点字リストを登録します。すでに登録されている場合、そのマッピングは上書きされます。

        IT
        Registra una lettera e la lista di braille associata. Se la lettera esiste già, la mappatura viene sovrascritta.

        PT
        Registra uma letra e sua lista de brailles associada. Se a letra já existir, sua configuração é sobrescrita.
        
        CH
        注册一个字母及其对应的点字列表。如果该字母已存在，则其映射将被覆盖。
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
    def append_special_braille_lettr_rules02(self, letter: str, braille_list: list):
        """
        """
        if not isinstance(letter, str):
            raise TypeError("letter must be a string")

        if len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)

        self.__letter_brailles[letter] = braille_list
        self.__letter_specialBraille_rules02[letter] = braille_list

    #0001-B
    def get_brailles_with_letter(self, letter: str):
        """
        EN
        This method is the core of the application: it receives a letter* and returns the list of braille symbols associated with it. 
        If the letter* is not registered, an error is raised.

        JP
        このメソッドはアプリケーションの中核であり、文字* を受け取り、その文字* に対応する点字の一覧を返します。
        文字* が登録されていない場合はエラーを発生させます。

        IT
        Questo metodo è il nucleo dell’applicazione: riceve una lettera* e restituisce l’elenco dei simboli braille associati ad essa. 
        Se la lettera* non è registrata, viene generato un errore.

        PT
        Este método é o núcleo da aplicação: recebe uma letra* e retorna a lista de brailles associados a ela. 
        Caso a letra* não esteja registrada, um erro é gerado.

        CH
        此方法是整个应用程序的核心：它接收一个字符*，并返回与该字符* 对应的点字列表。如果该字符* 未被注册，则会引发错误。
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")
        return self.__letter_brailles[letter]

    #0001-CA
    def has_letter(self, letter: str) -> bool:
        """
        EN
        Checks whether the given letter is registered in the internal mapping. Returns True or False.

        JP
        指定した文字が内部マッピングに登録されているかを確認します。結果は True または False です。

        IT
        Verifica se la lettera indicata è registrata nella mappatura interna. Restituisce True o False.

        PT
        Verifica se a letra informada está registrada no mapeamento interno. Retorna True ou False.

        CH
        检查指定字母是否已在内部映射中注册。返回 True 或 False。
        """
        return letter in self.__letter_brailles
    
    #0001-CB
    def has_letter_specialBraille_rules01(self, letter: str) -> bool:
        """
        """
        return letter in self.__letter_specialBraille_rules01
    
    #0001-CC
    def has_letter_specialBraille_rules02(self, letter: str) -> bool:
        """
        """
        return letter in self.__letter_specialBraille_rules02

    #0001-D
    def remove_letter(self, letter: str):
        """
        EN
        Removes the given letter from the internal mapping. Returns True if the letter existed and was removed, otherwise returns False.

        JP
        指定した文字を内部マッピングから削除します。削除に成功した場合は True、存在しなかった場合は False を返します。

        IT
        Rimuove la lettera indicata dalla mappatura interna. Restituisce True se la lettera esisteva ed è stata rimossa, altrimenti False.

        PT
        Remove a letra informada do mapeamento interno. Retorna True se a letra existia e foi removida, caso contrário retorna False.

        CH
        从内部映射中删除指定字母。若该字母存在且成功删除，则返回 True，否则返回 False。
        """
        if letter in self.__letter_brailles:
            del self.__letter_brailles[letter]
            return True
        return False


    #0001-EA
    def get_registered_letters(self):
        """
        EN
        Returns a list containing all letters currently registered in the internal mapping.

        JP
        内部マッピングに現在登録されているすべての文字を含むリストを返します。

        IT
        Restituisce una lista contenente tutte le lettere attualmente registrate nella mappatura interna.

        PT
        Retorna uma lista contendo todas as letras atualmente registradas no mapeamento interno.

        CH
        返回当前在内部映射中注册的所有字母列表。
        """
        return list(self.__letter_brailles.keys())
    
    #0001-EB
    def get_registered_letters_specialBraille_Rules01(self):
        """
        """
        return list(self.__letter_specialBraille_rules01.keys())
    
    #0001-EC
    def get_registered_letters_specialBraille_Rules02(self):
        """
        """
        return list(self.__letter_specialBraille_rules02.keys())

    #0001-F
    def append_multiple_braille_letters(self, mapping: dict):
        """
        EN
        Registers multiple letter-to-braille mappings at once. Each entry is validated and added individually.

        JP
        複数の文字と点字の対応関係を一度に登録します。各項目は個別に検証されて追加されます。

        IT
        Registra più associazioni lettera‑braille in un’unica operazione. Ogni voce viene validata e aggiunta singolarmente.

        PT
        Registra várias associações letra‑braille de uma só vez. Cada item é validado e adicionado individualmente.

        CH
        一次性注册多个字母‑点字映射。每个条目都会被单独验证并添加。
        """
        if not isinstance(mapping, dict):
            raise TypeError("mapping must be a dict")

        for letter, braille_list in mapping.items():
            self.append_braille_letter(letter, braille_list)

    #0001-G
    def edit_braille_letter(self, letter: str, new_braille_list: list):
        """
        EN
        Edits the braille list associated with the given letter. Raises an error if the letter is not registered.

        JP
        指定した文字に対応する点字リストを編集します。文字が登録されていない場合はエラーを発生させます。

        IT
        Modifica la lista di braille associata alla lettera indicata. Genera un errore se la lettera non è registrata.

        PT
        Edita a lista de brailles associada à letra informada. Gera um erro se a letra não estiver registrada.

        CH
        编辑指定字母对应的点字列表。若该字母尚未注册，则会引发错误。
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")

        self.__validate_braille_list(new_braille_list)

        self.__letter_brailles[letter] = new_braille_list

#---------------------------------------- Mapping group (0003) ----------------------------------------
    #0003-A
    def get_braille_to_index(self, braille: str) -> int:
        """
        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63

        EN
        Receives a character (string), which must be a valid braille symbol, 
        and returns an integer (int) that represents its position in the Unicode braille table (U+2800 to U+283F).
        
        JP
        1 文字の入力（string）を受け取り、その文字が有効な点字記号であることを前提として、
        Unicode の点字表（U+2800～U+283F）における位置を表す整数（int）を返します。

        IT
        Riceve un carattere (stringa), che deve essere un simbolo braille valido, 
        e restituisce un intero (int) che rappresenta la posizione corrispondente nella tabella Unicode del braille (U+2800–U+283F).
        
        PT
        Recebe um caractere (string), obrigatoriamente correspondente a um símbolo braille, 
        e retorna um inteiro (int) que representa a posição na tabela Unicode do braille (U+2800 a U+283F).

        CH
        接收一个字符（string），该字符必须是有效的点字符号，并返回一个整数（int），表示其在 Unicode 点字表（U+2800 至 U+283F）中的位置。
        """

        return self.__braille_to_index[braille]
    #0003-C
    def get_index_to_braille(self, index: int) -> str:
        return self.__BrailleList[index]
    #0003-B
    def get_braille_list_to_index_list(self, braille_list: list[str]) -> list[int]:
        """
        EN
        Receives multiple characters (strings), each of which must be a valid braille symbol, and returns a list of integers (int), 
        where each value represents the position of the corresponding symbol in the Unicode braille table (U+2800 to U+283F).

        JP
        複数の文字（string）を受け取り、各文字が有効な点字記号であることを前提として、
        Unicode の点字表（U+2800～U+283F）における各記号の位置を表す整数（int）のリストを返します。

        IT
        Riceve più caratteri (stringhe), ognuno dei quali deve essere un simbolo braille valido, e restituisce una lista di interi (int), 
        in cui ogni valore rappresenta la posizione del rispettivo simbolo nella tabella Unicode del braille (U+2800–U+283F).
        
        PT
        Recebe múltiplos caracteres (string), cada um obrigatoriamente correspondente a um símbolo braille,
        e retorna uma lista de inteiros (int), onde cada valor representa a posição do respectivo símbolo
        na tabela Unicode do braille (U+2800 a U+283F).

        CH
        接收多个字符（string），每个字符都必须是有效的点字符号，并返回一个整数（int）列表，其中每个值表示相应符号在 Unicode 点字表（U+2800 至 U+283F）中的位置。
        """
        return [self.get_braille_to_index(b) for b in braille_list]
    
#---------------------------------------- Tables group (0004) ----------------------------------------
    #0004-A
    def braille_list(self) -> list[str]:
        """
            '⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇',
            '⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏',
            '⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗',
            '⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟',
            '⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧',
            '⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯',
            '⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷',
            '⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿'

        EN
        Returns all braille characters organized in the standard Unicode order, covering the range U+2800 to U+283F.
 
        JP
        Unicode の標準順（U+2800〜U+283F）に従って並べられた点字文字をすべて返します。
        
        IT
        Restituisce tutti i caratteri braille organizzati nell’ordine standard Unicode, coprendo l’intervallo da U+2800 a U+283F.
        
        PT
        Retorna todos os caracteres braille organizados na ordem padrão do Unicode, cobrindo o intervalo de U+2800 a U+283F.
        
        CH
        返回按 Unicode 标准顺序排列的所有点字符号，范围覆盖 U+2800 至 U+283F。
        """
        return self.__BrailleList
    #0004-B
    def get_binary_list(self) -> list[list[int]]:

        """
        EN
        Returns a list with 64 items; each item is an array of 6 bits representing a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字を表す 6 ビットの配列です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array di 6 bit che rappresenta un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é um array de 6 bits que representa um caractere braille.

        CH
        返回一个包含 64 个项目的列表；每个项目都是由 6 位组成的数组，用于表示一个点字符号。
        """
        return self.__BinaryList
    #0004-C
    def get_binary_string_list(self) -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is a 6‑bit binary string representing a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字を表す 6 ビットの文字列です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa binaria di 6 bit che rappresenta un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é uma string binária de 6 bits que representa um caractere braille.

        CH
        返回一个包含 64 个项目的列表；每个项目都是一个由 6 位组成的二进制字符串，用于表示一个点字符号。
        """
        return self.__BinaryStringList
    #0004-D
    def get_unicode_list(self) -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is the Unicode code in hexadecimal format corresponding to a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字に対応する Unicode の 16 進コードです。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è il codice Unicode in formato esadecimale corrispondente a un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é o código Unicode em formato hexadecimal correspondente a um caractere braille.

        CH
        返回一个包含 64 个项目的列表；每个项目都是对应点字符号的 Unicode 十六进制代码。
        """
        return self.__UnicodeList
    #0004-E
    def get_dot_count(self) -> list[int]:
        """
        EN
        Returns a list with 64 items; each item is an integer indicating how many points are active (1 to 6) in the corresponding braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の数を示す整数です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un intero che indica quanti punti (da 1 a 6) sono attivi nel carattere braille corrispondente.
        PT
        Retorna uma lista com 64 itens; cada item é um inteiro indicando quantos pontos estão ativos (1 a 6) no caractere braille correspondente.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个整数，用于表示对应点字符号中有多少个激活点（1 至 6）。
        """
        return self.__DotCountList
    #0004-F
    def get_dot_numbering_list(self) -> list[list[int]]:
        """
        EN
        Returns a list with 64 items; each item is an array containing the numbers of the active points (1 to 6) of the corresponding braille character. Commonly used in educational materials.
        
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号を含む配列です。教育用資料でよく使用されます。
        
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente. Molto utilizzato in materiali didattici.
        
        PT
        Retorna uma lista com 64 itens; cada item é um array contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente. Muito usado em materiais didáticos.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个数组，包含对应点字符号中激活点（1 至 6）的编号。常用于教学材料。
        """
        return self.__DotNumberingList
    #0004-G
    def get_dot_numbering_string_list(self) -> list[str]:
        """
        EN
        Returns a list with 64 items; each item is a string containing the numbers of the active points (1 to 6) of the corresponding braille character, separated by hyphens. Commonly used in educational materials.
        
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号をハイフンで区切った文字列です。教育用資料でよく使用されます。
        
        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente, separati da trattini. Molto utilizzato in materiali didattici.
        
        PT
        Retorna uma lista com 64 itens; cada item é uma string contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente, separados por hífens. Muito usado em materiais didáticos.
        
        CH
        返回一个包含 64 个项目的列表；每个项目都是一个字符串，包含对应点字符号中激活点（1 至 6）的编号，并以连字符分隔。常用于教学材料。
        """
        return self.__DotNumberingStringList
#---------------------------------------- Translate group (0002) ----------------------------------------
   #0002-A
    def translate_text_to_braille(self, text: str) -> list:
        """
        EN
        The method expects a string as an argument — the text to be translated into braille.
        Each character is converted into braille.
        This is the main method of the translate group.
        The entire text is processed and converted into a list of braille symbols, which will later be transformed into a list of indices.
        All methods in the translate group are fully dependent on translate_text_to_braille(text: str).


        JP
        このメソッドは、引数として文字列（点字に変換したいテキスト）を受け取ります。
        各文字* は点字に変換されます。
        これは translate グループの主要なメソッドです。
        テキスト全体が処理され、点字記号のリストに変換され、その後インデックスのリストへと変換されます。
        translate グループのすべてのメソッドは translate_text_to_braille(text: str) に完全に依存しています。


        IT
        Il metodo accetta una stringa come argomento — il testo da tradurre in braille.
        Ogni carattere* viene convertito in braille.
        Questo è il metodo principale del gruppo translate.
        L’intero testo viene elaborato e convertito in una lista di simboli braille, che successivamente sarà trasformata in una lista di indici.
        Tutti i metodi del gruppo translate dipendono completamente da translate_text_to_braille(text: str).


        PT
        O método espera uma string como argumento — o texto que se deseja traduzir para braille.
        Cada caractere* é transformado em braille.
        Esse é o principal método do grupo translate.
        Todo o texto é processado e convertido em uma lista de símbolos braille, que posteriormente será transformada em uma lista de índices.
        Todos os métodos do grupo translate são totalmente dependentes de translate_text_to_braille(text: str).

        CH
        该方法接收一个字符串作为参数，即要转换为点字的文本。
        每个字符* 都会被转换为点字。
        这是 translate 组的主要方法。
        整个文本会被处理并转换为点字符号列表，之后将进一步转换为索引列表。
        translate 组的所有方法都完全依赖于 translate_text_to_braille(text: str)。

        """
        text = self.prepare_number_braille(text)
        #apply rules 1
        text = self.prepare_special_braille_rules01(text)
        #apply rules 2
        text = self.prepare_special_braille_rules02(text)
        tokens = self.tokenize_text(text)

        result = []
        for token in tokens:
            brailles = self.get_brailles_with_letter(token)
            result.extend(brailles)

        return result

    
    #0002-B
    def translate_text_to_index(self, textBraille: str) -> list:
        """
        EN
        Translates the input text into a list of braille indices. Each character may expand into multiple braille cells.

        JP
        入力テキストを点字インデックスのリストに変換します。文字によっては複数の点字セルに展開されます。

        IT
        Traduce il testo di input in una lista di indici braille. Alcuni caratteri possono espandersi in più celle braille.

        PT
        Traduz o texto de entrada para uma lista de índices braille. Alguns caracteres podem se expandir em múltiplas células braille.

        CH
        将输入文本转换为点字索引列表。某些字符可能会展开为多个点字单元。
        """
        brailles = self.translate_text_to_braille(textBraille)
        return self.get_braille_list_to_index_list(brailles)
    
    #0002-C
    def translate_text_to_binary_string(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of 6‑bit binary strings representing each braille cell.

        JP
        入力テキストを、各点字セルを表す 6 ビットのバイナリ文字列のリストに変換します。

        IT
        Traduce il testo di input in una lista di stringhe binarie a 6 bit che rappresentano ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista de strings binárias de 6 bits que representam cada célula braille.

        CH
        将输入文本转换为表示每个点字单元的 6 位二进制字符串列表。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        binary_strings = self.get_binary_string_list()
        return [binary_strings[i] for i in indices]
    
    #0002-D
    def translate_text_to_binary_list(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of 6‑bit binary arrays representing each braille cell.

        JP
        入力テキストを、各点字セルを表す 6 ビットのバイナリ配列のリストに変換します。

        IT
        Traduce il testo di input in una lista di array binari a 6 bit che rappresentano ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista de arrays binários de 6 bits que representam cada célula braille.

        CH
        将输入文本转换为表示每个点字单元的 6 位二进制数组列表。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        binary_lists = self.get_binary_list()
        return [binary_lists[i] for i in indices]
    
    #0002-E
    def translate_text_to_unicode(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of Unicode code representations for each braille cell.

        JP
        入力テキストを、各点字セルの Unicode 表現のリストに変換します。

        IT
        Traduce il testo di input in una lista di valori Unicode che rappresentano ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista contendo os valores Unicode que representam cada célula braille.

        CH
        将输入文本转换为表示每个点字单元的 Unicode 代码列表。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        unicode_lists = self.get_unicode_list()
        return [unicode_lists[i] for i in indices]
    
    #0002-F
    def translate_text_to_dot_count(self, text: str) -> list:
        """
        EN
        Translates the input text into a list containing the dot count of each braille cell.

        JP
        入力テキストを、各点字セルの点の数を表すリストに変換します。

        IT
        Traduce il testo di input in una lista contenente il numero di punti attivi di ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista contendo a contagem de pontos de cada célula braille.

        CH
        将输入文本转换为一个列表，其中包含每个点字单元的点数。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        dot_count_lists = self.get_dot_count()
        return [dot_count_lists[i] for i in indices]
    
    #0002-G
    def translate_text_to_numbering_string(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of numbering strings, each indicating the active dot positions of every braille cell.

        JP
        入力テキストを、各点字セルのアクティブな点位置を示す番号文字列のリストに変換します。

        IT
        Traduce il testo di input in una lista di stringhe numeriche che indicano le posizioni dei punti attivi di ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista de strings numéricas que indicam as posições dos pontos ativos de cada célula braille.
        
        CH
        将输入文本转换为编号字符串列表，每个字符串表示对应点字单元的激活点位置。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        numbering_strings = self.get_dot_numbering_string_list()
        return [numbering_strings[i] for i in indices]
    
    #0002-H
    def translate_text_to_numbering_list(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of numbering lists, each containing the active dot positions of every braille cell.

        JP
        入力テキストを、各点字セルのアクティブな点位置を含む番号リストの一覧に変換します。

        IT
        Traduce il testo di input in una lista di elenchi numerici che indicano le posizioni dei punti attivi di ogni cella braille.

        PT
        Traduz o texto de entrada para uma lista de listas numéricas que indicam as posições dos pontos ativos de cada célula braille.
        
        CH
        将输入文本转换为编号列表的列表，每个编号列表包含对应点字单元的激活点位置。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)
        numbering_lists = self.get_dot_numbering_list()
        return [numbering_lists[i] for i in indices]
    
    #0002-I
    def translate_text_to_full_list(self, text: str) -> list:
        """
        EN
        Translates the input text into a full list of braille‑related data.  
        Each entry contains: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキストを点字関連データの完全なリストに変換します。  
        各要素には、点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Traduce il testo di input in un elenco completo di dati relativi al braille.  
        Ogni elemento contiene: simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Traduz o texto de entrada para uma lista completa de dados relacionados ao braille.  
        Cada item contém: símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        CH
        将输入文本转换为完整的点字相关数据列表。每个条目包含：点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        brailles = self.translate_text_to_braille(text)
        indices = self.get_braille_list_to_index_list(brailles)

        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_count_lists = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        result = []

        for idx in range(len(indices)):
            i = indices[idx]
            result.append([
                brailles[idx],
                i,
                binary_strings[i],
                binary_lists[i],
                unicode_lists[i],
                dot_count_lists[i],
                numbering_strings[i],
                numbering_lists[i]
            ])
        return result
#---------------------------------------- Output group (0005) ----------------------------------------

    #0005-A
    def output_all_json(self, text: str) -> str:
        """
        EN
        Generates a JSON array containing all braille‑related data for each character in the input text.  
        Each entry includes: original letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む JSON 配列を生成します。  
        各要素には、元の文字・点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera un array JSON contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni elemento include: lettera originale, simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera um array JSON contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada item inclui: letra original, símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        CH
        生成一个 JSON 数组，其中包含输入文本中每个字符的所有点字相关数据。每个条目包括：原始字符、点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        import json

        result = []

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            result.append({
                "braille": braille_list[idx],
                "index": idx,
                "binary_string": binary_strings[idx],
                "binary_list": binary_lists[idx],
                "unicode": unicode_lists[idx],
                "dot_count": dot_counts[idx],
                "numbering_string": numbering_strings[idx],
                "numbering_list": numbering_lists[idx]
            })

        return json.dumps(result, ensure_ascii=False, indent=4)

    #0005-B
    def output_all_csv(self, text: str) -> str:
        """
        EN
        Generates a CSV string containing all braille‑related data for each character in the input text.  
        Each row includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む CSV 文字列を生成します。  
        各行には、元の文字・点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa CSV contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni riga include: lettera originale, simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string CSV contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada linha inclui: letra original, símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        
        CH
        生成一个 CSV 字符串，其中包含输入文本中每个字符的所有点字相关数据。每一行包括：原始字符、点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
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

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            writer.writerow([
                "",
                braille_list[idx],
                idx,
                binary_strings[idx],
                str(binary_lists[idx]),
                unicode_lists[idx],
                dot_counts[idx],
                numbering_strings[idx],
                str(numbering_lists[idx])
            ])

        return output.getvalue()


    #0005-C
    def output_all_xml(self, text: str) -> str:
        """
        EN
        Generates a formatted XML string containing all braille‑related data for each character in the input text.  
        Each <item> node includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む整形済み XML 文字列を生成します。  
        各 <item> ノードには、元の文字・点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa XML formattata contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni nodo <item> include: lettera originale, simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string XML formatada contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada nó <item> inclui: letra original, símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        
        CH
        生成一个格式化的 XML 字符串，其中包含输入文本中每个字符的所有点字相关数据。
        每个 <item> 节点包括：原始字符、点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        import xml.etree.ElementTree as ET
        import xml.dom.minidom as minidom

        root = ET.Element("braille_output")

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            item = ET.SubElement(root, "item")
            ET.SubElement(item, "braille").text = braille_list[idx]
            ET.SubElement(item, "index").text = str(idx)
            ET.SubElement(item, "binary_string").text = binary_strings[idx]
            ET.SubElement(item, "binary_list").text = str(binary_lists[idx])
            ET.SubElement(item, "unicode").text = unicode_lists[idx]
            ET.SubElement(item, "dot_count").text = str(dot_counts[idx])
            ET.SubElement(item, "numbering_string").text = numbering_strings[idx]
            ET.SubElement(item, "numbering_list").text = str(numbering_lists[idx])

        rough_xml = ET.tostring(root, encoding="utf-8")
        reparsed = minidom.parseString(rough_xml)
        return reparsed.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8")

    #0005-D
    def output_all_yaml(self, text: str) -> str:
        """
        EN
        Generates a YAML‑formatted string containing all braille‑related data for each character in the input text.  
        Each entry includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む YAML 形式の文字列を生成します。  
        各項目には、元の文字・点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa in formato YAML contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni voce include: lettera originale, simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string YAML formatada contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada item inclui: letra original, símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        
        CH
        生成一个 YAML 格式的字符串，其中包含输入文本中每个字符的所有点字相关数据。
        每个条目包括：原始字符、点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        lines = []

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            lines.append(f"- braille: \"{braille_list[idx]}\"")
            lines.append(f"  index: {idx}")
            lines.append(f"  binary_string: \"{binary_strings[idx]}\"")
            lines.append(f"  binary_list: {binary_lists[idx]}")
            lines.append(f"  unicode: \"{unicode_lists[idx]}\"")
            lines.append(f"  dot_count: {dot_counts[idx]}")
            lines.append(f"  numbering_string: \"{numbering_strings[idx]}\"")
            lines.append(f"  numbering_list: {numbering_lists[idx]}")
            lines.append("")

        return "\n".join(lines)

    
    #0005-E
    def output_all_markdown(self, text: str) -> str:
        """
        EN
        Generates a Markdown‑formatted string containing all braille‑related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む Markdown 形式の文字列を生成します。  
        各セクションには、点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa in formato Markdown contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni sezione include: simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string Markdown formatada contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada seção inclui: símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        
        CH
        生成一个 Markdown 格式的字符串，其中包含输入文本中每个字符的所有点字相关数据。
        每个部分包括：点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        lines = []

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            lines.append(f"## Braille {count}")
            lines.append(f"- **Braille:** {braille_list[idx]}")
            lines.append(f"- **Index:** {idx}")
            lines.append(f"- **Binary:** `{binary_strings[idx]}`")
            lines.append(f"- **Binary List:** {binary_lists[idx]}")
            lines.append(f"- **Unicode:** {unicode_lists[idx]}")
            lines.append(f"- **Dot Count:** {dot_counts[idx]}")
            lines.append(f"- **Numbering:** {numbering_strings[idx]}")
            lines.append(f"- **Numbering List:** {numbering_lists[idx]}")
            lines.append("")

            count += 1

        return "\n".join(lines)

    
    #0005-F
    def output_all_html(self, text: str) -> str:
        """
        EN
        Generates an HTML‑formatted string containing all braille‑related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含む HTML 形式の文字列を生成します。  
        各セクションには、点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa in formato HTML contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni sezione include: simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string HTML formatada contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada seção inclui: símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        CH
        生成一个 HTML 格式的字符串，其中包含输入文本中每个字符的所有点字相关数据。
        每个部分包括：点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        lines = []

        lines.append('<div class="braille-output">')

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            lines.append(f'  <section class="braille-item">')
            lines.append(f'    <h2>Braille {count}</h2>')
            lines.append('    <ul>')
            lines.append(f'      <li><strong>Braille:</strong> {braille_list[idx]}</li>')
            lines.append(f'      <li><strong>Index:</strong> {idx}</li>')
            lines.append(f'      <li><strong>Binary:</strong> <code>{binary_strings[idx]}</code></li>')
            lines.append(f'      <li><strong>Binary List:</strong> {binary_lists[idx]}</li>')
            lines.append(f'      <li><strong>Unicode:</strong> {unicode_lists[idx]}</li>')
            lines.append(f'      <li><strong>Dot Count:</strong> {dot_counts[idx]}</li>')
            lines.append(f'      <li><strong>Numbering:</strong> {numbering_strings[idx]}</li>')
            lines.append(f'      <li><strong>Numbering List:</strong> {numbering_lists[idx]}</li>')
            lines.append('    </ul>')
            lines.append('  </section>')

            count += 1

        lines.append('</div>')

        return "\n".join(lines)

    
    #0005-GA
    def output_all_txt(self, text: str) -> str:
        """
        EN
        Generates a plain text string containing all braille‑related data for each character in the input text.  
        Each block includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.

        JP
        入力テキスト内の各文字について、点字関連データをすべて含むプレーンテキスト文字列を生成します。  
        各ブロックには、点字記号・インデックス・バイナリ文字列・バイナリ配列・Unicode 値・点の数・番号文字列・番号リストが含まれます。

        IT
        Genera una stringa di testo semplice contenente tutti i dati relativi al braille per ogni carattere del testo di input.  
        Ogni blocco include: simbolo braille, indice, stringa binaria, array binario, valore Unicode, numero di punti, stringa numerica e lista numerica.

        PT
        Gera uma string TXT contendo todos os dados relacionados ao braille para cada caractere do texto de entrada.  
        Cada bloco inclui: símbolo braille, índice, string binária, array binário, valor Unicode, contagem de pontos, string de numeração e lista de numeração.
        
        CH
        生成一个纯文本字符串，其中包含输入文本中每个字符的所有点字相关数据。
        每个区块包括：点字符号、索引、二进制字符串、二进制数组、Unicode 值、点数、编号字符串以及编号列表。
        """
        lines = []

        braille_list = self.braille_list()
        binary_strings = self.get_binary_string_list()
        binary_lists = self.get_binary_list()
        unicode_lists = self.get_unicode_list()
        dot_counts = self.get_dot_count()
        numbering_strings = self.get_dot_numbering_string_list()
        numbering_lists = self.get_dot_numbering_list()

        brailles = self.translate_text_to_braille(text)

        count = 1
        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)

            lines.append(f"Braille {count}")
            lines.append(f"Braille: {braille_list[idx]}")
            lines.append(f"Index: {idx}")
            lines.append(f"Binary: {binary_strings[idx]}")
            lines.append(f"Binary List: {binary_lists[idx]}")
            lines.append(f"Unicode: {unicode_lists[idx]}")
            lines.append(f"Dot Count: {dot_counts[idx]}")
            lines.append(f"Numbering: {numbering_strings[idx]}")
            lines.append(f"Numbering List: {numbering_lists[idx]}")
            lines.append("-" * 40)
            lines.append("")

            count += 1

        return "\n".join(lines)

    
    #0005-GB
    def output_binary_txt(self, text: str) -> str:
        """
        EN
        Generates a plain text string containing only the binary strings of each braille cell derived from the input text.

        JP
        入力テキストから得られる各点字セルのバイナリ文字列のみを含むプレーンテキスト文字列を生成します。

        IT
        Genera una stringa di testo contenente solo le stringhe binarie di ogni cella braille derivata dal testo di input.

        PT
        Gera uma string TXT contendo apenas as binary strings de cada célula braille derivada do texto de entrada.

        CH
        生成一个纯文本字符串，其中仅包含从输入文本转换而来的各个点字单元的二进制字符串。
        """
        lines = []

        binary_strings = self.get_binary_string_list()
        braille_list = self.braille_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)
            lines.append(binary_strings[idx])

        return "\n".join(lines)

    #0005-GC
    def output_braille_txt(self, text: str) -> str:
        """

        """
        lines = []

        braille_strings = self.braille_list()
        braille_list = self.braille_list()

        brailles = self.translate_text_to_braille(text)

        for braille_cell in brailles:
            idx = braille_list.index(braille_cell)
            lines.append(braille_strings[idx])

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
        EN
        Internal method that validates a list of braille symbols.  
        Ensures the value is a list, that each item is a string, and that every string is a valid Unicode braille character (U+2800–U+283F).

        JP
        点字記号のリストを検証する内部メソッドです。  
        値がリストであること、各要素が文字列であること、そしてすべての文字列が Unicode の有効な点字文字（U+2800～U+283F）であることを確認します。

        IT
        Metodo interno che convalida una lista di simboli braille.  
        Verifica che il valore sia una lista, che ogni elemento sia una stringa e che ogni stringa rappresenti un carattere braille Unicode valido (U+2800–U+283F).

        PT
        Método interno que valida uma lista de símbolos braille.  
        Garante que o valor seja uma lista, que cada item seja uma string e que cada string seja um caractere braille Unicode válido (U+2800–U+283F).
        
        CH
        用于验证点字符号列表的内部方法。确保该值为列表、每个项目为字符串，并且每个字符串都是有效的 Unicode 点字字符（U+2800–U+283F）。
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
                result.append(self.__braille_rules01_a)
                result.append(self.__braille_rules01_a)

            elif  not has_previous_letter and has_current_letter and not has_next_letter:
                result.append(self.__braille_rules01_a)


            if has_previous_letter and has_current_letter and not has_next_letter:
                result.append(current_letter)
                result.append(self.__braille_rules01_b)
            else:
                result.append(current_letter)

        return "".join(result)
    
    def setting_braille_rules01(self, braille_uppercase: str, braille_lowercase: str):
        self.__braille_rules01_a = braille_uppercase
        self.__braille_rules01_b = braille_lowercase

    #----------------------------Prepare Special 02---------------------------
    
    def prepare_special_braille_rules02(self, text: str) -> str:
        result = []
        previous = False

        for ch in text:
            is_special = ch in self.__letter_specialBraille_rules02

            if is_special and not previous:
                result.append(self.__braille_rules02)

            result.append(ch)
            previous = is_special

        return "".join(result)
    
    def setting_braille_rules02(self, braille: str):
        self.__braille_rules02 = braille

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
        text = self.prepare_special_braille_rules02(text)

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
