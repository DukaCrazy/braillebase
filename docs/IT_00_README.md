📘 BrailleBase — Panoramica dell’Architettura Interna (IT)
BrailleBase è organizzata in gruppi funzionali numerati, ognuno responsabile di una parte specifica della logica interna.
Questa struttura modulare migliora leggibilità, manutenibilità, scalabilità e coerenza nella documentazione multilingue.
Di seguito trovi la descrizione ufficiale di ogni gruppo.

<span style="color:red">📌 Nota di Osservazione
Stiamo lavorando continuamente per migliorare la nostra applicazione.
La versione 0.0.5 è già in grado di gestire testi che contengono numeri, purché tali caratteri siano correttamente registrati nel sistema.
Attualmente stiamo aggiornando ed espandendo la documentazione per rendere l’utilizzo della libreria più chiaro.
Nella versione 0.1.0, problemi noti — come le chiavi di mappatura con più di due caratteri — saranno stati risolti.
Per domande, suggerimenti o segnalazioni di problemi, ti invitiamo a utilizzare la sezione Issues su GitHub.
Il tuo feedback è fondamentale per aiutarci a migliorare questo progetto.</span>


0001 Registry → registra lettere e liste braille
0002 Translate → converte testo in braille e indici
0003 Mapping → mappa braille ↔ indici
0004 Tables → fornisce tabelle interne fisse
0005 Output → esporta i dati elaborati

🧩 0001 — Registry group (Gruppo Registro)
Gestisce il registro interno dei caratteri e le rispettive liste di simboli braille.
Funzioni principali
- append_braille_letter
Registra una lettera e la lista di braille associata. Se la lettera esiste già, la mappatura viene sovrascritta.
- get_brailles_with_letter
Restituisce la lista di braille associata a una lettera registrata.
- has_letter
Verifica se una lettera è presente nel registro.
- remove_letter
Rimuove una lettera dal registro interno.
Responsabilità del gruppo
Questo gruppo funge da database interno della classe.
Nessuna traduzione avviene senza passare da qui.

🔤 0002 — Translate group (Gruppo Traduzione)
Responsabile della conversione del testo in braille e successivamente in indici numerici.
Funzioni principali
- translate_text_to_braille
Converte ogni carattere in una o più celle braille.
Include anche la preparazione dei numeri (⠼).
- translate_text_to_index
Converte una lista di simboli braille in una lista di indici (0–63).
Responsabilità del gruppo
Questo è il motore centrale di traduzione.
Tutto il testo passa da questo gruppo prima dell’esportazione o di ulteriori elaborazioni.

🔁 0003 — Mapping group (Gruppo Mappature)
Fornisce le conversioni dirette tra:
- braille → indice
- lista di braille → lista di indici
Funzioni principali
- get_braille_to_index
Restituisce l’indice Unicode del simbolo braille (U+2800–U+283F).
- get_braille_list_to_index_list
Converte un’intera lista di simboli braille nei rispettivi indici.
Responsabilità del gruppo
Questo gruppo rappresenta il nucleo matematico della libreria.
Tutte le conversioni numeriche avvengono qui.

📚 0004 — Tables group (Gruppo Tabelle)
Contiene tabelle interne fisse, utilizzate come strutture di riferimento.
Funzioni principali
- braille_list
Restituisce l’elenco completo dei 64 simboli braille Unicode.
- get_binary_list
Restituisce 64 array di 6 bit, ciascuno rappresentante un simbolo braille.
- get_binary_string_list
Restituisce 64 stringhe binarie di 6 bit.
Responsabilità del gruppo
Fornisce strutture di base per conversioni, validazioni e formattazione dell’output.

📤 0005 — Output group (Gruppo Output)
Responsabile della formattazione ed esportazione dei dati elaborati.
Funzioni principali
- output_all_json
Esporta testo, braille e indici in formato JSON.
Responsabilità del gruppo
Questo è lo strato finale della libreria.
Tutti i dati che escono da BrailleBase passano attraverso questo gruppo.