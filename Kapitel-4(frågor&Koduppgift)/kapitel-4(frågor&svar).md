Kapitel 4-Klassificering.

1. Vad kännetecknar klassificeringsproblem? Ge några exempel på tillämpningsområden.

svar: Klassificering innebär att en modell försöker placera data i olika kategorier, ett exempel kan vara att en modell avgör om ett meddelande eller mejl är skräppost eller inte.

Det kan också användas för att upptäcka bedrägerier, komma ihåg bilder eller eventuellt avgöra hur stor sannolikhet en kund avslutar sin prenumeration.

1. Förklara hur OVR och OVO algoritmerna fungerar.

svar: OvR står för: (One vs rest) och det innebär att man tränar en klassificering för varje kategori man har på datan. Varje klassificerare försöker skilja sig ifrån varandra helt enkelt. Ett exempel kan vara att man har 3 olika hundraser. så tränas en modell för en hund, en katt och en fågel.

Ovo står för: (One vs one) och det innebär att man tränar en separat klassificering för varje par av kategorier man har. Har man 3 kategorier så behövs det tre klassificerare också: ett exempel kan vara: fågel mot katt, hund mot katt, eller fågel mot hund. Sedan bestämmer vilken kategori som vinner och skickar resultat.

OvO är väldigt användbart för vissa algoritmer när man behöver skilja mellan två kategorier i taget. Medans OvR fungerar om man har färre modeller om det finns flertal kategorier.

1. Förklara följande utvärderingsmått

a) Confusion matrix

svar: Confusion matrix visar hur många förutsägelser modellen har gjort rätt eller fel på datan för varje kategori. Den hjälper oss att se vilka kategorier modellen blandar ihop.

ett exempel på detta kan vara om modellen ska upptäcka spam mejl så kan confusion matrix visa hur många spam mejl som har hittats och hur många vanliga mejl har klassificerats som skräppost.

b) Accuracy

svar: Accuracy visar hur stor procentuell andel av alla förutsägelser blir korrekta. Om en modell klassificerar 100 biler som är i 90 fall korrekta, då får vi en accuracy på 90%

Måttet kan däremot vara missvisande om en kategori är vanligare än andra.

c) Precision visar hur stor andel av de fall som modellen klassficerar det faktiska värden som är positivt.

exempel: om modellen gör en markering på 20 mail som är klassificerade som skräppost. och 16 av dem är faktikst skräppost och inte vanliga mejl. Så ligger precisionen på 80%

d) Recall

svar: Recall visar hur stor andel av alla positiva fall som modellen har lyckats få tag på.

e) F1 score

F1 score kombinerar precision och recall till ett enda måttvärde. Det är väldigt användbart när man ska ha koll på både falska positva och falska negativa resultat.

Om F1 score är högt, så innebär det att både precision och recall är höga.

f) ROC kurva

svar: En ROC kurva visar sambandet mellan andelen fall som är korrekt identifierade och andelen fall som är falska positiva. Med andra ord: (true positive rate) och (false positive rate) vid olika beslut man får utifrån datan.

kurvan hjälper oss att se hur bra modellern är och skiljer mellan kategorierna.

1. Vad är precision recall trade off för något?

svar: Det innebär att det finns en avvägning mellan precision och recall.

Om man ändrar modellens beslutröskel, så kan man få en högre precision men lägre recall. eller så kan det också bli tvärtom. Får man en högre tröskel, så innebär det att modellen blir mer försiktig med att klassificera något som är positivt. Vilket betyder att antalet falska positiva minskar, men modellen kan göra misstag och missa flera fall som är positiva.

så det beror mestadels på vad modellen ska användas till för att avgöra balansen på vad som är bäst.

1. Förklara översikligt hur klassificeringsmodellerna fungerar.

a) Logisitc Regression

svar: Det används för att få fram sannolikheten att något tillhör en viss kategori. Som tex, när en kund kommer att säga upp medlemskap.

b) Support Vector Machine (SVM)

