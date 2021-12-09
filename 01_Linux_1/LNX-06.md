# File Permissions
Elk bestand in Linux heeft een set van rechten. Dit kunnen lees, schrijf of executie rechten zijn (read, write, execute: rwx).  
Daarnaast zijn er nog drie entiteiten die rechten hebben: de eigenaar van het bestand, de groep en alle anderen. De gebruiker root heeft geen rechten nodig voor rwx.

## Key-terms
chmod - commando om rechten aan te passen  
chown - commando om de eigenaar of groep aan te passen

## Opdracht
- Create a text file.
- Make a long listing to view the file’s permissions. Who is the file’s owner and group? What kind of permissions does the file have?
- Make the file executable by adding the execute permission (x).
- Remove the read and write permissions (rw) from the file for the group and everyone else, but not for the owner. Can you still read it?
- Change the owner of the file to a different user. If everything went well, you shouldn’t be able to read the file unless you assume root privileges with ‘sudo’.
Change the group ownership of the file to a different group.

### Gebruikte bronnen
Uitleg chown: https://manpages.ubuntu.com/manpages/trusty/man1/chown.1.html  
Uitleg chmod: https://help.ubuntu.com/community/FilePermissions

### Ervaren problemen
Geen probleem

### Resultaat
- Ik heb een tekst bestand aangemaakt m.b.v. Nano  
- Daarna heb ik de lijst van bestandrechten opgevraagd, eigenaar en groep  
- Ik heb het bestand executable gemaakt en gecontroleerd of het is aangepast  
- Permissies rw verwijderd voor de group en other en gecontroleerd  
- Gecontroleerd of ik de inhoud nog steeds kan zien  
- De eigenaar veranderd van het tekst bestand (note to self: wel sudo gebruiken!). Daar gecontroleerd of er een nieuwe eigenaar is. Gekeken of ik (gebruiker: henk) het bestand kan inzien. Dat kan ik niet.  
- Daarna gekeken of ik m.b.v. het commando sudo wel kan kijken. Dat lukt.  
- M.b.v. commando groups gekeken welke groepen ik tot mijn beschikking heb.  
- De group adm wordt eigenaar van het tekst bestand. En ik controleer of deze groep de nieuwe eigenaar is.  

Zie de afbeeldingen voor de resultaten:  
![lnx06](../00_includes/LNX-06a.png)  

![lnx06](../00_includes/LNX-06b.png)  