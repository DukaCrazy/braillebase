class BrailleBaseOutputString():

    def __init__(self, braille_list: list[str], binary_list: list[list[int]], binary_string_list: list[str], unicode_list: list[str], dot_count_list: list[int], dot_numbering_list: list[list[int]], dot_numbering_stringList: list[str], reverse_braille_list: list[str], braille_index: dict[str, int]):
        self.__BrailleList = braille_list
        self.__BinaryList = binary_list
        self.__BinaryStringList = binary_string_list
        self.__UnicodeList = unicode_list
        self.__DotCountList = dot_count_list
        self.__DotNumberingList = dot_numbering_list
        self.__DotNumberingStringList = dot_numbering_stringList
        self.__ReverseBrailleList = reverse_braille_list
        self.__BrailleIndex = braille_index


    #0005-A
    def output_all_json(self, brailles_map: dict) -> str:
        """
        Generates a JSON array containing all braille-related data for each character in the input text.  
        Each entry includes: original letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import json

        result = []

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
    def output_all_csv(self, brailles_map: dict) -> str:
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
    def output_all_xml(self, brailles_map: dict) -> str:
        """
        Generates a formatted XML string containing all braille-related data for each character in the input text.  
        Each <item> node includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        import xml.etree.ElementTree as ET
        import xml.dom.minidom as minidom

        root = ET.Element("braille_output")

        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)

                item = ET.SubElement(root, "item")
                ET.SubElement(item, "index").text = str(key)
                ET.SubElement(item, "Letter").text = braille_list[0]

                ET.SubElement(item, "Braille").text = self.__BrailleList[idx]
                ET.SubElement(item, "Binary").text = self.__BinaryStringList[idx]
                ET.SubElement(item, "Numbering").text = self.__DotNumberingStringList[idx]
                ET.SubElement(item, "Unicode").text = "U+" + self.__UnicodeList[idx]

                ET.SubElement(item, "ReverseBraille").text = self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]
                ET.SubElement(item, "ReverseBinary").text = self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]
                ET.SubElement(item, "ReverseNumbering").text = self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]
                ET.SubElement(item, "ReverseUnicode").text = "U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]


            rough_xml = ET.tostring(root, encoding="utf-8")
            reparsed = minidom.parseString(rough_xml)
        return reparsed.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8")
        
    #0005-D
    def output_all_yaml(self, brailles_map: dict) -> str:
        """
        Generates a YAML-formatted string containing all braille-related data for each character in the input text.  
        Each entry includes: letter, braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)

                lines.append(f"- index: {key}")
                lines.append(f"  Letter: \"{braille_list[0]}\"")

                lines.append(f"  Braille: \"{self.__BrailleList[idx]}\"")
                lines.append(f"  Binary: \"{self.__BinaryStringList[idx]}\"")
                lines.append(f"  Numbering: \"{self.__DotNumberingStringList[idx]}\"")
                lines.append(f"  Unicode: \"{"U+" + self.__UnicodeList[idx]}\"")

                lines.append(f"  ReverseBraille: \"{self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}\"")
                lines.append(f"  ReverseBinary: \"{self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}\"")
                lines.append(f"  ReverseNumbering: \"{self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}\"")
                lines.append(f"  ReverseUnicode: \"{"U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}\"")
                lines.append("")

        return "\n".join(lines)

    #0005-E
    def output_all_markdown(self, brailles_map: dict, braille: list, reverse_braille: list, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        Generates a Markdown-formatted string containing all braille-related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []


        lines.append("## Character -> Braille")
        lines.append(f"### Text: {text}")
        lines.append(f"### Text: {braille}")
        lines.append(f"### Text: {reverse_braille}")

        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:

                idx = self.__BrailleList.index(braille_cell)

                lines.append(f"- **index:** {key}")
                lines.append(f"- **Letter:** {braille_list[0]}")

                lines.append(f"- **Braille:** {self.__BrailleList[idx]}")
                lines.append(f"- **Binary:** {self.__BinaryStringList[idx]}")
                lines.append(f"- **Numbering:** {self.__DotNumberingStringList[idx]}")
                lines.append(f"- **Unicode:** {"U+" + self.__UnicodeList[idx]}")

                lines.append(f"- **ReverseBraille:** {self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"- **ReverseBinary:** {self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"- **ReverseNumbering:** {self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"- **ReverseUnicode:** {"U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append("")


        lines.append(f"- {footer}")

        return "\n".join(lines)
    
    #0005-F
    def output_all_html(self, brailles_map: dict, braille: list, reverse_braille: list, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        Generates an HTML-formatted string containing all braille-related data for each character in the input text.  
        Each section includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

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
        lines.append(f'<p>{braille}</p>')
        lines.append('</div>')

        lines.append('<div class="read-braille-output">')
        lines.append('<h2>Write Braille</h2>')
        lines.append(f'<p>{reverse_braille}</p>')
        lines.append('</div>')

        lines.append('<div class="braille-table-output">')

        for key, braille_list in brailles_map.items():
            lines.append(f'    <h3>Letter {key}</h3>')
            lines.append('<table>')

            #iToken
            for braille_cell in braille_list[1]:
                

                idx = self.__BrailleList.index(braille_cell)

                
                lines.append(f'    <tr>    <td class="cell-letter" rowspan="10">{braille_list[0]}</td>')
            #Braille
                lines.append(f'      <td colspan="2"><b>Read Braille</b></td>')
                lines.append(f'      <tr>    <td>Braille:</td><td>{self.__BrailleList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Binary:</td><td>{self.__BinaryStringList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Numbering:</td><td>{self.__DotNumberingStringList[idx]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Unicode:</td><td>U+{self.__UnicodeList[idx]}</td>  </tr>')
            #Reverse Braille
                lines.append(f'      <tr>    <td colspan="2"><b>Write Braille</b></td>  </tr>')
                lines.append(f'      <tr>    <td>Braille:</td><td>{self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Binary:</td><td>{self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Numbering:</td><td>{self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}</td>  </tr>')
                lines.append(f'      <tr>    <td>Unicode:</td><td>U+{self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}</td>  </tr>')

                

            lines.append('</table>')
            lines.append('<br>')

                
        lines.append('</div>')
        lines.append(f'<footer><p>{footer}</p></footer>')
        lines.append('</body>')
        lines.append('</html>')

        return "\n".join(lines)

     #0005-GA
    def output_all_txt(self, brailles_map: dict, braille: list, reverse_braille: list, text: str, footer = "Thank you for using Braille Base.") -> str:
        """
        Generates a plain text string containing all braille-related data for each character in the input text.  
        Each block includes: braille symbol, index, binary string, binary array, Unicode value, dot count, numbering string, and numbering list.
        """
        lines = []

        lines.append("Character -> Braille")
        lines.append("")
        lines.append(f"Text: {text}")
        lines.append(f"Braille: {braille}")
        lines.append(f"Reverse Braille: {reverse_braille}")
        lines.append("")
        for key, braille_list in brailles_map.items():

            #iToken
            for braille_cell in braille_list[1]:
            
                idx = self.__BrailleList.index(braille_cell)

                lines.append(f"index: {key}")
                lines.append(f"Letter: {braille_list[0]}")

                lines.append(f"Braille: {self.__BrailleList[idx]}")
                lines.append(f"Binary: {self.__BinaryStringList[idx]}")
                lines.append(f"Numbering List: {self.__DotNumberingStringList[idx]}")
                lines.append(f"Unicode: {"U+" + self.__UnicodeList[idx]}")

                lines.append(f"ReverseBraille: {self.__BrailleList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"ReverseBinary: {self.__BinaryStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"ReverseNumbering: {self.__DotNumberingStringList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append(f"ReverseUnicode: {"U+" + self.__UnicodeList[self.__BrailleList.index(self.__ReverseBrailleList[idx])]}")
                lines.append("-" * 40)
                lines.append("")

        lines.append(footer)
        return "\n".join(lines)