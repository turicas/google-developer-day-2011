#!/usr/bin/env python
#coding: utf-8

from funcoes import *
import unittest

class TestOrdemAlfabetica(unittest.TestCase):
	def test_apenas_uma_letra_iguais(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('m', 'm'), 0)


	def test_apenas_uma_letra_diferentes(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('m', 'b'), -1)


	def test_duas_letras_com_a_primeira_igual(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('mm', 'mb'), -1)


	def test_duas_letras_com_a_primeira_igual_ao_contrario(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('mb', 'mm'), 1)


	def test_palavras_de_tamanho_diferente_com_a_primeira_menor(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('mbg', 'mbgsw'), -1)


	def test_palavras_de_tamanho_diferente_com_a_primeira_maior(self):
		self.assertEqual(primeira_palavra_vem_primeiro_que_segunda('mbgsw', 'mbg'), 1)


class TestOrdemAlfabeticaNaClasse(unittest.TestCase):
	def test_apenas_uma_letra_iguais(self):
		primeira = 'm'
		segunda = 'm'
		lista = [primeira, segunda]
		ordena_palavras(lista)
		self.assertEqual(lista, [primeira, segunda])


	def test_apenas_uma_letra_diferentes(self):
		lista = ['m', 'b']
		ordena_palavras(lista)
		self.assertEqual(lista, ['m', 'b'])


	def test_com_duas_letras_sendo_a_primeira_igual_com_a_primeira_palavra_vindo_antes(self):
		primeira = 'mm'
		segunda = 'mb'
		lista = [primeira, segunda]
		ordena_palavras(lista)
		self.assertEqual(lista, [primeira, segunda])


	def test_com_duas_letras_sendo_a_primeira_igual_com_a_segunda_palavra_vindo_antes(self):
		primeira = 'mb'
		segunda = 'mm'
		lista = [primeira, segunda]
		ordena_palavras(lista)
		self.assertEqual(lista, [segunda, primeira])


	def test_com_palavras_de_tamanhos_diferentes(self):
		primeira = 'mbgsw'
		segunda = 'mbg'
		lista = [primeira, segunda]
		ordena_palavras(lista)
		self.assertEqual(lista, [segunda, primeira])


	def test_com_cinco_palavras_de_tamanhos_diferentes(self):
		lista_desordenada = ['mbgsw', 'mbg', 'dlj', 'qvhnc', 'mmm']
		lista_ordenada = ['mmm', 'mbg', 'mbgsw', 'qvhnc', 'dlj']
		ordena_palavras(lista_desordenada)
		self.assertEqual(lista_desordenada, lista_ordenada)


class TesteNumeros(unittest.TestCase):
	def test_numero_exemplo(self):
		self.assertEqual(converte_numero_googlon_para_decimal('fpk'), 6785)


unittest.main()
