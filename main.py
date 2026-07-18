import customtkinter as ctk

# Define o tema escuro da interface para toda a aplicação.
ctk.set_appearance_mode('dark')

# Função responsável por validar as credenciais informadas pelo usuário.
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

# Compara os dados digitados com as credenciais cadastradas.
    if usuario == 'matheus' and senha =='123456':
        resultado_login.configure(text='Login feito com sucesso!', text_color='green')
    else: resultado_login.configure(text='Dados de login incorretos', text_color='red')
  

# Cria a janela principal da aplicação.
app = ctk.CTk()
app.title('Sistema de Login')
app.geometry('300x300')

# -------------------------
# Componentes da interface
# ------------------------

# Texto que identifica o campo de usuário.
label_ususario = ctk.CTkLabel (app, text ='Usuário')
label_ususario.pack(pady =10)

# Campo onde o usuário informa seu nome de acesso.
campo_usuario= ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady =10)


# Texto que identifica o campo desenha.
label_senha = ctk.CTkLabel (app, text ='Senha')
label_senha.pack(pady=10)

# Campo de senha com caracteres ocultos por segurança.
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite a sua senha', show = '*')
campo_senha.pack(pady=10)


# Button login
botao_login = ctk.CTkButton(app, text='Login',command=validar_login)
botao_login.pack(pady=10)


# Área utilizada para exibir mensagens de sucesso ou erro ao usuário.
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)


# Inicia o loop da aplicação
app.mainloop()