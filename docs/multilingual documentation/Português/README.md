📘 BrailleBase — Internal Architecture Overview
A BrailleBase é organizada em grupos funcionais numerados, cada um responsável por uma parte específica da lógica interna.
Essa estrutura modular facilita manutenção, leitura, expansão e documentação multilíngue.
A seguir está a descrição oficial de cada grupo.

Braille é um sistema de escrita tátil composto por pontos em relevo, organizados em uma célula de 6 pontos (2 colunas × 3 linhas).
Cada combinação de pontos representa letras, números, pontuação ou símbolos especiais.
Ele foi criado por Louis Braille, em 1824, quando tinha apenas 15 anos.
https://en.wikipedia.org/wiki/Braille

📚 Para que serve
Segundo as fontes, Braille é um sistema de escrita completo, não apenas um código do alfabeto visual.
Ele permite:
- leitura em papel em relevo
- leitura em displays braille eletrônicos
- escrita com reglete e punção
- escrita com máquinas braille ou computadores conectados a impressoras braille
https://en.wikipedia.org/wiki/Braille

🧠 Origem e história (resumo)
- Criado por Louis Braille, que ficou cego após um acidente na infância.
- Baseado no “night writing” de Charles Barbier, mas simplificado para 6 pontos.
- Publicado pela primeira vez em 1829.
https://www.britannica.com/topic/Braille-writing-system

<span style="color:red">📌 Nota de Observação
Estamos trabalhando continuamente para melhorar nossa aplicação.
A versão 0.0.5 já é capaz de lidar com textos que contenham números, desde que esses caracteres estejam devidamente cadastrados no sistema.
Atualmente estamos revisando e expandindo nossa documentação para tornar o uso da biblioteca mais claro.
Na versão 0.1.0, problemas conhecidos — como chaves de mapeamento com mais de dois caracteres — já terão sido resolvidos.
Para dúvidas, sugestões ou relatórios de problemas, por favor entre em contato através da aba Issues no GitHub.
Sua participação é essencial para aprimorarmos este projeto.</span>


0001 Registry → registra letras e brailles
0002 Translate → converte texto para braille e índices
0003 Mapping → mapeia braille ↔ índices
0004 Tables → fornece tabelas internas fixas
0005 Output → exporta resultados

🧩 0001 — Registry group
Gerencia o registro interno de caracteres e seus respectivos mapeamentos para braille.
Funções principais
- append_braille_letter
Registra uma letra e sua lista de células braille.
Se já existir, sobrescreve.
- get_brailles_with_letter
Retorna a lista de brailles associada a uma letra registrada.
- has_letter
Verifica se uma letra está registrada.
- remove_letter
Remove uma letra do registro interno.
Responsabilidade do grupo
Este grupo funciona como o banco de dados interno da classe.
Nada é traduzido sem passar por aqui.

🔤 0002 — Translate group
Responsável por converter texto em braille e depois em índices numéricos.
Funções principais
- translate_text_to_braille
Converte cada caractere em uma ou mais células braille.
Inclui pré‑processamento de números (⠼).
- translate_text_to_index
Converte a lista de brailles em uma lista de índices (0–63).
Responsabilidade do grupo
Este é o coração da tradução.
Todo texto passa por aqui antes de ser exportado ou manipulado.

🔁 0003 — Mapping group
Fornece mapeamentos diretos entre:
- braille → índice
- lista de brailles → lista de índices
Funções principais
- get_braille_to_index
Retorna o índice Unicode braille (U+2800–U+283F).
- get_braille_list_to_index_list
Converte listas inteiras de braille para índices.
Responsabilidade do grupo
É o núcleo matemático da biblioteca.
Nenhuma conversão numérica acontece fora deste grupo.

📚 0004 — Tables group
Contém tabelas internas fixas, usadas como referência.
Funções principais
- braille_list
Lista completa dos 64 símbolos braille Unicode.
- get_binary_list
Lista de 64 arrays de 6 bits (representação binária).
- get_binary_string_list
Lista de 64 strings binárias de 6 bits.
Responsabilidade do grupo
Fornece estruturas base para conversões, validações e exportações.

📤 0005 — Output group
Responsável por formatar e exportar dados em diferentes formatos.
Funções principais
- output_all_json
Exporta texto, braille e índices em formato JSON.
Responsabilidade do grupo
É a camada final da biblioteca.
Tudo que sai da BrailleBase passa por aqui.
