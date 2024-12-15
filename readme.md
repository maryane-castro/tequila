# Tequila 

## Estrutura de Diretórios

Este projeto possui a seguinte estrutura de diretórios:

```
.
├── api                   # Código da API
│   ├── app.py            # Arquivo principal da aplicação Flask
│   ├── best.pt           # Modelo treinado
│   ├── Dockerfile        # Dockerfile para containerizar a aplicação
│   ├── requirements.txt  # Dependências da API
│   └── templates         # Templates HTML
│       └── index.html    # Página principal
├── data                  # Scripts relacionados aos dados
│   └── download_data.py  # Script para baixar e preparar dados
├── notebooks             # Notebooks Jupyter para treinamento de modelos
│   └── model_training.ipynb # Notebook para treinar o modelo
├── readme.md             # Este arquivo de README
├── scripts               # Scripts auxiliares
│   ├── load_test.py      # Script para testar o desempenho da aplicação
│   ├── readme.md         # README para scripts
│   └── requirements.txt  # Dependências dos scripts
```

## Como Rodar o Projeto

### Requisitos

1. Python 3.11
2. Dependências especificadas nos arquivos `requirements.txt`.

### Instalar Dependências

Instale as dependências para a API e para os scripts:

```bash
pip install -r api/requirements.txt
pip install -r scripts/requirements.txt
```

### Rodando a API

Para rodar a API localmente, execute o seguinte comando:

```bash
cd api
python app.py
```

A aplicação estará disponível em [http://localhost:5000](http://localhost:5000).

### Treinamento do Modelo

Para treinar o modelo, abra o notebook `notebooks/model_training.ipynb` e siga as instruções. O modelo treinado será salvo como `best.pt`.

### Teste de Desempenho

Para rodar o teste de carga, execute o script `scripts/load_test.py`:

```bash
python scripts/load_test.py
```
