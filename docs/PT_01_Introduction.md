# Introdução

**BrailleBase é um pacote de métodos com o objetivo de criar tecnologia para pessoas cegas.  
Você pode usar essa biblioteca diretamente, mas recomendamos que crie uma classe com a língua‑alvo que você deseja mapear para Braille.**


## Instalação via PyPI
Para isso, é preciso instalar a biblioteca com:

```bash
pip install braillebase
```

## Criando mapas da língua de sua preferência

O recomendado é importar a biblioteca e criar uma classe com a nomenclatura **BrailleBase + Língua**, que herda da classe `BrailleBase`. Por exemplo:

```python
from braillebase import BrailleBase

class BrailleBaseJapanese(BrailleBase):
    pass
```
## Mapeamento de cada letra com sua lista de Braille
Após isso, dentro do `def __init__(self):`, chame o construtor da superclasse com `super().__init__()` e podemos começar o mapeamento das letras com o Braille.

Chamando o método `self.append_braille_letter("あ", ["⠁"])`, é possível cadastrar a chave — que, nesse exemplo, é a string `"あ"` — e o valor, que é a lista `["⠁"]`.

Veja um exemplo mais amplo de como cadastrar o alfabeto. Sempre a letra no primeiro argumento e sempre uma lista com o Braille no segundo argumento.

`append_braille_letter("letter", braille[])`

- **letter**: uma string representando a letra que será usada como chave.
- **braille[]**: uma lista contendo um ou mais caracteres Braille associados à letra.

```python
class BrailleBaseJapanese(BrailleBase):
    def __init__(self):
        super().__init__()

        self.append_braille_letter("あ", ["⠁"])
        self.append_braille_letter("い", ["⠃"])
        self.append_braille_letter("う", ["⠉"])
        self.append_braille_letter("え", ["⠋"])
        self.append_braille_letter("お", ["⠊"])
        self.append_braille_letter("ア", ["⠰", "⠁"])
        self.append_braille_letter("イ", ["⠰", "⠃"])
        self.append_braille_letter("ウ", ["⠰", "⠉"])
        self.append_braille_letter("エ", ["⠰", "⠋"])
        self.append_braille_letter("オ", ["⠰", "⠊"])
```

Cada letra é considerada uma chave que terá armazenada uma lista de Braille. Por exemplo, a letra japonesa `あ` (que contém a fonética `"a"`) usa apenas um caractere Braille, o `"⠁"`. Porém, a letra `ア` contém dois caracteres de Braille: `"⠰", "⠁"`.

### Cuidado: chaves com no máximo 1 caractere
A biblioteca permite que você cadastre mais de um Braille para a mesma letra através do método `append_braille_letter("letter", braille[])`, mas a versão atual 0.0.4 não permite que uma chave contenha dois caracteres, como por exemplo **"きゃ"** (fonética *kya*), que deveria retornar:

`"きゃ"` = `"⠈", "⠣"`

mas retorna:

`"き", "ゃ"` = `"⠣", "⠂", "⠌"`

Isso acontece pois a biblioteca não dá suporte para chaves com 2 ou mais caracteres. Então, o que deveria ser:

`self.append_braille_letter("きゃ", ["⠈", "⠣"])`

é interpretado como:

`self.append_braille_letter("き", ["⠣"])`  
`self.append_braille_letter("ゃ", ["⠂", "⠌"])`

### Resumo
**Chave:** com no máximo 1 caractere  
**Valores:** listas com quantos caracteres forem necessários, desde que sejam Braille.

## É possível usar todos os métodos de instância

Uma vez que as letras estão cadastradas pelo método `append_braille_letter()`, todos os métodos de instância conseguem traduzir seu texto em listas binárias, códigos Unicode e, principalmente, em textos em Braille. Veja o exemplo abaixo.

