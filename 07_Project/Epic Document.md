# Epic Document

## Inhoud
- [Wat zijn de eisen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#wat-zijn-de-eisen-epic---01)
- [Een duidelijk overzicht van de aannames](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-aannames-epic---02)
- [Een duidelijk overzicht van de Cloud Infrastructuur](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-cloud-infrastructuur-epic---03)
- [Klant wil een veilig netwerk deployen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-veilig-netwerk-deployen-epic---04)
- [Klant wil een werkende webserver deployen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-werkende-webserver-deployen-epic---05)
- [Klant wil een werkende management server deployen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-werkende-management-server-deployen-epic---06)
- [Klant wil opslagoplossing voor bootstrapscript(s)](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-opslagoplossing-voor-bootstrapscripts-epic---07)
- [Klant wil alle data versleuteld hebben](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-alle-data-versleuteld-hebben-epic---08)
- [Klant wil iedere dag een backup, met bewaartermijn van 7 dagen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-iedere-dag-een-backup-met-bewaartermijn-van-7-dagen-epic---09)
- [Klant wil weten hoe hij/zij de applicatie kan gebruiken](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-weten-hoe-hijzij-de-applicatie-kan-gebruiken-epic---10)
- [Klant wil de MVP kunnen deployen om te testen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-de-mvp-kunnen-deployen-om-te-testen-epic---11)

## Wat zijn de eisen (Epic - 01)
| Item                | Opmerking                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | Exploratie                                                                                                                                                                                                   |
| Omschrijving        | Je hebt al heel wat informatie gekregen. Mogelijk zijn er vragen die geen van de stakeholders heeft kunnen beantwoorden. Je team moet een overzicht kunnen produceren van de aannames die je daardoor maakt. |
| Doel                | Een puntsgewijze overzicht van alle eisen                                                                                                                                                                    |
| Team problem        | Projectdocument is op een aantal punten niet duidelijk                                                                                                                                                       |
| Team value          | A.d.h.v. het vragen document duidelijkheid krijgen over de eisen                                                                                                                                             |
| Aannames            | De product Owner heeft antwoord op alle vragen                                                                                                                                                               |
| Doen we niet        | Alvast antwoorden invullen bij de vragen                                                                                                                                                                     |
| Acceptatie criteria | De Product Owner heeft alle vragen naar onze tevredenheid beantwoord                                                                                                                                         |

### Vragen document met de antwoorden
Wij hebben meerdere gesprekken gehad met de Product Owner. In het document [Project Cloud6.Sentia1](https://docs.google.com/document/d/1pNPWIce4kDnR9kopbH4t7jD9nX6LFySnBpsTfaWT_r4/edit#heading=h.higkk7mphvwd) staan alle vragen inclusief de antwoorden die wij hebben gekregen, van het gesprek van 10 februari jl. De besluitenlijst is tot stand gekomen aan de hand van de antwoorden en toevoegingen van de Product Owner.

### Opsomming van de Eisen en Besluiten
| Eisen                                                                  |
| :--------------------------------------------------------------------- |
| VM disks worden ge-encrypt                                             |
| Gebruik CDK/Python                                                     |
| Webserver: dagelijkse backup (7 dagen behouden)                        |
| Webserver: extern toegankelijk voor publiek via HTTP/HTTPS             |
| Webserver: geautomatiseerd geïnstalleerd                               |
| Admin/Management server: bereikbaar via Public IP                      |
| Admin/Management server: alleen bereikbaar vanaf vertrouwde locaties   |
| Webserver alleen te bereiken vanaf Admin/Management Server via SSH/RDP |
| IP ranges: 10.10.10.0/24 en 10.20.20.0/24                              |
| Subnets: firewalls op subnet niveau                                    |

| Besluiten                                                                      |
| :----------------------------------------------------------------------------- |
| Webserver: Linux VM                                                            |
| Admin/Management server: Windows Server VM                                     |
| Lege Availablity Zone is voor de failover                                      |
| Trusted resources = AWS Team                                                   |
| Admin/Management server meenemen in de backup cyclus (1x per week/ 1 behouden) |
| testomgeving is separate omgeving. Parameterfile gebruiken!                    |
| Documentatie wordt geschreven voor een Engineer                                |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Een duidelijk overzicht van de aannames (Epic - 02)
| Item                | Opmerking                                                                                                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | Exploratie                                                                                                                                                                                                                                              |
| Omschrijving        | Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten                                      |
| Doel                | Een puntsgewijze overzicht van alle aannames                                                                                                                                                                                                            |
| Team problem        | Product Owner heeft, tijdens het eerste gesprek, bij een aantal vragen aangegeven dat van ons het antwoord/advies wordt verwacht. Er zijn meerdere gesprekken geweest met de Product Owner. Daardoor zijn alle aannames inmiddels omgezet in besluiten. |
| Team value          | Overzicht van de aannames per Epic                                                                                                                                                                                                                      |
| Aannames            | geen aannames                                                                                                                                                                                                                                           |
| Doen we niet        | Alles wat buiten de scope van het project document en PRD ligt                                                                                                                                                                                          |
| Acceptatie criteria | Als er bij de Epics aannames zijn benoemd of is aangegven dat ze er niet zijn                                                                                                                                                                           |

| Epic no.                                                                                                                                                                                                    | Aannames                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [01]([../07_Project/Epic01.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#wat-zijn-de-eisen-epic---01))                                             | geen aannames                                                  |
| [02]([../07_Project/Epic02.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-aannames-epic---02))                       | geen aannames                                                  |
| [03]([../07_Project/Epic03.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-cloud-infrastructuur-epic---03))           | Aanname: Project document is incompleet v.w.b. de AWS diensten |
| [04]([../07_Project/Epic04.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-veilig-netwerk-deployen-epic---04))                         | geen aannames                                                  |
| [05]([../07_Project/Epic05.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-werkende-webserver-deployen-epic---05))                     | geen aannames                                                  |
| [06]([../07_Project/Epic06.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-een-werkende-management-server-deployen-epic---06))             | geen aannames                                                  |
| [07]([../07_Project/Epic07.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-opslagoplossing-voor-bootstrapscripts-epic---07))               | geen aannames                                                  |
| [08]([../07_Project/Epic08.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-alle-data-versleuteld-hebben-epic---08))                        | geen aannames                                                  |
| [09]([../07_Project/Epic09.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-iedere-dag-een-backup-met-bewaartermijn-van-7-dagen-epic---09)) | geen aannames                                                  |
| [10]([../07_Project/Epic10.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-weten-hoe-hijzij-de-applicatie-kan-gebruiken-epic---10))        | geen aannames                                                  |
| [11]([../07_Project/Epic11.md](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#klant-wil-de-mvp-kunnen-deployen-om-te-testen-epic---11))                 | geen aannames                                                  |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Een duidelijk overzicht van de Cloud Infrastructuur (Epic - 03)
| Item                | Opmerking                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | Exploratie                                                                                                                                                                                                         |
| Omschrijving        | Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten |
| Doel                | Een overzicht van alle diensten die gebruikt gaan worden.                                                                                                                                                          |
| Team problem        | Niet alle te gebruiken AWS diensten zijn benoemd in het Project Document                                                                                                                                           |
| Team value          | Overzicht van de AWS diensten die gebruikt gaan worden                                                                                                                                                             |
| Aannames            | Het Project document is incompleet v.w.b. de AWS diensten                                                                                                                                                          |
| Doen we niet        | Alle diensten en oplossingen die buiten AWS liggen en die **niet** beschreven zijn in de PRD                                                                                                                       |
| Acceptatie criteria | Overzicht van de te gebruiken AWS diensten                                                                                                                                                                         |

### Overzicht AWS diensten
![aws diensten](../00_includes/MVP%20v1.0%20AWS%20Services.drawio.png)  

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)

## Klant wil een veilig netwerk deployen (epic - 04)
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen. |
| Doel                | IaC-code voor het netwerk en alle onderdelen                                                                                                                                         |
| User problem        | Alleen trusted sources (IP Adressen) mogen de management server benaderen                                                                                                            |
| User value          | Afschermen van ongewenst verkeer naar de Admin/Management server                                                                                                                     |
| Aannames            | Trusted Sources is het AWS team                                                                                                                                                      |
| Doen we niet        | De rest van de wereld toegang geven tot de Admin/Management Server. HTTP/HTTPS toegang tot de Webserver is geoorloofd                                                                |
| Acceptatie criteria | Als bij test blijkt dat alleen het AWS Team toegang kan krijgen en al het andere verkeer niet                                                                                        |

![AWS Netwerk](../00_includes/MVP%20v1.0%20Network%20(AWS).drawio.png)    

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil een werkende webserver deployen (Epic - 05)
| Item                | Opmerking                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                      |
| Omschrijving        | De applicatie moet een webserver starten en deze beschikbaar maken voor algemeen publiek. |
| Doel                | IaC-code voor en webserver en alle benodigdheden                                          |
| User problem        | Er moet een webserver komen                                                               |
| User value          | Een webserver die te benaderen is van buitenaf, door het publiek                          |
| Aannames            | Webserver is een Linux server                                                             |
| Doen we niet        | Complete website bouwen, alleen wat in de opdracht staat                                  |
| Acceptatie criteria | Als de gemaakte webpagina zichtbaar is                                                    |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil een werkende management server deployen (epic - 06)
| Item                | Opmerking                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                 |
| Omschrijving        | De applicatie moet een management server starten en deze beschikbaar maken voor een beperkt publiek. |
| Doel                | IaC-code voor een management server met alle benodigdheden                                           |
| User problem        | Admin/Management server met beperkte toegang                                                         |
| User value          | Een Admin/Management server die een beperkte toegang kent                                            |
| Aannames            | Epic04 is een onderdeel van de oplossing, rest oplossen m.b.v. SG                                    |
| Doen we niet        | Firewall plaatsen voor de Admin/Management server                                                    |
| Acceptatie criteria | Als getest is dat de toegang beperkt is tot hoe wij het ingericht hebben                             |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil opslagoplossing voor bootstrapscript(s) (epic - 07)
| Item                | Opmerking                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                    |
| Omschrijving        | Er moet een locatie beschikbaar zijn waar bootstrap scripts beschikbaar worden. Deze script moeten niet publiekelijk toegankelijk zijn. |
| Doel                | IaC-code voor een opslagoplossing voor scripts                                                                                          |
| User problem        | SCripts die de klant wil gaan gebruiken moeten veilig opgeslagen worden                                                                 |
| User value          | Op eenvoudige wijze bij de scripts kunnen in een veilige omgeving                                                                       |
| Aannames            | S3 bucket wordt gebruikt met versioning en encryptie                                                                                    |
| Doen we niet        | Aannames doen over de mate van opvragingen uit de S3 bucket                                                                             |
| Acceptatie criteria | Als de S3 Bucket er is en niet publiekelijk te benaderen is                                                                             |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil alle data versleuteld hebben (epic - 08)
| Item                | Opmerking                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                                            |
| Omschrijving        | Er wordt veel gehecht aan de veiligheid van de data at rest en in motion. Alle data moet versleuteld zijn met een encryptie sleutel in het beheer van de klant. |
| Doel                | IaC-code voor versleuteling voorzieningen                                                                                                                       |
| User problem        | Data moet versleuteld worden, zowel in Rest als in Motion                                                                                                       |
| User value          | Als de data versleuteld is, is dat veiliger                                                                                                                     |
| Aannames            |                                                                                                                                                                 |
| Doen we niet        |                                                                                                                                                                 |
| Acceptatie criteria | Als de data versleuteld is en dit is getest                                                                                                                     |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil iedere dag een backup, met bewaartermijn van 7 dagen (Epic - 09)
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De klant wil graag dat er een backup beschikbaar is, mocht het nodig zijn om de servers terug te brengen naar een eerdere staat. (Zorg ervoor dat de Backup ook daadwerkelijk werkt) |
| Doel                | IaC-code voor backup voorzieningen                                                                                                                                                   |
| User problem        | Elke dag een backup van de webserver                                                                                                                                                 |
| User value          | Indien er iets fout gaat, kan het hersteld worden m.b.v. een backup van één dag oud                                                                                                  |
| Aannames            | Management server ook meenmenen in een backup structuur (1x per week, 1 behouden)                                                                                                    |
| Doen we niet        | Snapshots                                                                                                                                                                            |
| Acceptatie criteria | Als de backups zijn gedraaid en er zijn                                                                                                                                              |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil weten hoe hij/zij de applicatie kan gebruiken (Epic - 10)

| Item                | Opmerking                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                                         |
| Omschrijving        | Zorg dat de klant kan begrijpen hoe deze de applicatie kan gebruiken. Zorg dat het duidelijk is wat de klant moet configureren voor de deployment kan starten en welke argumenten het programma nodig heeft. |
| Doel                | Documentatie voor het gebruik van de applicatie                                                                                                                                                              |
| User problem        | Geen idee hoe het allemaal werkt                                                                                                                                                                             |
| User value          | Handleiding met hoe het allemaal werkt                                                                                                                                                                       |
| Aannames            | User weet niets                                                                                                                                                                                              |
| Doen we niet        | Cursus organiseren, videos maken                                                                                                                                                                             |
| Acceptatie criteria | Als de user in staat is om het zelf te deployen                                                                                                                                                              |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
## Klant wil de MVP kunnen deployen om te testen (Epic - 11)
| Item                | Opmerking                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                                                                   |
| Omschrijving        | De klant wilt zelf intern je architectuur testen voordat ze de code gaan gebruiken in productie. Zorg ervoor dat er configuratie beschikbaar is waarmee de klant een MVP kan deployen. |
| Doel                | Configuratie voor een MVP deployment                                                                                                                                                   |
| User problem        | User wil zelf testen op aparte omgeving                                                                                                                                                |
| User value          | User ziet dat het allemaal werkt in een test omgeving                                                                                                                                  |
| Aannames            | Wij maken gebruik van een environment file voor de parameters                                                                                                                          |
| Doen we niet        | test omgeving inrichten, testplan/scripts maken                                                                                                                                        |
| Acceptatie criteria | Als de user aangeeft dat het werkt in de test omngevings                                                                                                                               |

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Epic%20Document.md#inhoud)
