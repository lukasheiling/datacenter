# Network Manager

In den folgenden Einheiten sollen Sie ein Werkzeug entwickeln zur Planung und Dokumentation eines Computernetzwerkes.

Während der Entwicklung des Werkzeugs sollen Sie übliche Praktiken anwenden.

## Teil 1: die Aufgabenerfassung

Zuerst werden Sie sich mit dem Zusammentragen von Anforderungen für unser Netzwerktool beschäftigen.

```markdown
# User story <name>

short description

## Actors

Who is the actor and i which role?

## Input

Description of Input data.

## Internal State change

Internal state change description.

## Output

Output of process

## Errors

possible errors

```

Eine Beispiel Userstory könnte folgendermaßen aussehen.

```markdown
# User story add wall socket.

Add a network wall socket to the system

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Room number, Socket numbers, 

## Internal state change

The socket is persisted into the system

## Output 

Acknowledgement

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* already existent socket number
```

### Vorgehen

Erzeugen Sie einen Fork von dem Repository https://github.com/htlweiz/datacenter.git.

Erstellen Sie Ihre User-story im Verzeichnis `userstories`, in der Form des angegebenen Beispiels.

Immer wenn Sie eine User-story fertiggestellt haben, erzeugen Sie einen Pull-Request, damit ich Sie in den Hauptzweig aufnehmen kann.
