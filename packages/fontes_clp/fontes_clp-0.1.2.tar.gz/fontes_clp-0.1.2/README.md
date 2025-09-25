# Bibliotecas para Extração de Fontes do CLP

## Instalação

Se você usar o `uv`:

```sh
uv add fontes-clp
```

Se você usar o `pip`:

```sh
pip install --upgrade fontes-clp
```

## Exemplos

### TabNet Óbitos

```python
from fontes_clp import Estado, GruposObitos, TabNetObitos

# Dados são retornados como um DataFrame do Pandas
dados = TabNetObitos(
  ano=2023,
  estado=Estado.SP,
  grupo=GruposObitos.ACIDENTES_TERRESTRES,
).get_dados()

print(dados)
```

### TabNet Óbitos

```python
from fontes_clp import Estado, GruposCausas, TabNetCausas

# Dados são retornados como um DataFrame do Pandas
dados = TabNetCausas(
  ano=2025,
  estado=Estado.TO,
  grupo=GruposCausas.ACIDENTES_TERRESTRES,
).get_dados()

print(dados)
```

### IBGE População

```python
from fontes_clp import Estado, Sexo, IBGEPopulacao

# Dados são retornados como um DataFrame do Pandas
dados = IBGEPopulacao(
  ano=2024,
  estado=Estado.RR,
  sexo=Sexo.M,  # Se o sexo não for especificado, ele puxará os dados de ambos
).get_dados()

print(dados)
```
