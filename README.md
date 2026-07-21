# BrailleBase
## How to use Braille Base?

### First, install the Braille library.
- pip install braille

## Then just use it.
```python
from braille import *

bbj = BrailleBaseJapanese()
print(bbj.output_all_html("おはよう"))
```
## HTML Generate.
In the example above, the method generates an HTML with the data needed to write the word in Japanese 'おはよう'.

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

### We also offer JSON, YAML, XML generators, and many more.

## Supports 4 languages. 
Right now, we offer Braille translations in 4 languages: English, Japanese, Arabic, and Portuguese.

### braillebasearabic
- Apache License Version 2.0
### braillebaseenglish
- Apache License Version 2.0
### braillebasejapanese
- Apache License Version 2.0
### braillebaseportuguese
- Apache License Version 2.0
### brailletable
- MIT
### braillebase
- MIT

## Create your own dictionaries using the base Braille library. Here's an example.
### Any Language
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

## Output
𓃒 𓃖 𓃯 𓅅 𓅼

⠁⠀⠃⠀⠉⠀⠙⠀⠑

## Thanks
The tool is still in development, but it's fully usable and we’d love your opinion. Thanks for reading this far. Cheers.
