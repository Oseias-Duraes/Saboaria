import psycopg2
# Update connection string information
host = "localhost"
dbname = "saboaria"
user = "postgres"
password = "masterkey"
sslmode = "disable"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

id = input("insira o ID")
nome = input("Insira o nome")
preco_custo = input("Informe o preço de custo")
preco_venda = input("Informe o preço de venda")


def create_product(id,nome,preco_custo,preco_venda):
    cursor.execute("INSERT INTO produtos (id, nome, preco_custo, preco_venda) VALUES (%s, %s, %s, %s);", (id, nome,preco_custo,preco_venda))

create_product(id, nome, preco_custo, preco_venda)
#def find_all():
  #  cursor.execute("SELECT*FROM produtos;")
   # return cursor.fetchall()

#def find_one(id):
    #cursor.execute("SELECT * FROM prodtos WHERE id=%s ;",(id, ))
    #return cursor.fetchall()

#def update_user(id, nome, email, senha):
    #cursor.execute("UPDATE usuario SET nome=%s, email=%s , senha=%s WHERE id=%s;", (nome, email, senha, id))

#def delete_user(id):
    #cursor.execute("DELETE FROM usuario WHERE id=%s ;",(id,))



conn.commit()
cursor.close()
conn.close()