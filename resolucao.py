#!/usr/bin/env python
#coding: utf-8

from funcoes import *


print '01 -- Preposições'
preposicoes_texto_A = conta_preposicoes(texto_A)
preposicoes_texto_B = conta_preposicoes(texto_B)
print '  Preposições no texto A:', preposicoes_texto_A
print '  *** Preposições no texto B:', preposicoes_texto_B
assert preposicoes_texto_A == 62
print

print '02 -- Verbos'
verbos_texto_A = retorna_verbos(texto_A)
verbos_texto_B = retorna_verbos(texto_B)
print '  Verbos no texto A:', len(verbos_texto_A)
print '  *** Verbos no texto B:', len(verbos_texto_B)
assert len(verbos_texto_A) == 79
print

print '03 -- Verbos em primeira pessoa'
verbos_em_primeira_pessoa_texto_A = filtra_verbos_em_primeira_pessoa(verbos_texto_A)
verbos_em_primeira_pessoa_texto_B = filtra_verbos_em_primeira_pessoa(verbos_texto_B)
print '  Verbos em primeira pessoa no texto A:', len(verbos_em_primeira_pessoa_texto_A)
print '  *** Verbos em primeira pessoa no texto B:', len(verbos_em_primeira_pessoa_texto_B)
assert len(verbos_em_primeira_pessoa_texto_A) == 10
print

print '04 -- Lista de vocabulário'
lista_de_vocabulario_texto_A = retorna_lista_de_vocabulario(texto_A)
lista_de_vocabulario_texto_B = retorna_lista_de_vocabulario(texto_B)
print '  Lista de vocabulário no texto A:', ' '.join(lista_de_vocabulario_texto_A)
print '  *** Lista de vocabulário no texto B:', ' '.join(lista_de_vocabulario_texto_B)
assert lista_de_vocabulario_texto_A == gabarito_vocabulario_A
print

print '05 -- Números bonitos'
numeros_bonitos_texto_A = retorna_numeros_bonitos(retorna_numeros(texto_A))
numeros_bonitos_texto_B = retorna_numeros_bonitos(retorna_numeros(texto_B))
print '  Números bonitos distintos no texto A:', len(set(numeros_bonitos_texto_A))
print '  *** Números bonitos distintos no texto B:', len(set(numeros_bonitos_texto_B))
assert len(numeros_bonitos_texto_A) == 101
print
