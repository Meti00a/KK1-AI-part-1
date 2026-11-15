
Faktafrågor 1.

1. I kapitlet beskrivs en checklista med sju steg. Beskriv de sju tegen översiktligt. I verkligheten, följs dessa steg i en rak progression eller arbetar men generellt iterativt? ?

svar: De första sju stegen beskrivs följande:

1. Definiera ett problem och bestämma över vad modellen ska lösa och vilket resultat ska ges ut

2. Samla och hämta relevant data från olika typer av filer. (csv, databaser eller ett API)

3. Undersök datan, hantera de saknade värden och se till att datan är tillämpad för träning.

4. Skapa datan i 3 olika syften. Träningsdata, testdata och valideringsdata om det behövs.

5. testa datan i lämpliga algoritmer så att den kan lära sig mönster för att få fram resultat.

6. göra en utvärdering och förbättra modellen genom att mäta prestanda och justera funktioner eller hyperparametrar.

7. Övervaka modellen genom att skapa ett integration i applikation och sedan följa upp om hur modellen visar prestation med ny data.

arbetsprocessen på modellen & datan kan behöva upprepas och lägga till förbättringar om problem uppstår,  

Jag skulle säga att man arbetar mer iterativt. Beroende på vilket företag man jobbar på, så skulle jag säga att man jobbar steg för steg istället för att satsa hela delen och hamna i risk för att städa om hela projektet eller börja om från början.

1. Vad menas med att en modell produktionssätts?
 svar:  att en modell produktionsätts, innebär att man att man färdig utvecklar modellen för att sedan kunna tillämpas & användas i verkligheten. Först planerar man projektet och hittar en källa för datan. Sedan bygger man upp stabil kodstruktur & tvättar datan för att den ska vara användingsbar. Det går även att följa upp utav arbetsprocessen och kontrollera att allt fungerar som det ska. Och därefter, testar datan & se till att den är färdig för lansering.

2. Vad är scikit-learn för något? Biblioteket följer några centrala designprinciper. Vilka är dessa? Vad är estimators, predictors och transformers?

 svar: Scikit-learn är ett bibliotek i python som används för maskininlärning. Det har en tydlig struktur i koden som gör att funktionerna fungerar på samma sätt & förenklar arbetsprocessen genom olika modeller.

 Estimator: används för att träna en modell genom att använda hjälp från data.

 predictor: används för att förutspå och predika utifrån datan man får.

 transformer: används för att ändra eller bearbeta datan så att den är anpassad för modellen.

1. Vad är TensorFlow och Keras?

TensorFlow är ett verktyg som används när man ska bygga och träna modeller inom maskininlärning. Keras gör så att det är enklare att tillverka och träna neurala nätverk utan att behöva spendera mycket tid till att skriva komplicerad kod. Dessa två används ihop när man arbetar med djupinlärning.

"Resonemangfrågor"

1. Kalle och Stina diskuterar maskininlärning över en lunch. Kalle säger “om jag tränat en modell och den inte presterar bra nog på testdatan så justerar jag den tills den gör det.” Stina säger “det är ett stort fel att göra så, det enda du då åstadkommer är att du överanpassar testdatan. Hela syftet med testdatan försvinner då”. Vad säger du om deras dialog?

svar: Jag tycker att Stinas åsikt stämmer. Om kalle ska fortsätta med att ändra modellen för att den ska vara anpassningsbar för testdatan, så är risken stor att den blir endast anpassad för just den datan. Och då blir det osäkert ifall modellen kan prestera och fungera när man stoppar in ny data i modellen. Det är alltid bättre att ha 3 olika typer av data för att få modellen till att fungera. Träningsdata: för att träna modellen, (Valideringsdata): för att kunna förbättra modellen. Och slutligen, testa för att kontrollera resultatet (testdata)

1. Många AI/ML projekt uppnår inte de ursprungligen satta målen eller att ens passera någon form av prototyp-stadie. Vad tror du detta beror på och hur ska vi förhålla oss till det?

svar: Jag tror att många AI och ML projekt som inte blir färdiga för produktion är för att man har alldeles för höga förväntingar på vad datan kan klara av, och för att datan är inte tillräckligt bra att utgå sig ifrån. Men det kan också bero på att man spenderar mer tid än planerat, vilket gör att projektet tar längre tid än vad man förväntade sig. Eller att man har mindre kunskaper och resurser för att slutföra projektet i god tid.

Men jag tycker att man kan se detta som en möjlighet att lära sig. Om modellen inte fungerar som man hade förväntat sig, så kan man undersöka vad som gick fel och försöka göra en förbättring av modellen. Det är också viktigt att man testar modellen under arbetets gång för att upptäcka problem i tid och se vad som behöver ändras under arbetsprocessen.
