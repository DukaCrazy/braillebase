class BrailleBase:
    #0000
    def __init__(self):
        self.__letter_brailles = {}

    #0001-A
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
        """
        if not isinstance(letter, str):
            raise TypeError("letter must be a string")

        if len(letter) == 0:
            raise ValueError("letter cannot be empty")
        
        self.__validate_braille_list(braille_list)

        self.__letter_brailles[letter] = braille_list

    #0001-B
    def get_brailles_with_letter(self, letter: str):
        """
        EN
        Returns the braille list associated with the given letter. Raises an error if the letter is not registered.

        JP
        指定した文字に対応する点字リストを返します。登録されていない場合はエラーを発生させます。

        IT
        Restituisce la lista di braille associata alla lettera indicata. Genera un errore se la lettera non è registrata.

        PT
        Retorna a lista de brailles associada à letra informada. Gera um erro se a letra não estiver registrada.
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")
        return self.__letter_brailles[letter]

    #0001-C
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
        """
        return letter in self.__letter_brailles

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
        """
        if letter in self.__letter_brailles:
            del self.__letter_brailles[letter]
            return True
        return False


    #0001-E
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
        """
        return list(self.__letter_brailles.keys())

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
        """
        if letter not in self.__letter_brailles:
            raise KeyError(f"letter '{letter}' not registered")

        self.__validate_braille_list(new_braille_list)

        self.__letter_brailles[letter] = new_braille_list
