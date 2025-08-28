# 💰 Calculadora de Salário Líquido

Este script em Python realiza o cálculo do salário líquido mensal de um trabalhador com base no valor da hora trabalhada e na quantidade de horas trabalhadas no mês. Ele também considera os descontos obrigatórios como **Imposto de Renda (IR)**, **INSS** e **contribuição sindical**.

> ⚠️ **Aviso:** Esta atividade foi desenvolvida exclusivamente para fins acadêmicos como parte do processo de qualificação na **Softex PE**.

## 📋 Funcionalidades

- Cálculo do salário bruto
- Cálculo dos descontos:
  - IR (11%)
  - INSS (9%)
  - Sindicato (4%)
- Exibição formatada dos valores
- Cálculo do salário líquido

## 🧮 Fórmulas Utilizadas

- `salario_bruto = valor_hora * horas_trabalhadas`
- `ir = salario_bruto * 0.11`
- `inss = salario_bruto * 0.09`
- `sindicato = salario_bruto * 0.04`
- `salario_liquido = salario_bruto - (ir + inss + sindicato)`

## 📦 Requisitos

- Python 3.x instalado

## 🚀 Como Executar

1. Copie o código para um arquivo `.py` (por exemplo, `salario.py`)
2. Execute o script com o comando:

```bash
python salario.py
```

## ✏️ Exemplo de Saída

```text
+ Salário Bruto   : R$ 3200.00
- IR (11%)        : R$ 352.00
- INSS (9%)       : R$ 288.00
- Sindicato (4%)  : R$ 128.00
= Salário Líquido : R$ 2432.00
```

## 📌 Observações

- Os valores de hora e horas trabalhadas são fixos no código. Para torná-lo mais dinâmico, você pode utilizar `input()` para receber esses dados do usuário.
- As porcentagens de desconto são baseadas em valores comuns, mas podem variar conforme a legislação vigente.
