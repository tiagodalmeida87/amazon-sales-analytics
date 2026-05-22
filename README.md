# Amazon Sales Analytics - Projeto de Portfólio

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Power%20BI](https://img.shields.io/badge/Power%20BI-Integrado-orange) ![Moeda](https://img.shields.io/badge/Moeda-Real%20Brasileiro-green)

---

## 1. Título do Projeto

**Amazon Sales Analytics: Análise Exploratória de 1.465 Produtos com Insights Estratégicos para Otimização de E-commerce**.

Palavras-chave: E-commerce Analytics, Data Analysis, Python, Power BI, Business Intelligence, Data Visualization, Real Brasileiro

---

## 2. Imagem da Capa

![Dashboard Preview](https://via.placeholder.com/1200x400?text=Amazon+Analytics+Dashboard)

*Dashboard interativo exibindo métricas de faturamento, ratings e distribuição de preços em Real Brasileiro*

---

## 3. Problema de Negócio

A Amazon, como plataforma de e-commerce global, enfrenta desafios críticos na otimização de seu portfólio de produtos. Com milhões de itens disponíveis, gestores precisam entender padrões de preço, satisfação do cliente e oportunidades de crescimento. As principais questões de negócio são:

- **Como os descontos agressivos afetam a percepção de qualidade?** Existe um risco real de danos à marca ao oferecer descontos acima de 80%?
- **Quais categorias representam as maiores oportunidades de faturamento?** Onde devem ser concentrados os esforços de marketing e expansão de catálogo?
- **Qual é o impacto da "prova social" (número de avaliações) na confiança do consumidor?** Investir em programas de incentivo a reviews é mais eficaz que apenas reduzir preços?
- **Como a satisfação do cliente varia por faixa de preço?** Clientes que pagam mais são mais exigentes?

Essas questões afetam diretamente a estratégia de precificação, alocação de recursos de marketing e desenvolvimento de catálogo da plataforma.

---

## 4. Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de realizar uma **análise exploratória abrangente** de 1.465 produtos da Amazon, gerando insights acionáveis para otimizar a estratégia de e-commerce. Os objetivos específicos incluem:

1. **Entender padrões de preço e desconto:** Identificar como os descontos influenciam a satisfação do cliente
2. **Segmentar categorias por potencial:** Classificar categorias por faturamento, satisfação e oportunidades de crescimento
3. **Validar hipóteses de negócio:** Testar correlações entre preço, desconto, rating e volume de avaliações
4. **Gerar recomendações estratégicas:** Fornecer insights baseados em dados para decisões de negócio

O retorno financeiro esperado inclui: aumento de 15-20% no faturamento através de otimização de descontos, redução de 10% em custos de marketing através de segmentação mais precisa, e melhoria de 5% na satisfação do cliente através de estratégias baseadas em dados.

---

## 5. Estratégia da Solução

A solução foi desenvolvida seguindo uma metodologia de **Analytics em 5 Etapas**, garantindo rigor científico e entrega de valor em cada fase:

### Etapa 1: Análise da Estrutura e Qualidade dos Dados
Realizei uma auditoria completa da base de dados, identificando valores ausentes, duplicatas e inconsistências. A qualidade dos dados foi excelente, com apenas 0.14% de perda (2 registros sem rating_count) e zero duplicatas.

### Etapa 2: Definição de Hipóteses de Negócio
Formulamos 5 hipóteses testáveis baseadas em conhecimento de e-commerce:
- H1: Produtos com maiores descontos possuem ratings menores
- H2: Categorias de Electronics possuem maior faturamento
- H3: Existe correlação positiva entre número de avaliações e rating
- H4: O desconto não influencia diretamente a nota do produto
- H5: Produtos mais caros têm ratings mais rigorosos

### Etapa 3: Análise Exploratória (EDA)
Utilizamos Python com Pandas e Matplotlib para explorar distribuições, correlações e padrões nos dados. Geramos visualizações para testar cada hipótese.

### Etapa 4: Análise de Resultados e Insights
Consolidamos os achados em insights estratégicos acionáveis, validando ou refutando cada hipótese com base em evidências quantitativas.

### Etapa 5: Criação de Dashboard Interativo
Desenvolvemos um dashboard web interativo usando React + Recharts, permitindo exploração visual dos dados em tempo real com valores em Real Brasileiro.

---

## 6. Tecnologias Utilizadas

| Categoria | Tecnologia | Propósito |
|-----------|-----------|----------|
| **Linguagem de Programação** | Python 3.11 | Processamento e análise de dados |
| **Bibliotecas Python** | Pandas, NumPy | Manipulação e transformação de dados |
| **BI** | Power BI Desktop | Dashboard profissional para stakeholders |
| **Controle de Versão** | Git, GitHub | Versionamento e colaboração |
| **Documentação** | Markdown | Documentação técnica e executiva |
| **Conversão de Moeda** | Python | Conversão de INR para BRL (fator: 0,052) |

---

## 7. Etapas do Projeto

### Etapa 1: Análise da Estrutura da Base de Dados
Realizei uma auditoria completa da qualidade dos dados, incluindo verificação de tipos de dados, valores ausentes, duplicatas e outliers. Identificamos que a base possui 1.465 registros com 16 colunas, sendo todas as colunas numéricas carregadas como strings devido a símbolos especiais (₹, %, ,).

### Etapa 2: Definição de Hipóteses de Negócio
Formulei 5 hipóteses testáveis baseadas em conhecimento de e-commerce e comportamento do consumidor. Essas hipóteses guiaram toda a análise exploratória.

### Etapa 3: Análise Exploratória dos Dados (EDA)
Utilizei Python para limpar os dados, remover símbolos especiais e converter tipos. Convertemos valores de Rupee Indiano para Real Brasileiro usando fator de 0,052 (cotação do dia). Gerei visualizações de distribuições, correlações e relações entre variáveis.

### Etapa 4: Análise de Resultados e Geração de Insights
Consolidei os achados em 5 insights estratégicos acionáveis, cada um com recomendações específicas para gestores de produto e marketing.

### Etapa 5: Criação de Dashboard Interativo
Desenvolvi um dashboard responsivo usando Power BI, exibindo KPIs, gráficos interativos e filtros para exploração de dados com valores em **Real Brasileiro (R$)**.

---

## 8. Principais Insights

### Insight 1: O Poder Absoluto dos Eletrônicos
A categoria **Electronics** representa aproximadamente **70% do faturamento potencial total** (R$ 166.400,00 de R$ 237.955,95), apesar de representar apenas 22% dos produtos. Isso indica que eletrônicos são o motor financeiro da plataforma e devem ser o foco de estratégias de crescimento.

**Recomendação:** Implementar estratégias de cross-selling entre acessórios de baixo custo (R$ 10-50) e itens de alto valor (R$ 500-2.000) para aumentar o ticket médio.

### Insight 2: Descontos Agressivos Não Prejudicam Significativamente a Satisfação
Encontrei uma correlação negativa fraca (-0.16) entre percentual de desconto e rating. Produtos com descontos até 70% mantêm ratings praticamente iguais (4,1), enquanto apenas produtos com >80% de desconto mostram uma leve queda (3,9).

**Recomendação:** Descontos agressivos podem ser usados estrategicamente para aumentar volume sem comprometer a marca. Recomenda-se monitorar o sentimento das avaliações em produtos com >80% de desconto.

### Insight 3: A Importância da Prova Social
Produtos com mais de 10.000 avaliações mantêm um rating médio de 4,1, enquanto produtos com <1.000 avaliações têm rating médio de 3,9. Isso sugere que a "prova social" é um fator importante na confiança do consumidor.

**Recomendação:** Programas de incentivo a reviews (pequenos descontos, brindes) podem ser mais eficazes que apenas reduzir preços para atrair novos compradores.

### Insight 4: Oportunidades em Categorias Nicho
Categorias como **Office Products** (rating 4,3) e **Musical Instruments** (rating 4,3) têm alta satisfação, mas baixo volume de produtos (80 e 52 respectivamente). Essas categorias representam oportunidades de expansão com baixa competição interna.

**Recomendação:** Expandir o catálogo nessas categorias com 50-100 novos produtos e investir em marketing direcionado.

### Insight 5: Estratégia de Preços Previsível
A correlação quase perfeita entre preço real e preço com desconto (0,96) indica que a Amazon mantém uma política de descontos linear e previsível. Isso cria uma oportunidade para diferenciação através de "Preço Psicológico" ou pacotes.

**Recomendação:** Testar preços em 0.99 ou 0.95 para aumentar conversão. Implementar bundles estratégicos (ex: TV + Acessórios) para aumentar o ticket médio.

---

## 9. Resultados

### Resultados Quantitativos

| Métrica | Valor |
|---------|-------|
| Total de Produtos Analisados | 1.462 |
| Rating Médio | 4,10/5 |
| Faturamento Potencial | R$ 237.955,95 |
| Desconto Médio | 47,7% |
| Correlação Desconto-Rating | -0,16 |
| Correlação Popularidade-Rating | 0,10 |

### Resultados Qualitativos

**Acima da Expectativa Inicial:**
- A qualidade dos dados foi excelente (apenas 0.14% de perda).
- A correlação entre desconto e rating foi mais fraca que esperado, permitindo estratégias agressivas de desconto.
- A importância da "prova social" foi confirmada, validando investimentos em programas de reviews.

**Dentro da Expectativa:**
- A dominância de categoria "Electronics" foi confirmada.
- A existência de categorias nicho com alto potencial foi identificada.

**Abaixo da Expectativa:**
- Nenhum resultado significativamente abaixo das expectativas.

---

## 10. Conclusão

Este projeto demonstrou a importância da análise exploratória de dados para tomada de decisão estratégica em e-commerce. Os insights gerados fornecem uma base sólida para otimização de estratégias de precificação, alocação de recursos de marketing e desenvolvimento de catálogo.

A análise validou hipóteses críticas de negócio, particularmente a descoberta de que descontos agressivos não prejudicam significativamente a satisfação do cliente, abrindo novas oportunidades para estratégias de volume. A importância da "prova social" também foi confirmada, sugerindo que programas de incentivo a reviews podem ser mais eficazes que apenas reduzir preços.

O dashboard interativo desenvolvido permite que gestores explorem os dados em tempo real, facilitando a tomada de decisão baseada em dados. O relatório executivo fornece recomendações específicas e acionáveis para implementação imediata.

---

## 11. Próximos Passos

### Curto Prazo (0-3 meses)
1. Implementar programa de incentivo a reviews focado em produtos com <100 avaliações.
2. Otimizar estratégia de descontos em Electronics (manter entre 40-70%).
3. Monitorar sentimento em categorias nicho (Office Products, Musical Instruments).

### Médio Prazo (3-6 meses)
1. Expandir catálogo em categorias de alta satisfação (adicionar 50-100 produtos).
2. Implementar bundles estratégicos para aumentar ticket médio.
3. Testar preços psicológicos (0.99, 0.95) em categorias piloto.

### Longo Prazo (6-12 meses)
1. Implementar Machine Learning para recomendação de preços dinâmicos.
2. Criar dashboard de monitoramento em tempo real com alertas automáticos.
3. Desenvolver programa de fidelização baseado em dados de comportamento.

---

## Como Usar Este Projeto

### Pré-requisitos
- Python 3.11+
- Power BI Desktop (para visualizações avançadas)

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/amazon-analytics.git
cd amazon-analytics

# Instalar dependências Python
pip install pandas numpy matplotlib seaborn
```

### Executar Análise

```bash
# Executar script de análise com conversão para BRL
python etl_amazon_analysis.py
```

### Visualizar Resultados

- **Dashboard Web:** Acesse http://localhost:3000
- **Relatório Executivo:** Abra `Relatorio_Executivo_brl.pdf`

---

## Arquivos do Projeto

| Arquivo | Descrição |
|---------|-----------|
| `amazon.csv` | Base de dados original (1.465 produtos em INR) |
| `new_amazon.csv` | Base de dados limpa e convertida para BRL |
| `etl_amazon_analysis.py` | Script Python com conversão para Real Brasileiro |
| `Relatorio_Executivo_brl.pdf` | Relatório executivo em PDF (com valores em R$) |
| `sales_amazon.pbix` | Dashboard interativo (React) com valores em R$ |

---

## Conversão de Moeda

Todos os valores foram convertidos de Rupee Indiano (₹) para Real Brasileiro (R$) utilizando o fator de conversão **0,052**, com arredondamento para duas casas decimais.

**Exemplo de conversão:**
- ₹1.000 × 0,052 = R$ 52,00
- ₹10.000 × 0,052 = R$ 520,00

---

## Contato e Suporte

Para dúvidas ou sugestões sobre este projeto, entre em contato através de:
- **Email:** seu-email@exemplo.com
- **LinkedIn:** [Tiago Almeida](https://www.linkedin.com/in/tiago-l-almeida/)
- **GitHub:** [Tiago Almeida](https://github.com/tiagodalmeida87)

---

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

---

**Projeto desenvolvido como portfólio para demonstrar habilidades em Data Analytics, Python, Power BI e Business Intelligence com suporte a múltiplas moedas.**

*Última atualização: Maio de 2026 (Versão 2.0 - Com conversão para Real Brasileiro)*
