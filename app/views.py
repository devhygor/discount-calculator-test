from django.shortcuts import render
from app.controller import calculator


def form(request):
    if request.method == 'POST':
        consumption = [float(request.POST.get(f'consumption_{i}')) for i in range(3)]
        distributor_tax = float(request.POST.get('distributor_tax'))
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
