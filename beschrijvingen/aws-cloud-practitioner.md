# Global Infrastructure Key Terms
Hier zijn de alle Key Terms te vinden die horen bij Global Infrastructure.

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