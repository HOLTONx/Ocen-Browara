# ocenPiwo


Projekt strony internetowej Oceń Browara
Przedmiot : Projektowanie i programowanie front-end

Skład:
Jakub Duda 12K1
Bartłomiej Szpetko 12K3
Tomasz Górnicki 12K1

Link do filmu w skrócie prezentującego stronę:
https://www.youtube.com/watch?v=EskaAXety0w



Wstęp 

Strona powstała przy użyciu technologii HTML, CSS z biblioteką Bootstrap, Python z frameworkiem Flask oraz MySQL. Głównym założeniem projektu było stworzenie strony internetowej, której grupą docelową byli by pełnoletni ludzie chcący wyrazić swoją opinię na temat danego piwa. Strona pozwala użytkownikowi na sprawdzenie informacji o różnych piwach, zobaczyć gdzie dane piwo plasuje się w rankingu stworzonym na podstawie głosów użytkowników gdzie oczywiście sam również może zagłosować.

Budowa strony

Strona składa się czterech responsywnych podstron w tym ze strony głównej oraz trzech dodatkowych zakładek. Każda strona posiada pasek nawigacyjny oraz stopkę. Intuicyjny pasek nawigacyjny pozwala na bezproblemowe przemieszczanie się między stronami. Po lewej stronie znajduje się logo, które po kliknięciu przekieruje nas na stronę główną. Z prawej strony znajdują się kolejno zakładki “Strona główna”, “Ranking”, “Dodaj piwo” oraz “kontakt”. Stopka zawiera dane twórców oraz dwa loga(Politechniki Krakowskiej oraz platformy Facebook), które po kliknięciu prowadzą nas na dane strony.  

Na stronie głównej u samej góry znajdziemy obecne trzy pierwsze miejsca rankingu oraz losowe piwo, wraz z opisem, poniżej

Na stronie “Ranking” znajduje się lista piw w kolejności od najwyższej liczby głosów do najmniejszej wraz z możliwością zagłosowania na każde piwo.

W następnej zakładce znajduje się formularz, który użytkownik może uzupełnić w celu dodania nowego piwa do rankingu. Po wysłaniu nowe piwo zostaje dodane do bazy danych i staje się widoczne w liście rankingowej z poprzedniej zakładki.

Ostatnia zakładka zawiera formularz kontaktowy, który pozwala użytkownikowi na skontaktowanie się z administracją strony w razie jakichkolwiek pytań lub wątpliwości. 



Instrukcja instalacji strony:

Programy potrzebne do uruchomienia strony: Xampp oraz Phyton.
https://www.apachefriends.org/pl/download.html
https://www.python.org/downloads/

Uruchamiamy program Xampp i klikamy start przy Apache oraz MySQL

Klikamy “Admin” dla MySQL w programie Xampp
W phpMyAdmin klikamy “Nowa” a następnie “Import” po czym wybieramy plik browary_db.sql

Otwieramy wiersz poleceń i przechodzimy do folderu z plikami strony
Wpisujemy “pip install -r requirements.txt”, a następnie “flask run” 
W konsoli pokaże się komunikat “* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)”, przechodzimy na wskazany link gdzie ukaże się strona
