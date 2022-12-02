from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt

# Create your views here.
def home(request):
    receipt_instances = Receipt.objects.all()
    context = {
        "receipt_instances": receipt_instances,
    }
    return render(request, "receipts/list.html", context)
