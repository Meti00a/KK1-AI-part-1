1. faktafrågor

1. vad kännetecknar regressionsproblem? ge några exempel på tillämpningsområden.

svar: Regressionsproblem innebär att man förutspår ett numerisk värde med hjälp av datan man har.

Ett exempel på detta kan vara att man vill kunna lista ut olika statisker på: ålder och skick på en bil, kolla igenom en anställds lön på ett företag, eller kunna lista ut temperaturer i olika länder.

1. Förklara utvärderingsmåtten RMSE, MSE och MAE.

MAE som står för (Mean Absolute Error) beräknar fel i genomsnitt utan att lägga märke till om felet är positivt eller negativt.

MSE som står för (Mean Squared Error) Kvadrerar fel innan de räknas ihop. Stora fel får därför en större påverkan när resultatet visas.

RMSE som står för (Root Mean Squared Error): Tar roten ur MSE. Och ger resultat i samma enhet som värderna man försöker förutspå.

Ju mindre värde man på alla tre måtten, desto mindre fel gör modellen.

1. Om vi ska rangordna olika modeller, spelar det någon roll om RMSE eller MSE används? varför?

Nej, vanligtvis inte. Så länge modellerna utvärderas på samma data, så kommer den modell har lika låg värde.

eftersom RMSE tar kvadratroten ur MSE och bevarar ordningen, så kommer bägge ha lägst värde.

1. Förklara mycket översiktligt vad gradient descent är.

svar: Gradient descent är en metod som används för att förbättra modellen genom att försöka minska felen som den gör. Den justerar sina parametrar ett steg i taget i en riktning som gör att det minskar risken för att det blir fel. Målet är att hitta paramterar som gör att modellen get så bra resultat som möjligt.

ett exempel kan vara hur lång tid en bilresa tar om man jämför med beräknade restid mot den verkliga restiden som det faktiskt tar att åka för. Där kan man justera parametrar för att göra en bättre förutsägelse.

1. Vad är ett bias-variance trade off? varför är mer komplexa modeller inte alltid bättre?

svar: det handlar om balansen mellan en modell som är enkel och en modell som är anpassad för träningsdatan.

en enkel modell kan missa viktiga mönster i datan man har, en komplicerad modell kan lära sig detaljer som inte fungerar lika bra på en ny data, det kallas för överanpassning.

Man vill istället kunna få tag på en modell som kan lära sig utav träningsdatan och som fungera bra på ny data som man inte har sett tidigare.

1. Några vanligt förekommande modeller för regressionsproblem är enligt nedan. Förklara översiktlig hur de respektive modell fungerar. Läs även igenom respektive modells dokumenation, notera att du inte behöver förstå alla detaljer från dokumentationen men det är bra att ha läst igenom den.

a) Linjär regression.
svar: Den försöker att hitta en samband mellan olika egenskaper och värdet som man vill förutspå. Exempel på detta kan användas för att uppskatta ett pris på ett fordon utifrån ålder, och körsträcka.

b) Ridge Regression

svar: är en variant av linjär regression som begränsar modellens effecienter. Det kan hjälpa modellen att undvika att den överanpassas när det redan finns många egenskaper som påverkar resultatet.

c) Lasso Regression

svar: är väldigt lik Ridge regression, men kan ändra koefficienter till noll. Och kan leda till att modellen minskar betydelsen av mindre användbara egenskaper.

d) Elastic Net

svar: den kombinerar Ridge och Lasso. Men den kan både begränsa koefficienterna och göra vissa av de till noll.

e) Support Vector machines

svar: Den försöker att hitta en funktion som gör bra förutsägelser samtidigt som den håller modellens fel inom vissa gränser. Den kan användas för både linjära och mer komplicerade samband i modellen.

f) Beslutsträd

svar: Ett beslutträd som delar upp datan i olika grupper genom att ställa frågor om egenskaperna och sedan använder grupperna för att förutsäga ett numerisk värde. Ett för djupt träd kan däremot bli överanpassat.

g) Ensemble learning

VotingRegressor kombinerar förusägelser från flera olika modeller, genom att exempelvis: beräkna deras medelvärde.

h) Random Forest

svar: Består av många beslutsträd som tränas med olika urval av data och egenskaper som den har. Resultat från träden kan kombineras för att göra en gemensam förutsägelse, och kan ge bättre resultat än att använda ett enda beslutsträd.

1. Vad menas med white box modeller eller black box modeller?

svar: White box modeller är en modell som är lättare att förstå kring hur den kommer fram till sina resultat. Linjär regression är ett bra exempel från detta, eftersom man kan koeffecienterna och ser hur olika egenskaper påverkar förutsägelsen.

En black box modell är svårare att förstå i detaljer. Eftersom man kan få fram ett resultat utan att ha en förklaring kring hur modellen kom fram till svaret. Komplicerade neurala nätverk är ett exempel.

1. Vad är skillnaden mellan bagging och pasting?

svar: Bagging och Pasting är metoder som används på flera modeller som man skapar. Det som skiljer sig mellan de är att bagging tillåter att samma data väljer sig flera gånger  medans pasting väljer varje data bara en gång.

Resonemangsfrågor

1. Förklara hur man kan tolka figur 3.1 på sidan 113.

svar: Figur 3.1 visar hur den linjära regressionsmodellen går att använda för att beräkna inkomsten utifrån ålder.

X och Y värdet visar de faktiska värderna, medans den blå linjen visar det som modellen beräknar. De röda linjerna visar skillnaden mellan det som modellen visar, och det värdet som är faktiska.

1. Förklara hur man kan tolka figur 3.13 på sidan 140. Hur hänger den ihop med figur 3.14 på sidan 141?

svar: Figuren visar ett beslutsträd som delar upp datan på X1 och X2, och sedan gör modellen en beräkning på de sanna värden som visas längst ner i bilden. Om man jämför med Figur 3.14, så visar de samma besluträd, fast med olika färger. Dessa färgen som syns på bilden. Visar värden som modellen har delats upp beräknat på de olika områderna i beslutsträdet på tabellen.

1. vi har lärt oss utvärderingsmåtten RMSE, MSE OCH MAE. Ett annat utvärderingsmått är det som benämns för determinationskoefficienten eller r2. Förklara vad det är för mått.

svar: Kortfattat: RMSE,MSE och MAE används för att mätta det som datan förutspår resultatet. ju lägre värde, desto bättre är modellen på att visa resultat på datan korrekt.

R2 visar hur bra en bra modellen kan förklars på variationerna man får på datan. Ett värde som är nära 1 innebär att modellen förklarar en stor del av variationerna som man får. Medans ett värde som ligger på -0, innebär att den förklaras på ett mindre sätt. Är värdet negativt, så presterar modellen sämre än vad en enkel modell ger i motsvarande värde.
