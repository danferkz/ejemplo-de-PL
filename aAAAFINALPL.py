
from ortools.linear_solver import pywraplp

def SOLpldos_dos_1_1_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_1_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        solver = pywraplp.Solver.CreateSolver('GLOP')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_1_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_1_MAX_mas())
    else:
        print(SOLpldos_dos_1_1_MAX_men())

def SOLpldos_dos_1_2_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        solver = pywraplp.Solver.CreateSolver('GLOP')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_2_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_2_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_2_MAX_mas())
    else:
        print(SOLpldos_dos_1_2_MAX_men())

def SOLpldos_dos_1_3_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_3_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_3_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_3_MAX_mas())
    else:
        print(SOLpldos_dos_1_3_MAX_men())

def SOLpldos_dos_1_4_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_4_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_4_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_4_MAX_mas())
    else:
        print(SOLpldos_dos_1_4_MAX_men())


def SOLpldos_dos_2_1_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_1_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_1_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_1_MAX_mas())
    else:
        print(SOLpldos_dos_2_1_MAX_men())

def SOLpldos_dos_2_2_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_2_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_2_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_2_MAX_mas())
    else:
        print(SOLpldos_dos_2_2_MAX_men())

def SOLpldos_dos_2_3_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_3_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_3_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_3_MAX_mas())
    else:
        print(SOLpldos_dos_2_3_MAX_men())

def SOLpldos_dos_2_4_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_4_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_4_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_4_MAX_mas())
    else:
        print(SOLpldos_dos_2_4_MAX_men())


def SOLpldos_dos_3_1_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_1_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_1_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_1_MAX_mas())
    else:
        print(SOLpldos_dos_3_1_MAX_men())

def SOLpldos_dos_3_2_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_2_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_2_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_2_MAX_mas())
    else:
        print(SOLpldos_dos_3_2_MAX_men())

def SOLpldos_dos_3_3_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_3_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_3_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_3_MAX_mas())
    else:
        print(SOLpldos_dos_3_3_MAX_men())

def SOLpldos_dos_3_4_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_4_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_4_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_4_MAX_mas())
    else:
        print(SOLpldos_dos_3_4_MAX_men())


def SOLpldos_dos_4_1_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_1_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_1_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_1_MAX_mas())
    else:
        print(SOLpldos_dos_4_1_MAX_men())

def SOLpldos_dos_4_2_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_2_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_2_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_2_MAX_mas())
    else:
        print(SOLpldos_dos_4_2_MAX_men())

def SOLpldos_dos_4_3_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_3_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_3_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_3_MAX_mas())
    else:
        print(SOLpldos_dos_4_3_MAX_men())

def SOLpldos_dos_4_4_MAX_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_4_MAX_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_4_MAX():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_4_MAX_mas())
    else:
        print(SOLpldos_dos_4_4_MAX_men())




def lsitopcio_max_dd():
    listaOpciones = ['____ * X1 + ____ * X2 <= ____',
                     '____ * X1 - ____ * X2 <= ____',
                     '____ * X1 + ____ * X2 >= ____',
                     '____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    print(xuno)
    print(yuno)
    
    if xuno==1 and yuno==1:
        print(f'{SOLpldos_dos_1_1_MAX()}')
    elif xuno==1 and yuno==2:
        print(f'{SOLpldos_dos_1_2_MAX()}')
    elif xuno==1 and yuno==3:
        print(f'{SOLpldos_dos_1_3_MAX()}')
    elif xuno==1 and yuno==4:
        print(f'{SOLpldos_dos_1_4_MAX()}')
    elif xuno==2 and yuno==1:
        print(f'{SOLpldos_dos_2_1_MAX()}')
    elif xuno==2 and yuno==2:
        print(f'{SOLpldos_dos_2_2_MAX()}')
    elif xuno==2 and yuno==3:
        print(f'{SOLpldos_dos_2_3_MAX()}')
    elif xuno==2 and yuno==4:
        print(f'{SOLpldos_dos_2_4_MAX()}')
    elif xuno==3 and yuno==1:
        print(f'{SOLpldos_dos_3_1_MAX()}')
    elif xuno==3 and yuno==2:
        print(f'{SOLpldos_dos_3_2_MAX()}')
    elif xuno==3 and yuno==3:
        print(f'{SOLpldos_dos_3_3_MAX()}')
    elif xuno==3 and yuno==4:
        print(f'{SOLpldos_dos_3_4_MAX()}')
    elif xuno==4 and yuno==1:
        print(f'{SOLpldos_dos_4_1_MAX()}')
    elif xuno==4 and yuno==2:
        print(f'{SOLpldos_dos_4_2_MAX()}')
    elif xuno==4 and yuno==3:
        print(f'{SOLpldos_dos_4_3_MAX()}')
    elif xuno==4 and yuno==4:
        print(f'{SOLpldos_dos_4_4_MAX()}')
        
####################################################################################################################################

def SOLpldos_dos_1_1_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_1_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_1_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_1_MIN_mas())
    else:
        print(SOLpldos_dos_1_1_MIN_men())

def SOLpldos_dos_1_2_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_2_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_2_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_2_MIN_mas())
    else:
        print(SOLpldos_dos_1_2_MIN_men())

def SOLpldos_dos_1_3_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_3_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_3_MIN():
    print("Funcion Max:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_3_MIN_mas())
    else:
        print(SOLpldos_dos_1_3_MIN_men())

def SOLpldos_dos_1_4_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_4_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_1_4_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_1_4_MIN_mas())
    else:
        print(SOLpldos_dos_1_4_MIN_men())


