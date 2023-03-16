import random 

def gene_cb():
    """ gera um gene valido para cada caixa binária
    
        return:
            valor de 0 ou 1         
    """
    
    lista = [0,1]
    gene = random.choice(lista)
    return gene 

def ind_cb(n):
    """ gera o indivíuo 
    
        arg:
            n: número de genes do indivíduo 
            
        return:
            uma lista com n genes
    """
    
    ind = []
    for i in range(n):
        gene = gene_cb()
        ind.append(gene)
    return ind


def populacao_cb(tamanho, n):
    """cria uma população para o problema das caixas binárias
    
    args: 
        tamanho: tamanho da população
        n: número de genes em um individuo 
    
    returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(ind_cb(n))
        
    return populacao


def selecao_roleta_max(populacao, fitness):
    """ Seleciona indivuduos de uma populaçao usando método da roleta.
        
            Nota: apenas funciona para problemas de maximização
            
        args:
            população: lista com todos os individuos da população
            fitness: valor da funçao objetivo dos individuos da população 
            
       returns:
           População de individuos selecionados 
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_ponto_simples(pai, mae):
    """operador de cruzamento de ponto simples.
    
        Args:
            pai: uma lista representando um individuo 
            mae: uma lista representando um individuo 
            
        Returns:
            duas listas, sendo que cada uma representa um filho dos pais que foram os argumnetos 
    """
    ponto_de_corte = random.randint(1, len(pai)-1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias
        
        Args: 
           individuo: uma lista representando um individuo 
           
        Returns:
            Um individuo com um gene mutado
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo
    
    
def fun_obj_(individuo):
    """ soma os valores dos genes 
    
        arg:
            individuo: lista contendo as caixas binárias 
            
        return
            valor da soma 
    """
    return sum(individuo) 

def funcao_obj_pop_cb(populacao):
    """ calcula a função objetiva para todos os membros de uma populaçao 
    
        Args:
            populacao: lista com individuos da populaçao
            
        Returns:
            lista de valores representando a fitness de cada individuo da populaçao 
     """
    fitness = []
    for individuo in populacao:
        fobj = fun_obj_(individuo)
        fitness.append(fobj)
    return fitness