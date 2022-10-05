#Alunos: João Pedro Fonseca Rodrigues, Tales Miller Probst Novacoski

import copy
import random



def comparacao(no, no2):                     #compara as 3 pilhas da mesa p1, p2, e p3 de dois estados da arvore, comparar se os tamanhos de p1,p2 e p3 sao iguais, se sim, comparar a lista INTEIRA e ver se retorna True
  if no.p1 == no2.p1 and no.p2 == no2.p2 and no.p3 == no2.p3:
        return True
  else:
        return False
        


class Arvore(object):

    def __init__(self):
        self.p1=[]          #lista p1
        self.p2=[]          #lista p2
        self.p3=[]          #lista p3
        self.movimentos = []
        self.filhos=[]                    #filhos que estao sendo guardados em uma lista
        self.caminho = []

    def __repr__(self):
        return f'p1={self.p1}, p2={self.p2}, p3={self.p3},\t filhos:{self.filhos}\n movimentos:{self.movimentos}'




    def busca_largura(self, no, objetivo):      #executando a busca em largura
        nocopia = copy.deepcopy(no) 
        abertos= [nocopia]              #abertos recebe a copia do no
        fechados = []
        filhos = []
        caminhos = [nocopia.caminho[0]] #mostra os caminhos de abertos
        
        
        while (abertos !=[]):       #enquanto abertos for diferente de nulo
            x = abertos[0]          #x recebe o valor mais a esquerda de abertos
            #print (x)
            if comparacao(x, objetivo): #compara, se x é o objetivo, se sim, retorna SUCESSO
                caminhos.append(caminhos[0] + "Destino")
                print("Quantos caminhos se mantiveram abertos: " + str(len(abertos)))
                print("Quantos caminhos foram fechados: " + str(len(fechados))+"\n") 
                #print(len(abertos))
                #print(len(fechados))
                #print(fechados)
                #print(caminhos)
                return caminhos[len(caminhos)-1] + "\n\nSUCESSO"        #aqui ele entra
            
            else:
                #print (x)
                x.encontra_movimentos(x, abertos, fechados, caminhos)      #encontra os filhos de x, vendo se estao em abertos ou fechados, e colocando em abertos os que nao estao nem em abertos nem em fechados
                
                
            abertos.remove(x)
            caminhos.remove(caminhos[0])
            fechados.append(x)

  
    def encontra_filhos(self, no, objetivo):              #tentar colocar isto dentro de BFS ou DFS, colocar o pai dos filhos que foram gerados em fechados e continuar fazendo
         assert isinstance(no, Arvore)
         movimentos = self.encontra_movimentos(no)
         for estado in movimentos:
             g = self.g + 1
             self.filhos.append(estado[0], self, g=g)
         


    def encontra_movimentos(self, no, abertos=[], fechados=[],caminhos=[]): #if (pilha1 != vazia) pop pilha 1 e colocar em pilha 2 ou pilha 3  
         assert isinstance(no, Arvore)

         nocopia = copy.deepcopy(no)
         qtdfilhos = int (0)
         filhoatual = 0
         movimento = copy.deepcopy(no)   
        
        
        
         if no.p1!=[]:
            
            movimento = nocopia.p1_p2(nocopia)       #movendo da lista p1 para p2
            estados = abertos.copy() 
            estados.extend(fechados)                   #COMENTARIO IMPORTANTE ===>>  AQUI SE junta abertos e fechados em uma so lista estado, AQUI ESTAVA O BENDITO DO ERRO, quando foi feito dois for's um para comparar abertos e outro para fechados ele bugava, e dava o numero errado do tamanho de abertos e fechados, juntando os dois em apenas uma lista resolveu o problema
            teste = False
            for estado in estados:                        #fazendo comparacao se p1_p2 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento)        #a funcão append adiciona ao final, isso se transforma em uma fila ao ser utilizado pela funcao busca largura, logo realmente é busca largura
                caminhos.append(caminhos[0] + "P1-P2 -> ")


            movimento = nocopia.p1_p3(nocopia)
            estados = abertos.copy() 
            estados.extend(fechados)                   #juntando abertos e fechados em um so estado 
            teste = False
            for estado in estados:                        #fazendo comparacao se p1_p3 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento)  
                caminhos.append(caminhos[0] + "P1-P3 -> ")
              
         if no.p2!=[]:                  #funcional no p2

            movimento = nocopia.p2_p1(nocopia)
            estados = abertos.copy() 
            estados.extend(fechados)                   #juntando abertos e fechados em um so estado 
            teste = False
            for estado in estados:                        #fazendo comparacao se p2_p1 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento) 
                caminhos.append(caminhos[0] + "P2-P1 -> ")

            movimento = nocopia.p2_p3(nocopia)
            estados = abertos.copy() 
            estados.extend(fechados)                   #juntando abertos e fechados em um so estado 
            teste = False
            for estado in estados:                        #fazendo comparacao se p2_p3 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento)
                
                caminhos.append(caminhos[0] + "P2-P3 -> ")

         if no.p3!=[]:

            movimento = nocopia.p3_p1(nocopia)
            estados = abertos.copy() 
            estados.extend(fechados)                   #juntando abertos e fechados em um so estado 
            teste = False
            for estado in estados:                        #fazendo comparacao se p3_p1 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento)
                caminhos.append(caminhos[0] + "P3-P1 -> ")

            movimento = nocopia.p3_p2(nocopia)
            estados = abertos.copy() 
            estados.extend(fechados)                   #juntando abertos e fechados em um so estado, pq fazendo dois for's para cada um buga tudo e printa a quantidade de abertos/fechados errada 
            teste = False
            for estado in estados:                        #fazendo comparacao se p3_p2 esta em abertos ou fechados, se não estiver nem em abertos nem em fechados é colocado em abertos e em caminhos
                if comparacao(estado, movimento):
                    teste = False
                    break
                teste = True
            if teste:
                self.movimentos.append(movimento)
                abertos.append(movimento)       
                caminhos.append(caminhos[0] + "P3-P2 -> ")                 
            
            return self.movimentos
             

  #tipos de movimentos possíveis
    def p1_p2(self, no):                     #movendo da lista p1 para p2
        nocopia = copy.deepcopy(no)
        
        nocopia.p2.append(nocopia.p1.pop())
        return nocopia

    def p1_p3(self, no):                     #movendo da lista p1 para p3
        nocopia = copy.deepcopy(no)
        
        nocopia.p3.append(nocopia.p1.pop())
        return nocopia

    def p2_p1(self, no):                     #movendo da lista p2 para p1
        nocopia = copy.deepcopy(no)
        
        nocopia.p1.append(nocopia.p2.pop())
        return nocopia

    def p2_p3(self, no):                     #movendo da lista p2 para p3
        nocopia = copy.deepcopy(no)
        
        nocopia.p3.append(nocopia.p2.pop())
        return nocopia

    def p3_p2(self, no):                     #movendo da lista p3 para p2
        nocopia = copy.deepcopy(no)
        
        nocopia.p2.append(nocopia.p3.pop())
        return nocopia

    def p3_p1(self, no):                     #movendo da lista p3 para p1
        nocopia = copy.deepcopy(no)
        
        nocopia.p1.append(nocopia.p3.pop())
        return nocopia