def SOLpldos_dos_2_1_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_1_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_1_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_1_MIN_mas())
    else:
        print(SOLpldos_dos_2_1_MIN_men())

def SOLpldos_dos_2_2_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_2_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_2_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_2_MIN_mas())
    else:
        print(SOLpldos_dos_2_2_MIN_men())

def SOLpldos_dos_2_3_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_3_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_3_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_3_MIN_mas())
    else:
        print(SOLpldos_dos_2_3_MIN_men())

def SOLpldos_dos_2_4_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_4_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_2_4_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_2_4_MIN_mas())
    else:
        print(SOLpldos_dos_2_4_MIN_men())


def SOLpldos_dos_3_1_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_1_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_1_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_1_MIN_mas())
    else:
        print(SOLpldos_dos_3_1_MIN_men())

def SOLpldos_dos_3_2_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_2_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_2_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_2_MIN_mas())
    else:
        print(SOLpldos_dos_3_2_MIN_men())

def SOLpldos_dos_3_3_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_3_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_3_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_3_MIN_mas())
    else:
        print(SOLpldos_dos_3_3_MIN_men())

def SOLpldos_dos_3_4_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_4_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_3_4_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_3_4_MIN_mas())
    else:
        print(SOLpldos_dos_3_4_MIN_men())


def SOLpldos_dos_4_1_MIN_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_1_MIN_men():
    print("FuncionMAX:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_1_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_1_MIN_mas())
    else:
        print(SOLpldos_dos_4_1_MIN_men())

def SOLpldos_dos_4_2_MIN_mas():
    print("FuncionMAX:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMAX:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_2_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIn:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_2_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_2_MIN_mas())
    else:
        print(SOLpldos_dos_4_2_MIN_men())

def SOLpldos_dos_4_3_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_3_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_3_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_3_MIN_mas())
    else:
        print(SOLpldos_dos_4_3_MIN_men())

def SOLpldos_dos_4_4_MIN_mas():
    print("FuncionMIN:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_4_MIN_men():
    print("FuncionMIN:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"FuncionMIN:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    tre=int(input('___x1: '))
    cua=int(input('___x2: '))
    cic=int(input('>=__: '))
    print(f"restricion 2:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('>=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Minimize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a
def SOLpldos_dos_4_4_MIN():
    print("Funcion Min:_x1 (_) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_dos_4_4_MIN_mas())
    else:
        print(SOLpldos_dos_4_4_MIN_men())

def lsitopcio_min_dd():
    listaOpciones = ['____ * X1 + ____ * X2 <= ____',
                     '____ * X1 - ____ * X2 <= ____',
                     '____ * X1 + ____ * X2 >= ____',
                     '____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    print(xuno)
    print(yuno)
    
    if xuno==1 and yuno==1:
        print(f'{SOLpldos_dos_1_1_MIN()}')
    elif xuno==1 and yuno==2:
        print(f'{SOLpldos_dos_1_2_MIN()}')
    elif xuno==1 and yuno==3:
        print(f'{SOLpldos_dos_1_3_MIN()}')
    elif xuno==1 and yuno==4:
        print(f'{SOLpldos_dos_1_4_MIN()}')
    elif xuno==2 and yuno==1:
        print(f'{SOLpldos_dos_2_1_MIN()}')
    elif xuno==2 and yuno==2:
        print(f'{SOLpldos_dos_2_2_MIN()}')
    elif xuno==2 and yuno==3:
        print(f'{SOLpldos_dos_2_3_MIN()}')
    elif xuno==2 and yuno==4:
        print(f'{SOLpldos_dos_2_4_MIN()}')
    elif xuno==3 and yuno==1:
        print(f'{SOLpldos_dos_3_1_MIN()}')
    elif xuno==3 and yuno==2:
        print(f'{SOLpldos_dos_3_2_MIN()}')
    elif xuno==3 and yuno==3:
        print(f'{SOLpldos_dos_3_3_MIN()}')
    elif xuno==3 and yuno==4:
        print(f'{SOLpldos_dos_3_4_MIN()}')
    elif xuno==4 and yuno==1:
        print(f'{SOLpldos_dos_4_1_MIN()}')
    elif xuno==4 and yuno==2:
        print(f'{SOLpldos_dos_4_2_MIN()}')
    elif xuno==4 and yuno==3:
        print(f'{SOLpldos_dos_4_3_MIN()}')
    elif xuno==4 and yuno==4:
        print(f'{SOLpldos_dos_4_4_MIN()}')
        


def EelccionFroma2_2():
    i=True
    while i:
        print('\t.:Opcion A o B:.')
        print('A. Maximizar')
        print('B. Minimizar')
        print('*************************')
        opci=str(input('Digite una opcion del menu: ')).upper()
        
        if opci=='A':
            print(f'{lsitopcio_max_dd()}')
        else:
            print(f'{lsitopcio_min_dd()}')
            

##############################--------------------------------------------------############################################


def SOLpldos_tre_1_1_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_1_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_1_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_2_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1  {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_2_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_2_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_2_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_2_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_2_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_3_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_3_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_3_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_3_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_3_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_3_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_3_MAX_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_3_MAX_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_3_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_3_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 > __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 > __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_4_MAX_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_4_MAX_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

################################
#################################


def SOLpldos_tre_1_1_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 3:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_1_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_1_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 - {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_2_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1  {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_2_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_2_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_2_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

#""""""""""""""""#

def SOLpldos_tre_2_1_2_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_2_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

##################

def SOLpldos_tre_2_2_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_2_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_2_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 <= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y <= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_3_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_3_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_3_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_3_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_3_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_3_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_3_MIN_mas():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_3_MIN_men():
    print("Funcion Max:__x1 + __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_3_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_3_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 + __x2 = _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 + {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x + die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 > __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_1_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 > __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_2_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_3_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_1_4_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_1_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_2_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_3_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_2_4_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 <= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 <= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y <= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_1_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_2_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_3_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_3_4_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 + __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 > {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x + cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_1_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 <= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_2_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 <= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 <= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y <= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_3_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 + {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 + __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 + {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x + sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_4_MIN_mas():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x + dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a

def SOLpldos_tre_4_4_4_MIN_men():
    print("Funcion Max:__x1 - __x2")
    uno=int(input('__x1: '))
    dos=int(input('__x2: '))
    print(f"Funcion:{uno}x1 + {dos}x2")
    print("__________________")
    print("restricion 1: x1 - __x2 >= _")
    tre=int(input('__x1: '))
    cua=int(input('__x2: '))
    cic=int(input('<=__: '))
    print(f"restricion 1:{tre}x1 - {cua}x2 >= {cic}")
    print("__________________")
    print("restricion 2: x1 - __x2 >= _")
    sei=int(input('___x1: '))
    sie=int(input('___x2: '))
    och=int(input('<=__: '))
    print(f"restricion 2:{sei}x1 - {sie}x2 >= {och}")
    print("__________________")
    print("restricion 3: x1 - __x2 >= _")
    nue=int(input('___x1: '))
    die=int(input('___x2: '))
    dion=int(input('<=__: '))
    print(f"restricion 2:{nue}x1 - {die}x2 >= {dion}")
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')
    print('Numero de Variables =', solver.NumVariables())
    solver.Add(tre * x - cua*y >= cic)
    solver.Add(sei * x - sie*y >= och)
    solver.Add(nue * x - die*y >= dion)
    print('Numero de Restricciones =', solver.NumConstraints())
    solver.Maximize(uno* x - dos* y)
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print('....::SOLUCION::....')
        print('Valor Objetivo =', solver.Objective().Value())
        print('x1 =', x.solution_value())
        print('x2 =', y.solution_value())
        print('\nValores avanzados:')
        print('El problema fue resuelto en %f milisegundos' % solver.wall_time())
        print('El problema fue resuelto en %d iteraciones' % solver.iterations())
    else:
        print('El problema no tiene solucion potima')
    a='**************'
    return a


################################

def SOLpldos_tre_1_1_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_1_MAX_mas())
    else:
        print(SOLpldos_tre_1_1_1_MAX_men())

def SOLpldos_tre_1_2_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_1_MAX_mas())
    else:
        print(SOLpldos_tre_1_2_1_MAX_men())

def SOLpldos_tre_1_3_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_1_MAX_mas())
    else:
        print(SOLpldos_tre_1_3_1_MAX_men())

def SOLpldos_tre_1_4_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_1_MAX_mas())
    else:
        print(SOLpldos_tre_1_4_1_MAX_men())

def SOLpldos_tre_2_1_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_1_MAX_mas())
    else:
        print(SOLpldos_tre_2_1_1_MAX_men())

def SOLpldos_tre_2_2_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_1_MAX_mas())
    else:
        print(SOLpldos_tre_2_2_1_MAX_men())

def SOLpldos_tre_2_3_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_1_MAX_mas())
    else:
        print(SOLpldos_tre_2_3_1_MAX_men())

def SOLpldos_tre_2_4_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_1_MAX_mas())
    else:
        print(SOLpldos_tre_2_4_1_MAX_men())

def SOLpldos_tre_3_1_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_1_MAX_mas())
    else:
        print(SOLpldos_tre_3_1_1_MAX_men())

def SOLpldos_tre_3_2_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_1_MAX_mas())
    else:
        print(SOLpldos_tre_3_2_1_MAX_men())

