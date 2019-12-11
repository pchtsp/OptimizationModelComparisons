import lqcp_pyomo
from pyomo.environ import SolverFactory

solver = SolverFactory("gurobi")
solver.solve(lqcp_pyomo.model, options={"timelimit":0}, load_solutions=False, tee=True)
