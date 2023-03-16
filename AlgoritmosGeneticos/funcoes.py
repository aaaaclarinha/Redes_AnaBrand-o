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

def fun_obj_(individuo):
    """ soma os valores dos genes 
    
        arg:
            individuo: lista contendo as caixas binárias 
            
        return
            valor da soma 
    """
    return sum(individuo) 
