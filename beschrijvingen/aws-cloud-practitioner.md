# AWS Cloud Practitioner Key Terms
Hier zijn de alle Key Terms te vinden die horen bij AWS Cloud Practitioner.

## AWSR
### AWS Regions
een fysieke locatie ergens op deze wereld, waar meerdere AZ's zich bevinden

## AZ 
### Availability Zones
een Az bestaat uit één of meerdere datacenters, elk met z'n eigen redundant energie voorziening, netwerk en verbindingen. Gehuisvest in gescheiden faciliteiten.

## Edge
### Edge Locations
dit zijn CDN (content delivery network) eindpunten voor AWS CloudFront

## Datacenter
ook wel aangeduid onder de Nederlandse naam rekencentrum, is een faciliteit waar bedrijfskritische ICT-apparatuur (bijvoorbeeld servers) kan worden ondergebracht. Een datacenter is uitgerust met diverse voorzieningen, waaronder klimaatbeheersing door middel van airconditioning, geavanceerde automatische brandblussystemen en back-up stroomvoorzieningen. Daarnaast bevat een datacenter doorgaans verbindingen met het internet en is het voorzien van fysieke veiligheidsmaatregelen. In verband met het bedrijfskritische karakter van de apparatuur in een datacenter, zijn de voorzieningen doorgaans redundant uitgevoerd.

## Cloudfront
AWS CloudFront is een CDN service specifiek gebouwd voor high performance, security en developer gemak.

## Redundant
Technische systemen kunnen zowel op component- als systeemniveau redundant worden uitgevoerd. Dit houdt in dat bepaalde onderdelen (onder regie van een speciaal algoritme) dubbel, of nog vaker, aanwezig zijn, zodat het geheel goed blijft functioneren wanneer een onderdeel uitvalt. Voorbeelden zijn: redundant array of independent disks (RAID) en Cluster Computing.

## LowLatency
### Low Latency
dit beschrijft een computernetwerk dat is geoptimaliseerd om een zeer grote hoeveelheid databerichten met minimale vertraging (latency) te verwerken. Deze netwerken zijn ontworpen om operaties te ondersteunen die bijna realtime toegang tot snel veranderende gegevens vereisen.

## Instance
Instances in AWS zijn in feite virtuele omgevingen. Deze virtuele omgevingen zijn geïsoleerd van het onderliggende basis-OS. Het is een on-demand service, d.w.z. een gebruiker kan de virtuele server(s) op uurbasis huren en zijn applicaties erop implementeren.

##### Soorten instancesa in AWS

Amazon biedt een breed scala aan instances voor verschillende gebruiksscenario's. Je kan degene kiezen die het beste bij je past. Laten we eens kijken naar verschillende soorten instances die je zullen helpen bij het selecteren van je perfecte match.

- **Instanties voor algemeen gebruik**  
Het is het meest gebruikte instance type. Het wordt voornamelijk gebruikt voor webservers en actieve implementatieomgevingen voor mobiele of gaming-applicaties. Het is perfect als je een nieuweling bent. Voorbeelden voor algemene doeleinden zijn: A1, M5, M5a, M4, T3, T3a, T2.

- ***Voor computer geoptimaliseerde instanties**  
Voor computer geoptimaliseerde instance typen zijn perfect wanneer je prioriteit moet geven aan onbewerkte rekenkracht, zoals gamingservers, wetenschappelijke modellering, krachtige webservers en mediatranscodering. Ze zijn sneller maar duurder (kosten gebaseerd op geheugen, CPU, instantieopslag, netwerk en EBS-bandbreedte). Compute Optimized-instance omvatten - C5, C5n, C4.

- **Voor geheugen geoptimaliseerde instanties**  
Deze instances zijn ideaal voor geheugengevoelige toepassingen, zoals realtime analyse van big data, krachtige databases, enz. Voor geheugen geoptimaliseerde instances omvatten: R5, R5a, R4, X1e, X1, Z1d, High Memory.

- **Versnelde computerinstanties**  
Versnelde (accelerated) computerinstances gebruiken afzonderlijke grafische verwerkingseenheden of veldprogrammeerbare poortarrays voor grafisch gevoelige berekeningen. Accelerated Computing-instances omvatten - P3, P2, G3, F1.

