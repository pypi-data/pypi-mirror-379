from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.urls import reverse

from allianceauth.groupmanagement.models import Group

from .models import (
    DiscordWebhook,
    DiscordMessage,
    MarketTrackingConfig,
)

# ========= DiscordWebhook =========

@admin.register(DiscordWebhook)
class DiscordWebhookAdmin(admin.ModelAdmin):
    list_display = ("name", "url")
    search_fields = ("name", "url")
    list_per_page = 25


# ========= DiscordMessage =========

PING_BASE_CHOICES = [
    ("none", "@none"),
    ("here", "@here"),
    ("everyone", "@everyone"),
]

def build_ping_choices():
    choices = list(PING_BASE_CHOICES)
    for g in Group.objects.all().order_by("name"):
        choices.append((f"group:{g.pk}", f"{g.name}"))
    return choices

class DiscordMessageForm(forms.ModelForm):
    item_ping_target = forms.ChoiceField(label=_("Item ping target"), required=False)
    contract_ping_target = forms.ChoiceField(label=_("Contract ping target"), required=False)

    class Meta:
        model = DiscordMessage
        fields = ("item_alert_header", "contract_alert_header")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = build_ping_choices()
        self.fields["item_ping_target"].choices = choices
        self.fields["contract_ping_target"].choices = choices

        # initial dla Items
        inst = self.instance
        if inst and inst.pk:
            if inst.item_ping_choice:
                self.fields["item_ping_target"].initial = inst.item_ping_choice
            elif inst.item_ping_group_id:
                self.fields["item_ping_target"].initial = f"group:{inst.item_ping_group_id}"
            else:
                self.fields["item_ping_target"].initial = "none"

            # initial dla Contracts
            if inst.contract_ping_choice:
                self.fields["contract_ping_target"].initial = inst.contract_ping_choice
            elif inst.contract_ping_group_id:
                self.fields["contract_ping_target"].initial = f"group:{inst.contract_ping_group_id}"
            else:
                self.fields["contract_ping_target"].initial = "none"
        else:
            self.fields["item_ping_target"].initial = "none"
            self.fields["contract_ping_target"].initial = "none"

    def clean(self):
        cleaned = super().clean()

        # rozbij item target
        item_target = cleaned.get("item_ping_target") or "none"
        if item_target.startswith("group:"):
            cleaned["item_ping_choice"] = None
            try:
                gid = int(item_target.split(":", 1)[1])
            except Exception:
                gid = None
            cleaned["item_ping_group"] = Group.objects.filter(pk=gid).first()
        else:
            # none/here/everyone
            cleaned["item_ping_choice"] = item_target
            cleaned["item_ping_group"] = None

        # rozbij contract target
        contract_target = cleaned.get("contract_ping_target") or "none"
        if contract_target.startswith("group:"):
            cleaned["contract_ping_choice"] = None
            try:
                gid = int(contract_target.split(":", 1)[1])
            except Exception:
                gid = None
            cleaned["contract_ping_group"] = Group.objects.filter(pk=gid).first()
        else:
            cleaned["contract_ping_choice"] = contract_target
            cleaned["contract_ping_group"] = None

        return cleaned

    def save(self, commit=True):
        inst = super().save(commit=False)
        # przypisz już rozbite wartości z clean()
        inst.item_ping_choice = self.cleaned_data.get("item_ping_choice")
        inst.item_ping_group = self.cleaned_data.get("item_ping_group")
        inst.contract_ping_choice = self.cleaned_data.get("contract_ping_choice")
        inst.contract_ping_group = self.cleaned_data.get("contract_ping_group")
        if commit:
            inst.save()
        return inst


@admin.register(DiscordMessage)
class DiscordMessageAdmin(admin.ModelAdmin):
    form = DiscordMessageForm
    fieldsets = (
        (_("Items"), {
            "fields": ("item_alert_header", "item_ping_target"),
            "description": _("Header & ping for Items alerts."),
        }),
        (_("Contracts"), {
            "fields": ("contract_alert_header", "contract_ping_target"),
            "description": _("Header & ping for Contracts alerts."),
        }),
    )

    def has_add_permission(self, request):
        return False  # blokujemy dodawanie

    def has_delete_permission(self, request, obj=None):
        return False  # blokujemy usuwanie

    def changelist_view(self, request, extra_context=None):
        obj = DiscordMessage.objects.first()
        if not obj:
        # utwórz domyślny rekord i przekieruj na jego edycję
            obj = DiscordMessage.objects.create(
                item_alert_header="⚠️ MarketTracker Items",
                contract_alert_header="📦 MarketTracker Contracts",
            )
        return HttpResponseRedirect(
            reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=(obj.pk,))
        )


# ========= MarketTrackingConfig =========

@admin.register(MarketTrackingConfig)
class MarketTrackingConfigAdmin(admin.ModelAdmin):
    list_display = ("scope", "location_id", "yellow_threshold", "red_threshold", "updated_at")
    list_editable = ("yellow_threshold", "red_threshold")
    list_filter = ("scope",)
    search_fields = ("location_id",)
    fieldsets = (
        (_("Tracking scope"), {"fields": ("scope", "location_id")}),
        (_("Thresholds"), {"fields": ("yellow_threshold", "red_threshold")}),
        (_("Timestamps"), {"fields": ("created_at", "updated_at"), "classes": ("collapse",)}),
    )
    readonly_fields = ("created_at", "updated_at")

    class Media:

        js = ("markettracker/js/hide_fields.js",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = MarketTrackingConfig.objects.first()
        return HttpResponseRedirect(
            reverse(f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change", args=(obj.pk,))
        )
