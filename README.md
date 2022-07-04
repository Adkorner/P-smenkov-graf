# Pismenkovy_graf
* neorientovaný graf, v ktorom sa na niektorých hranách môže nachádzať nejaké písmeno z množiny {'a', 'b', 'c'}. 
* Ostatné hrany sú tzv. neoznačené. 
# úloha grafu 
zostaví čo najdlhšiu cestu, ktorá vychádza z nejakého zadaného štartového vrcholu pre ktorú platí:
* prvá hrana v ceste má označenie 'a' alebo je bez označenia
* druhá hrana v ceste má označenie 'b' alebo je bez označenia
* na hranách cesty sa stále striedajú písmená 'a', 'b', 'c', 'a', 'b', 'c', …, resp. niektoré hrany v ceste môžu byť neoznačené (fungujú niečo ako žolík)__
* cesta môže prechádzať aj viackrát cez tie isté vrcholy ale po hranách môže prejsť len raz 

Program prečíta textový súbor s popisom grafu a po zadaní štartového vrcholu vygeneruje všetky maximálne dlhé cesty, ktoré spĺňajú pravidlo striedania písmen.
# Popis textového súboru
* každý riadok obsahuje popis jednej hrany grafu buď ako dvojicu alebo ako trojicu
* dvojica v tvare meno1:meno2 označuje hranu bez písmena (žolík)
* trojica v tvare meno1:písmeno:meno2 označuje hranu so zadaným písmenom
* mená vrcholov sú nejaké znakové reťazce zložené len z písmen
