
# Tortoise ORM

Per il database ho scelto di utilizzare Tortoise ORM.

https://tortoise.github.io/

Mi è sembrato un progetto promettente ed in pieno stile Django, 
framework che ormai apprezzo ed utilizzo fin dalla versione 1.11!

Nonostante le ridotte dimensioni del progetto,
mi è sembrato un buon pretesto per testarne il funzionamento.

Tortoise nasce per essere completamente asincrono.
Per non dover gestire tale comportamento nel codice ho preferito adottare la libreria
`syncasync` che introduce un decorator che permette di "convertire" un metodo da asincrono a sincrono.

Le operazioni effettuate da Tortoise sono tutte raggruppate nella classe `DbManager`.
