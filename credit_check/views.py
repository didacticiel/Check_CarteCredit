from django.shortcuts import render

# Create your views here.
# credit_check/views.py
from django.shortcuts import render
from .forms import CardCheckForm
from .utils import card_type, luhn_checksum_is_valid
from django.views.decorators.http import require_POST
from django.http import JsonResponse

def home(request):
    result = None
    card_type_str = None
    if request.method == "POST":
        form = CardCheckForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            # luhn déjà validé par le form; on détermine le type
            card_type_str = card_type(number)
            result = "VALID" if luhn_checksum_is_valid(number) else "INVALID"
        else:
            # form.errors s'affichera
            pass
    else:
        form = CardCheckForm()
    return render(request, "credit_check/index.html", {"form": form, "result": result, "card_type": card_type_str})


# API simple (POST JSON), utile pour intégration frontend
@require_POST
def api_check_card(request):
    import json
    try:
        data = json.loads(request.body.decode())
        number = str(data.get("number", "")).strip().replace(" ", "").replace("-", "")
    except Exception:
        return JsonResponse({"error": "invalid_payload"}, status=400)

    if not number.isdigit():
        return JsonResponse({"valid": False, "reason": "non_numeric"}, status=400)

    valid = luhn_checksum_is_valid(number)
    ctype = card_type(number) if valid else "INVALID"
    return JsonResponse({"valid": valid, "card_type": ctype})