def SOLpldos_tre_3_3_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_1_MAX_mas())
    else:
        print(SOLpldos_tre_3_3_1_MAX_men())

def SOLpldos_tre_3_4_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_1_MAX_mas())
    else:
        print(SOLpldos_tre_3_4_1_MAX_men())

def SOLpldos_tre_4_1_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_1_MAX_mas())
    else:
        print(SOLpldos_tre_4_1_1_MAX_men())

def SOLpldos_tre_4_2_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_1_MAX_mas())
    else:
        print(SOLpldos_tre_4_2_1_MAX_men())

def SOLpldos_tre_4_3_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_1_MAX_mas())
    else:
        print(SOLpldos_tre_4_3_1_MAX_men())

def SOLpldos_tre_4_4_1_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_1_MAX_mas())
    else:
        print(SOLpldos_tre_4_4_1_MAX_men())

def SOLpldos_tre_1_1_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_2_MAX_mas())
    else:
        print(SOLpldos_tre_1_1_2_MAX_men())

def SOLpldos_tre_1_2_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_2_MAX_mas())
    else:
        print(SOLpldos_tre_1_2_2_MAX_men())

def SOLpldos_tre_1_3_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_2_MAX_mas())
    else:
        print(SOLpldos_tre_1_3_2_MAX_men())

def SOLpldos_tre_1_4_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_2_MAX_mas())
    else:
        print(SOLpldos_tre_1_4_2_MAX_men())

def SOLpldos_tre_2_1_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_2_MAX_mas())
    else:
        print(SOLpldos_tre_1_4_2_MAX_men())

