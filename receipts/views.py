from django.shortcuts import render
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    receipt_instances = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_instances": receipt_instances,
    }
    return render(request, "receipts/list.html", context)
