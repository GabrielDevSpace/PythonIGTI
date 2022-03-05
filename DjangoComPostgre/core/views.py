from django.views.generic import FormView

# Redirecionamento apos import
from django.urls import reverse_lazy

# Mensagem de retorno apos post
from django.contrib import messages

from .models import Servico, Funcionario, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')
    """ 
    Na função abaixo estamos recuperando o contexto ja existente get_context_data
    e abaixo adicionamos os dados que queremos = context['servicos'] e context['funcionarios'] no caso estes
    estao retornando do banco de dados Servico.objects.all() e por ultimo retornamos o contexto.
    """

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('servico').all()
        context['funcionarios'] = Funcionario.objects.all()
        context['features'] = Feature.objects.all()
        return context


    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar email!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