def SOLpldos_tre_2_2_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_2_MAX_mas())
    else:
        print(SOLpldos_tre_2_2_2_MAX_men())

def SOLpldos_tre_2_3_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_2_MAX_mas())
    else:
        print(SOLpldos_tre_2_3_2_MAX_men())

def SOLpldos_tre_2_4_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_2_MAX_mas())
    else:
        print(SOLpldos_tre_2_4_2_MAX_men())

def SOLpldos_tre_3_1_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_2_MAX_mas())
    else:
        print(SOLpldos_tre_3_1_2_MAX_men())

def SOLpldos_tre_3_2_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_2_MAX_mas())
    else:
        print(SOLpldos_tre_3_2_2_MAX_men())

def SOLpldos_tre_3_3_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_2_MAX_mas())
    else:
        print(SOLpldos_tre_3_3_2_MAX_men())

def SOLpldos_tre_3_4_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_2_MAX_mas())
    else:
        print(SOLpldos_tre_3_4_2_MAX_men())

def SOLpldos_tre_4_1_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_2_MAX_mas())
    else:
        print(SOLpldos_tre_4_1_2_MAX_men())

def SOLpldos_tre_4_2_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_2_MAX_mas())
    else:
        print(SOLpldos_tre_4_2_2_MAX_men())

def SOLpldos_tre_4_3_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_2_MAX_mas())
    else:
        print(SOLpldos_tre_4_3_2_MAX_men())

def SOLpldos_tre_4_4_2_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_2_MAX_mas())
    else:
        print(SOLpldos_tre_4_4_2_MAX_men())

def SOLpldos_tre_1_1_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_3_MAX_mas())
    else:
        print(SOLpldos_tre_1_1_3_MAX_men())

def SOLpldos_tre_1_2_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_3_MAX_mas())
    else:
        print(SOLpldos_tre_1_2_3_MAX_men())

def SOLpldos_tre_1_3_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_3_MAX_mas())
    else:
        print(SOLpldos_tre_1_3_3_MAX_men())

def SOLpldos_tre_1_4_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_3_MAX_mas())
    else:
        print(SOLpldos_tre_1_4_3_MAX_men())

def SOLpldos_tre_2_1_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_3_MAX_mas())
    else:
        print(SOLpldos_tre_2_1_3_MAX_men())

def SOLpldos_tre_2_2_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_3_MAX_mas())
    else:
        print(SOLpldos_tre_2_2_3_MAX_men())

def SOLpldos_tre_2_3_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_3_MAX_mas())
    else:
        print(SOLpldos_tre_2_3_3_MAX_men())

def SOLpldos_tre_2_4_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_3_MAX_mas())
    else:
        print(SOLpldos_tre_2_4_3_MAX_men())

def SOLpldos_tre_3_1_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_3_MAX_mas())
    else:
        print(SOLpldos_tre_3_1_3_MAX_men())

def SOLpldos_tre_3_2_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_3_MAX_mas())
    else:
        print(SOLpldos_tre_3_2_3_MAX_men())

def SOLpldos_tre_3_3_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_3_MAX_mas())
    else:
        print(SOLpldos_tre_3_3_3_MAX_men())

def SOLpldos_tre_3_4_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_3_MAX_mas())
    else:
        print(SOLpldos_tre_3_4_3_MAX_men())

def SOLpldos_tre_4_1_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_3_MAX_mas())
    else:
        print(SOLpldos_tre_4_1_3_MAX_men())

def SOLpldos_tre_4_2_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_3_MAX_mas())
    else:
        print(SOLpldos_tre_4_2_3_MAX_men())

def SOLpldos_tre_4_3_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_3_MAX_mas())
    else:
        print(SOLpldos_tre_4_3_3_MAX_men())

def SOLpldos_tre_4_4_3_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_3_MAX_mas())
    else:
        print(SOLpldos_tre_4_4_3_MAX_men())

def SOLpldos_tre_1_1_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_4_MAX_mas())
    else:
        print(SOLpldos_tre_1_1_4_MAX_men())

def SOLpldos_tre_1_2_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_4_MAX_mas())
    else:
        print(SOLpldos_tre_1_2_4_MAX_men())

def SOLpldos_tre_1_3_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_4_MAX_mas())
    else:
        print(SOLpldos_tre_1_3_4_MAX_men())

def SOLpldos_tre_1_4_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_4_MAX_mas())
    else:
        print(SOLpldos_tre_1_4_4_MAX_men())

def SOLpldos_tre_2_1_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_4_MAX_mas())
    else:
        print(SOLpldos_tre_2_1_4_MAX_men())

def SOLpldos_tre_2_2_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_4_MAX_mas())
    else:
        print(SOLpldos_tre_2_2_4_MAX_men())

def SOLpldos_tre_2_3_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_4_MAX_mas())
    else:
        print(SOLpldos_tre_2_3_4_MAX_men())

def SOLpldos_tre_2_4_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_4_MAX_mas())
    else:
        print(SOLpldos_tre_2_4_4_MAX_men())

def SOLpldos_tre_3_1_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_4_MAX_mas())
    else:
        print(SOLpldos_tre_3_1_4_MAX_men())

def SOLpldos_tre_3_2_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_4_MAX_mas())
    else:
        print(SOLpldos_tre_3_2_4_MAX_men())

def SOLpldos_tre_3_3_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_4_MAX_mas())
    else:
        print(SOLpldos_tre_3_3_4_MAX_men())

