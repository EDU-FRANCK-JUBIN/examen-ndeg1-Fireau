from skfuzzy import control as ctrl
import skfuzzy as fuzz
import numpy as np


error = ctrl.Antecedent(np.arange(-4, 4, 1), 'error')
error_dot = ctrl.Antecedent(np.arange(-10, 10, 1), 'error_dot')
percent_output = ctrl.Consequent(np.arange(-100, 100, 1), 'percent_output')

error_name = ['too_cold', 'just_right', 'too_hot']
error_dot_name = ['getting_colder', 'no_change', 'getting_hotter']

error.automf(names=error_name)
error_dot.automf(names=error_dot_name)

error.view()
error_dot.view()

percent_output['cool'] = fuzz.trimf(percent_output.universe, [-100, -50, 0])
percent_output['do_nothing'] = fuzz.trimf(
    percent_output.universe, [-50, 0, 50])
percent_output['heat'] = fuzz.trimf(percent_output.universe, [0, 50, 100])


percent_output.view()

# Rule Application
rule1 = ctrl.Rule(error['too_hot'] &
                  error_dot['getting_colder'], percent_output['cool'])
rule2 = ctrl.Rule(error['just_right'] &
                  error_dot['getting_colder'], percent_output['heat'])
rule3 = ctrl.Rule(error['too_cold'] &
                  error_dot['getting_colder'], percent_output['heat'])
rule4 = ctrl.Rule(error['too_hot'] &
                  error_dot['no_change'], percent_output['cool'])
rule5 = ctrl.Rule(error['just_right'] &
                  error_dot['no_change'], percent_output['do_nothing'])
rule6 = ctrl.Rule(error['too_cold'] &
                  error_dot['no_change'], percent_output['heat'])
rule7 = ctrl.Rule(error['too_hot'] &
                  error_dot['getting_hotter'], percent_output['cool'])
rule8 = ctrl.Rule(error['just_right'] &
                  error_dot['getting_hotter'], percent_output['cool'])
rule9 = ctrl.Rule(error['too_cold'] &
                  error_dot['getting_hotter'], percent_output['heat'])

temperature_ctrl = ctrl.ControlSystem(
    rules=[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
temperature = ctrl.ControlSystemSimulation(temperature_ctrl)


error = float(input("Enter error [-4/ 4]"))
error_dot = float(input("Enter error_dot [-10 / 10]"))


temperature.input['error_dot'] = error_dot
temperature.input['error'] = error

temperature.compute()

percent_output.view(sim=temperature)