#Fim dos tipos de movimentos possíveis 

t = Arvore()
goal = Arvore()
goal.p2.append('C')      #adicionando c a p1
goal.p2.append('B')      #adicionando b a p1
goal.p2.append('A')      #adicionando a a p3

j = [] #Verificador de blocos ja colocados

#Colocar os blocos em posição aleatório
while (len(t.p1) + len(t.p2) + len(t.p3)) < 3: #verifica se foram colocadas 3 blocos na mesa
    x = random.randint(0,2) #Impõe qual mesa que sera colocada o Bloco
    y = random.randint(0,2) #Impõe qual Bloco sera colocado na mesa
    
    if x == 0: #Verifica se o Bloco foi adicionado na mesa P1
        if(y == 1 and y not in j): #Verifica se o Bloco "B"  Bloco sera adicionado na mesa P1 e se o Bloco "B" ja esta na mesa
            j.append(y)#Demonstra que "B" ja foi colocado na mesa
            t.p1.append("B")#Adiciona o Bloco "B" na Mesa
        if(y == 2 and y not in j):#Verifica se o Bloco "C"  Bloco sera adicionado na mesa P1 e se o Bloco "C" ja esta na mesa
            j.append(y)#Demonstra que "C" ja foi colocado na mesa
            t.p1.append("C")#Adiciona o Bloco "C" na Mesa
        if(y == 0 and y not in j):#Verifica se o Bloco "A"  Bloco sera adicionado na mesa P1 e se o Bloco "A" ja esta na mesa
            j.append(y)#Demonstra que "A" ja foi colocado na mesa
            t.p1.append("A")#Adiciona o Bloco "A" na Mesa
    else:            
        if x == 1:#Verifica se o Bloco foi adicionado na mesa P3
            if(y == 1 and y not in j): #Verifica se o Bloco "B"  Bloco sera adicionado na mesa P1 e se o Bloco "B" ja esta na mesa
                j.append(y) #Demonstra que "B" ja foi colocado na mesa
                t.p2.append("B") #Adiciona o Bloco "B" na Mesa
            if(y == 2 and y not in j): #Verifica se o Bloco "C"  Bloco sera adicionado na mesa P1 e se o Bloco "C" ja esta na mesa
                j.append(y)#Demonstra que "C" ja foi colocado na mesa
                t.p2.append("C")#Adiciona o Bloco "C" na Mesa
            if(y == 0 and y not in j): #Verifica se o Bloco "A"  Bloco sera adicionado na mesa P1 e se o Bloco "A" ja esta na mesa
                j.append(y)#Demonstra que "A" ja foi colocado na mesa
                t.p2.append("A")#Adiciona o Bloco "A" na Mesa
        else:
            if x == 2:#Verifica se o Bloco foi adicionado na mesa P2
                if(y == 1 and y not in j):
                    j.append(y)#Demonstra que "B" ja foi colocado na mesa
                    t.p3.append("B")#Adiciona o Bloco "B" na Mesa
                if(y == 2 and y not in j):
                    j.append(y)#Demonstra que "C" ja foi colocado na mesa
                    t.p3.append("C")#Adiciona o Bloco "C" na Mesa
                if(y == 0 and y not in j):
                    j.append(y)#Demonstra que "A" ja foi colocado na mesa
                    t.p3.append("A")#Adiciona o Bloco "A" na Mesa


t.caminho.append("Original -> ")
print("Original:")
print(t)
print("\nDestino:")
print(goal)
print("")
print(t.busca_largura(t, goal))