def SOLpldos_tre_3_4_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_4_MAX_mas())
    else:
        print(SOLpldos_tre_3_4_4_MAX_men())

def SOLpldos_tre_4_1_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_4_MAX_mas())
    else:
        print(SOLpldos_tre_4_1_4_MAX_men())

def SOLpldos_tre_4_2_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_4_MAX_mas())
    else:
        print(SOLpldos_tre_4_2_4_MAX_men())

def SOLpldos_tre_4_3_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_4_MAX_mas())
    else:
        print(SOLpldos_tre_4_3_4_MAX_men())

def SOLpldos_tre_4_4_4_MAX():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_4_MAX_mas())
    else:
        print(SOLpldos_tre_4_4_4_MAX_men())

################################



def SOLpldos_tre_1_1_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_1_MIN_mas())
    else:
        print(SOLpldos_tre_1_1_1_MIN_men())

def SOLpldos_tre_1_2_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_1_MIN_mas())
    else:
        print(SOLpldos_tre_1_2_1_MIN_men())

def SOLpldos_tre_1_3_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_1_MIN_mas())
    else:
        print(SOLpldos_tre_1_3_1_MIN_men())

def SOLpldos_tre_1_4_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_1_MIN_mas())
    else:
        print(SOLpldos_tre_1_4_1_MIN_men())

def SOLpldos_tre_2_1_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_1_MIN_mas())
    else:
        print(SOLpldos_tre_2_1_1_MIN_men())

def SOLpldos_tre_2_2_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_1_MIN_mas())
    else:
        print(SOLpldos_tre_2_2_1_MIN_men())

def SOLpldos_tre_2_3_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_1_MIN_mas())
    else:
        print(SOLpldos_tre_2_3_1_MIN_men())

def SOLpldos_tre_2_4_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_1_MIN_mas())
    else:
        print(SOLpldos_tre_2_4_1_MIN_men())

def SOLpldos_tre_3_1_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_1_MIN_mas())
    else:
        print(SOLpldos_tre_3_1_1_MIN_men())

def SOLpldos_tre_3_2_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_1_MIN_mas())
    else:
        print(SOLpldos_tre_3_2_1_MIN_men())

def SOLpldos_tre_3_3_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_1_MIN_mas())
    else:
        print(SOLpldos_tre_3_3_1_MIN_men())

def SOLpldos_tre_3_4_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_1_MIN_mas())
    else:
        print(SOLpldos_tre_3_4_1_MIN_men())

def SOLpldos_tre_4_1_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_1_MIN_mas())
    else:
        print(SOLpldos_tre_4_1_1_MIN_men())

def SOLpldos_tre_4_2_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_1_MIN_mas())
    else:
        print(SOLpldos_tre_4_2_1_MIN_men())

def SOLpldos_tre_4_3_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_1_MIN_mas())
    else:
        print(SOLpldos_tre_4_3_1_MIN_men())

def SOLpldos_tre_4_4_1_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_1_MIN_mas())
    else:
        print(SOLpldos_tre_4_4_1_MIN_men())

def SOLpldos_tre_1_1_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_2_MIN_mas())
    else:
        print(SOLpldos_tre_1_1_2_MIN_men())

def SOLpldos_tre_1_2_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_2_MIN_mas())
    else:
        print(SOLpldos_tre_1_2_2_MIN_men())

def SOLpldos_tre_1_3_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_2_MIN_mas())
    else:
        print(SOLpldos_tre_1_3_2_MIN_men())

def SOLpldos_tre_1_4_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_2_MIN_mas())
    else:
        print(SOLpldos_tre_1_4_2_MIN_men())

def SOLpldos_tre_2_1_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_2_MIN_mas())
    else:
        print(SOLpldos_tre_2_1_2_MIN_men())

def SOLpldos_tre_2_2_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_2_MIN_mas())
    else:
        print(SOLpldos_tre_2_2_2_MIN_men())

def SOLpldos_tre_2_3_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_2_MIN_mas())
    else:
        print(SOLpldos_tre_2_3_2_MIN_men())

def SOLpldos_tre_2_4_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_2_MIN_mas())
    else:
        print(SOLpldos_tre_2_4_2_MIN_men())

def SOLpldos_tre_3_1_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_2_MIN_mas())
    else:
        print(SOLpldos_tre_3_1_2_MIN_men())

def SOLpldos_tre_3_2_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_2_MIN_mas())
    else:
        print(SOLpldos_tre_3_2_2_MIN_men())

def SOLpldos_tre_3_3_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_2_MIN_mas())
    else:
        print(SOLpldos_tre_3_3_2_MIN_men())

def SOLpldos_tre_3_4_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_2_MIN_mas())
    else:
        print(SOLpldos_tre_3_4_2_MIN_men())

def SOLpldos_tre_4_1_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_2_MIN_mas())
    else:
        print(SOLpldos_tre_4_1_2_MIN_men())

def SOLpldos_tre_4_2_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_2_MIN_mas())
    else:
        print(SOLpldos_tre_4_2_2_MIN_men())

def SOLpldos_tre_4_3_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_2_MIN_mas())
    else:
        print(SOLpldos_tre_4_3_2_MIN_men())

def SOLpldos_tre_4_4_2_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_2_MIN_mas())
    else:
        print(SOLpldos_tre_4_4_2_MIN_men())

def SOLpldos_tre_1_1_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_3_MIN_mas())
    else:
        print(SOLpldos_tre_1_1_3_MIN_men())

def SOLpldos_tre_1_2_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_3_MIN_mas())
    else:
        print(SOLpldos_tre_1_2_3_MIN_men())

