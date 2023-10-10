
# Flyobj Telegram BOT

Nel 2017 ho scritto un bot per avere informazioni sugli aerei di passaggio sopra la mia testa. 
Creava una mappa con un segnalino per ogni aereo segnalato in zona e una tastiera con cui era possibile avere ulteriori informazioni.
Credo sia molto "grezzo" e per niente elegante, ma ero veramente alle prime armi.
Ha girato perfettamente fino a che l'API da cui prendevo le notizie non ha cambiato qualcosa e ho lasciato perdere.


## Update 1

Il qualcosa che e' cambiato e' il fatto che l'API e' diventata a pagamento. 

Ci sono alternative free ma riguardano ben determinate zone del pianeta e non mi pare che al momento contemplino l'Italia. 

Qui una directory https://www.virtualradarserver.com/Directory.aspx


## Update 2

Trovata un API con free tier su RapiAPI.

Nell'ultima release è stato integrato un piccolo database sqlite che tiene traccia delle chiamate API che fa' il bot.
Una volta raggiunto il limite gratuito si ferma fino al mese successivo.

Qui una semplice e breve documentazione su come configurare e avviare il bot: [documentazione](docs/quick_start.md) 
