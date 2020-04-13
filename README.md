# LearningParameter
## Prerequisiti e installazione
NB: il seguente progetto è stato sviluppato su la versione di Python 3.6

Per sviluppare il seguente progetto è stato utilizza il progetto github dell'utente ncullen93, [pyBN](https://github.com/ncullen93/pyBN).
Quindi per eseguire è necessario scaricare e installare il progetto suddetto al quale vi rimando per la sua installazione.
Unica cosa da rilevare come possibile problema nell'uso del suddetto progetto, è l'impiego di componenti non compatibili con python 3.6,  che impediscono cosi l'installazione e uso del suo pacchetto. Questo risolto, commentando la riga from pyBN.plotting import *, del file /pyBN-master/pyBN/ init .py. 

$ git clone https://github.com/cipo64/LearningParameter.git
$ cd LearningParameter
$ pip3 install -r requirements.txt



Gli esempi di rete bayesiane prese in considerazione, sono presenti nella cartella data della reposity di Ncullen93 o caricate per comodità anche all'interno di questo progetto, nella cartella data
Per l'installazione dei pacchetti aggiuntivi, si
## Esecuzione
Per l'esecuzione digitare:
```python
  python3 progetto.py
```

## Riferimenti
L'algoritmo per l'apprendimento dei parametri si basa sul documento di [Heckerman del 1997](http://machinelearning102.pbworks.com/f/Tutorial-BayesianNetworks.pdf), mentre per calcolare la divergenza tra una distribuzione di probabilità p e q, si applica la divergenza di Kullback-Leibler.

