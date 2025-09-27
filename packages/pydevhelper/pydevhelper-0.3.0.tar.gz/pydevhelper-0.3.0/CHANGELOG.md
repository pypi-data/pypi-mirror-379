# Changelog

Todas as mudanças notáveis neste projeto serão documentadas aqui.  
O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)  
e este projeto adere a [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [0.3.0] - 2025-09-27

### 🚀 Novidades
- **Módulo `text_utils`** adicionado com várias funções utilitárias:
  - `slugify` com suporte a **Unicode** (`allow_unicode=True`);
  - Conversores `camel_to_snake` e `snake_to_camel`;
  - `normalize_whitespace` para limpar espaços extras;
  - `remove_html_tags` para sanitização de strings;
  - Extratores `extract_emails` e `extract_urls`.
- **Módulo `config`** revisado e expandido:
  - Suporte a **esquema tipado** com `EnvSpec` e `VarSpec`;
  - Integração opcional com `.env` via `python-dotenv`;
  - Suporte a `parser` customizado e `validator` por variável;
  - Mensagens de erro claras e estruturadas via `MissingEnvVarsError`;
  - Suporte a prefixos (`prefix="APP_"`) para ambientes complexos.

### ✅ Melhorias na qualidade do projeto
- Testes unitários expandidos para `config`:
  - Verificação de variáveis obrigatórias ausentes;
  - Defaults aplicados corretamente;
  - Falha de **casting** (`int("not-a-number")`) devidamente sinalizada;
  - Validação customizada falhando;
  - Prefixos de variáveis.
- Cobertura de testes ampliada → **maior robustez e confiança**.

---

## [0.2.0] - 2025-09-26

### 🚀 Novidades
- **Decorator `@retry`** para reexecução automática de funções em caso de exceções.
  - Suporte a `tries`, `delay`, `backoff` exponencial;
  - Permite especificar exceções capturadas (`exceptions=(Exception,)`);
  - Possibilidade de injetar `sleep_func` para testes (sem atrasos reais);
  - Logging de falhas e sucessos.

---

## [0.1.1] - 2025-09-25

### 🚀 Novidades
- **Logger colorido** com `setup_logging(colors=True)`;
- **Timer** com suporte a timestamp e template customizado.

### ✅ Qualidade
- Cobertura de testes completa para `logging` e `timer`.

---

## [0.1.0] - 2025-09-24

### 🚀 Versão inicial
- `setup_logging` para configuração simples de logs.
- `require_vars` para validação de variáveis de ambiente.
- `@timer` decorator para medir tempo de execução.
- `print_table` para renderizar dados em tabela de terminal.
