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
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