- **Voor opslag geoptimaliseerde instanties**  
Dit soort instances bieden hoge sequentiële lees-schrijfbewerkingen voor grote gegevenssets. Deze instanties worden gebruikt wanneer een gebruiker hoge SSD-opslag nodig heeft. Voor opslag geoptimaliseerde instanties omvatten - I3, I3en, D2, H1.

## EC2
Amazon Elastic Compute Cloud (Amazon EC2) biedt schaalbare rekencapaciteit in de Amazon Web Services (AWS) Cloud. Door Amazon EC2 te gebruiken, hoef je niet vooraf in hardware te investeren, zodat je applicaties sneller kunt ontwikkelen en implementeren. Je kunt Amazon EC2 gebruiken om zo veel of zo weinig virtuele servers te starten als je nodig hebt, beveiliging en netwerken te configureren en opslag te beheren. Met Amazon EC2 kunt je omhoog of omlaag schalen om veranderingen in vereisten of pieken in populariteit op te vangen, waardoor je minder verkeer hoeft te voorspellen.

## Elastic-IP
Een Elastic IP-adres is een gereserveerd openbaar IP-adres dat je kan toewijzen aan een EC2-instance in een bepaalde regio, totdat je ervoor kiest om het vrij te geven. 

Wanneer je een Elastic IP-adres koppelt aan een EC2-instance, vervangt dit het standaard openbare IP-adres. Als er vanuit jouw opstartinstellingen een externe hostnaam aan de instance is toegewezen, zal deze ook deze hostnaam vervangen; anders wordt er een voor de instance gemaakt. Het Elastic IP-adres blijft bestaan ondanks door de gebeurtenissen die er normaal gesproken voor zorgen dat het adres wordt gewijzigd, zoals het stoppen of opnieuw starten van de instantie.

## UPS
Noodstroomvoeding (UPS) is de voeding van een elektrisch netwerk, die in bedrijf komt zodra de gebruikelijke primaire voeding (bijvoorbeeld netspanning van het elektriciteitsbedrijf) uitvalt.  
bron: https://nl.wikipedia.org/wiki/Noodstroomvoeding

## Backup
Een goed Nederlands woord voor back-up is: reservekopie. Dat is dan ook precies wat een back-up is, een reservekopie van alle belangrijke bestanden die op de computer/server staan. Een kopie waarmee kan worden voorkomen dat er niets verloren gaat wanneer er onverhoopt iets mis mocht gaan. 

## Tier-1
Onder een Tier 1-netwerk verstaat men een IP-netwerk (van een internet service provider), dat uitsluitend via peering met de rest van het internet gekoppeld is. Anders gezegd, een provider die aan geen enkele andere provider geld betaalt voor IP-transit.

Een kenmerk van vrijwel alle Tier 1-providers is dat ze zowel in Noord-Amerika als in Europa uitgebreide netwerken beheren en exploiteren. 

## Data-Compliance
Datacompliance is de praktijk om ervoor te zorgen dat organisaties de voorschriften volgen om ervoor te zorgen dat de gevoelige digitale activa (gegevens) die ze bezitten, worden georganiseerd, opgeslagen en beheerd zodat ze worden beschermd tegen verlies, corruptie, diefstal en misbruik.

Deze voorschriften beschrijven welke gegevens moeten worden beschermd, welke processen acceptabel zijn en wat de sancties zijn als de regels niet worden nageleefd.

## AMI
Een AMI (Amazon Machine Interface) levert de informatie die nodig is om een instance te starten. Je moet een AMI opgeven wanneer je een instance start. U kunt meerdere instances starten vanuit één AMI wanneer je meerdere instances met dezelfde configuratie nodig heeft. Je kunt verschillende AMI's gebruiken om instances te starten wanneer je instances met verschillende configuraties nodig hebt.

Een AMI omvat het volgende:  
- Een of meer Amazon EBS (Amazon Elastic Block Store)-snapshots, of, bijvoorbeeld door e-store ondersteunende AMI's, een sjabloon voor het hoofdvolume van de instance (bijvoorbeeld een besturingssysteem, een toepassingsserver en toepassingen).  
- Startrechten die bepalen welke AWS-accounts de AMI kunnen gebruiken om instances te starten.  
- Een 'block device mapping' die de volumes specificeert die aan de instance moeten worden gekoppeld wanneer deze wordt gestart.

