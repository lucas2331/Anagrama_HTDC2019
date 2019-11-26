# Import da biblioteca REGEX
import re

# Import da biblioteca System
import sys

# Abortar a Execução
def AbortarExec():
  sys.exit("Execução Abortada!")

# Verificação primaria da palavra
def VerificaPalavra(Palavra):
  # Passagem de Parametros
  PalavraRecebida = Palavra

  # Remoção dos espaços em branco
  PalavraNormalizada = PalavraRecebida.replace(" ", "")

  # Colocar a palavra como minusculo para fazer a comparação
  PalavraMinuscula = PalavraNormalizada.lower()

  # Verificação se é nula ou vazia
  if(PalavraMinuscula == ""):
    print("Você digitou um palavra Nula!")
    # Chamada do Abortar Execução
    AbortarExec()

  # Verificação se a palavra estão nas conformidades
  elif(PalavraNormalizada == re.sub('[^a-z]', "", PalavraMinuscula)):
    # Chamada da Continuidade da Funçãow
    PalavraMaiuscula(PalavraMinuscula)
  
  # Verificação se a palavra não estão nas conformidades
  else:
    # Chamada do Abortar Execução
    AbortarExec()

def PalavraMaiuscula(Palavra):
  PalavraRecebida = Palavra
  PalavraMaiuscula = PalavraRecebida.upper()
  LeituraArquivo(PalavraMaiuscula)

def LeituraArquivo(Palavra):
  PalavraRecebida = Palavra
  Arquivo = open('palavras.txt', 'r')
  
  ListaArquivo = []
  
  for Contador in Arquivo:
      PalavraArquivo = Contador
      ListaArquivo.append(PalavraArquivo.replace("\n", ""))
  
  Resultado(PalavraRecebida, ListaArquivo)
  
def Resultado(Palavra, Lista):
    PalavraRecebida = Palavra
    ListaRecebida = Lista
    ListaPalavraVerif = []
    ListaFinal = []
    ContadorVerf = 0    
    
    TamanhoPalavraUsuario = len(PalavraRecebida)
    
    for Contador in ListaRecebida:
        ParteLista = Contador
        TamanhoPalavraLista = len(ParteLista)
        
        if(TamanhoPalavraUsuario == TamanhoPalavraLista):
            ListaPalavraVerif.append(ParteLista)
        
    for Contador in ListaPalavraVerif:
        PalavraLista = Contador
        ContadorVerf = 0   
        
        for Contador in PalavraRecebida:
            PartePalavraUser = Contador
            
            for Contador in PalavraLista:
                PartePalavraLista = Contador
                
                if PartePalavraUser == PartePalavraLista:
                    ContadorVerf = ContadorVerf + 1
                
                else:
                    ContadorVerf = ContadorVerf + 0
                    
            if(ContadorVerf == len(PalavraRecebida)):
                ListaFinal.append(PalavraLista)
    
    print(ListaFinal)
                
if __name__ == "__main__":

  # Leitura da Palavra ou Frase
  print("Olá, seja bem vindo!")
  AnagramaPalavra = str(input("Digite uma palavra: "))
  VerificaPalavra(AnagramaPalavra)