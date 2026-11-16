
# 🌤️ WeatherHub

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Open-Meteo](https://img.shields.io/badge/API-Open--Meteo-2196F3?style=flat-square)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square)

**WeatherHub** é uma aplicação de linha de comando (CLI) desenvolvida em Python para consultar informações meteorológicas de cidades ao redor do mundo utilizando a API pública [Open-Meteo](https://open-meteo.com/).

O projeto tem como objetivo oferecer uma central de meteorologia simples e acessível, permitindo consultar condições climáticas, acompanhar previsões e, futuramente, identificar os melhores dias para atividades ao ar livre.

## ✨ Funcionalidades

### Disponíveis

- 🔎 **Busca de cidades:** localização de cidades pelo nome, com informações geográficas.
- 🌡️ **Clima atual:** consulta de temperatura e sensação térmica.
- 💧 **Umidade relativa do ar:** acompanhamento das condições de umidade.
- 💨 **Velocidade do vento:** consulta da velocidade atual do vento.
- 🖥️ **Interface CLI:** menu interativo para navegação pelo terminal.

### Planejadas

- [ ] Previsão meteorológica para os próximos dias.
- [ ] Comparação das condições climáticas entre cidades.
- [ ] Alertas de chuva e precipitação.
- [ ] Identificação dos melhores horários para atividades ao ar livre.
- [ ] Recomendação automática do melhor dia para passeios, considerando as condições meteorológicas.

> **Nota:** o projeto está em desenvolvimento. As funcionalidades planejadas serão implementadas progressivamente.

## 🛠️ Tecnologias

| Tecnologia | Utilização |
|------------|------------|
| Python 3.10+ | Linguagem principal |
| Requests | Comunicação HTTP com APIs externas |
| Pydantic | Modelagem e validação dos dados |
| Open-Meteo | Consulta de dados meteorológicos |
| Open-Meteo Geocoding | Busca de cidades e coordenadas geográficas |

## 🚀 Instalação e execução

### Pré-requisitos

- Python 3.10 ou superior
- pip
- Conexão com a internet

### 1. Clone o repositório

```bash
git clone https://github.com/BrunoRS17/weatherhub.git
cd weatherhub
```

### 2. Crie um ambiente virtual

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app/main.py
```

## 💻 Como utilizar

Ao executar a aplicação, será apresentado um menu interativo:

```text
===WeatherHub===
1. Buscar Cidade
2. Consultar clima atual
0. Sair
```

### Buscar cidade

Selecione a opção `1` e informe o nome da cidade desejada.

**Exemplo de saída:**

```text
Digite o nome da cidade: Campinas

Campinas - Brasil
Latitude: -22.9056°
Longitude: -47.0608°
```

### Consultar clima atual

Selecione a opção `2` e informe a cidade desejada.

**Exemplo de saída (valores ilustrativos):**

```text
Digite o nome da cidade: Campinas

Campinas - Clima Atual
Temperatura: 25.0 °C
Sensação Térmica: 26.0 °C
Umidade: 65.0%
Velocidade do Vento: 12.0 km/h
```

Os valores meteorológicos são obtidos dinamicamente e podem variar conforme o momento da consulta.

## 🌐 Integração com Open-Meteo

O WeatherHub utiliza a [Open-Meteo](https://open-meteo.com/), que disponibiliza dados meteorológicos por meio de APIs HTTP.

A integração atual utiliza dois serviços:

**Geocoding API**

Responsável por localizar cidades e retornar informações como nome, país, latitude e longitude.

**Forecast API**

Responsável por consultar informações meteorológicas com base nas coordenadas geográficas.


## 🗺️ Roadmap

O desenvolvimento está organizado em etapas incrementais. Novas funcionalidades serão adicionadas conforme a evolução do projeto.

## 👨‍💻 Autor

**Bruno Ribeiro**

[GitHub](https://github.com/BrunoRS17) • [Portfólio](https://bruno-software.vercel.app/)
