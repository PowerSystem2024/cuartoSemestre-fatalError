#manejo de valores infinitos
infinito_positivo = float('inf')
print(f'infinito positivos:{infinito_positivo}')
print(f'es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = float('-inf')
print(f'infinito negativos:{infinito_negativo}')
print(f'es infinito?: {math.isinf(infinito_negativo)}')

#modulo math
infinito_positivo = math.inf
print(f'infinito positivos:{infinito_positivo}')
print(f'es infinito?: {math.isinf(infinito_positivo)}')

infinito_negativo = -math.inf
print(f'infinito negativos:{infinito_negativo}')
print(f'es infinito?: {math.isinf(infinito_negativo)}')

#modulo  decimal
infinito_positivo = decimal('infinity')
print(f'infinito positivos:{infinito_positivo}')
print(f'es infinito?: {math.isinf(infinito_positivo)}')


infinito_negativo = decimal ('-infinity')
print(f'infinito negativos:{infinito_negativo}')
print(f'es infinito?: {math.isinf(infinito_negativo)}')
