from django.shortcuts import render
from .controller.calculator import calculator


def form(request):
    if request.method == 'POST':
        consumption = [float(request.POST.get(f'consumption_{i}')) if request.POST.get(f'consumption_{i}') else 0.0 for i in range(3)]
        distributor_tax = float(request.POST.get('distributor_tax')) if request.POST.get('distributor_tax') else 0.0
        tax_type = request.POST.get('tax_type')

        annual_savings, monthly_savings, applied_discount, coverage = calculator(
            consumption=consumption,
            distributor_tax=distributor_tax,
            tax_type=tax_type,
        )

        context = {
            'annual_savings': annual_savings,
            'monthly_savings': monthly_savings,
            'applied_discount': applied_discount,
            'coverage': coverage,
        }

        return render(request, 'calculadora/resultado.html', context)

    return render(request, 'calculadora/form.html')


def resultado(request):
    annual_savings = float(request.GET.get('annual_savings')) if request.GET.get('annual_savings') else 0.0
    monthly_savings = float(request.GET.get('monthly_savings')) if request.GET.get('monthly_savings') else 0.0
    applied_discount = float(request.GET.get('applied_discount')) if request.GET.get('applied_discount') else 0.0
    coverage = float(request.GET.get('coverage')) if request.GET.get('coverage') else 0.0

    context = {
        'annual_savings': annual_savings,
        'monthly_savings': monthly_savings,
        'applied_discount': applied_discount,
        'coverage': coverage,
    }
    return render(request, 'calculadora/resultado.html', context)
