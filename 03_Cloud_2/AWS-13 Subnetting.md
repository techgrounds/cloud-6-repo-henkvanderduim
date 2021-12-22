# Subnetting
Een subnet, of subnetwerk, is een netwerk binnen een netwerk. Subnetten maken netwerken efficiënter. Door middel van subnetting kan netwerkverkeer een kortere afstand afleggen zonder onnodige routers te passeren om zijn bestemming te bereiken.  

![Subnet](../00_includes/subnet-diagram.png)  

Opbouw IP Subnet:  
![Subnet](../00_includes/AWS-13aa.jpg)

## Key-terms
Alle key-terms die betrekking hebben op AWS Cloud Practitioner, zijn te vinden in het document: [AWS-Cloud-Practitioner](../beschrijvingen/aws-cloud-practitioner.md)  
[Subnet](../beschrijvingen/aws-cloud-pratitioner.md#Subnet)  
[Public Subnet](../beschrijvingen/aws-cloud-practitioner.md#Public-Subnet)  
[Private Subnet](../beschrijvingen/aws-cloud-practitioner.md#Private-Subnet)  
[NAT Gateway](../beschrijvingen/aws-cloud-practitioner.md#NAT)  
[Internet Gateway](../beschrijvingen/aws-cloud-practitioner.md#Internet-Gateway)  
[CIDR](../beschrijvingen/aws-cloud-practitioner.md#CIDR)  
[LAN](../beschrijvingen/aws-cloud-practitioner.md#LAN)  
[Subnet Mask](../beschrijvingen/aws-cloud-practitioner.md#Subnet-Mask)  
[VLSM](../beschrijvingen/aws-cloud-practitioner.md#VLSM)  

## Opdracht
- Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
    - 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.
    - 1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).
    - 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).
- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.

### Gebruikte bronnen
- https://nl.wikipedia.org/wiki/Subnet  
- https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking  
- https://www.youtube.com/watch?v=ecCuyq-Wprc  
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-public-private-vpc.html  
- https://subnettingpractice.com/vlsm.html  

### Ervaren problemen
Geen probleem

### Resultaat
Ik heb er bewust voor gekozen om bij de eerste opdracht gebruik te maken van 'Sunny's Table'. Dit wordt uitgelegd in de Youtube video die bij de bronnen staat.  
Dit is Sunny's Table:  
![Sunny's Table](../00_includes/AWS-13a.png)  

Het aantal hosts verminder je met 2. Eén voor het Network ID en één voor de Broadcast ID. Dan houd je het aantal Usable Hosts over.

#### Opdracht 1
1 private subnet, niet van buitenaf benaderbaar en minimaal 15 hosts.

Uit Sunny's Table haal ik dan:  
Subnet | Hosts | Subnet Mask
:----- | :---- | :----------
1 | 256 | /24

Private IP adres: 10.0.0.0

Dan kom ik tot het volgende private subnet:  
Network ID | Broadcast ID  | Mask | Slash | Range | Wildcard
:--------- | :------------ | :--- | :---- | :---- | :-------
10.0.0.0 | 10.0.0.255 | 255.255.225.0 | /24 | 10.0.0.1 - 10.0.0.254 | 0.0.0.255

De architectuur is als volgt weergegeven:  
![architectuur](../00_includes/AWS-13b.png)  

#### Opdracht 2
1 private subnet, internet toegang via NAT Gateway en minimaal 30 hosts.

Uit Sunny's Table haal ik dan:  
Subnet | Hosts | Subnet Mask
:----- | :---- | :----------
1 | 256 | /24

Private IP adres: 10.0.0.0  
Public IP adres: EIP 18.195.114.13  
Voor de NAT Gateway wordt dat dan een Elastic IP adres (AWS)

Dan kom ik tot het volgende private subnet:  
Network ID | Broadcast ID  | Mask | Slash | Range | Wildcard
:--------- | :------------ | :--- | :---- | :---- | :-------
10.0.0.0 | 10.0.0.255 | 255.255.225.0 | /24 | 10.0.0.1 - 10.0.0.254 | 0.0.0.255

De architectuur van het private subnet en de NAT Gateway is als volgt weergegeven:  
![architectuur](../00_includes/AWS-13c.png)  

#### Opdracht 3
1 public subnet, Internet Gateway en minimaal 5 hosts.

Uit Sunny's Table haal ik dan:  
Subnet | Hosts | Subnet Mask
:----- | :---- | :----------
32 | 8 | /29

Public IP adres: 17.5.7.8

Dan kom ik op het volgende subnet:  
Network ID | Broadcast ID  | Mask | Slash | Range | Wildcard
:--------- | :------------ | :--- | :---- | :---- | :-------
10.0.0.0 | 10.0.0.255 | 255.255.225.0 | /24 | 10.0.0.1 - 10.0.0.254 | 0.0.0.255

De architectuur is als volgt weergegeven:  
![architectuur](../00_includes/AWS-13d.png)  