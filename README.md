# Modelagem Epidemiológica com Autômatos Celulares – SEIR aplicado à Conjuntivite Viral

Este repositório reúne o código e os artigos produzidos sobre o uso de **Autômatos Celulares (Cellular Automata – CA)** para simular o espalhamento de doenças de transmissão local, com foco em um modelo SEIR aplicado à conjuntivite viral.  
O objetivo é mostrar como os **AC podem representar de forma intuitiva, espacial e visual** a progressão de um surto epidemiológico.

---

## 📌 Como os artigos se conectam: Epidemiologia + Cellular Automata

O projeto é composto por dois textos principais:

### **1. Artigo Epidemiológico (foco na doença e no modelo SEIR)**
Este artigo apresenta:
- A dinâmica epidemiológica da conjuntivite viral  
- A estrutura SEIR tradicional (Suscetível, Exposto, Infectado, Recuperado)  
- Parâmetros como período de incubação, duração da infecção, transmissibilidade etc.  
- Como essas etapas se comportam na vida real  

Ele fornece a **base conceitual** da doença e explica por que o modelo SEIR é adequado.

### **2. Artigo de Autômato Celular (foco no modelo computacional)**
Este segundo texto aprofunda o uso de um **Autômato Celular 2D** como alternativa espacial ao SEIR clássico.  
Discute:
- Construção da grade
- Regras locais (vizinhança de Moore)
- Transições S → E → I → R no contexto de AC
- Emergência de padrões
- Visualização de clusters e frentes de transmissão

Enquanto o artigo sobre epidemiologia explica *o que* está sendo modelado,  
o artigo sobre automatos celulares explica *como* a dinâmica está sendo simulada computacionalmente.

Os dois juntos fornecem uma visão completa do problema:
> Epidemiologia teórica + Simulação espacial computacional



## ▶️ Como baixar e rodar o código

### **1. Clonar o repositório**

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

```

### **2. Criar ambiente virtual (opcional, recomendado)**

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

```
### **3. Rodar a simulação**

```bash
python simulacao_conjuntivite.py
```

Isso vai gerar:

  - A matriz SEIR ao longo das gerações

  - O mapa de cores baseado no colormap viridis
