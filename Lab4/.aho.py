class AhoAutomaton:
    def __init__(self, slowo_kluczowe) -> None:
        self.main_list = []
        """
        - wartosc -- znak reprezentujacy wezel,
        - nastepne stany -- lista identyfikatorow wezlow podrzednych,  
        - niepowodzenia stanu -- identyfikator niepowodzenia stanu,
        - wyjscie -- lista wszystkich slow kluczowych, ktore napotkalismy.
        """
        self.main_list.append({"wartosc": "", 
                               "kolejny stan": [], 
                               "ostatni stan": 0, 
                               "wyjscie": []})
        
        for i in slowo_kluczowe:
            self.dodaj_slowo_kluczowe(i)


    def znajdz_kolejny_stan(self, aktualny_stan, znak):
        """
        Zwraca identyfikator potomka tego wezla
        """
        for i in self.main_list[aktualny_stan]["wartosc"]:
            if znak == self.main_list[i]["wartosc"]:
                return 
        return None

    def dodaj_slowo_kluczowe(self, slowo_klucz):
        slowo_klucz.lower()
        aktualny_stan = 0
        start = 0
        stan = self.znajdz_kolejny_stan(aktualny_stan, slowo_klucz[start])

        while stan != None:
            aktualny_stan = stan
            start += 1
            if start < len(slowo_klucz):
                stan = self.znajdz_kolejny_stan(aktualny_stan, slowo_klucz[start])
            else:
                break

        for i in range(start, len(slowo_klucz)):
            wezel = {"wartosc": slowo_klucz[i], 
                     "kolejny stan": [], 
                     "niepowodzenie stanu": 0, 
                     "wyjscie": []}
            self.main_list.append(wezel)
            self.main_list[aktualny_stan]["kolejny stan"].append(len(self.main_list) - 1)
            aktualny_stan = len(self.main_list) - 1

        self.main_list[aktualny_stan]["wyjscie"].append(slowo_klucz)



