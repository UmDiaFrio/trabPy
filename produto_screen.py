import tkinter as tk
from tkinter import messagebox
import database


class ProdutoScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        self.root.geometry("600x400")
        self.root.configure(bg="khaki3")

        self.label_nome = tk.Label(self.root, text="Nome do Produto:", bg = "light cyan3", relief="groove",font= ("Helvetica", 10, "bold"))
        self.label_nome.pack(pady=3)
        self.entry_nome = tk.Entry(self.root,bg= "gray70",relief="solid")
        self.entry_nome.pack(pady=3)

        self.label_preco = tk.Label(self.root, text="Preço:", bg = "light cyan3", relief="groove",font= ("Helvetica", 10, "bold"))
        self.label_preco.pack(pady=3)
        self.entry_preco = tk.Entry(self.root,bg= "gray70",relief="solid")
        self.entry_preco.pack(pady=3)

        self.button_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar_produto, bg="OliveDrab4", fg="black")
        self.button_cadastrar.pack(pady=3)

        self.button_alterar = tk.Button(self.root, text="Alterar", command=self.alterar_produto, bg="OliveDrab4")
        self.button_alterar.pack(pady=3)

        self.button_deletar = tk.Button(self.root, text="Deletar", command=self.deletar_produto, bg="OliveDrab4")
        self.button_deletar.pack(pady=3)

        self.lista_produtos = tk.Listbox(self.root, width=80,height=10, bg= "gray70", fg="black", relief="solid")
        self.lista_produtos.pack()

        self.lista_produtos.bind("<<ListboxSelect>>", self.selecionar_produto)

        self.carregar_produtos()

    def cadastrar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()

        if nome and preco:
            database.insert_produto(nome, preco)
            messagebox.showinfo("Cadastro de Produtos", "Produto cadastrado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
            self.carregar_produtos()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def alterar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()
        indice_selecionado = self.lista_produtos.curselection()

        if nome and preco and indice_selecionado:
            produto_selecionado = self.lista_produtos.get(indice_selecionado)
            produto_id = produto_selecionado.split(":")[1].strip().split(",")[0]
            database.update_produto(produto_id, nome, preco)
            messagebox.showinfo("Alteração de Produto", "Dados do produto alterados com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
            self.carregar_produtos()
        else:
            messagebox.showerror("Erro", "Selecione um produto e preencha todos os campos!")

    def deletar_produto(self):
        indice_selecionado = self.lista_produtos.curselection()

        if indice_selecionado:
            produto_selecionado = self.lista_produtos.get(indice_selecionado)
            produto_id = produto_selecionado.split(":")[1].strip().split(",")[0]
            database.delete_produto(produto_id)
            messagebox.showinfo("Deletar Produto", "Produto deletado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_preco.delete(0, tk.END)
            self.carregar_produtos()

    def carregar_produtos(self):
        self.lista_produtos.delete(0, tk.END)
        produtos = database.get_produtos()

        for produto in produtos:
            self.lista_produtos.insert(tk.END, f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}")

    def selecionar_produto(self, event):
        indice_selecionado = self.lista_produtos.curselection()

        if indice_selecionado:
            produto_selecionado = self.lista_produtos.get(indice_selecionado)
            produto_id = produto_selecionado.split(":")[1].strip().split(",")[0]
            produto = database.get_produto(produto_id)

            if produto:
                self.entry_nome.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                self.entry_nome.insert(tk.END, produto[1])
                self.entry_preco.insert(tk.END, produto[2])


def open_product_screen():
    root = tk.Tk()
    produto_screen = ProdutoScreen(root)
    root.mainloop()


if __name__ == "__main__":
    open_product_screen()
