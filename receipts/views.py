from django.shortcuts import render, redirect
from receipts.models import ExpenseCategory, Account, Receipt
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm, ExpenseCategoryForm

# Create your views here.
@login_required
def home(request):
    receipt_instances = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipt_instances": receipt_instances,
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {"form": form}

    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {"categories": categories}
    return render(request, "receipts/categories.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {"accounts": accounts}
    return render(request, "receipts/accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm()

    context = {"form": form}

    return render(request, "categories/create.html", context)
