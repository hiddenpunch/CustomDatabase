from lark import Lark, Transformer


class MyTransformer(Transformer):

    def create_table_query(self, item):
        print("DB_2018-13627> 'CREATE TABLE' requested")
    def drop_table_query(self, item):
        print("DB_2018-13627> 'DROP TABLE' requested")
    def desc_query(self, item):
        print("DB_2018-13627> 'DESC' requested")
    def insert_query(self, item):
        print("DB_2018-13627> 'INSERT' requested")
    def delete_query(self, item):
        print("DB_2018-13627> 'DELETE' requested")
    def select_query(self, item):
        print("DB_2018-13627> 'SELECT' requested")
    def show_tables_query(self, item):
        print("DB_2018-13627> 'SHOW TABLES' requested")

with open('grammar.lark') as file:
    sql_parser = Lark(file.read(), start="command", lexer="standard")

exit_flag=0

while True:
    sentence = input("DB_2018-13627> ")
    sentence = sentence.rstrip()
    while len(sentence)==0 or sentence[-1]!=';':
        sentence = sentence + " " + input()
        sentence = sentence.rstrip()
        #print(sentence)
    queries = sentence.split(sep=';')
    for query in queries:
        if query!='':
            query+=';'
            try:
                tree = sql_parser.parse(query)
            except:
                print("DB_2018-13627> Syntax error")
                break
            if tree.children[0] == 'exit':
                exit_flag=1
                break
            a = MyTransformer().transform(tree)
    if exit_flag==1:
        break