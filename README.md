# BrailleBase
## Custom Language and Mapping Implementation
This code snippet demonstrates how to extend the core BrailleBase class to create a custom translator using Object-Oriented Programming (OOP) inheritance. By inheriting from BrailleBase and leveraging the append_braille_letter() method, you can map any custom character or language symbol to its corresponding Braille unicode character.

Step-by-step breakdown:

Class Inheritance: Defines BrailleBaseAnyLanguage, which inherits all core functionality from BrailleBase.

Character Mapping: Inside the constructor (__init__), it registers custom symbols (hieroglyphs in this example) alongside their corresponding Braille dots.

Execution: Instantiates the custom class (bbal) and translates the input string into Braille text output via output_braille_txt().

Key Technical Takeaways
Design Pattern: Class Inheritance and Extensibility.

Core Advantage: Demonstrates that the library is not restricted to pre-packaged languages, allowing developers to define custom Braille lookup tables for any writing system.

```python
from braillebase import BrailleBase

class BrailleBaseAnyLanguage(BrailleBase):
    def __init__(self):
        super().__init__()
        self.append_braille_letter("𓃒", ["⠁"]) 
        self.append_braille_letter("𓃖", ["⠃"]) 
        self.append_braille_letter("𓃯", ["⠉"]) 
        self.append_braille_letter("𓅅", ["⠙"]) 
        self.append_braille_letter("𓅼", ["⠑"]) 

bbal = BrailleBaseAnyLanguage()
print("𓃒 𓃖 𓃯 𓅅 𓅼")
print(bbal.output_braille_txt("𓃒 𓃖 𓃯 𓅅 𓅼"))
```

### Output
𓃒 𓃖 𓃯 𓅅 𓅼

⠁⠀⠃⠀⠉⠀⠙⠀⠑


## Generating Full HTML Reports and Alternative Data Formats
This code snippet illustrates how to process Japanese text using a pre-configured language module (BrailleBaseJapanese) and export a comprehensive HTML report containing detailed Braille character metadata.

Step-by-step breakdown:

```python
from braille import *

bbj = BrailleBaseJapanese()
print(bbj.output_all_html("おはよう"))
```

Language Module Import: Imports the library components and instantiates the BrailleBaseJapanese parser.

HTML Document Generation: The output_all_html() method converts the input string (e.g., "おはよう") into a complete, structured HTML document.

Structured Metadata Display: The generated HTML provides detailed character breakdown tables, including:

Reading vs. Writing Braille: Visual representations for reading and writing modes.

Encoding & Metrics: Binary representations, standard cell numbering (dot positions 1 through 6), and Unicode values (e.g., U+280a) for each character.

Multi-Format Export Support: In addition to HTML output, the library provides built-in serializers for JSON, YAML, XML, and other data formats for integration with web APIs and external applications.

Key Technical Takeaways
Primary Function: Comprehensive document and dataset generation for language-specific Braille conversion.

Core Advantage: Provides full character inspection (binary, cell dot numbering, Unicode hex) alongside visual Braille characters, making it ideal for rendering in web browsers or exporting to data pipelines.


```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Braille Base - HTML Generate</title>
  <style>
    table {      border-collapse: collapse;      width: 400px;      font-family: sans-serif;    }
    td {      border: 1px solid #000;      padding: 6px 10px;    }
    .cell-letter {      font-size: 48px;      text-align: center;      vertical-align: middle;      width: 100px;    }
  </style>
</head>
<body>
<div class="text-output">
<h2>Text</h2>
<p>おはよう</p>
</div>
<div class="read-braille-output">
<h2>Read Braille</h2>
<p>['⠊', '⠥', '⠜', '⠉']</p>
</div>
<div class="read-braille-output">
<h2>Write Braille</h2>
<p>['⠉', '⠣', '⠬', '⠑']</p>
</div>
<div class="braille-table-output">
    <h3>Letter 1</h3>
<table>
    <tr>    <td class="cell-letter" rowspan="10">お</td>
      <td colspan="2"><b>Read Braille</b></td>
      <tr>    <td>Braille:</td><td>⠊</td>  </tr>
      <tr>    <td>Binary:</td><td>001010</td>  </tr>
      <tr>    <td>Numbering:</td><td>2-4</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+280a</td>  </tr>
      <tr>    <td colspan="2"><b>Write Braille</b></td>  </tr>
      <tr>    <td>Braille:</td><td>⠑</td>  </tr>
      <tr>    <td>Binary:</td><td>010001</td>  </tr>
      <tr>    <td>Numbering:</td><td>1-5</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+2811</td>  </tr>
</table>
<br>
    <h3>Letter 2</h3>
<table>
    <tr>    <td class="cell-letter" rowspan="10">は</td>
      <td colspan="2"><b>Read Braille</b></td>
      <tr>    <td>Braille:</td><td>⠥</td>  </tr>
      <tr>    <td>Binary:</td><td>100101</td>  </tr>
      <tr>    <td>Numbering:</td><td>1-3-6</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+2825</td>  </tr>
      <tr>    <td colspan="2"><b>Write Braille</b></td>  </tr>
      <tr>    <td>Braille:</td><td>⠬</td>  </tr>
      <tr>    <td>Binary:</td><td>101100</td>  </tr>
      <tr>    <td>Numbering:</td><td>3-4-6</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+282c</td>  </tr>
</table>
<br>
    <h3>Letter 3</h3>
<table>
    <tr>    <td class="cell-letter" rowspan="10">よ</td>
      <td colspan="2"><b>Read Braille</b></td>
      <tr>    <td>Braille:</td><td>⠜</td>  </tr>
      <tr>    <td>Binary:</td><td>011100</td>  </tr>
      <tr>    <td>Numbering:</td><td>3-4-5</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+281c</td>  </tr>
      <tr>    <td colspan="2"><b>Write Braille</b></td>  </tr>
      <tr>    <td>Braille:</td><td>⠣</td>  </tr>
      <tr>    <td>Binary:</td><td>100011</td>  </tr>
      <tr>    <td>Numbering:</td><td>1-2-6</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+2823</td>  </tr>
</table>
<br>
    <h3>Letter 4</h3>
<table>
    <tr>    <td class="cell-letter" rowspan="10">う</td>
      <td colspan="2"><b>Read Braille</b></td>
      <tr>    <td>Braille:</td><td>⠉</td>  </tr>
      <tr>    <td>Binary:</td><td>001001</td>  </tr>
      <tr>    <td>Numbering:</td><td>1-4</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+2809</td>  </tr>
      <tr>    <td colspan="2"><b>Write Braille</b></td>  </tr>
      <tr>    <td>Braille:</td><td>⠉</td>  </tr>
      <tr>    <td>Binary:</td><td>001001</td>  </tr>
      <tr>    <td>Numbering:</td><td>1-4</td>  </tr>
      <tr>    <td>Unicode:</td><td>U+2809</td>  </tr>
</table>
<br>
</div>
<footer><p>Thank you for using Braille Base.</p></footer>
</body>
</html>
```

## Thanks
The tool is still in development, but it's fully usable and we’d love your opinion. Thanks for reading this far. Cheers.