def SOLpldos_tre_1_3_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_3_MIN_mas())
    else:
        print(SOLpldos_tre_1_3_3_MIN_men())

def SOLpldos_tre_1_4_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_3_MIN_mas())
    else:
        print(SOLpldos_tre_1_4_3_MIN_men())

def SOLpldos_tre_2_1_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_3_MIN_mas())
    else:
        print(SOLpldos_tre_2_1_3_MIN_men())

def SOLpldos_tre_2_2_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_3_MIN_mas())
    else:
        print(SOLpldos_tre_2_2_3_MIN_men())

def SOLpldos_tre_2_3_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_3_MIN_mas())
    else:
        print(SOLpldos_tre_2_3_3_MIN_men())

def SOLpldos_tre_2_4_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_3_MIN_mas())
    else:
        print(SOLpldos_tre_2_4_3_MIN_men())

def SOLpldos_tre_3_1_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_3_MIN_mas())
    else:
        print(SOLpldos_tre_3_1_3_MIN_men())

def SOLpldos_tre_3_2_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_3_MIN_mas())
    else:
        print(SOLpldos_tre_3_2_3_MIN_men())

def SOLpldos_tre_3_3_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_3_MIN_mas())
    else:
        print(SOLpldos_tre_3_3_3_MIN_men())

def SOLpldos_tre_3_4_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_3_MIN_mas())
    else:
        print(SOLpldos_tre_3_4_3_MIN_men())

def SOLpldos_tre_4_1_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_3_MIN_mas())
    else:
        print(SOLpldos_tre_4_1_3_MIN_men())

def SOLpldos_tre_4_2_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_3_MIN_mas())
    else:
        print(SOLpldos_tre_4_2_3_MIN_men())

def SOLpldos_tre_4_3_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_3_MIN_mas())
    else:
        print(SOLpldos_tre_4_3_3_MIN_men())

def SOLpldos_tre_4_4_3_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_3_MIN_mas())
    else:
        print(SOLpldos_tre_4_4_3_MIN_men())

def SOLpldos_tre_1_1_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_1_4_MIN_mas())
    else:
        print(SOLpldos_tre_1_1_4_MIN_men())

def SOLpldos_tre_1_2_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_2_4_MIN_mas())
    else:
        print(SOLpldos_tre_1_2_4_MIN_men())

def SOLpldos_tre_1_3_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_3_4_MIN_mas())
    else:
        print(SOLpldos_tre_1_3_4_MIN_men())

def SOLpldos_tre_1_4_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_1_4_4_MIN_mas())
    else:
        print(SOLpldos_tre_1_4_4_MIN_men())

def SOLpldos_tre_2_1_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_1_4_MIN_mas())
    else:
        print(SOLpldos_tre_2_1_4_MIN_men())

def SOLpldos_tre_2_2_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_2_4_MIN_mas())
    else:
        print(SOLpldos_tre_2_2_4_MIN_men())

def SOLpldos_tre_2_3_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_3_4_MIN_mas())
    else:
        print(SOLpldos_tre_2_3_4_MIN_men())

def SOLpldos_tre_2_4_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_2_4_4_MIN_mas())
    else:
        print(SOLpldos_tre_2_4_4_MIN_men())

def SOLpldos_tre_3_1_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_1_4_MIN_mas())
    else:
        print(SOLpldos_tre_3_1_4_MIN_men())

def SOLpldos_tre_3_2_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_2_4_MIN_mas())
    else:
        print(SOLpldos_tre_3_2_4_MIN_men())

def SOLpldos_tre_3_3_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_3_4_MIN_mas())
    else:
        print(SOLpldos_tre_3_3_4_MIN_men())

def SOLpldos_tre_3_4_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_3_4_4_MIN_mas())
    else:
        print(SOLpldos_tre_3_4_4_MIN_men())

def SOLpldos_tre_4_1_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_1_4_MIN_mas())
    else:
        print(SOLpldos_tre_4_1_4_MIN_men())

def SOLpldos_tre_4_2_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_2_4_MIN_mas())
    else:
        print(SOLpldos_tre_4_2_4_MIN_men())

def SOLpldos_tre_4_3_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_3_4_MIN_mas())
    else:
        print(SOLpldos_tre_4_3_4_MIN_men())

def SOLpldos_tre_4_4_4_MIN():
    print("Funcion Max:__x1 (__) __x2")
    print('A)__x1 + __x2')
    print('B)__x1 - __x2')
    print('....:A o B:....')
    sumres=str(input(': ')).upper()
    if sumres=='A':
        print(SOLpldos_tre_4_4_4_MIN_mas())
    else:
        print(SOLpldos_tre_4_4_4_MIN_men())

########################################################################################################

"""
def lsitopcio_max_dd():
    listaOpciones = ['____ * X1 + ____ * X2 <= ____',
                     '____ * X1 - ____ * X2 <= ____',
                     '____ * X1 + ____ * X2 >= ____',
                     '____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    print(xuno)
    print(yuno)
    
    if xuno==1 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==4:
        print(f'{SOLpl()}')
        


def lsitopcio_min_dd():
    listaOpciones = ['____ * X1 + ____ * X2 <= ____',
                     '____ * X1 - ____ * X2 <= ____',
                     '____ * X1 + ____ * X2 >= ____',
                     '____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    print(xuno)
    print(yuno)
    
    if xuno==1 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==1 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==2 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==3 and yuno==4:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==1:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==2:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==3:
        print(f'{SOLpl()}')
    elif xuno==4 and yuno==4:
        print(f'{SOLpl()}')
        

"""

