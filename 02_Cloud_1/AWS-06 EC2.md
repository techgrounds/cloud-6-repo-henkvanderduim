# Elastic Compute Cloud (EC2)
EC2 is de service waarbinnen je een VM kunt draaien. Connectie met de VM maak je via internet. Als je een Linux VM hebt doe je dat middels SSH, als je een Windows VM hebt dan doe je dat via RDP

## Key-terms
Alle key-terms die betrekking hebben op AWS Cloud Practitioner, zijn te vinden in het document: [AWS-Cloud-Practitioner](../beschrijvingen/aws-cloud-practitioner.md)  
[EC2](../beschrijvingen/aws-cloud-practitioner.md#EC2)  
[SHH](../beschrijvingen/aws-cloud-practitioner.md#SSH)  
[RDP](../beschrijvingen/aws-cloud-practitioner.md#RDP)  
[AMI](../beschrijvinen/aws-cloud-practitioner.md#AMI)  
[EBS](../beschrijingen/aws-cloud-practitioner.md#EBS)  
[Firewall](../beschrijvingen/aws-cloud-practitioner.md#Firewall)  


## Opdracht
**Opdracht 1**  
- Start je sandbox en open de AWS console
- Ga naar het EC2 menu
- Launch een EC2 instance met de volgende voorwaarden:
    - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
    - Instance type: t2.micro
    - Default network, no preference for subnet
    - Termination protection: enabled
    - User data:
        - #!/bin/bash
        yum -y install httpd
        systemctl enable httpd
        systemctl start httpd
        echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
    - Root volume: general purpose SSD, Size: 8 GiB
    - New Security Group:
        - Name: Web server SG
        - Rules: Allow SSH, HTTP and HTTPS from anywhere
    - Key Pair: vockey (this can be downloaded from the sandbox lab environment)  

**Opdracht 2**  
- Wacht tot alle Status Checks uit de initialisatie fase zijn. Als je op de Status Checks tab klikt, zou je moeten zien dat de System reachability en de Instance reachability checks gedaan moeten zijn.  
- Vind de EC2 system logs. Controleer dat de HTTP Package is geïnstalleerd.

**Opdracht 3**  
- Stop je EC2 instance (kies NIET voor terminate).
- Verander het instance type in t2.small.
- Verander het EBS volume naar 10GiB.
- Start je EC2 instance.

**Opdracht 4**  
- Terminate je EC2 instance.  
Tip: je moet eerst de terminate protection uitzetten.

### Gebruikte bronnen
Naast de genoemde bronnen in het opdrachtdocument, heb ik nog de volgende gebruikt:  
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html  
https://aws.amazon.com/premiumsupport/knowledge-center/ec2-not-auth-launch/  
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html  
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html  

### Ervaren problemen
Bij de launch van de EC2 instance krijg ik de melding dat ik niet de juiste rechten heb.
Ik heb dit verder uitgewerkt in het document: [Error-Message](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/02_Cloud_1/AWS-06%20Error%20Message.md)  

Casper heeft in Slack aangegeven dat hij het probleem heeft gefixt. En daarna kunnen wij gewoon de EC2 instance aanmaken.

### Resultaat  
**Opdracht 1**  
In het EC2 menu kies ik voor de Launch van een Instance:  
![EC2 Launch](../00_includes/AWS-06a.png)  

Na alles ingevuld te hebben is dit het resultaat:  
![ECS Instance](../00_includes/AWS-06b.png)  

De website:  
![website](../00_includes/AWS-06o.png)  

**Opdracht 2**  
Hier zijn de status checks:  
![Status Checks](../00_includes/AWS-06c.png)  

De controle van het HTTP Package:  
![HTTP Package](../00_includes/AWS-06d.png)  

**Opdracht 3**  
Stop de Instance:  
![Stop Instance](../00_includes/AWS-06e.png)

![Stpped Instance](../00_includes/AWS-06f.png)

Verander het instance type:  
![Instance](../00_includes/AWS-06g.png)

![t2small](../00_includes/AWS-06h.png)

Verander het EBS volume:  
![EBS](../00_includes/AWS-06i.png)

![EBS](../00_includes/AWS-06j.png)

Start de EC2 instance:  
[Start Instance](../00_includes/AWS-06k.png)  

**Opdracht 4**  
Termineer je EC2 Instance  
![Terminate](../00_includes/AWS-06l.png)

![Terminate](../00_includes/AWS-06m.png)

![Terminate](../00_includes/AWS-06n.png)