### Exemplo 1 - A saída é um array com os brailles referentes ao texto inserido.
```python
from braillebase import BrailleBase

class BrailleBaseJapanese(BrailleBase):
    def __init__(self):
        super().__init__()

        self.append_braille_letter("あ", ["⠁"])
        self.append_braille_letter("い", ["⠃"])
        self.append_braille_letter("う", ["⠉"])
        self.append_braille_letter("え", ["⠋"])
        self.append_braille_letter("お", ["⠊"])
        ...
        self.append_braille_letter("わ", ["⠄"])
        self.append_braille_letter("ゐ", ["⠆"])
        self.append_braille_letter("ゑ", ["⠖"])
        self.append_braille_letter("を", ["⠔"])
        self.append_braille_letter("ん", ["⠴"])


braille_base_obj = BrailleBaseJapanese()

braille = braille_base_obj.translate_text_to_braille("あいしてる")

print(braille)
```

`Output: ['⠁', '⠃', '⠳', '⠟', '⠙']`

### Exemplo 2 - A saída é um código HTML totalmente funcional em string.

```python

braille_base_obj = BrailleBaseJapanese()

braille = braille_base_obj.output_all_html("あいしてる")

print(braille)
```

`Output:`
```html
 <div class="braille-output">
  <section class="braille-item">
    <h2>あ — Braille 1</h2>
    <ul>
      <li><strong>Braille:</strong> ⠁</li>
      <li><strong>Index:</strong> 1</li>
      <li><strong>Binary:</strong> <code>000001</code></li>
      <li><strong>Binary List:</strong> [0, 0, 0, 0, 0, 1]</li>
      <li><strong>Unicode:</strong> 2801</li>
      <li><strong>Dot Count:</strong> 1</li>
      <li><strong>Numbering:</strong> 1</li>
      <li><strong>Numbering List:</strong> [1]</li>
    </ul>
  </section>
  <section class="braille-item">
    <h2>い — Braille 1</h2>
    <ul>
      <li><strong>Braille:</strong> ⠃</li>
      <li><strong>Index:</strong> 3</li>
      <li><strong>Binary:</strong> <code>000011</code></li>
      <li><strong>Binary List:</strong> [0, 0, 0, 0, 1, 1]</li>
      <li><strong>Unicode:</strong> 2803</li>
      <li><strong>Dot Count:</strong> 2</li>
      <li><strong>Numbering:</strong> 1-2</li>
      <li><strong>Numbering List:</strong> [1, 2]</li>
    </ul>
  </section>
  <section class="braille-item">
    <h2>し — Braille 1</h2>
    <ul>
      <li><strong>Braille:</strong> ⠳</li>
      <li><strong>Index:</strong> 51</li>
      <li><strong>Binary:</strong> <code>110011</code></li>
      <li><strong>Binary List:</strong> [1, 1, 0, 0, 1, 1]</li>
      <li><strong>Unicode:</strong> 2833</li>
      <li><strong>Dot Count:</strong> 4</li>
      <li><strong>Numbering:</strong> 1-2-5-6</li>
      <li><strong>Numbering List:</strong> [1, 2, 5, 6]</li>
    </ul>
  </section>
  <section class="braille-item">
    <h2>て — Braille 1</h2>
    <ul>
      <li><strong>Braille:</strong> ⠟</li>
      <li><strong>Index:</strong> 31</li>
      <li><strong>Binary:</strong> <code>011111</code></li>
      <li><strong>Binary List:</strong> [0, 1, 1, 1, 1, 1]</li>
      <li><strong>Unicode:</strong> 281f</li>
      <li><strong>Dot Count:</strong> 5</li>
      <li><strong>Numbering:</strong> 1-2-3-4-5</li>
      <li><strong>Numbering List:</strong> [1, 2, 3, 4, 5]</li>
    </ul>
  </section>
  <section class="braille-item">
    <h2>る — Braille 1</h2>
    <ul>
      <li><strong>Braille:</strong> ⠙</li>
      <li><strong>Index:</strong> 25</li>
      <li><strong>Binary:</strong> <code>011001</code></li>
      <li><strong>Binary List:</strong> [0, 1, 1, 0, 0, 1]</li>
      <li><strong>Unicode:</strong> 2819</li>
      <li><strong>Dot Count:</strong> 3</li>
      <li><strong>Numbering:</strong> 1-4-5</li>
      <li><strong>Numbering List:</strong> [1, 4, 5]</li>
    </ul>
  </section>
</div>
```

## Esta documentação está em construção e será traduzida para inglês, japonês e italiano.
