# LearningParameter
## Prerequisiti e installazione
Il seguente progetto è stato sviluppato su la versione di Python 3.6

Per sviluppare il seguente progetto è stato utilizza il progetto github dell'utente ncullen93, [pyBN](https://github.com/ncullen93/pyBN), di cui si specifica l'uso della struttura dati rappresentante le reti e l'algoritmo di generazione dataset

Per scaricare il progetto pyBN di ncullen93 ed installare le dipendenze necessarie,  aprire il terminale ed eseguire i seguenti comandi:
```terminal
 git clone https://github.com/ncullen93/pyBN.git (o scaricare lo zip e unzip)
 cd pyBN-master/pyBN
 commentare la riga from pyBN.plotting import *, del file /pyBN-master/pyBN/__ini__.py
 sostituire la riga 582 della file factor.py 
 da "new_cpt = np.zeros((exp_len,))" a  "new_cpt = np.zeros(int(exp_len,))"
 sostituire la riga 591 della file factor.py
 da "for j in self.cpt[idx:(idx + rv_stride)]:"  a  "for j in self.cpt[int(idx):int(idx + rv_stride)]:"
 cd ..
 pip install .
 ```
 Per scaricare il programma ed installare le dipendenze necessarie aprire il terminale ed eseguire i seguenti comandi:
 ```terminal
 git clone https://github.com/BernabeiPietro/LearningParameter.git
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

