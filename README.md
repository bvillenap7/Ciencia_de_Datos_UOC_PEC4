# PEC4
## Autor: Borja Villena Pardo
### Asignatura: Programación para Ciencia de Datos

***This software is MIT licensed (see LICENSE)***

Este proyecto forma parte del entregable para la PEC_4 de la
asignatura ***Programación para Ciencia de Datos***, includia en el
***Grado de Ingeniería en Ciencia de Datos Aplicada***, cursada en 
***Universidad Oberta de Catalunya, UOC***.

A continuación puede encontrar una breve descripción
de como se organiza y ejecuta nuestro proyecto.

Nuestro proyecto, se organiza de la siguiente manera para trabajar en PyCharm:

- PEC4_Borja Villena Pardo
  - data
    - __ init.py __
    - TMDB.zip
    
  - dist
    - PEC4_Borja_Villena_Pardo-0.1.tar.gz **(archivo de instalación)**
    
  - PEC4_Borja_Villena_Pardo.egg-info
    - dependency_links.txt
    - PKG-INFO
    - requires.txt
    - SOURCES.txt
    - top_level.txt
    
  - src
    - __ init __.py
    - Ejercicio_1_1.py
    - Ejercicio_1_2.py
    - Ejercicio_1_3.py
    - Ejercicio_1_4.py
    - Ejercicio_2_1.py
    - Ejercicio_2_2.py
    - Ejercicio_3_1.py
    - Ejercicio_3_2.py
    - Ejercicio_3_3.py
    - Ejercicio_4_1.py
    - Ejercicio_4_2.py
    - Ejercicio_4_3.py
    - Ejercicio_5.py
    - main.py
  - Tests
    - data
    - test.txt
    - test_Ejercicio_1_1.py
    - test_Ejercicio_1_2.py
    - test_Ejercicio_1_3.py
    - test_Ejercicio_2_1.py
    - test_Ejercicio_2_2.py
    - test_Ejercicio_3_1.py
    - test_Ejercicio_3_2.py
    - test_Ejercicio_3_3.py
    - test_Ejercicio_4_1.py
    - test_Ejercicio_4_2.py
    - test_Ejercicio_4_3.py
  - venv
    - Include
    - Lib 
      - *(...)*
    - Scripts
      - *(...)*
    - share
      - *(...)*
    - pyvenv.cfg
  - __ init.py __
  - LICENSE.txt
  - main.py
  - README.md
  - requirements.txt
  - setup.py

    
Para llevar a cabo la instalación de nuestro programa `setup.py`
lleve a cabo los siguientes pasos:

- Vaya a la siguiente subcarpeta de nuestro proyecto: `dist`
- Copie el archivo de instalación `PEC4_Borja_Villena_Pardo-0.1.tar.gz` y peguelo
en la ruta local que desee.
- Abra un terminal en local, navegue hasta el directorio dónde haya copiado y guardado el archivo.
- Ahora vamos a instalaro. Para ello, escriba: `pip install -Nombre completo del archivo`
Nota: en nuestro caso sería: `pip install PEC4_Borja_Villena_Pardo-0.1.tar.gz`
- Una vez instalado, descomprima el archivo de manera manual. Botón derecho sobre el archivo de instalación, y click en 
`Extraer en`.
- **MUY IMPORTANTE** Copie la BBDD con la que desea trabajar dentro del archivo de instlación que acabamos de 
descomprimir, concretamente dentro de la subcarpeta `PEC4_Borja_Villena_Pardo-0.1\data`. Sin este paso nuestro 
programa no funcionará correctamente.
Nota: en la subcarpeta `data` de nuestro proyecto puede encontrar disponible el 
archivo de la BBDD `TMDB.zip`. Úselo si lo desea.
- Una vez copiada la BBDD en la ruta especificada, navegaremos en el terminal hasta llegar al archivo `main.py`. 
Este archivo se encuentra en la siguiente subcarpeta del archivo de instalación:
`..\PEC4_Borja_Villena_Pardo-0.1\PEC4_Borja_Villena_Pardo-0.1\src`
- Una vez ubicados en esta ruta, ejecutaremos nuestro programa escribiendo en el terminal:
`python main.py`
Nota: puede que si le da error deba de escribir en su lugar: `python3 main.py`
- Una vez hecho esto, acabamos de ejecutar nuestro programa. A partir de este momento seguiremos las indicaciones que 
nos devuelva el propio programa a través del terminal.

Por otro lado, para llevar a cabo los tests, estos están realizados para ser ejecutados desde PyCharm.
Hay un archivo de test por cada uno de los ejercicios de la PEC. Los encontraremos en la subcarpeta
`tests` de nuestro proyecto.

Para ejecutarlos, iremos uno a uno desde la interfaz d PyCharm, pulsaremos botón derecho encima, y haremos
click en `RUN` o `Ctrl+Mayus+F10`. Observaremos en la pantalla de ejecución si llevan a cabo
sus comprobaciones correctamente. 
NOTA: En cada uno de los tests, se han codificado Repositorios temporales que serán eliminados 
automáticamente una vez realizadas las pruebas pertinentes.
