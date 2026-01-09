# 🌩️ Weather Alert Engine (Open-Meteo API)

> Consulta temperatura atual e previsão do tempo de qualquer cidade direto no terminal, com logs estruturados em JSON.


## 📌 Sobre

O **Weather Alert Engine** é um script em Python que permite ao usuário:

- Digitar o nome de uma cidade
- Converter esse nome em **coordenadas geográficas** (geocoding)
- Consultar a **temperatura atual em °C**
- Exibir a **previsão do tempo das próximas 48h**
- Registrar todas as consultas e eventos em **logs estruturados no formato JSON**
- Evitar imprevistos causados por mudanças climáticas inesperadas

Projeto feito para **aprendizado**, estudo de consumo de APIs e para resolver problemas do dia a dia relacionados à imprevisibilidade do clima.


## 🚀 Tecnologias utilizadas

- Python  
- Biblioteca `requests`  
- Manipulação de dados com `json`  
- Datas e horários com `datetime`  
- Controle de tempo com `time`  
- Processamento do sistema com `sys`  
- Sistema de logs em `JSON`
- **Open-Meteo API** (não requer API key)


## ⚙️ Funcionalidades

- [x] Consulta de temperatura atual por cidade
- [x] Previsão do tempo para 48h
- [x] Conversão de cidade → coordenadas geográficas
- [x] Interação via terminal
- [x] Geração de logs de execução em JSON
- [ ] Alertas automáticos para temperaturas extremas *(futuro)*
- [ ] Sugestões de roupas baseadas no clima *(futuro)*


## 📁 Estrutura do projeto

Weather-Alert-Engine/
│
├── engine.log # Pasta onde os logs JSON são salvos
├── engine.py # Função engine
├── geo.py # Pega dados geográficos
├── log.py # Função que cria o log JSON
├── main.py # Script principal
├── README.md # Documentação do projeto
├── rules.py # Regras com boa escalabilidade
├── weather.py # Função que pega o clima atual e as previsões
└── requirements.txt # Dependências


## ▶️ Como executar o projeto

```bash
git clone https://github.com/gabrielribamar/Weather-Alert-Engine.git
cd Weather-Alert-Engine
pip install requests
python main.py
