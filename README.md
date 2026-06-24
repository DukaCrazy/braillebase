# BrailleBase
## What is BrailleBase
- BrailleBase is an algorithm that translates characters into Braille.
- Today, each country uses different Braille rules, and there is no universal standard for developers. This makes it almost impossible to create tools that are compatible with each other.
- BrailleBase creates a universal layer that standardizes the logic, allowing any tool — from screen readers to Braille embossers — to speak the same language.
- As a result, learning languages, accessing culture, and integrating devices becomes more accessible for millions of people.
### Beyond translation
- BrailleBase provides the number of dots in each Braille symbol.
`Example: the character '⠼', which indicates that a number follows, contains 4 dots.`

- It also provides the numeric position of each dot and the corresponding binary pattern.
` For '⠼', the positions are 3‑4‑5‑6 and the binary is 001111.`

- These data can be accessed directly through methods that return dot counts, positions, binary patterns, and other metadata.
- For integration with other tools, the output methods generate a complete map of each symbol in formats such as JSON, XML, YAML, and more.
- The library is still under development, so method signatures may change. We are working to release a stable version as soon as possible.

## Purpose of BrailleBase
### Standardized Technology
- Many companies and developers who want to create tools and technologies for blind people face a major barrier: integrating their microsystems with other equipment.
- BrailleBase is the first library that combines translation, complete metadata, and multiple output formats without external dependencies.
## Challenges to Be Addressed
- Many countries do not have a well‑structured Braille system or documented rules.
- Understanding these rules, standardizing them, and converting them into a base algorithm usable by subclasses is one of the biggest challenges.
- Presenting BrailleBase to companies in the accessibility sector is another area we need to improve, especially in communicating the value of the tool.
- It is also essential to produce educational material and clear documentation, ensuring that both beginners and experienced developers can use BrailleBase without difficulty.
## Final Statement
- This is the first official text of the BrailleBase tool.
- The system currently includes the Japanese, Portuguese, Arabic, and English alphabets.
- All letters have been individually verified, but the second‑level rules are still under development.
- There is still no support for full‑word translation, but this feature is already planned.
- We are preparing a draft of the Pinyin class.
- Once the English documentation is completed, the Pinyin class finalized, and the known bugs fixed, we will release the first usable version of the package.
- From that release onward, the method signatures will become stable, ensuring that updates do not break dependent applications.
- We do not use external dependencies beyond those provided by default in each programming language.
- The classes braille, braillebase, braillebasejapanese, braillebaseportuguese, braillebasearabic, and braillebaseenglish have (or will have) CC0, MIT, or Apache 2.0 licenses.

` Get in touch through GitHub: https://github.com/DukaCrazy`

` My name is Duka — and if a project isn’t crazy enough to change the world, it’s probably not mine.`

- 2026/06/24
