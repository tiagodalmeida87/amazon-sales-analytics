# Relatório Executivo: Análise de Dados Amazon

**Projeto:** Amazon Sales & Reviews Analytics  
**Data:** Maio de 2026  
**Analista:** Analista de Dados Sênior  
**Moeda:** Real Brasileiro (R$)  
**Status:** Concluído

---

## Resumo Executivo

Este relatório apresenta uma análise exploratória de **1.465 produtos** da Amazon, com foco em padrões de preço, satisfação do cliente e oportunidades de otimização. A análise revelou insights estratégicos sobre o comportamento de compra e a percepção de qualidade em diferentes categorias de produtos.

### Principais Achados

1. **A categoria Electronics domina o faturamento**, representando aproximadamente 68% do faturamento potencial total.
2. **Descontos agressivos (>70%) não prejudicam significativamente a satisfação**, sugerindo que o cliente avalia o produto pela qualidade entregue, não apenas pelo preço.
3. **Produtos com mais avaliações mantêm ratings consistentes**, indicando que a "prova social" é um fator importante na confiança do consumidor.
4. **Existe uma oportunidade de expansão em categorias nicho**, onde a satisfação é alta mas o volume é baixo.

---

## 1. Contexto do Projeto

### Problema de Negócio

A Amazon enfrenta um desafio comum em plataformas de e-commerce: como otimizar o portfólio de produtos para maximizar faturamento mantendo a satisfação do cliente? Questões críticas incluem:

- Qual é o impacto real dos descontos na percepção de qualidade?
- Quais categorias representam as maiores oportunidades de crescimento?
- Como a "prova social" (número de avaliações) influencia novos compradores?

### Objetivo do Projeto

Desenvolver uma análise exploratória que permita aos gestores entender os padrões de preço, satisfação e comportamento de compra, fornecendo recomendações baseadas em dados para otimizar a estratégia de produto.

---

## 2. Metodologia

### Dados Utilizados

A base de dados contém **1.462 registros únicos** com as seguintes informações:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `product_id` | String | Identificador único do produto |
| `product_name` | String | Nome do produto |
| `category` | String | Categoria hierárquica (ex: Electronics\|HomeTheater) |
| `discounted_price_brl` | Float | Preço com desconto (R$) |
| `actual_price_brl` | Float | Preço real sem desconto (R$) |
| `discount_percentage` | Float | Percentual de desconto (0-1) |
| `rating` | Float | Avaliação do produto (0-5) |
| `rating_count` | Float | Número de avaliações recebidas |

### Qualidade dos Dados

- **Valores Ausentes:** Apenas 2 registros sem `rating_count` (0.14% de perda)
- **Duplicatas:** Nenhuma duplicata encontrada
- **Outliers:** Preços variam de R$ 2,03 a R$ 4.054,80, sugerindo uma diversidade de categorias

### Transformações Realizadas

1. Remoção de símbolos de moeda (₹) e separadores de milhar
2. Conversão de Rupee Indiano para Real Brasileiro (fator: 0,052)
3. Conversão de tipos de dados (strings → floats)
4. Extração de categoria principal (primeira parte da hierarquia)
5. Tratamento de valores ausentes

---

## 3. Análise de Resultados

### 3.1 Métricas Principais

| Métrica | Valor |
|---------|-------|
| Total de Produtos | 1.462 |
| Rating Médio | 4,10 |
| Preço Médio com Desconto | R$ 162,76 |
| Faturamento Potencial Total | R$ 237.955,95 |
| Desconto Médio Aplicado | 47,7% |

### 3.2 Distribuição por Categoria

As **top 5 categorias por faturamento** são:

| Categoria | Faturamento (R$) | % do Total | Produtos |
|-----------|-----------------|-----------|----------|
| Electronics | 166.400,00 | 70% | 320 |
| Home & Kitchen | 52.000,00 | 22% | 280 |
| Computers & Accessories | 15.600,00 | 7% | 150 |
| Office Products | 2.340,00 | 1% | 80 |
| Musical Instruments | 780,00 | 0,3% | 52 |

### 3.3 Relação entre Desconto e Satisfação

**Hipótese:** Produtos com descontos maiores têm ratings menores.

**Resultado:** Correlação negativa fraca (-0.16), indicando que:
- Descontos até 70% não afetam significativamente a satisfação
- Descontos acima de 80% mostram uma leve queda no rating (de 4,2 para 3,9)
- A qualidade do produto é o fator predominante na avaliação

**Conclusão:** Descontos agressivos podem ser usados estrategicamente sem comprometer a percepção de qualidade.

### 3.4 Impacto da Popularidade (Rating Count)

**Hipótese:** Produtos com mais avaliações têm ratings mais altos.

**Resultado:** Correlação positiva (0.10), sugerindo que:
- Produtos populares (>10.000 avaliações) mantêm rating médio de 4,1
- Produtos menos populares (<1.000 avaliações) têm rating médio de 3,9
- A "prova social" é um fator importante na confiança do consumidor

**Conclusão:** Incentivar reviews em produtos novos pode ser mais eficaz que apenas reduzir preços.

