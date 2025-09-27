# ☀️ Energia Solar - ETL + Dashboard

Este projeto realiza um processo **ETL ** em dados de energia solar, armazena os dados em um **banco PostgreSQL** e disponibiliza uma visualização interativa através de um **dashboard com Streamlit**.

---

## 🚀 Tecnologias utilizadas
- **Python 3.10+**
- **Pandas** → manipulação de dados
- **SQLAlchemy** → conexão com banco de dados
- **PostgreSQL** → persistência dos dados
- **Streamlit** → criação do dashboard



## 📂 Estrutura do projeto
``` 
📦 Energia_Solar_ETL
 ┣ 📜 main.py              # Arquivo principal
 ┣ 📜 etl.py               # Funções de extração e transformação
 ┣ 📜 db.py                # Conexão com PostgreSQL
 ┣ 📜 dashboard.py         # Interface interativa com Streamlit
 ┣ 📜 DataModel.xlsx       # Arquivo de dados de entrada
 ┣ 📜 dependencias.txt     # Dependências do projeto
 ┗ 📜 README.md            # Este arquivo
```


## ⚙️ Pré-requisitos
1. **Python 3.10 ou superior** instalado  
2. **PostgreSQL** em execução  
3. Criar um banco de dados chamado `etl_db` no PostgreSQL:
````
CREATE DATABASE etl_db;
````
4. Ajustar os dados de conexão no arquivo `db.py`:  
``
url = "postgresql://usuario:senha@localhost:5432/etl_db"
``
---

## 🔧 Instalação
Clone o repositório:
````
git clone https://github.com/ThiagoCh12/Energia_Solar_ETL.git
cd Energia_Solar_ETL
````
Crie um ambiente virtual e ative:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate  # Windows
```
Caso o windows apresente um erro de acesso nao autorizado, rode:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate 
```

Instale as dependências:
```
pip install -r dependencias.txt
```
---

## ▶️ Como executar

### 1. Iniciar o dashboard interativo:
````
streamlit run main.py
````
Acesse no navegador: 👉 http://localhost:8501

---

## 📊 Funcionalidades do Dashboard
- **Home** → Métricas principais (maior/menor rendimento, geração total, etc.)  
- **Planilha** → Exibe os dados da planilha  
- **Gráfico de Barras** → Evolução do rendimento do inversor  
- **Gráfico Personalizado** → Usuário escolhe colunas para gerar gráficos dinâmicos  

---

## 👨‍💻 Autor

Thiago Chagas 







