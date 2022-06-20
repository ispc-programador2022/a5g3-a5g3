![172445821-245dee9a-7c37-4f00-97b4-7c03965467f3](https://user-images.githubusercontent.com/105888331/173205673-c8ded2e2-6f02-4b6a-b370-a13a5e046e60.png)

[![GitHub forks](https://img.shields.io/github/forks/ispc-programador2022/a5g3-a5g3)](https://github.com/ispc-programador2022/a5g3-a5g3/network)
[![GitHub stars](https://img.shields.io/github/stars/ispc-programador2022/a5g3-a5g3)](https://github.com/ispc-programador2022/a5g3-a5g3/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/ispc-programador2022/a5g3-a5g3)](https://github.com/ispc-programador2022/a5g3-a5g3/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/ispc-programador2022/a5g3-a5g3?color=green)](https://github.com/ispc-programador2022/a5g3-a5g3/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Tecnicatura en Ciencia de Datos e Inteligencia Artificial

## Bienvenidos al AULA 5 - GRUPO 3 - COHORTE 2022

Colaboradores:

• [Escobar, Tomás](https://github.com/tomasescobar24)

• [Ferreira, Juan David.](https://github.com/juniors90)

• [Feraboli, Germán Alejandro.](https://github.com/IAferaboli)

• [Ferragutti, Silvia](https://github.com/ferrsil)

• [Espada, Cecilia](https://github.com/ceciespada) 

• [Fehr, Julieta](https://github.com/julietacfehr) 

• [Fioranelli, Bruno](https://github.com/brufio)

• [Elizondo, Silvana](https://github.com/silelizondo)

•[Espiga, Nahuel](https://github.com/espiganahuel)


## Testing

Para checkear que el código de alguna función esté realizando
lo que se solicita en los requerimientos, podemos ejecutar por
consola, por ejemplo:

```
$> python -m doctest funciones/varianza.py
$>
```

Para obtener más detalles, usamos la bandera `-v`:

```
$> python -m doctest funciones/varianza.py -v     
Trying:
    vector = [2, 4, 3, 6, 7, 33, 75, 30]
Expecting nothing
ok
Trying:
    varianza_de_lista_ramdom = varianza(vector=vector)
Expecting nothing
ok
Trying:
    varianza_de_lista_ramdom
Expecting:
    566.0
ok
Trying:
    from funciones.genrnd import genrnd
Expecting nothing
ok
Trying:
    vector1 = genrnd()
Expecting nothing
ok
Trying:
    varianza_de_lista_ramdom = varianza(vector=vector1)
Expecting nothing
ok
1 items had no tests:
    varianza
1 items passed all tests:
   6 tests in varianza.varianza
6 tests in 2 items.
6 passed and 0 failed.
Test passed.
$>
```

- No todas poseen (por el momento) esta funcionalidad.

## Contributors

<a href="https://github.com/ispc-programador2022/a5g3-a5g3/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ispc-programador2022/a5g3-a5g3" />
</a>