## Workload
Bij informatica is een werkbelasting (workload) meestal elk programma of elke toepassing die op de computer wordt uitgevoerd. Een workload kan een eenvoudige wekker- of contact-app zijn die op een smartphone draait, of een complexe bedrijfsapplicatie die wordt gehost op een of meer servers met duizenden client- (gebruikers)systemen die zijn verbonden en communiceren met de applicatieservers via een uitgebreid netwerk. Tegenwoordig worden de termen werklast, applicatie, software en programma door elkaar gebruikt.

Workload kan ook verwijzen naar de hoeveelheid werk (of belasting) die software oplegt aan de onderliggende computerbronnen. In grote lijnen is de werkbelasting van een applicatie gerelateerd aan de hoeveelheid tijd en computerbronnen die nodig zijn om een ​​specifieke taak uit te voeren of een output te produceren uit de geleverde input. Een lichte werklast bereikt de beoogde taken of prestatiedoelen met relatief weinig computerbronnen, zoals processors, CPU (central processing unit) klokcycli, opslag I/O (input/output) enzovoort. Een zware werklast vereist aanzienlijke hoeveelheden computerbronnen.

De taken van een werkbelasting variëren sterk, afhankelijk van de complexiteit en het beoogde doel van de toepassing. Een webservertoepassing kan bijvoorbeeld de belasting meten aan de hand van het aantal webpagina's dat de server per seconde levert, terwijl andere toepassingen de belasting kunnen meten aan de hand van het aantal transacties dat per seconde wordt uitgevoerd met een specifiek aantal gelijktijdige netwerkgebruikers. Gestandaardiseerde statistieken die worden gebruikt om de prestaties of belasting van een applicatie te meten en erover te rapporteren, worden gezamenlijk benchmarks genoemd.

## Local-Zones
AWS Local Zones plaatsen rekenkracht, opslag, database en andere geselecteerde AWS-services dichter bij de eindgebruikers.

Met AWS Local Zones kun je eenvoudig veeleisende applicaties uitvoeren die een milliseconde latency voor je eindgebruikers vereisen.

Elke AWS Local Zone-locatie is een uitbreiding van een AWS-regio waar je jouw latency gevoelige applicaties kunt uitvoeren met behulp van AWS-services zoals Amazon Elastic Compute Cloud, Amazon Virtual Private Cloud, Amazon Elastic Block Store, Amazon File Storage en Amazon Elastic Load Balancing in geografische nabijheid van je eindgebruikers.

AWS Local Zones bieden een veilige verbinding met hoge bandbreedte tussen lokale workloads en die in de AWS-regio, zodat je naadloos verbinding kunt maken met het volledige scala aan services in de regio via dezelfde API's en toolsets.

## AWS-Wavelength
Met AWS Wavelength kunnen ontwikkelaars applicaties bouwen die een milliseconde latency leveren aan mobiele apparaten en eindgebruikers.

AWS-ontwikkelaars kunnen hun applicaties implementeren in Wavelength Zones, AWS-infrastructuurimplementaties die AWS-computing- en opslagservices inbedden in de datacenters van de telecommunicatieproviders aan de rand van de 5G-netwerken, en naadloos toegang krijgen tot de breedte van AWS-services in de regio.

AWS Wavelength brengt AWS-services naar de rand van het 5G-netwerk en minimaliseert de latentie om vanaf een mobiel apparaat verbinding te maken met een applicatie.

## AWS-Outposts
AWS Outposts brengen native AWS-services, infrastructuur en operationele modellen naar vrijwel elk datacenter, co-locatieruimte of on-premises faciliteit.

U kunt dezelfde AWS API's, tools en infrastructuur gebruiken voor zowel on-premises als de AWS-cloud om een echt consistente hybride ervaring te bieden.

AWS Outposts is ontworpen voor verbonden omgevingen en kan worden gebruikt om workloads te ondersteunen die on-premises moeten blijven vanwege lage latentie of lokale gegevensverwerkingsbehoeften. 

