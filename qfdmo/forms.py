from django import forms

from qfdmo.models import ActionDirection, SousCategorieObjet


class AutoCompleteInput(forms.Select):
    template_name = "django/forms/widgets/autocomplete.html"

    def __init__(
        self,
        attrs=None,
        max_options_displayed=10,
        is_ban_address=False,
        data_controller="autocomplete",
        **kwargs
    ):
        self.data_controller = data_controller
        self.max_options_displayed = max_options_displayed
        self.is_ban_address = is_ban_address
        super().__init__(attrs=attrs, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["data_controller"] = self.data_controller
        context["widget"]["max_options_displayed"] = self.max_options_displayed
        if self.is_ban_address:
            context["widget"]["is_ban_address"] = "true"
        return context


class InlineRadioSelect(forms.RadioSelect):
    template_name = "django/forms/widgets/inline_radio.html"
    option_template_name = "django/forms/widgets/inline_radio_option.html"

    def __init__(self, attrs=None, fieldset_attrs=None, choices=()):
        self.fieldset_attrs = {} if fieldset_attrs is None else fieldset_attrs.copy()
        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["fieldset_attrs"] = self.build_attrs(self.fieldset_attrs)
        return context


class GetReemploiSolutionForm(forms.Form):
    sous_categorie_objet = forms.ModelChoiceField(
        queryset=SousCategorieObjet.objects.all(),
        widget=AutoCompleteInput(
            attrs={
                "class": "fr-input",
                "placeholder": "Vêtement, Meuble, Smartphone, etc.",
            }
        ),
        label="",
        empty_label="",
        required=False,
    )
    adresse = forms.CharField(
        widget=AutoCompleteInput(
            attrs={
                "class": "fr-input",
                "placeholder": "Quelle est votre adresse ?",
            },
            data_controller="address-autocomplete",
            is_ban_address=True,
            max_options_displayed=5,
        ),
        label="",
        required=False,
    )
    latitude = forms.FloatField(
        widget=forms.HiddenInput(
            attrs={"data-address-autocomplete-target": "latitude"}
        ),
        required=False,
    )
    longitude = forms.FloatField(
        widget=forms.HiddenInput(
            attrs={"data-address-autocomplete-target": "longitude"}
        ),
        required=False,
    )

    direction = forms.ModelChoiceField(
        widget=InlineRadioSelect(
            attrs={
                "class": "fr-radio",
                "data-action": "click -> choose-action#changeDirection",
            },
            fieldset_attrs={
                "class": "fr-fieldset fr-mb-0",
                "data-choose-action-target": "direction",
            },
        ),
        queryset=ActionDirection.objects.all().order_by("order"),
        to_field_name="nom",
        label="",
        required=False,
    )

    overwritten_direction = forms.ModelChoiceField(
        widget=InlineRadioSelect(
            attrs={
                "class": "fr-radio",
                "data-action": "click->choose-action#displayActionList",
            },
            fieldset_attrs={
                "class": "fr-fieldset",
                "data-choose-action-target": "overwrittenDirection",
            },
        ),
        queryset=ActionDirection.objects.all().order_by("order"),
        to_field_name="nom",
        label="",
        required=False,
    )

    action_list = forms.CharField(
        widget=forms.HiddenInput(
            attrs={"data-choose-action-target": "actionList"},
        ),
        required=False,
    )
