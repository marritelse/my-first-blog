def hi(name):
    print('Hi '+name)
    if name=='Marrit':
        print('Hi Marrit!')

#hi(input('Wat is je naam? '))


def printlijst():
    namen = input('Welke namen moeten op de lijst? ')
    print(namen)
    namenlijst = []
    for naam in namen.split(','):
        naam = naam.strip()
        if naam.startswith('A'):
            namenlijst.append(naam)
        else:
            print('Naam '+naam+' begint niet met een A')
    
    #namenlijst = [naam.strip() for naam in namen.split(',') if naam.startswith('A')]
    #namenlijst = map(hi, namen.split(','))
    print(namenlijst)
    namenlijst.append('Menzo')
    print('Menzo is toegevoegd aan de lijst:')
    print(namenlijst)
    

printlijst()