## TCO
Total Cost of Ownership (TCO) heet ook wel life cycle cost analysis of levensduurcyclus. Niet alleen de aanschafkosten maar de gehele economische levensduur wordt berekend.  

De Total Cost of Ownership (de levensduurcyclus) is het totaalbedrag aan kosten voor de aanschaf en het bezit van een product of dienst gedurende de hele levenscyclus/gebruikscyclus. Behalve de aanschafprijs reken je alle kosten mee: vanaf het moment van aankoop tot het moment dat je er afstand van doet. Zo breng je de kosten van zakendoen met een bepaalde leverancier systematisch in kaart. Vervolgens kijk je niet alleen naar kostenreductie bij die leverancier, maar bekijk je ook wat je binnen je eigen organisatie kunt doen om kosten te besparen. TCO is een onderdeel van cost management.

Kosten die onderdeel zijn van TCO zijn bijvoorbeeld:
- Onderhoudskosten
- Reparatiekosten
- Afschrijvingen
- Verzekeringen
- Belastingen
- Financieringskosten
- Kosten voor training en scholing
- Personeelskosten
- Distributiekosten
- Voorraadkosten
- Etc.

## Capex
CAPEX is een afkorting van Capital expenditures oftewel investeringsuitgaven.  
Dit zijn uitgaven die pas in latere perioden als last worden opgeschreven. Een voorbeeld is de aankoop van een computer, waar de entiteit 5 jaar plezier van heeft. De uitgave aan de computer wordt in 5 jaar tijd ten laste van het resultaat gebracht onder aftrek van de veronderstelde restwaarde na 5 jaar. De jaarlijkse last heet de afschrijving.

## Opex
OPEX is een afkorting van Operational expenses oftewel operationele kosten. Dit zijn alle kosten die voortvloeien uit de bedrijfsactiviteiten, bijvoorbeeld arbeidskosten.  
Operating expenses zijn terugkerende kosten voor een product, systeem of onderneming.

**Verschil OPEX en CAPEX**  
De tegenhanger van OPEX is CAPEX, dit zijn investeringskosten.

Als je een printer als voorbeeld neemt dan valt de aanschaf ervan onder CAPEX en de jaarlijkse kosten voor papier en inkt onder OPEX.

Video over Opex: https://youtu.be/HluLXhmCP1g

## Encryptie
Binnen de cryptografie staat encryptie of versleuteling voor het omzetten van een bericht als leesbare tekst, de klare tekst, naar de versleutelde tekst, het geheimschrift, ook wel als cijfertekst aangeduid. Dit versleutelen is al een zeer oud gebruik. Het Caesarcijfer was bijvoorbeeld een geheimschrift dat al door Julius Caesar werd gebruikt. Een versleuteling die met de hand kan worden uitgevoerd, noemt men een handcijfer; maar tegenwoordig gebeurt het versleutelen en ontsleutelen meestal met behulp van een computer. De cijfertekst kan nadien weer worden ontsleuteld, zodat men de originele klare tekst weer terugkrijgt. Dit proces wordt decryptie genoemd. Een methode van encryptie wordt wel een cijfer genoemd.

Een van de bedoelingen van cryptografie is dat gegevens veilig tussen twee personen kunnen worden uitgewisseld over een onveilig communicatiekanaal, dat wil zeggen een communicatiekanaal waartoe ook derden toegang kunnen hebben, zoals het internet. De versleuteling zorgt er dan voor dat deze derden de gegevens niet kunnen lezen. Dit gebeurt meestal door het gebruik van sleutels. Wat precies een sleutel vormt verschilt per algoritme, maar meestal is een sleutel een reeks van tientallen of honderden cijfers en letters. Het doel van het cryptografische algoritme is ervoor te zorgen dat alleen de personen met de juiste sleutel de cijfertekst weer kunnen ontsleutelen. Het versleutelen en ontsleutelen kan met de huidige elektronica zo snel, dat het bijvoorbeeld mogelijk is een telefoongesprek te versleutelen zonder dat het opgemerkt wordt. De sleutel om een klare tekst te versleutelen, de codeersleutel, en de sleutel om de verkregen cijfertekst te ontsleutelen, de decodeersleutel, verschillen meestal van elkaar, maar zijn wel uit elkaar te berekenen. 

