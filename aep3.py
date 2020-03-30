#!/usr/bin/python
# coding: utf-8
#
# file: aep3.py
#
# AEP 3 - Pesquisa Operacional
# Você foi solicitado para desenvolver um software de logística para uma cooperativa que transporta grãos e combustível
# utilizando vagões para carga a granel e vagões tanque.
# O vagão para carga a granel tem peso máximo de carga de 105.000 kg,
# e o vagão tanque tem peso máximo de carga de 70.000kg quando cheios.
# No total, a cooperativa precisa transportar, no mínimo, 4.000.000kg de carga em grãos e 2.000.000kg de combustível,
# podendo utilizar, na composição, apenas 70 vagões no maximo.
# O custo do vagão de carga a granel é de R$750,00 por vagão, e do vagão tanque, de R$890,00.
# Elabore um modelo de programação linear e resolva-o no Solver para minimizar o custo de transporte por viagem para a
# empresa, atribua condição de variáveis de decisão inteiras.
# Calcule a quantidade de vagões de carga a granel e vagões tanque utilizados, o custo mínimo encontrado e a
# quantidade de cada carga que poderá ser transportada. Anexe seus cálculos e resultados.


import sys
from pulp import *

prob = LpProblem('Problema_do_Custo_de_Transporte', LpMinimize)

# Variaveis

x1 = LpVariable('Vagao_Granel', cat='Integer')
x2 = LpVariable('Vagao_Tanque', cat='Integer')

# Cria função objetivo

prob += (x1 * 750) + (x2 * 890)  # Custo Total

# Restrições

prob += x1 + x2 <= 70  # Queremos usar 70 vagões no máximo
prob += x1 >= 0  # Queremos usar algum vagão né
prob += x2 >= 0
prob += x1 * 105000 >= 4000000  # Limite máximo do peso granel
prob += x2 * 70000 >= 2000000  # Limite máximo do peso tanque

# Cria um arquivo LP
prob.writeLP('aep3.lp')

# Resolve o problema
prob.solve()

# Status da Resolução
print("Status:", LpStatus[prob.status])

# Solucoes otimas das variaveis
for variable in prob.variables():
    print("{} = {}".format(variable.name, variable.varValue))

# Objetivo otimizado
print("Custo total do melhor transporte: R$ %0.2f" % value(prob.objective))
