# 📘 Assignment: APIs REST com FastAPI

## 🎯 Objective

Construir uma API REST simples usando o framework FastAPI, explorando criação de rotas, modelos de dados (Pydantic), validação automática, documentação interativa e boas práticas de organização de código.

Ao final, o estudante terá uma aplicação funcional com endpoints CRUD documentados automaticamente.

## 📝 Tasks

### 🛠️ Tarefa 1: Estrutura Inicial da API

#### Description
Configurar o projeto FastAPI com um aplicativo básico, incluindo um ponto de entrada (`main.py`), criação da instância `FastAPI`, e uma rota de verificação de saúde (`/health`). Definir um modelo Pydantic para um recurso simples (por exemplo, `Item`) e retornar dados fictícios.

#### Requirements
Completed program should:

- Ter arquivo `main.py` inicializando `FastAPI()`
- Expor rota GET `/health` retornando `{ "status": "ok" }`
- Definir modelo `Item` com campos: `id: int`, `name: str`, `price: float`, `in_stock: bool = True`
- Expor rota GET `/items` retornando lista de 2–3 itens fictícios
- Usar tipagem Pydantic correta e resposta JSON válida

### 🛠️ Tarefa 2: CRUD Básico para Itens

#### Description
Expandir a API adicionando operações CRUD em memória (sem banco de dados) para o recurso `Item`: criar, listar, buscar por ID, atualizar e remover. Implementar validação automática, códigos de status apropriados e lidar com erros (ex.: item não encontrado).

#### Requirements
Completed program should:

- Implementar endpoint POST `/items` aceitando JSON do `Item` (sem `id` fornecido; gerar incrementalmente)
- Implementar endpoint GET `/items/{item_id}` retornando item ou erro 404
- Implementar endpoint PUT `/items/{item_id}` para atualizar campos existentes
- Implementar endpoint DELETE `/items/{item_id}` retornando 204 em sucesso
- Usar lista in-memory para armazenar itens
- Garantir documentação automática visível em `/docs`
- Retornar códigos HTTP adequados (201 para criação, 404 quando não encontrado)

### 🛠️ Tarefa Extra (Opcional): Filtro e Busca

#### Description
Adicionar suporte a filtros simples nos itens para praticar query parameters: permitir filtrar por `in_stock` e buscar por fragmento de `name`.

#### Requirements
Completed program should:

- Aceitar query params opcionais em GET `/items`: `in_stock: bool`, `q: str`
- Filtrar corretamente combinando parâmetros
- Retornar lista (possivelmente vazia) sem erros
- Manter tipagem e validação correta

---
### ✅ Objetivos de Aprendizagem
- Compreender estrutura básica de um app FastAPI
- Praticar criação e validação de modelos com Pydantic
- Implementar endpoints REST com códigos HTTP apropriados
- Explorar documentação automática Swagger/OpenAPI

### 📦 Recursos Fornecidos
Starter `main.py` com estrutura inicial e comentários orientando evolução.

### 🗓️ Prazo
Entrega até: 2025-11-12

### 🚀 Próximos Passos
1. Instale dependências: `pip install fastapi uvicorn`
2. Execute localmente: `uvicorn main:app --reload`
3. Acesse: `http://localhost:8000/docs`

Boa prática: evolua em passos pequenos e teste cada endpoint com a doc automática.

Bom estudo! 💡