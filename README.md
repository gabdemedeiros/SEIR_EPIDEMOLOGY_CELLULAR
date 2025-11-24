# Modelagem Epidemiológica com Autômatos Celulares – SEIR aplicado à Conjuntivite Viral

Este repositório reúne o código e os artigos produzidos sobre o uso de **Autômatos Celulares (Cellular Automata – CA)** para simular o espalhamento de doenças de transmissão local, com foco em um **modelo SEIR** aplicado à conjuntivite viral.  
O objetivo é mostrar como os **AC podem representar de forma intuitiva, espacial e visual** a progressão de um surto epidemiológico.

---

## 📄 Artigos Completos

[Baixar cellular_automata.pdf](cellular_automata.pdf)
[Baixar cellular_automata.pdf](epidemiology.pdf)


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
