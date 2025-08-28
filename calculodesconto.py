# Valores fixos
valor_hora = 20.0          # (Valor recebido por hora)
horas_trabalhadas = 160    # (Quantidade de horas trabalhadas no mês)

# Cálculos
salario_bruto = valor_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.09
sindicato = salario_bruto * 0.04
salario_liquido = salario_bruto - (ir + inss + sindicato)

# Exibe os resultados formatados
print(f"+ Salário Bruto   : R$ {salario_bruto:.2f}")
print(f"- IR (11%)        : R$ {ir:.2f}")
print(f"- INSS (9%)       : R$ {inss:.2f}")
print(f"- Sindicato (4%)  : R$ {sindicato:.2f}")
print(f"= Salário Líquido : R$ {salario_liquido:.2f}")
