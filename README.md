# BrailleBase
### pip install braille or pip install braillebase
## Announcement
- This package is part of an ecosystem called Braille Base. This name does not represent a company or business; it is an independent initiative aimed at providing registered braille tables for all of humanity.

- We constantly need help to register, update, and validate braille tables. There is still no official contact channel, but you can find new information on the blog braillebase.blogspot.com or brailletable.blogspot.com.

## English
### We believe that the translation generated in this test is 100% correct.
"Library Developed to Handle Simple and Complex Braille 2026"

```python
from braille import *

bb = bbe()
print(bb.output_braille_txt("Library Developed to Handle Simple and Complex Braille 2026"))
```
Output: ⠠⠇⠊⠃⠗⠁⠗⠽⠀⠠⠙⠑⠧⠑⠇⠕⠏⠑⠙⠀⠞⠕⠀⠠⠓⠁⠝⠙⠇⠑⠀⠠⠎⠊⠍⠏⠇⠑⠀⠁⠝⠙⠀⠠⠉⠕⠍⠏⠇⠑⠭⠀⠠⠃⠗⠁⠊⠇⠇⠑⠀⠼⠃⠚⠃⠋

## Japanese
### We believe that the translation generated in this test is 100% correct.
"単純な点字と複雑な点字の両方に対応できるライブラリが開発されました 2026年。"

```python
from braille import *

bb = bbj()
print(bb.output_braille_txt("たんじゅんな てんじ と ふくざつな てんじ の りょうほう に たいおう できる らいぶらり が かいはつ されました 2026ねん 。"))
```
Output: ⠕⠴⠘⠹⠴⠅⠀⠟⠴⠐⠳⠀⠞⠀⠭⠩⠐⠱⠝⠅⠀⠟⠴⠐⠳⠀⠎⠀⠈⠚⠉⠮⠉⠀⠇⠀⠕⠃⠊⠉⠀⠐⠟⠣⠙⠀⠑⠃⠐⠭⠑⠓⠀⠐⠡⠀⠡⠃⠥⠝⠀⠱⠛⠵⠳⠕⠀⠼⠃⠚⠃⠋⠏⠴⠀⠲⠀

## Portuguese
### We believe that the translation generated in this test is 100% correct.
"Biblioteca Desenvolvida para Lidar com Braille Simples e Complexo 2026"

```python
from braille import *

bb = bbp()
print(bb.output_braille_txt("Biblioteca Desenvolvida para Lidar com Braille Simples e Complexo 2026"))
```
Output: ⠨⠃⠊⠃⠇⠊⠕⠞⠑⠉⠁⠀⠨⠙⠑⠎⠑⠝⠧⠕⠇⠧⠊⠙⠁⠀⠏⠁⠗⠁⠀⠨⠇⠊⠙⠁⠗⠀⠉⠕⠍⠀⠨⠃⠗⠁⠊⠇⠇⠑⠀⠨⠎⠊⠍⠏⠇⠑⠎⠀⠑⠀⠨⠉⠕⠍⠏⠇⠑⠭⠕⠀⠼⠃⠚⠃⠋

## In Test

## Arabic
### The algorithm behaves normally, as it does in any other language; however, we are not able to verify whether the braille generated for the Arabic library is correct.
"مكتبة برمجية طُوِّرت للتعامل مع نصوص برايل البسيطة والمعقدة 2026"

```python
from braille import *

bb = bba()
print()
print(bb.output_braille_txt("مكتبة برمجية طُوِّرت للتعامل مع نصوص برايل البسيطة والمعقدة 2026"))
```
Output: ⠍⠅⠞⠃⠡⠀⠃⠗⠍⠚⠊⠡⠀⠾⠥⠺⠠⠑⠗⠞⠀⠇⠇⠞⠷⠁⠍⠇⠀⠍⠷⠀⠝⠯⠺⠯⠀⠃⠗⠁⠊⠇⠀⠁⠇⠃⠎⠊⠾⠡⠀⠺⠁⠇⠍⠷⠟⠙⠡⠀⠼⠃⠚⠃⠋

## Viet
### We have managed to achieve our goals so far. We have not found braille representations for the accented letters of the Vietnamese language. We need help to update this part of the database.
"Thư viện được phát triển để xử lý chữ nổi Braille đơn giản và phức tạp năm 2026"

```python
from braille import *

bb = bbv()
print(bb.output_braille_txt("Thư viện được phát triển để xử lý chữ nổi Braille đơn giản và phức tạp năm 2026"))
```
Output: ⠠⠞⠓⠳⠀⠧⠊⠣⠝⠀⠮⠳⠪⠉⠀⠏⠓⠁⠞⠀⠞⠗⠊⠣⠝⠀⠮⠣⠀⠭⠳⠀⠇⠽⠀⠉⠓⠳⠀⠝⠹⠊⠀⠠⠃⠗⠁⠊⠇⠇⠑⠀⠮⠪⠝⠀⠛⠊⠁⠝⠀⠧⠁⠀⠏⠓⠳⠉⠀⠞⠁⠏⠀⠝⠜⠍⠀⠼⠃⠚⠃⠋

# Confidence Test Method 
```python
from braille import *

bb = bbe()
print(bb.confidence_test("Braille"))
```
- Output: {0: ['⠠', ['⠠']], 1: ['B', ['⠃']], 2: ['r', ['⠗']], 3: ['a', ['⠁']], 4: ['i', ['⠊']], 5: ['l', ['⠇']], 6: ['l', ['⠇']], 7: ['e', ['⠑']]}

  <img src="./img/logo.png" alt="Logo" width="500" height="493">
