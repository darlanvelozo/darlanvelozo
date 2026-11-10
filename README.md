<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <img src="./assets/banner-light.svg" width="100%" alt="Darlan Velozo — Full Stack Developer. Construo produtos SaaS e opero sistemas que não podem cair.">
</picture>

<p align="center">
  <a href="https://arminda.site"><img src="https://img.shields.io/badge/arminda.site-em_produção-2ea043?style=flat-square&labelColor=0d1117" alt="arminda.site em produção"></a>
  <a href="https://www.linkedin.com/in/darlan-velozo-81b52020a/"><img src="https://img.shields.io/badge/LinkedIn-Darlan_Velozo-0A66C2?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117" alt="LinkedIn"></a>
  <a href="mailto:darlanveloso14@gmail.com"><img src="https://img.shields.io/badge/E--mail-darlanveloso14@gmail.com-22d3ee?style=flat-square&logo=gmail&logoColor=white&labelColor=0d1117" alt="E-mail"></a>
  <a href="https://github.com/darlanvelozo/engenharia-telecom"><img src="https://img.shields.io/badge/Artigos-engenharia--telecom-a78bfa?style=flat-square&logo=readdotcv&logoColor=white&labelColor=0d1117" alt="Artigos"></a>
</p>

<br>

Sou desenvolvedor **full stack** e trabalho em duas frentes. Na primeira, **projeto produtos SaaS do zero**, com teste, CI e decisões de arquitetura registradas. Dois deles já estão em produção com clientes reais. Na segunda, **desenvolvo para um provedor de internet regional**, com integrações, automações e atendimento automatizado.

Comecei com Django em 2018, aos 15 anos, no técnico do IFPI, e uso a mesma stack em produção até hoje. São oito anos aprofundando uma tecnologia só. Meu método é **medir antes de decidir** e **documentar o que não é óbvio**.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/metrics-dark.svg">
  <img src="./assets/metrics-light.svg" width="100%" alt="8 anos de Django em produção; 3 SaaS no ar, 2 deles próprios; 694 testes no Arminda; 2 prefeituras usando o Arminda; checkout Pix próprio, sem gateway.">
</picture>

## Produtos

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://arminda.site">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/card-arminda-dark.svg">
          <img src="./assets/card-arminda-light.svg" width="100%" alt="Arminda — folha de pagamento e RH para prefeituras. Em produção em 2 municípios; eSocial validado no XSD oficial; multi-tenant por schema, 694 testes, CI.">
        </picture>
      </a>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/darlanvelozo/Vape_project">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/card-vape-dark.svg">
          <img src="./assets/card-vape-light.svg" width="100%" alt="PDV & Vitrine — SaaS de varejo multi-loja. PDV, caixa, estoque e vitrine online; checkout Pix sem gateway; reserva de estoque com lock de linha.">
        </picture>
      </a>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="./assets/card-hubtrix-dark.svg">
        <img src="./assets/card-hubtrix-light.svg" width="100%" alt="Hubtrix — CRM, marketing e CS para provedores de internet. 190+ commits no core; módulos de Cobrança e Analytics; integração com ERP, WhatsApp e LLMs.">
      </picture>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/darlanvelozo/blue_matrics">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="./assets/card-bluemetrics-dark.svg">
          <img src="./assets/card-bluemetrics-light.svg" width="100%" alt="BlueMetrics — BI B2B sobre o ERP Conta Azul. OAuth2, Row-Level Security, insights por IA, Stripe.">
        </picture>
      </a>
    </td>
  </tr>
</table>

<details>
<summary><b>Detalhes técnicos de cada produto</b></summary>
<br>

**Arminda.** É um substituto moderno para os sistemas legados de folha do setor público, com paridade funcional. Prefeituras migram sozinhas por um importador self-service que aceita vários fornecedores de origem. O eSocial está completo até o lote: geração, assinatura, eventos periódicos e transmissão. Cada município fica num schema próprio do PostgreSQL. O cálculo assíncrono roda em Celery + Redis. O front usa Vite, React 18, TypeScript, shadcn/ui e TanStack Query. A aplicação roda em VPS própria com gunicorn, Nginx e systemd. O projeto foi construído em 11 blocos sequenciais e está na `v0.42`.

**PDV & Vitrine.** Cada loja se cadastra sozinha e enxerga só os próprios dados. O sistema cobre PDV com leitor de código de barras e pagamento dividido, caixa com sangria e conferência, estoque com custo médio ponderado e extrato auditável, compras, financeiro e relatórios (curva ABC, giro e margem). No checkout Pix, o próprio sistema gera o BR Code estático do Banco Central e o testa contra o exemplo oficial. O estoque fica reservado com `SELECT … FOR UPDATE`, e há testes para a disputa pela última unidade e para o isolamento entre lojas. O changelog e as ADRs são versionados no repositório.

**Hubtrix.** Sou co-desenvolvedor do core de um SaaS multi-tenant usado por vários provedores. Construí o módulo de **Cobrança** (régua de cobrança e reconquista pós-cancelamento) e o de **Analytics** (jornada do bot de vendas e painel comercial). Também trabalho nas integrações com ERP, WhatsApp e provedores de IA.

**BlueMetrics.** Conecta ao ERP Conta Azul via OAuth2 e sincroniza os dados financeiros e comerciais. O isolamento por tenant é feito com Row-Level Security no PostgreSQL 16. Os insights são gerados pelo Claude e a cobrança passa pela Stripe. O front é em Next.js 15, com Docker e GitHub Actions.

