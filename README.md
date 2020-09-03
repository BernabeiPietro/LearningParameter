# LearningParameter
## Prerequisiti e installazione
Il seguente progetto è stato sviluppato su la versione di Python 3.8

Per sviluppare il seguente progetto è stato utilizza il progetto github dell'utente ncullen93, [pyBN](https://github.com/ncullen93/pyBN), da cui sono stati ripresi  gli esempi di reti bayesiane. Questi sono inclusi all'interno del seguente progetto, nella cartella data.

 Per scaricare il programma ed installare le dipendenze necessarie aprire il terminale ed eseguire i seguenti comandi:
 ```terminal
 git clone https://github.com/BernabeiPietro/LearningParameter.git
 cd LearningParameter
 conda env create -f environment.yml
```


## Esecuzione
Per l'esecuzione digitare:
```python
  python3 main.py
```

## Riferimenti
L'algoritmo per l'apprendimento dei parametri si basa sul documento di [Heckerman del 1997](http://machinelearning102.pbworks.com/f/Tutorial-BayesianNetworks.pdf), mentre per calcolare la divergenza tra una distribuzione di probabilità p e q, si applica la divergenza di Kullback-Leibler.