def lsitopcio_max_dt():
    
    listaOpciones = ['1) ____ * X1 + ____ * X2 <= ____',
                     '2) ____ * X1 - ____ * X2 <= ____',
                     '3) ____ * X1 + ____ * X2 >= ____',
                     '4) ____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    zuno=int(input("trecersa restriccion: "))
    
    if xuno==1 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_1_1_1_MAX()}')
    elif xuno==1 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_1_2_1_MAX()}')
    elif xuno==1 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_1_3_1_MAX()}')
    elif xuno==1 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_1_4_1_MAX()}')
    elif xuno==2 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_2_1_1_MAX()}')
    elif xuno==2 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_2_2_1_MAX()}')
    elif xuno==2 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_2_3_1_MAX()}')
    elif xuno==2 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_2_4_1_MAX()}')
    elif xuno==3 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_3_1_1_MAX()}')
    elif xuno==3 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_3_2_1_MAX()}')
    elif xuno==3 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_3_3_1_MAX()}')
    elif xuno==3 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_3_4_1_MAX()}')
    elif xuno==4 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_4_1_1_MAX()}')
    elif xuno==4 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_4_2_1_MAX()}')
    elif xuno==4 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_4_3_1_MAX()}')
    elif xuno==4 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_4_4_1_MAX()}')
    elif xuno==1 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_1_1_2_MAX()}')
    elif xuno==1 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_1_2_2_MAX()}')
    elif xuno==1 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_1_3_2_MAX()}')
    elif xuno==1 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_1_4_2_MAX()}')
    elif xuno==2 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_2_1_2_MAX()}')
    elif xuno==2 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_2_2_2_MAX()}')
    elif xuno==2 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_2_3_2_MAX()}')
    elif xuno==2 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_2_4_2_MAX()}')
    elif xuno==3 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_3_1_2_MAX()}')
    elif xuno==3 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_3_2_2_MAX()}')
    elif xuno==3 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_3_3_2_MAX()}')
    elif xuno==3 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_3_4_2_MAX()}')
    elif xuno==4 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_4_1_2_MAX()}')
    elif xuno==4 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_4_2_2_MAX()}')
    elif xuno==4 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_4_3_2_MAX()}')
    elif xuno==4 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_4_4_2_MAX()}')
    elif xuno==1 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_1_1_3_MAX()}')
    elif xuno==1 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_1_2_3_MAX()}')
    elif xuno==1 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_1_3_3_MAX()}')
    elif xuno==1 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_1_4_3_MAX()}')
    elif xuno==2 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_2_1_3_MAX()}')
    elif xuno==2 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_2_2_3_MAX()}')
    elif xuno==2 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_2_3_3_MAX()}')
    elif xuno==2 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_2_4_3_MAX()}')
    elif xuno==3 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_3_1_3_MAX()}')
    elif xuno==3 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_3_2_3_MAX()}')
    elif xuno==3 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_3_3_3_MAX()}')
    elif xuno==3 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_3_4_3_MAX()}')
    elif xuno==4 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_4_1_3_MAX()}')
    elif xuno==4 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_4_2_3_MAX()}')
    elif xuno==4 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_4_3_3_MAX()}')
    elif xuno==4 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_4_4_3_MAX()}')
    elif xuno==1 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_1_1_4_MAX()}')
    elif xuno==1 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_1_2_4_MAX()}')
    elif xuno==1 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_1_3_4_MAX()}')
    elif xuno==1 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_1_4_4_MAX()}')
    elif xuno==2 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_2_1_4_MAX()}')
    elif xuno==2 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_2_2_4_MAX()}')
    elif xuno==2 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_2_3_4_MAX()}')
    elif xuno==2 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_2_4_4_MAX()}')
    elif xuno==3 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_3_1_4_MAX()}')
    elif xuno==3 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_3_2_4_MAX()}')
    elif xuno==3 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_3_3_4_MAX()}')
    elif xuno==3 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_3_4_4_MAX()}')
    elif xuno==4 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_4_1_4_MAX()}')
    elif xuno==4 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_4_2_4_MAX()}')
    elif xuno==4 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_4_3_4_MAX()}')
    elif xuno==4 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_4_4_4_MAX()}')
    
    a=''
    
    return a

#########################################################################################################

