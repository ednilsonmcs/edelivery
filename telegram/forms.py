from django import forms

class MyForm(forms.Form):
    nome = forms.CharField(label='Nome:')

    endereco = forms.CharField(label='Endereço:')

    hamburguer = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )

    acai = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )

    pizza = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )

    refrigerante = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )


    agua = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )

    suco = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'custom-class'}),  # Pode adicionar classes CSS personalizadas
    )

    formas_pagamento = forms.ChoiceField(
        choices= [ ('dinheiro', 'Dinheiro'), ('pix', 'PIX'), ('cartão', 'Cartão'), ],
        widget=forms.Select,
        label='Forma de pagamento:'
    )