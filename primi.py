
import sys

class archivio_primi:
    def __init__(self):
        self.primi = []
    
    def load(self, val):
        self.primi = val
    
    def add_prime(self, x):
        self.primi.append(x)


def next_num(x):
    # salta i pari (divisibili per 2)
    if str(x).endswith("3"):
        return int(x)+4
    return int(x)+2


def run(classe,x,fin):
    
    while x<fin:
        
        # Escludo il numero 1
        for primo in classe.primi[1:]:
            if (x/primo).is_integer():
                # Se la divisione genera un numero senza virgola
                # interrompi il for
                break
        else:
            # Se il for non viene interrotto
            # Aggiungi il numero nella lista dei primi
            classe.add_prime(x)
        
        # Chiedi il prossimo numero
        x = next_num(x)
    
    return x

def main():
    
    classe = archivio_primi()
    
    
    try:
        with open("numeri_primi.txt", "r", encoding="UTF-8") as f:
            # Prima riga numero di inizio
            start_from = int(f.readline())
            
            val = f.readline().split(",")
            # Seconda riga numeri primi
            val = list(map( (lambda x: int(x) ) , val[1:-1] ))
            
            # Terza riga numero di fine
            end_to = int(f.readline())
            
            
    except: # Se non trova il file
        print("File non trovato o Errore: ",sys.exc_info())
        start_from = 11
        val = [1,2,3,5,7]
        end_to = 1000
    
    # Carica i numeri primi nella classe
    classe.load(val)
    
    # Esegui la ricerca dei primi
    last_num = run(classe,start_from,end_to)
    
    print("Ultimo numero trovato: ", last_num)
    #print("sequenza di numeri primi: ", classe.primi)
    
    with open("numeri_primi.txt", "w", encoding="UTF-8") as f:
        f.write(str(last_num)+"\n")
        f.write(str(classe.primi)+"\n")
        f.write(str(last_num*2))
    
    return



if __name__ == "__main__":
    print('inizio programma');
    main()
