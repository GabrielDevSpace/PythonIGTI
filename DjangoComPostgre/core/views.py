from django.views.generic import TemplateView
from .models import Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'index.html'

    """ 
    Na função abaixo estamos recuperando o contexto ja existente get_context_data
    e abaixo adicionamos os dados que queremos = context['servicos'] e context['funcionarios'] no caso estes
    estao retornando do banco de dados Servico.objects.all() e por ultimo retornamos o contexto.
    """

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('servico').all()
        context['funcionarios'] = Funcionario.objects.all()
        return context