def lsitopcio_min_dt():
    listaOpciones = ['____ * X1 + ____ * X2 <= ____',
                     '____ * X1 - ____ * X2 <= ____',
                     '____ * X1 + ____ * X2 >= ____',
                     '____ * X1 - ____ * X2 >= ____']
    print('\n'.join(listaOpciones))
    
    xuno=int(input("primera restricion: "))
    yuno=int(input("segunda restricion: "))
    zuno=int(input("trecersa restriccion: "))
    print(xuno)
    print(yuno)
    print(zuno)
    
    if xuno==1 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_1_1_1_MIN()}')
    elif xuno==1 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_1_2_1_MIN()}')
    elif xuno==1 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_1_3_1_MIN()}')
    elif xuno==1 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_1_4_1_MIN()}')
    elif xuno==2 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_2_1_1_MIN()}')
    elif xuno==2 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_2_2_1_MIN()}')
    elif xuno==2 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_2_3_1_MIN()}')
    elif xuno==2 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_2_4_1_MIN()}')
    elif xuno==3 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_3_1_1_MIN()}')
    elif xuno==3 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_3_2_1_MIN()}')
    elif xuno==3 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_3_3_1_MIN()}')
    elif xuno==3 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_3_4_1_MIN()}')
    elif xuno==4 and yuno==1 and zuno==1:
        print(f'{SOLpldos_tre_4_1_1_MIN()}')
    elif xuno==4 and yuno==2 and zuno==1:
        print(f'{SOLpldos_tre_4_2_1_MIN()}')
    elif xuno==4 and yuno==3 and zuno==1:
        print(f'{SOLpldos_tre_4_3_1_MIN()}')
    elif xuno==4 and yuno==4 and zuno==1:
        print(f'{SOLpldos_tre_4_4_1_MIN()}')
    elif xuno==1 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_1_1_2_MIN()}')
    elif xuno==1 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_1_2_2_MIN()}')
    elif xuno==1 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_1_3_2_MIN()}')
    elif xuno==1 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_1_4_2_MIN()}')
    elif xuno==2 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_2_1_2_MIN()}')
    elif xuno==2 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_2_2_2_MIN()}')
    elif xuno==2 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_2_3_2_MIN()}')
    elif xuno==2 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_2_4_2_MIN()}')
    elif xuno==3 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_3_1_2_MIN()}')
    elif xuno==3 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_3_2_2_MIN()}')
    elif xuno==3 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_3_3_2_MIN()}')
    elif xuno==3 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_3_4_2_MIN()}')
    elif xuno==4 and yuno==1 and zuno==2:
        print(f'{SOLpldos_tre_4_1_2_MIN()}')
    elif xuno==4 and yuno==2 and zuno==2:
        print(f'{SOLpldos_tre_4_2_2_MIN()}')
    elif xuno==4 and yuno==3 and zuno==2:
        print(f'{SOLpldos_tre_4_3_2_MIN()}')
    elif xuno==4 and yuno==4 and zuno==2:
        print(f'{SOLpldos_tre_4_4_2_MIN()}')
    elif xuno==1 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_1_1_3_MIN()}')
    elif xuno==1 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_1_2_3_MIN()}')
    elif xuno==1 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_1_3_3_MIN()}')
    elif xuno==1 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_1_4_3_MIN()}')
    elif xuno==2 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_2_1_3_MIN()}')
    elif xuno==2 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_2_2_3_MIN()}')
    elif xuno==2 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_2_3_3_MIN()}')
    elif xuno==2 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_2_4_3_MIN()}')
    elif xuno==3 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_3_1_3_MIN()}')
    elif xuno==3 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_3_2_3_MIN()}')
    elif xuno==3 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_3_3_3_MIN()}')
    elif xuno==3 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_3_4_3_MIN()}')
    elif xuno==4 and yuno==1 and zuno==3:
        print(f'{SOLpldos_tre_4_1_3_MIN()}')
    elif xuno==4 and yuno==2 and zuno==3:
        print(f'{SOLpldos_tre_4_2_3_MIN()}')
    elif xuno==4 and yuno==3 and zuno==3:
        print(f'{SOLpldos_tre_4_3_3_MIN()}')
    elif xuno==4 and yuno==4 and zuno==3:
        print(f'{SOLpldos_tre_4_4_3_MIN()}')
    elif xuno==1 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_1_1_4_MIN()}')
    elif xuno==1 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_1_2_4_MIN()}')
    elif xuno==1 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_1_3_4_MIN()}')
    elif xuno==1 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_1_4_4_MIN()}')
    elif xuno==2 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_2_1_4_MIN()}')
    elif xuno==2 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_2_2_4_MIN()}')
    elif xuno==2 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_2_3_4_MIN()}')
    elif xuno==2 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_2_4_4_MIN()}')
    elif xuno==3 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_3_1_4_MIN()}')
    elif xuno==3 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_3_2_4_MIN()}')
    elif xuno==3 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_3_3_4_MIN()}')
    elif xuno==3 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_3_4_4_MIN()}')
    elif xuno==4 and yuno==1 and zuno==4:
        print(f'{SOLpldos_tre_4_1_4_MIN()}')
    elif xuno==4 and yuno==2 and zuno==4:
        print(f'{SOLpldos_tre_4_2_4_MIN()}')
    elif xuno==4 and yuno==3 and zuno==4:
        print(f'{SOLpldos_tre_4_3_4_MIN()}')
    elif xuno==4 and yuno==4 and zuno==4:
        print(f'{SOLpldos_tre_4_4_4_MIN()}')




def EelccionFroma2_3():
    print('\t.:Opcion A o B:.')
    print('A. Maximizar')
    print('B. Minimizar')
    print('SALIR')
    print('*************************')
    opci=str(input('Digite una opcion del menu: ')).upper()
        
    if opci=='A':
        print(f'{lsitopcio_max_dt()}')  #esto va aqui ----v lsitopcio_max_dt()
    else:
        print(f'{lsitopcio_min_dt()}')  #esto va aqui ----v lsitopcio_min_dt()




bol=True

while bol:
    print('\t.:MENU:.')
    numvar=int(input('1. Ingresar numero de variables:'))
    numresar=int(input('2. Ingresar numero de restricciones:'))
    print('Salir')
    print('**********')
    while numvar<2 or numvar>3 or numresar<1 or numresar>3:
        numvar=int(input('1. Ingresar numero de variables:'))
        numresar=int(input('2. Ingresar numero de restricciones:'))
        
        
    if numvar==2 and numresar==2:
        print(f'La solucion Optima: {EelccionFroma2_2()}')
        
    if numvar==2 and numresar==3:
        print(f'La solucion Optima: {EelccionFroma2_3()}')
        
