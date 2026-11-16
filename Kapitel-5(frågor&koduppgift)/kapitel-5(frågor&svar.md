Faktafrågor

1. vad menas med curse of dimensionality?

svar: Curse of dimensionality betyder att det blir svårare att arbeta med data när antalet egenskaper ökar. Det kan krävas på mer data och mer beräkningskraft för att modellen ska hitta tydliga mönster i datan. Vilken kan också leda till att det bli svårare för modellen att göra bra förutsägelser.

1. vad är dimensionsreducering och varför görs det?

svar: det är att man minskar antalet egenskaper i ett dataset. Men också att man behåller viktigt info. Det används för att göra datan enklare och minska tid på att beräkna och även förbättra resultatet av modellen.

1. Förklara översiktligt hur PCA fungerar, Använd figur 5.4 på sidan 224 i din förklaring.

svar: PCA fungerar genom att minska antalet på variablerna som finns i datan, men samtidigt se till att behålla mycket information som möjligt också.

på figur 5.4, så ser man hur PCA används för att projicera data från två till en dimension. Linjen C1 påpekar den riktning för att samla mycket variationer så möjligt av datan, medans C2 påpekar åt ett annat håll. I bilden så visar det punkterna på värdet och hur datan har fördelats när den projiceras på olika linjer. Med detta, så går datan att förenklas och göra den mer lättare att arbeta med

1. hur kan kernel PCA utvärderas?

svar: Det kan utvärderas genom att göra en undersökning på hur metoden lyckas fånga mönster i datan efter att man har gjort dimensionsreducering. Man kan träna en modell på datan som är reducerad och jämföra resultat med en annan modell som använder den ursprungliga datan.

Resonemangfrågor

1. Stina påstår att man i maskininlärning alltid vill ha modeller som genomför så bra prediktioner som möjligt. Kalle påstår att det inte riktigt stämmer eftersom tid också är en viktig aspekt. Både för själva modellträningen och för själva prediktionerna. Vad säger du?

svar: Jag tycker att både stina och kalle har rätt. Det är viktigt att att en modell ger bra förutsägelser. Men man måste ha koll på hur lång tid det kan ta för att modellen ska träna och hur snabb den ger resultat. En modell som är mer advancerad kan ta mycket mer längre tid men ger endast lite bättre resultat. Det är därför man bör hitta en bra balans mellan modellens prestanda, men också ha koll på tiden det tar för att få resultat.

1. Efter att vi genomfört en PCA, vad händer med tolkningen av variablerna?

svar: Efter att PCA har genomförts, så blir det svårt att tolka variablerna. Eftersom de gamla variablerna omvandlas till nya huvudkomponenter. Varje komponent består utav en kombination av de gamla variablerna som har använts. Men kan fortfarande göra en undersökning för att se vilka gamla variabler som har störst påverkan på komponenterna. Men resultatet blir inte lika enkelt att förstå i jämförelse med de variablerna som man hade tidigare. Det positiva är att man kan förminska antalet dimensioner men samtidigt behålla mycket utav infot från datan.
