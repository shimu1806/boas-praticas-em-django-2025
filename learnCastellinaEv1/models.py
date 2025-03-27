from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import URLValidator

class Categoria(models.TextChoices):
    """
    Enum para categorias de locais.
    Você pode adicionar mais categorias conforme necessário.
    """
    HISTORICO = 'historico', _('Histórico')
    ESPORTIVO = 'esportivo', _('Esportivo')
    CULINARIO = 'culinario', _('Culinário')
    CULTURAL = 'cultural', _('Cultural')
    NATURAL = 'natural', _('Natural')

class Local(models.Model):
    """
    Modelo para representar locais para visitar na Itália.
    """
    categoria = models.CharField(
        max_length=20,
        choices=Categoria.choices,
        default=Categoria.HISTORICO,
        verbose_name=_('Categoria'),
        help_text=_('Classificação do tipo de local.')
    )
    
    habilitado = models.BooleanField(
        default=True,
        verbose_name=_('Habilitado'),
        help_text=_('Define se o local estará visível no front-end.')
    )
    
    nome = models.CharField(
        max_length=255,
        verbose_name=_('Nome'),
        help_text=_('Nome do local.')
    )
    
    descricao = models.TextField(
        verbose_name=_('Descrição'),
        help_text=_('Breve descrição sobre o local.')
    )
    
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        validators=[URLValidator()],
        verbose_name=_('Link'),
        help_text=_('Link para o site oficial ou página no Wikipedia.')
    )
    
    imagem = models.ImageField(
        upload_to='locais/',
        blank=True,
        null=True,
        verbose_name=_('Imagem'),
        help_text=_('Imagem representativa do local.')
    )

    class Meta:
        verbose_name = _('Local')
        verbose_name_plural = _('Locais')
        ordering = ['nome']  # Ordena por nome por padrão

    def __str__(self):
        return self.nome