</details>

## O que entrego

- **Produtos SaaS do zero ao deploy**: multi-tenant, autenticação e permissões, cobrança, testes, CI e operação em servidor próprio.
- **Integrações com ERPs e APIs de terceiros**: sincronização de dados, gateways de API com controle de acesso e documentação.
- **Automação de processos**: rotinas agendadas, réguas de comunicação e bots de atendimento e vendas no WhatsApp.
- **IA aplicada a produto**: LLMs para geração de insights, validação de documentos e assistentes conversacionais.
- **Dados e BI**: dashboards, indicadores comerciais e financeiros, análise de funil e carteira.
- **Conformidade brasileira**: eSocial, Pix (BR Code) e regras de folha do setor público.

## Onde colaboro

<table>
  <tr>
    <td width="72" align="center"><a href="https://github.com/Megalink-Telecom"><img src="https://github.com/Megalink-Telecom.png?size=96" width="48" alt="Megalink Telecom"></a></td>
    <td><b><a href="https://github.com/Megalink-Telecom">Megalink Telecom</a></b> · time de desenvolvimento<br><sub>Desenvolvo funcionalidades e reviso PRs da plataforma interna da empresa.</sub></td>
  </tr>
  <tr>
    <td align="center">🚀</td>
    <td><b>Hubtrix</b> · co-desenvolvedor do core<br><sub>Tenho 190+ commits num SaaS multi-tenant para provedores (Django 5.2, Channels, WebSocket, integração com LLMs).</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/CONSULTECHPI"><img src="https://github.com/CONSULTECHPI.png?size=96" width="48" alt="CONSULTECHPI"></a></td>
    <td><b><a href="https://github.com/CONSULTECHPI">CONSULTECHPI</a></b> · admin<br><sub>Consultoria em tecnologia. Responsável pelo site institucional.</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/jobstechorg"><img src="https://github.com/jobstechorg.png?size=96" width="48" alt="jobstechorg"></a></td>
    <td><b><a href="https://github.com/jobstechorg">jobstechorg</a></b> · admin<br><sub>Ferramentas de atendimento.</sub></td>
  </tr>
</table>

Também uso **engenharia assistida por IA** no dia a dia. Montei um painel de revisão de PRs que roda o Claude Code headless, em modo somente leitura, num worktree descartável. Ele confronta a especificação com o diff e só permite aprovar o commit exato que foi analisado.

## Stack

| Profundidade | Tecnologias |
|:--|:--|
| **Opero em produção** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white) ![DRF](https://img.shields.io/badge/DRF-A30000?style=flat-square&logo=django&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white) ![Celery](https://img.shields.io/badge/Celery-37814A?style=flat-square&logo=celery&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) |
| **Front-end** | ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![React](https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white) ![Tailwind](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white) ![TanStack Query](https://img.shields.io/badge/TanStack_Query-FF4154?style=flat-square&logo=reactquery&logoColor=white) ![Vue.js](https://img.shields.io/badge/Vue.js-35495E?style=flat-square&logo=vuedotjs&logoColor=4FC08D) |
| **Qualidade & entrega** | ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) ![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white) ![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black) |
| **IA & integrações** | ![Anthropic](https://img.shields.io/badge/Claude-191919?style=flat-square&logo=anthropic&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) ![Stripe](https://img.shields.io/badge/Stripe-635BFF?style=flat-square&logo=stripe&logoColor=white) ![WhatsApp](https://img.shields.io/badge/WhatsApp_API-25D366?style=flat-square&logo=whatsapp&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) |
| **Também uso** | ![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white) ![Laravel](https://img.shields.io/badge/Laravel-FF2D20?style=flat-square&logo=laravel&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white) ![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white) ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black) |

## Trajetória

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/timeline-dark.svg">
  <img src="./assets/timeline-light.svg" width="100%" alt="2018: Técnico em Informática no IFPI e 1º certificado em Django. Medalhista em olimpíadas de matemática, nacionais e internacionais. Graduação em Análise e Desenvolvimento de Sistemas no IFPI. Produção: sistemas de um provedor de internet. Hoje: produtos SaaS próprios.">
</picture>

> Olimpíada não é sobre matemática. É atacar um problema que você não sabe resolver, com tempo contado e sem consultar a resposta. É a mesma habilidade que se usa às duas da manhã com um serviço fora do ar.

## Escrevo sobre isso

Escrevo casos técnicos de integração em provedores de internet, sempre na estrutura **problema → medição → decisão → resultado**.

- [**Quando a API oficial é o caminho errado**](https://github.com/darlanvelozo/engenharia-telecom/blob/main/artigos/api-oficial-caminho-errado.md). Como decidir o caminho de uma integração medindo, e não por preferência.
- [**Sua documentação de API conta demais**](https://github.com/darlanvelozo/engenharia-telecom/blob/main/artigos/documentacao-por-escopo.md). Como filtrar a documentação pelo escopo do token.

<br>

<p align="center">
  <sub>Teresina, Piauí · aberto a conversas sobre produto, integrações e consultoria</sub><br>
  <a href="https://www.linkedin.com/in/darlan-velozo-81b52020a/">LinkedIn</a> ·
  <a href="mailto:darlanveloso14@gmail.com">E-mail</a> ·
  <a href="https://arminda.site">arminda.site</a>
</p>
