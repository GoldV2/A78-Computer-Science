# File Name: U4_M4_A4_RAlmeida.py
# Purpose: 
# Edited - Revised: 

from textwrap import dedent

def step(n, name = ''):
    width = len(name) + 8

    s = f"""
         +{'-'*width}+
         |{f'Step {n}':^{width}}|"""

    if name:
        s += f"""
         |{f' Name: {name}':^{width}}|
         +{'-'*width}+
         """

    else:
        s += f"""
         +{'-'*width}+
         """

    print(dedent(s))