#------------------------------------------------------------------------------------------------------------------------------------
    #0002-A
    def translate_text_to_braille(self, text: str) -> list:
        """
        EN
        Translates the input text into a flat list of braille symbols. Each character may expand into multiple braille cells.

        JP
        入力テキストを点字記号のフラットなリストに変換します。文字によっては複数の点字セルに展開されます。

        IT
        Traduce il testo di input in una lista piatta di simboli braille. Alcuni caratteri possono espandersi in più celle braille.

        PT
        Traduz o texto de entrada para uma lista linear de símbolos braille. Alguns caracteres podem se expandir em múltiplas células braille.
        """
        result = []
        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            result.extend(brailles)
        return result
    
    #0002-B
    def translate_text_to_index(self, text: str) -> list:
        """
        EN
        Translates the input text into a list of braille indices. Each character may expand into multiple braille cells.

        JP
        入力テキストを点字インデックスのリストに変換します。文字によっては複数の点字セルに展開されます。

        IT
        Traduce il testo di input in una lista di indici braille. Alcuni caratteri possono espandersi in più celle braille.

        PT
        Traduz o texto de entrada para uma lista de índices braille. Alguns caracteres podem se expandir em múltiplas células braille.
        """
        brailles = self.translate_text_to_braille(text)
        return BrailleBase.get_braille_list_to_index_list(brailles)
    
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        binary_strings = BrailleBase.get_binary_string_list()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        binary_lists = BrailleBase.get_binary_list()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        unicode_lists = BrailleBase.get_unicode_list()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        dot_count_lists = BrailleBase.get_dot_count()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)
        numbering_lists = BrailleBase.get_dot_numbering_list()
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
        """
        brailles = self.translate_text_to_braille(text)
        indices = BrailleBase.get_braille_list_to_index_list(brailles)

        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_count_lists = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

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
#------------------------------------------------------------------------------------------------------------------------------------
    #0003-A
    @staticmethod
    def get_braille_to_index(braille: str) -> int:
        """
        EN
        Returns the index associated with the given braille symbol. The mapping follows the standard Unicode braille order (U+2800 to U+283F).

        JP
        指定した点字記号に対応するインデックスを返します。マッピングは Unicode の点字標準順（U+2800 ～ U+283F）に従います。

        IT
        Restituisce l’indice associato al simbolo braille indicato. La mappatura segue l’ordine standard Unicode del braille (U+2800–U+283F).

        PT
        Retorna o índice associado ao símbolo braille informado. O mapeamento segue a ordem padrão Unicode do braille (U+2800 a U+283F).
        """
        braille_to_index = {
        '⠀': 0, '⠁': 1, '⠂': 2, '⠃': 3, '⠄': 4, '⠅': 5, '⠆': 6, '⠇': 7,
        '⠈': 8, '⠉': 9, '⠊': 10, '⠋': 11, '⠌': 12, '⠍': 13, '⠎': 14, '⠏': 15,
        '⠐': 16, '⠑': 17, '⠒': 18, '⠓': 19, '⠔': 20, '⠕': 21, '⠖': 22, '⠗': 23,
        '⠘': 24, '⠙': 25, '⠚': 26, '⠛': 27, '⠜': 28, '⠝': 29, '⠞': 30, '⠟': 31,
        '⠠': 32, '⠡': 33, '⠢': 34, '⠣': 35, '⠤': 36, '⠥': 37, '⠦': 38, '⠧': 39,
        '⠨': 40, '⠩': 41, '⠪': 42, '⠫': 43, '⠬': 44, '⠭': 45, '⠮': 46, '⠯': 47,
        '⠰': 48, '⠱': 49, '⠲': 50, '⠳': 51, '⠴': 52, '⠵': 53, '⠶': 54, '⠷': 55,
        '⠸': 56, '⠹': 57, '⠺': 58, '⠻': 59, '⠼': 60, '⠽': 61, '⠾': 62, '⠿': 63
    }
        return braille_to_index[braille]
    
    #0003-B
    @staticmethod
    def get_braille_list_to_index_list(braille_list: list) -> list:
        """
        EN
        Converts a list of braille symbols into a list of their corresponding indices.

        JP
        点字記号のリストを、それぞれに対応するインデックスのリストへ変換します。

        IT
        Converte una lista di simboli braille in una lista dei rispettivi indici.

        PT
        Converte uma lista de símbolos braille em uma lista com seus respectivos índices.
        """
        return [BrailleBase.get_braille_to_index(b) for b in braille_list]
    
    #------------------------------------------------------------------------------------------------------------------------------------
    #0004-A
    @staticmethod
    def braille_list():
        """
            EN
            Returns all braille characters organized in the standard Unicode order, covering the range U+2800 to U+283F.
            JP
            Unicode の標準順（U+2800〜U+283F）に従って並べられた点字文字をすべて返します。
            IT
            Restituisce tutti i caratteri braille organizzati nell’ordine standard Unicode, coprendo l’intervallo da U+2800 a U+283F.
            PT
            Retorna todos os caracteres braille organizados na ordem padrão do Unicode, cobrindo o intervalo de U+2800 a U+283F.
        """
        return [
            '⠀','⠁','⠂','⠃','⠄','⠅','⠆','⠇',
            '⠈','⠉','⠊','⠋','⠌','⠍','⠎','⠏',
            '⠐','⠑','⠒','⠓','⠔','⠕','⠖','⠗',
            '⠘','⠙','⠚','⠛','⠜','⠝','⠞','⠟',
            '⠠','⠡','⠢','⠣','⠤','⠥','⠦','⠧',
            '⠨','⠩','⠪','⠫','⠬','⠭','⠮','⠯',
            '⠰','⠱','⠲','⠳','⠴','⠵','⠶','⠷',
            '⠸','⠹','⠺','⠻','⠼','⠽','⠾','⠿'
        ]
    #0004-B
    @staticmethod
    def get_binary_list():

        """
        EN
        Returns a list with 64 items; each item is an array of 6 bits representing a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字を表す 6 ビットの配列です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array di 6 bit che rappresenta un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é um array de 6 bits que representa um caractere braille.
        """
        return [
            [int(b) for b in f"{i:06b}"] for i in range(64)
        ]
    #0004-C
    @staticmethod
    def get_binary_string_list():
        """
        EN
        Returns a list with 64 items; each item is a 6‑bit binary string representing a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字を表す 6 ビットの文字列です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa binaria di 6 bit che rappresenta un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é uma string binária de 6 bits que representa um caractere braille.
        """
        return [f"{i:06b}" for i in range(64)]
    #0004-D
    @staticmethod
    def get_unicode_list():
        """
        EN
        Returns a list with 64 items; each item is the Unicode code in hexadecimal format corresponding to a braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、点字文字に対応する Unicode の 16 進コードです。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è il codice Unicode in formato esadecimale corrispondente a un carattere braille.
        PT
        Retorna uma lista com 64 itens; cada item é o código Unicode em formato hexadecimal correspondente a um caractere braille.
        """
        return [f"{0x2800 + i:04x}" for i in range(64)]
    #0004-E
    @staticmethod
    def get_dot_count():
        """
        EN
        Returns a list with 64 items; each item is an integer indicating how many points are active (1 to 6) in the corresponding braille character.
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の数を示す整数です。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un intero che indica quanti punti (da 1 a 6) sono attivi nel carattere braille corrispondente.
        PT
        Retorna uma lista com 64 itens; cada item é um inteiro indicando quantos pontos estão ativos (1 a 6) no caractere braille correspondente.
        """
        return [bin(i).count("1") for i in range(64)]
    #0004-F
    @staticmethod
    def get_dot_numbering_list():
        """
        EN
        Returns a list with 64 items; each item is an array containing the numbers of the active points (1 to 6) of the corresponding braille character. Commonly used in educational materials.
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号を含む配列です。教育用資料でよく使用されます。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è un array che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente. Molto utilizzato in materiali didattici.
        PT
        Retorna uma lista com 64 itens; cada item é um array contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente. Muito usado em materiais didáticos.
        """
        lst = []
        for i in range(64):
            dots = []
            for d in range(6):
                if (i >> d) & 1:
                    dots.append(d+1)
            lst.append(dots)
        return lst
    #0004-G
    @staticmethod
    def get_dot_numbering_string_list():
        """
        EN
        Returns a list with 64 items; each item is a string containing the numbers of the active points (1 to 6) of the corresponding braille character, separated by hyphens. Commonly used in educational materials.
        JP
        64 個の項目を持つリストを返します。各項目は、対応する点字文字でアクティブな点（1〜6）の番号をハイフンで区切った文字列です。教育用資料でよく使用されます。
        IT
        Restituisce una lista con 64 elementi; ogni elemento è una stringa che contiene i numeri dei punti attivi (da 1 a 6) del carattere braille corrispondente, separati da trattini. Molto utilizzato in materiali didattici.
        PT
        Retorna uma lista com 64 itens; cada item é uma string contendo os números dos pontos ativos (1 a 6) do caractere braille correspondente, separados por hífens. Muito usado em materiais didáticos.
        """
        return [
            "-".join(str(d) for d in dots)
            for dots in BrailleBase.get_dot_numbering_list()
        ]

#----------------------------------------------------------------------------------------------------------------------------------------
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
        """
        import json

        result = []

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            for idx in indices:
                result.append({
                    "letter": ch,
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

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            for idx in indices:
                writer.writerow([
                    ch,
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
        """
        import xml.etree.ElementTree as ET
        import xml.dom.minidom as minidom

        root = ET.Element("braille_output")

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            for idx in indices:
                item = ET.SubElement(root, "item")

                ET.SubElement(item, "letter").text = ch
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
        """
        lines = []

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            for idx in indices:
                lines.append(f"- letter: \"{ch}\"")
                lines.append(f"  braille: \"{braille_list[idx]}\"")
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
        """
        lines = []

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            count = 1
            for idx in indices:
                lines.append(f"## {ch} — Braille {count}")
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
        """
        lines = []

        lines.append('<div class="braille-output">')

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            count = 1
            for idx in indices:
                lines.append(f'  <section class="braille-item">')
                lines.append(f'    <h2>{ch} — Braille {count}</h2>')
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
        """
        lines = []

        braille_list = BrailleBase.braille_list()
        binary_strings = BrailleBase.get_binary_string_list()
        binary_lists = BrailleBase.get_binary_list()
        unicode_lists = BrailleBase.get_unicode_list()
        dot_counts = BrailleBase.get_dot_count()
        numbering_strings = BrailleBase.get_dot_numbering_string_list()
        numbering_lists = BrailleBase.get_dot_numbering_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            count = 1
            for idx in indices:
                lines.append(f"{ch} — Braille {count}")
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
    def output_binary_string_txt(self, text: str) -> str:
        """
        EN
        Generates a plain text string containing only the binary strings of each braille cell derived from the input text.

        JP
        入力テキストから得られる各点字セルのバイナリ文字列のみを含むプレーンテキスト文字列を生成します。

        IT
        Genera una stringa di testo contenente solo le stringhe binarie di ogni cella braille derivata dal testo di input.

        PT
        Gera uma string TXT contendo apenas as binary strings de cada célula braille derivada do texto de entrada.
        """
        lines = []

        binary_strings = BrailleBase.get_binary_string_list()

        for ch in text:
            brailles = self.get_brailles_with_letter(ch)
            indices = BrailleBase.get_braille_list_to_index_list(brailles)

            for idx in indices:
                lines.append(binary_strings[idx])

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
        """
        if not isinstance(braille_list, list):
            raise TypeError("braille_list must be a list")

        for b in braille_list:
            if not isinstance(b, str):
                raise TypeError("each braille item must be a string")
            if not ("\u2800" <= b <= "\u283F"):
                raise ValueError(f"invalid braille character: {b}")
#linguajaponesa = BrailleBase()
#TESTE 1 OK
#linguajaponesa.braille_letter_append("ぎ", ["⠂","⠣"])
#print(linguajaponesa.get_brailles_with_letter("ぎ"))


#TESTE 2
#a = BrailleBase.get_dot_count()
#print(a[BrailleBase.get_braille_to_index(linguajaponesa.get_brailles_with_letter("ぎ")[0])])