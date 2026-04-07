🧠 Tradutor com LLM (Gemini + LangChain)

Este projeto consiste em uma aplicação de tradução de textos baseada em Modelos de Linguagem (LLM). O sistema permite que o usuário insira um texto e receba automaticamente sua tradução, utilizando inteligência artificial para gerar resultados naturais e contextualizados.

A aplicação foi desenvolvida com foco em simplicidade e integração moderna de IA, utilizando uma API backend construída com FastAPI e orquestração de prompts via LangChain.

🚀 Tecnologias utilizadas

🐍 Python

⚡ FastAPI

🔗 LangChain

🤖 Google Gemini API


💡 Funcionalidades
Tradução automática de textos digitados pelo usuário
Uso de LLM para respostas mais naturais e contextuais
API REST para integração com outras aplicações
Estrutura simples e fácil de expandir

📦 Como funciona

O usuário envia um texto para a API, que é processado por uma cadeia (chain) do LangChain. Essa cadeia interage com o modelo Gemini, responsável por gerar a tradução com base no contexto fornecido.