svar: SVM försöker hitta gränsen som skiljer de olika kategorier åt. Den försöker att skapa en stor marginal som är möjligt mellan kategorierna.

c) Decision tree classifier

svar: ett beslutträd som ställer frågor om datan ett steg i taget för att komma fram till en kategori som finns.

exempelvis: avgöra om ett samtal från utomlands kan vara spam. utifrån olika egenskaper.

d) en voting classifier

svar: en Voting classifer fungerar genom att kombinera resultat från flera klassificeringsmodeller. Sedan kan modellerna avgöra vilken kategori som är sant, eller kombinera andra sannolikheter som är förutspått.

e) Bagging Classifier

svar: en bagging classifier fungerar genom att man tränar på flera modeller på olika slumpmässiga urval av träningsdatan och kombinerar resultat på vad resultatet blir. Det gör att modellen blir mer stabiliserat.

f) Random forest Classifier

svar: En random forest består utav flera beslutsträd som arbetar tillsammans. Varje träd visar ett resultat och sedan kombineras det med andra modellerna för att bestämma det slutgiltiga kategorin.

g) Extra Trees Classifier

svar: Extra Trees classifier är nästan lika som random forest, men istället för att ett träd visar ett resultat i taget, så är den mer slumpmässig när träden byggs upp. Det gör att överanpassning minskar och ger ett bra resultat.

1. Vad innebär det att man kan titta på feature importance med hjälp av trädmodeller?

svar: När man tittar på feature importance, så visar den vilka egenskaper som har en större betydelse på vad modellen förutspår.

om man tränar en modell för att förutspå om en kund ska avsluta en prenumeration, så kan egenskapen av kundens förbrukandet av tjänsten eller antal klagomål vara viktiga.

Med random forest kan man undersöka vilka egenskaper som går att bidra för att modellen ska beslutas. Det hjälper oss till att få en bättre förståelse på datan och se vilka variabler som går att använda.

Resonemangsfrågor

1. I vilka fall kan man tänka sig att vilja ha en så hög precision som möjligt? I vilka fall kan det vara dåligt? Om vi tänker oss rättsväsendet där en slutgiltig dom kan leda till fängelse, vad kan vi då säga om precision-recall trade off?

Jag tycker att det beror mestadels på vad modellen ska användas i syfte. Är man ute efter en hög precision som möjligt, så vill man också se till att minska antalet falska positiva resultat. Ska man använda en modell för att upptäcka misstänkta samtal, så vill man undvika att oskyldiga personer pekas ut i onödan.

Recall är viktigt eftersom man vill hitta verkliga fall som möjligt, om man nu fokuserar endast på precision så kan modellen missa många relevanta fall.

När det handlar om rättsäkerhet och misstänksamma människor, så är det särskilt viktigt att undvika falska positiva resultat. Eftersom en felaktig bedömning kan leda till att man får allvarliga konsekvenser för något man inte har gjort. Därför bör man inte lits sig allt för mycket på modellens resultat. Utan mer att man gör en mänsklig gransking och bevisning av det.

1. Förklara hur man kan tolka figur 4.8 på sidan 175.

svar: utifrån bilden som figuren visas på. Så visar den hur man delar upp datan i två klasser med nollor och ettor med hjälp av logistisk regression. Klass nollor tillhör de lila punkterna, medans de gula punkterna tillhör klass ettor.

Färgerna på bakgrunderna visar också hur stor sannolikheten är att en färg punkt tillhör klass ettor. Ju ljusare färgen är på områden. Desto högre är värderna stämmer.  

1. På sidan 209 står det "på träningsdatan använder vi .fit_transform(), på valideringsdatan och testdatan använder vi endast .transform()." förklara logiken bakom detta.

svar: logiken bakom detta är att modellen ska lära sig hur datan omvandlas utifrån träningsdatan som man får utav. Sedan omvandlar man det på validering och test datan för att det processen ska behandlas likadant och undvika att informationen från testdatan ska påverka träningsmodellen. Vilket är därför man använder fit_transform på träningsdatan och transform() på validering och testdatan.
