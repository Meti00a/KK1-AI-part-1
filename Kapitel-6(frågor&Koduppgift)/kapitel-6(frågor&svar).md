faktafrågor

1. Vad är klustring för något? Ge några exempel på tillämpningsområden.

svar: Klustring är en metod som används inom maskininlärning, det är ett sätt där man delar upp data i olika grupper baserad på hur lika de är. Ett exempel på detta kan vara hur man grupperar datorspel efter vad det kostar, vilket betyg spelet har och vad för spelgenre det är, för att kunna hitta andra datorspel som har liknande grupper.

1. Förklara översiktligt hur K-means fungerar. Använd figur 6.3 (sidan 238) och figur 6.4 (sidan 239 i din förklaring)

svar: K-means fungerar genom att man först väljer hur många grupper man är ute efter och sedan låta modellen placera punkterna i de gruppen som matchar. Om man kollar på figur 6.3, så ser man hur datan kan bli uppdelad i olika kluster. Men om kollar på figur 6.4, så ser man att slutresultatet blir felaktigt. Eftersom modellen delar upp olika punkter som gör att datan inte är passande för modellen och inte tränat modellen tillräckligt.

resonemangfrågor

1. hur kan man välja vilket antal kluster som ska användas för en K-means modell? använd intertia, silhouette score och silhouette diagram i ditt svar.

svar: Man kan testa att använda sig utav olika typer av kluster och se vad som passar i bäst. inertia kan användas för att se hur nära punkterna ligger i mitten av sina grupper på resultatet. Silhouette score kan användas för att se hur bra punkterna passar i sina egna grupper om man jämför med de andra grupperna. Silhouette diagram används för att visa hur punkterna har fördelats i de olika grupperna och se om de passar bra i sitt kluster. Genom att kolla och jämföra resultatet man får, så kan man avgöra vilket antal kluster som passar bäst för datan.

1. om du kollar på figur 6.10 på sidan 247, hur många kluster hade du valt och varför? är det en "exakt vetenskap" att välja antalet kluster?

svar: utifrån figur 6.10 så hade jag hade valt 4 kluster, eftersom kurvan börjar sakta gå ner gradvis från K-1 och landa på K-4, vilket då gör en armbåge i grafen. Efter det, så kommer inte detta påverka mycket mer om man skulle lägga in flera kluster i grafen. Så detta är inte en exakt vetenskap, eftersom allt beror på vad för data det är och vad resultatet kan gå ut på.

1. hur tolkar man figur 6.13 på sidan 251?

svar: På Figuren 6.13 tolkas genom att jämföra olika kluster med hjälp av silhouette score. Enligt bilden, så ser man att 6 kluster ge sämre resultat, medans 5 kluster ger bättre resultat eftersom klustern är lika stora. 3 och 4 kluster går också bra att använda, men det finns inget riktigt svar på hur exakt många kluster man ska behöva. Det avgörs genom resultatet man får utifrån datan.
