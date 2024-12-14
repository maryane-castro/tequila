```
bottle-detector/
├── app/
│   ├── __init__.py               # Inicializador do módulo 'app'
│   ├── api/
│   │   ├── __init__.py           # Inicializador do módulo 'api'
│   │   ├── endpoints.py          # Endpoints da API Flask
│   │   ├── schemas.py            # Esquemas de validação (pydantic ou marshmallow)
│   ├── services/
│   │   ├── __init__.py           # Inicializador do módulo 'services'
│   │   ├── classify_service.py   # Lógica de inferência e manipulação do modelo
│   │   ├── preprocessing.py      # Pré-processamento das imagens
│   │   ├── logger.py             # Configuração de logs
│   ├── config.py                 # Configurações da aplicação (ex.: paths, API keys)
│   ├── models/
│   │   ├── model.h5              # Modelo treinado (exemplo: TensorFlow)
│   │   ├── onnx_model.onnx       # Modelo em formato ONNX (opcional)
│   ├── utils/
│       ├── __init__.py           # Inicializador do módulo 'utils'
│       ├── image_validator.py    # Validação de arquivos de entrada
│       ├── metrics.py            # Funções para métricas e monitoramento
│       ├── cache.py              # Configuração de cache (Redis ou local)
├── data/
│   ├── raw/                      # Dados brutos para treinamento e teste
│   │   ├── open/                 # Imagens de garrafas abertas
│   │   ├── closed/               # Imagens de garrafas fechadas
│   ├── processed/                # Dados pré-processados
├── notebooks/
│   ├── eda.ipynb                 # Notebook para análise exploratória dos dados
│   ├── model_training.ipynb      # Notebook para treinamento do modelo
├── tests/
│   ├── __init__.py               # Inicializador do módulo de testes
│   ├── test_api.py               # Testes dos endpoints da API
│   ├── test_services.py          # Testes de lógica de negócio (inferência, validação)
│   ├── test_integration.py       # Testes de integração (API + modelo)
├── docker/
│   ├── Dockerfile                # Arquivo Docker para o container principal
│   ├── docker-compose.yml        # Configuração para serviços adicionais (Redis, DB)
├── scripts/
│   ├── train_model.py            # Script para treinamento automatizado do modelo
│   ├── convert_to_onnx.py        # Script para converter o modelo para ONNX
│   ├── load_test.py              # Simulações de carga para a API
├── static/
│   ├── index.html                # Página inicial (se interface HTML for usada)
│   ├── css/                      # Arquivos de estilo CSS
│   ├── js/                       # Scripts JavaScript
├── .gitignore                    # Arquivos e pastas a serem ignorados no Git
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação do projeto
├── run.py                        # Ponto de entrada da aplicação Flask
```
