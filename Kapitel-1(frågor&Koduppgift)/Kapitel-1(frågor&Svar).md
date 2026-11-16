Kapitel 1- Introduktion till maskininlärning
Faktafrågor

1. Hur hänger AI, ML och DL ihop?
svar: AI (som står för artificell intelligens) är ett system som kan utföra uppgifter snabbare än vad en mänsklig människa kan utföra.

ML (som står för machine learning) är en del av ai som lär sig mönster direkt ur en data istället för att programmeras med specifika regler utifrån olika scenarios.

DL (som står för Deep Learning) är en del av ML som används av neurala nätverk som har flera lager, och kan lära sig mer komplexa mönster och data.

1. Vilka är de fyra problemkategorierna inom ML?
svar: Regression, Klassificering, Klustring och Dimensionsreduktion

Regression är att man kan se ett numerisk värde, och förutspå vad det kan ge i result: tex, en pris på en bil eller en lägenhet.

Klassificering: är att man kan kika och förutse vilka olika klasser någon tillhör. kan vara allt ifrån: Bilmärke, Bostadsförening eller något annat.

Dimensionsreduktion: innebär att man minskar antalet variabler i ett dataset, men också sparar viktig information som kan behövas.

1. Förklara följande:
a) Vad är syftet med att dela upp data i träningsdata, valideringsdata och
testdata?
Svar: Träningsdata: används mest för att träna modellen som finns i datasetet och se vilka variabler och resultat man får utifrån.
Valideringsdata: används mestadels för att jämföra olika typer av modeller och parametrar, och detta går att göra utan att använda testdatan. Vilket också gör risken blir mindre ifall man skulle möjligtvis anpassa datan som vi använder under utvecklingens gång.

b) Vad är k-delad korsvalidering för något?
Svar: Korsvalidering (eller även känd som Cross validation) betyder att dataset används när man delar upp i k delar.

Modellen som används från datasetet, kan delas upp och användas som testdata. Vilket resulterar i att man får en sammanställning på hela splittringen utifrån cross validation. Och resulterat kommer då geneom att köra från medelvärdet. Vilket också ger en stabil upskattning utifrån modellens punkt.

c) Vad är root mean squared error (RMSE) för något?
Svar: RMSE innebär att man mäter hur stort en modell kan vara felaktig i genomsnitt. RMSE används för att beräkna skillnaden mellan de resultaten som modellen ger ut, med de faktiska värden man tar reda på, och det gör man genom att man tar kikar på felet, tar medelvärdet och sedan roten ut det.
Skulle man ta ett mindre värde så är det betyldigt mer bättre, eftersom det kan betyda att de faktiska värderna man får, kan överrenskomma med det modellen visar enligt beräkningarna.

d) Vad är en hyperparameter för något? Vad är en parameter för något?
Svar: en hypeparameter är en slags tillägg som man själva gör ett beslut innan modellen lär tränas och påverkas.
En parameter innebär att modellen själv lär utifrån testdatan när den tränas.

e) Vad är grid search och hur hänger namnet “grid” och “search” ihop med
processen som genomförs? Läser vi dokumentationen: <https://scikit-learn>.
org/stable/modules/generated/sklearn.model_selection.GridSearchCV så
ser vi att hyperparametern refit har standardvärdet True, vad innebär
det?
svar: Grid search används för att testa olika kombinationer av hyperparametrar för att få tag på vilka tillägg som fungerar bäst utifrån modellen. ordet "Grid" används för att skapa en rutnät med flertal värden av olika slag, medans "Search" låter programmet kolla igenom värden för att få tag på den bästa.
Hur refit med standardvärdet true kommer in i bilden. Betyder att modellen tränas om med de bästa hyperparametrarna, och kan fortsätta användas för att göra nya prediktioner.

f) Vad är kategorisk data och hur hanteras det? I ditt svar, använd begreppen
nominal data, ordinal data, one-hot-encoding, dummy-variable-encoding
och ordinal encoding.
svar: Kategorisk data innebär data som är tillgänglig och sorterad i olika typer av kategorier som de ska tillhöras.
Nominal data: är en slags kategori som inte behöver någon struktur eller ordning, tex: färger.

Original data är en kategori som har en tydlig ordning. Tex en skala från 1-10, där 1 är sämst, och 10 är bäst.

för att implementera kategorisk data i en modell med ML, så finns det flera metoder som går att använda. Och detta gör man med hjälp utav "One-Hot-encoding" som skapar en egen kolumn utifrån varje kategori och predikerar med 0 eller 1 över vilken kategori som är relevant. Sen finns det Dummy Variable encoding också, fast den tar bort ett av kategorierna för att undvika onödig information.

g) Vad är feature engineering för något?

svar: Feature engineering betyder att man bearbeta och förändrar data för att sedan tillämpa nya eller andra features som modellen kan använda. Anledningen är för att datan ska kunna vara mer läsbar för att modellen ska lättare kunna hitta mönster bättre.
h) Vad menas med principle of parsimony?
Prince of parsimony innebär att man väljer den enklaste modellen som kan förutspå bättre svar eller mönster.
4. Vad menas med att “en modell är en förenkling av verkligheten”?
svar: det som menas med det är att modellen använder det viktigaste informationen och försöker hitta de mönstren som finns i datan för att sedan kunna göra förutsägelser. Det betyder inte att modellen inte kan ta hänsyn till alla faktorer som finns i verkligheten.
5. Vad menas med att en modell är “överanpassad” eller overfitted på engelska?
svar: En modell som är överanpassad innebär att man har läst igenom träningsdatan alltför mycket i detalj, men kan ha svårt att fungera bättre när den får in ny data som inte man känner till sedan tidigare.
6. Högre är bättre i scikit-learn scoring, vad innebär det?
svar: att högre är bättre i scikit-learn scoring innebär att modellen som läser in datan, får den högsta scoring värdet som räknas som bästa. Samma sak gäller även när mätvärdet ska egentligen vara låg som möjligt.

1. Vad är tvärsnittsdata, tidsseriedata och paneldata? Exemplifiera när respektive datakategori kan uppstå.
svar: Tvärsnittsdata: är data som samlas in från flera olika privatpersoner, företag eller något annat i samma tidpunkt. Tex årsinkomst för 50 personer under år 2026.

Tidsseriedata: är data som samlas in från samma objekt i en längre tidsperiod.
Tex: att försälningssiffrona på ett företag stiger/sjunker varje månad under många års tid.

Resonemangfrågor
8. Ge några exempel på verkliga tillämpningsområden inom ML. Sök gärna
på nätet för att besvara frågan.
Deet finns ett par exempel där företag använder verkliga tillämplningsområden inom ML.
Hälsovården: använder sig utav algoritmer som analyserar röntgenbilder, för att identifiera cancer eller andra sjukdomar, betydligt mer snabbare än mänskliga läkare.

Inom transport, så har bilföretagen implementerat ML i deras bilar för att kunna identifiera objekt, trafik, vägar, rutner och även alla situationer som sker i trafik. Vilket är viktigt för säkerheten.

inom Butik, så har man implementerat ML i självskannings-kassor, som gör att systemet läser av streckkoden på en produkt och registeras i systemet, för att sedan betala för varan med kortet och slutföra köpet.

1. Generellt sett gäller det att högre är bättre i scikit-learn scoring, därför
används exempelvis scoring='neg_mean_squared_error'. Förklara lo
giken bakom detta, det vill säga att vi använder “negative” mean squared

NMSE används för att mäta hur stora fel en modellen gör baserad på de faktiska värden och det som de förutsäger.  
