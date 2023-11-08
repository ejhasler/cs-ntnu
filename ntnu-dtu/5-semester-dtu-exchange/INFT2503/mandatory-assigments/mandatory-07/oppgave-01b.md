Exercise 01

b)

Programmet utfører beregningene fra venstre til høyre. Det starter med operasjonen 5 - 3, som resulterer i 2. Deretter fortsetter det sekvensielt: først utføres 2 - fraction1, etterfulgt av resultatet av den operasjonen minus 7, og til slutt minus fraction2.

Når programmet håndterer 2 - fraction1, er det ikke lenger en enkel subtraksjon mellom to heltall. Her anvendes en av de overbelastede subtraksjonsoperatorene. Spesifikt, operatoren som er definert utenfor klassedeklarasjonen, tar et heltall på venstre side og et `Fraction`-objekt på høyre side, for å returnere et nytt `Fraction`-objekt som er differansen av de to.

Deretter vil programmet ta for seg operasjonen fraction3 - 7. Dette vil føre at den overbelastede subtraksjonsoperatorene definert inne i selve header-klassen blir tatt i bruk.
Denne operatoren er definert som følger `Fraction operator-(const int other) const;`

Dette vil gi en ny instans av Fraction klassen slik som det gjør med den andre subtraksjonsoperatoren. Den nye instansen vil få navnet fraction4, og den tilsvarer fraction3
redusert med 7. Etter denne siste operasjonen vil det se slik ut: fraction4 - fraction2.

I hvert av trinnene, bortsett fra det første, anvendes de overbelastede subtraksjonsoperatorene som er definert i Fraction-klassen. Disse operasjonene utføres sekvensielt, hvor hver operasjon tar det forrige trinnets resultat som den venstre operanden. Uttrykket evalueres til et Fraction-objekt som representerer den endelige differansen.
