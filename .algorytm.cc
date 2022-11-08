//algorytm.edu.pl
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
  char tekst[100], wzorzec[100];
 
  cout<<"Podaj tekst: ";
  cin.getline(tekst,100);
 
  cout<<"Podaj wzorzec: ";
  cin.getline(wzorzec,100);
 
  //naiwne wyszukiwanie wzorca w tekscie
 
  int t = 0, w; //do poruszania się po tablicach znaków
  int dl_t = strlen(tekst), dl_w = strlen(wzorzec);
  bool ok = 0;
 
  for(int i=0; i <= dl_t - dl_w; i++)
  {
      ok = 1;
      
      //sprawdzamy, czy zgadzają się pozostałe znaki
      for(int j=0; j<dl_w; j++)
      if(tekst[j+i]!=wzorzec[j]) //jesli nie zgadzają się
      {
        ok = 0;  //gdy tu wejdziemy, to ok = 0
        break;
      }
 
      if(ok) //jesli wszystkie litery się zgadzają (ok = 1)
      {
        cout<<"Wzorzec znaleziono. Początek na "
          <<i+1<<" pozycji\n";
 
        cout<<tekst<<endl;
 
        cout.fill(' '); 
        cout.width(i+dl_w);
 
        cout<<wzorzec<<endl;
 
        break;
      }
  }
  if(!ok)
    cout<<"Wzorca nie znaleziono!";

  return 0;
}