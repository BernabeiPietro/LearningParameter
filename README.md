# LearningParameter
## Prerequisiti e installazione
Il seguente progetto è stato sviluppato su la versione di Python 3.6

Per sviluppare il seguente progetto è stato utilizza il progetto github dell'utente ncullen93, [pyBN](https://github.com/ncullen93/pyBN).
Quindi per eseguire è necessario scaricare e installare il progetto suddetto al quale vi rimando per la sua installazione.
Unica cosa da rilevare come possibile problema nell'uso del suddetto progetto, è l'impiego di componenti non compatibili con python 3.6,  che impediscono cosi l'installazione e uso. Si risolve, commentando la riga from pyBN.plotting import *, del file /pyBN-master/pyBN/ init .py. .

Per scaricare di ncullen93 ed installare le dipendenze necessarie aprire il terminale ed eseguire i seguenti comandi:
```terminal
 git clone https://github.com/ncullen93/pyBN.git
 cd pyBN-master/pyBN
 commentare la riga from pyBN.plotting import *, del file /pyBN-master/pyBN/ init .py.
 sostituire la riga 582 della file factor.py da 
 new_cpt = np.zeros((exp_len,)) in new_cpt = np.zeros(int(exp_len,))
 sostituire la riga 591 della file factor.py da 
  for j in self.cpt[idx:(idx + rv_stride)]: a  for j in self.cpt[int(idx):int(idx + rv_stride)]:
 cd ..
 pip install .
 ```
 Per scaricare il programma ed installare le dipendenze necessarie aprire il terminale ed eseguire i seguenti comandi:
 ```terminal
 git clone https://github.com/cipo64/LearningParameter.git
 cd LearningParameter
 pip install -r requirements.txt
```


## Esecuzione
Per l'esecuzione digitare:
```python
  python3 progetto.py
```

## Riferimenti
L'algoritmo per l'apprendimento dei parametri si basa sul documento di [Heckerman del 1997](http://machinelearning102.pbworks.com/f/Tutorial-BayesianNetworks.pdf), mentre per calcolare la divergenza tra una distribuzione di probabilità p e q, si applica la divergenza di Kullback-Leibler.

