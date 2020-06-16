# Cria um dicionario com {} e: que significa uma chave e um valor 
my_dict = {'key1' : 'value1','key2': 'value2'}

# Chamando valores pela chave 
my_dict ['key2']
my_dict = {'key1': 123 ,'key2':[12,23,33],'key3':['item0','intem1','item2']}

# Vamos chamar de itens do dicionario
my_dict ['key3']

# Podemos chamar itens de uma lista
my_dict ['key3']

#Podemos chamar metodo nos itens tambem 
my_dict ['key3'][0].upper()
my_dict ['key1']
my_dict ['key1'] = my_dict['key1'] - 123
my_dict ['key1']

# Define o objeto como sendo ele mesmo 123
my_dict ['key1'] -= 123
my_dict ['key1']

# Criar um novo dicionario
d = {}

# Criar uma chave por associoação
d['animal'] = 42

# Mostra
d
d = {'key1': {'nestkey':{'subnestkey':'value'}}}

# Continue chamando as chaves...
d['key1']['nestkey']['subnestkey']

# Cria um dicionario tipico
d = {'key1' :1, 'key2' :2, 'key3' :3}

# Retornar uma lista de todas as chaves 
d.keys()

# pega todos os valores
d.values()

# metodo para retornar as tuplas de 
d.items() 

