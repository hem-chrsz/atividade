# Sistema de Análise de Risco - Fuzzy Logic

## Descrição do Projeto
Este projeto implementa um sistema de **Análise de Risco Bancário** utilizando **Lógica Fuzzy**. O sistema avalia o risco de clientes com base em três variáveis principais:
- **Histórico de Crédito**: Avalia o comportamento passado do cliente em relação aos pagamentos.
- **Renda Mensal**: Analisa a renda do cliente comparada à média dos clientes do banco.
- **Dívida Atual**: Calcula o valor da dívida em relação à renda do cliente.

Com essas variáveis, o sistema determina se o risco do cliente é **baixo**, **médio** ou **alto**, através de regras fuzzy. O projeto utiliza a biblioteca `scikit-fuzzy` e foi construído em Python.

## Instalação e Configuração

### 1. Clone o Repositório
Faça o clone do repositório para o seu ambiente local:
```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>


#2. Criação do Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências:
-python -m venv myenv

#3. Ative o Ambiente Virtual
Windows:
-myenv\Scripts\activate

#Caso o arquivo requirements.txt não esteja disponível, execute:
-pip install numpy scikit-fuzzy matplotlib

#5. Execução do Código
Execute o arquivo principal
-python nome do projeto


Funcionamento do Sistema
Variáveis de Entrada (Inputs)
As variáveis de entrada representam as características financeiras do cliente:

Histórico de Crédito: Classificado como ruim, regular, bom, ou excelente.
Renda Mensal: Classificada como baixa, média, ou alta.
Dívida Atual: Classificada como baixa, moderada, ou alta.
Essas variáveis foram modeladas como conjuntos fuzzy e representam a incerteza nas classificações.

Regras Fuzzy
O sistema utiliza pelo menos 5 regras fuzzy para determinar o risco do cliente. As regras são como as descritas abaixo:

Se o Histórico de Crédito é excelente e a Dívida Atual é baixa, então o Risco é baixo.
Se o Histórico de Crédito é ruim e a Dívida Atual é alta, então o Risco é alto.
Essas regras consideram diferentes combinações de entradas para classificar o risco adequadamente.

Variável de Saída (Output)
O output é a classificação de risco do cliente, que pode ser:

Baixo
Médio
Alto
O sistema utiliza defuzzificação para converter os valores fuzzy em uma saída numérica clara.

Exemplo de Uso
O código permite a entrada de valores numéricos para as variáveis de entrada e calcula o risco com base nas regras fuzzy definidas.

# Entrando com valores de teste
risco_sim.input['credito'] = 9.5
risco_sim.input['divida'] = 3.5

Visualização de Gráficos
O sistema gera gráficos fuzzy para visualização dos resultados. Ao rodar o projeto, será exibido um gráfico representando o nível de risco do cliente.

Observação
Certifique-se de ter o matplotlib instalado para exibir os gráficos corretamente. Caso contrário, utilize:
- pip install matplotlib
