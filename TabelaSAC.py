import os

financiamento = float ( input ("1. Informe o valor a ser financiado: "))
os.system("cls")
n = int ( input ("2. Informe o prazo do financiamento (em meses): "))
os.system("cls")
taxa_juros_anual = float (input ("3. Informe a taxa de juros anual (em %): ")) / 100.0
os.system("cls")


amortizacao = financiamento / n

taxa_juros_mensal = pow(1.0 + taxa_juros_anual, 1.0 / 12) - 1.0

def juros_t(t, n, amortizacao, taxa):
    return (n - t + 1) * amortizacao * taxa

print ("AMORTIZAÇÃO: R$ %.2f" % amortizacao)
print ("VALOR DO FINANCIAMENTO: R$ %.2f\n\n" % financiamento)
print ("\t FINANCIAMENTO = R$ %.2f \t MESES: %i meses \t TAXA: %i%% ano (%.f%%)" % 
    (financiamento, n, taxa_juros_anual, taxa_juros_mensal))
print ("\t","-"*80,"\n")
print ("\t MÊS\tSALDO INICIAL\tPRESTAÇÃO\tAMORTIZAÇÃO\t  JUROS\tSALDO FINAL")
print ("\t ---\t-------------\t---------\t-----------\t-------\t-----------")

saldo_inicial = financiamento
for t in range(1, n + 1):
    saldo_final = saldo_inicial - amortizacao
    juros = juros_t(t, n, amortizacao, taxa_juros_mensal)
    prestacao = amortizacao + juros

    print ("\t%4.i\t%13.2f\t%9.2f\t%11.2f\t%7.2f\t%11.2f" % 
        (t, saldo_inicial, prestacao, amortizacao, juros, saldo_final))
    saldo_inicial = saldo_final

