from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

# Função a qual vamos recuperar os dados do formulario
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

# Vamos formatar os dados
        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

# Agora vamos configurar os dados necessarios para envio do email
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@developerspace.com',
            to=['gabrielpires@developerspace.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()
