import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Novas instâncias de Antecedent/Consequent
credito = ctrl.Antecedent(np.arange(0, 11, 1), 'credito')
divida = ctrl.Antecedent(np.arange(0, 11, 1), 'divida')
renda = ctrl.Antecedent(np.arange(0, 11, 1), 'renda')  # Definindo a variável renda
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Preenchendo as funções de pertinência
credito.automf(names=['ruim', 'regular', 'bom', 'excelente'])
divida.automf(names=['baixa', 'moderada', 'alta'])
renda.automf(names=['baixa', 'media', 'alta'])  # Funções de pertinência para renda
risco.automf(names=['baixo', 'medio', 'alto'])

# Regras
rule1 = ctrl.Rule(credito['excelente'] & divida['baixa'], risco['baixo'])
rule2 = ctrl.Rule(credito['ruim'] & divida['alta'], risco['alto'])
rule3 = ctrl.Rule(credito['bom'] & renda['alta'] & divida['moderada'], risco['medio'])
rule4 = ctrl.Rule(credito['regular'] & renda['baixa'] & divida['alta'], risco['alto'])
rule5 = ctrl.Rule(credito['ruim'] & renda['alta'] & divida['baixa'], risco['medio'])

# Sistema de controle e simulação
risco_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
risco_sim = ctrl.ControlSystemSimulation(risco_ctrl)

# Entrando com alguns valores para teste
risco_sim.input['credito'] = 9.5
risco_sim.input['divida'] = 3.5
risco_sim.input['renda'] = 7.0  # Adicionando o valor para renda

# Calculando o resultado
risco_sim.compute()
print(risco_sim.output['risco'])

# Visualizando o gráfico
risco.view(sim=risco_sim)
plt.show()
