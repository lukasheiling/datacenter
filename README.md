# Network manager

In den folgenden Einheiten sollen Sie ein Werkzeug entwickeln zur Planung und Dokumentation eines Computernetzwerkes.

Während der Entwicklung des Werkzeugs sollen Sie übliche Praktiken anwenden.

## Teil 1 die Aufgabenerfassung

Zuerst werden Sie sich mit dem Zusammentragen von Anforderungen für unser Netzwerktool beschäftigen.

```markdown
# Userstory <mame>

short description

## Actors

Who is the actor and i which role.

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
# Userstory add wall socket.

Add a network wall socket to the system

## Actors

* Person (Role: Admin)

## Input

Building, Floor, Roomnumber, Socket numbers, 

## Internal state change

The socket is persistet into the system

## Output 

Acknolegement

## Errors

* insufficient rights
* nonexistent building
* nonexistent floor
* nonexistent room 
* already existent socket number
```

### Vorgehen

Erzeugen Sie einen fork von dem repository `https://github.com/htlweiz/datacenter.git`.

Erstellen Sie Ihre userstory im Verzeichnis userstories, in der Form des angegebenen Beispiels.

Immer wenn Sie eine Userstory fertiggestellt haben, erzeugen Sie einen Merge-Request damit ich Sie in den Tree aufnehmen kann.