Zo had ik vroeger, samen met mijn broertje, een sjabloon wat wij over een geschreven tekst konden leggen. Dan kwam naar voren wat wij elkaar te vertellen hadden.  

## StorageTypes
AWS kent drie types Cloud Storage. Hieronder worden de drie verder uitgewerkt.

### ObjectStorage
Een object is een bestand plus metagegevens en een objectarchief is een verzameling objecten. Elk object heeft een unieke ID en je gebruikt dit ID om jouw objecten in je archief te vinden.

Hoewel object-ID's soms op bestandspaden lijken, zijn objectarchieven fundamenteel anders dan bestandsopslag. Objectopslagplaatsen bewaren gegevens op een manier die ze veel meer ruimte geeft om te schalen.

### BlockStorage
Block storage systemen worden gebruikt om databases te hosten, willekeurige lees-/schrijfbewerkingen te ondersteunen en systeembestanden van de draaiende virtuele machines te bewaren. Gegevens worden opgeslagen in volumes en blokken, waar bestanden worden opgesplitst in blokken van gelijke grootte. Elk blok heeft zijn eigen adres, maar in tegenstelling tot objecten hebben ze geen metadata. Bij het opslaan van grote hoeveelheden gegevens worden bestanden opgesplitst in kleinere brokken van een vaste grootte, de "blokken", die worden verdeeld over de opslagknooppunten. Dit ondersteunt ook de volume-IO-prestaties.

### FileStorage
Bestandsopslag in de cloud is een methode voor het opslaan van gegevens in de cloud die servers en applicaties toegang geeft tot gegevens via gedeelde bestandssystemen.

## API
Een application programming interface (API) is een verzameling definities op basis waarvan een computerprogramma kan communiceren met een ander programma of onderdeel (meestal in de vorm van bibliotheken).  Vaak vormen API's de scheiding tussen verschillende lagen van abstractie, zodat applicaties op een hoog niveau van abstractie kunnen werken en het minder abstracte werk uitbesteden aan andere programma's. Hierdoor hoeft bijvoorbeeld een tekenprogramma niet te weten hoe het de printer moet aansturen, maar roept het daarvoor een gespecialiseerd stuk software aan in een bibliotheek, via een afdruk-API.  
Bekende webservice API's zijn:  
- SOAP API  
- REST API  

### SOAP
SOAP (Simple Object Access Protocol) is een koppeling, waarbij je alle regels voor de koppeling strikt definieert. Hierdoor wordt er structuur aangebracht in de koppeling, waardoor het overzicht en de controle bewaard blijft. Door al deze regels is een SOAP koppeling zwaarder dan een REST koppeling en kan het technisch gezien een uitdaging zijn om de koppeling uit te lezen en tot stand te brengen.  

### REST
Bij een REST (Representational State Transfer) koppeling wordt er minder structuur en regels in de koppeling aangebracht. De REST koppeling is om deze reden een stuk lichter dan de SOAP koppeling. Dit zorgt er over het algemeen voor dat deze koppeling sneller is.  

## StorageClasses
Er zijn in totaal zes Storage Classes bij AWS. Zie onderstaande afbeelding:  
![Storage Classes](../00_includes/storage-classes.png)  

### S3-Standard
![S3 Standard](../00_includes/s3-standard.png)  

### S3 Intelligent Tiering
![S3 Intelligent Tiering](../00_includes/s3-intelligent-tiering.png)  

### S3 Standard Infrequent Access
![S3 Standard Infrequent Access](../00_includes/s3-standard-ia.png)  

### S3 One Zone-Infrequent Access
![S3 One Zone-Infrequent Access](../00_includes/s3-one-zone-ia.png)  

### S3 Glacier
![S3 Glacier](../00_includes/s3-glacier.png)  

### S3 Glacier Deep Archive
![S3 Glacier Deep Archive](../00_includes/s3-glacier-deep-archive.png)  

Voor de AWS S3 Storage Classes heb ik deze infographic gebruikt: [S3 Storage Classes](../00_includes/Amazon_S3_StorageClasses_Infographic_2020.pdf)  