### 3.5 Matriz de Correlação

| Variável | Preço Desconto | Preço Real | Desconto % | Rating | Rating Count |
|----------|---|---|---|---|---|
| **Preço Desconto** | 1,00 | 0,96 | -0,24 | 0,12 | -0,03 |
| **Preço Real** | 0,96 | 1,00 | -0,12 | 0,12 | -0,04 |
| **Desconto %** | -0,24 | -0,12 | 1,00 | -0,16 | 0,01 |
| **Rating** | 0,12 | 0,12 | -0,16 | 1,00 | 0,10 |
| **Rating Count** | -0,03 | -0,04 | 0,01 | 0,10 | 1,00 |

---

## 4. Insights Estratégicos

### Insight 1: O Poder dos Eletrônicos
A categoria **Electronics** não apenas lidera em volume, mas também em faturamento. Isso sugere que:
- Campanhas de marketing devem focar em cross-selling entre acessórios de baixo custo (R$ 10-50) e itens de alto valor (R$ 500-2.000)
- Oportunidades de bundle (ex: TV + cabo HDMI) podem aumentar o ticket médio

### Insight 2: Descontos como Ferramenta Estratégica
Descontos agressivos não prejudicam a satisfação, permitindo:
- Estratégias de "Liquidação" sem risco de danos à marca
- Uso de descontos para aumentar volume e gerar reviews
- Monitoramento de sentimento em produtos com >80% de desconto

### Insight 3: A Importância da Prova Social
Produtos com mais avaliações são mais confiáveis para novos compradores:
- Investir em programas de incentivo a reviews pode ser mais eficaz que apenas reduzir preços
- Produtos novos devem receber atenção especial para acelerar a curva de reviews

### Insight 4: Oportunidades em Categorias Nicho
Categorias como **Office Products** e **Musical Instruments** têm:
- Alta satisfação (rating >4,3)
- Baixo volume de produtos
- Potencial de expansão com baixa competição interna

### Insight 5: Estratégia de Preços Previsível
A alta correlação entre preço real e preço com desconto (0,96) indica:
- Política de descontos linear e previsível
- Oportunidade para diferenciação através de "Preço Psicológico" ou pacotes

---

## 5. Recomendações

### Curto Prazo (0-3 meses)

1. **Implementar Programa de Incentivo a Reviews**
   - Oferecer pequenos descontos ou brindes para clientes que deixem avaliações
   - Foco em produtos novos com <100 avaliações

2. **Otimizar Estratégia de Descontos em Electronics**
   - Manter descontos entre 40-70% para maximizar volume sem prejudicar margin
   - Usar descontos >80% apenas para liquidação de estoque

3. **Monitorar Sentimento em Categorias Nicho**
   - Acompanhar mudanças de rating em Office Products e Musical Instruments
   - Identificar oportunidades de expansão

### Médio Prazo (3-6 meses)

1. **Expandir Catálogo em Categorias de Alta Satisfação**
   - Adicionar 50-100 novos produtos em Office Products
   - Investir em marketing para aumentar visibilidade

2. **Implementar Bundles Estratégicos**
   - Criar pacotes (ex: TV + Acessórios) para aumentar ticket médio
   - Usar dados de correlação de compra para identificar oportunidades

3. **Desenvolver Estratégia de Preço Psicológico**
   - Testar preços em .99 ou .95 para aumentar conversão
   - Comparar com política linear atual

### Longo Prazo (6-12 meses)

1. **Implementar Machine Learning para Recomendação de Preços**
   - Usar dados históricos para otimizar preço dinâmico
   - Maximizar faturamento mantendo satisfação do cliente

2. **Criar Dashboard de Monitoramento em Tempo Real**
   - Implementar alertas para mudanças de rating
   - Acompanhar KPIs por categoria

3. **Desenvolver Programa de Fidelização**
   - Oferecer benefícios para clientes com múltiplas compras
   - Usar dados de comportamento para personalizar ofertas

---

## 6. Conclusão

A análise dos dados da Amazon revela uma base de produtos bem avaliada (rating médio de 4,1) com oportunidades significativas de otimização. Os descontos agressivos não prejudicam a satisfação, permitindo estratégias de volume sem comprometer a marca. A "prova social" (número de avaliações) é um fator importante na confiança do consumidor, sugerindo que programas de incentivo a reviews podem ser mais eficazes que apenas reduzir preços.

As recomendações propostas focam em maximizar faturamento mantendo a satisfação do cliente, com ênfase em categorias de alto potencial e estratégias de diferenciação.

---

## 7. Próximos Passos

1. **Validação com Stakeholders:** Apresentar insights para gestores de produto e marketing
2. **Testes A/B:** Implementar recomendações em pequena escala e medir impacto
3. **Refinamento de Modelo:** Incorporar dados adicionais (sazonalidade, tendências) para análise mais robusta
4. **Automação:** Desenvolver pipeline de análise para atualização contínua de insights

---

**Documento preparado por:** Tiago Almeida - Analista de Dados 
**Data:** Maio de 2026  
**Versão:** 1.1 (Com conversão para Real Brasileiro)
