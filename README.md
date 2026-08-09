# Red Neuronal Básica con TensorFlow / Keras

Una pequeña demostración en Python de una red neuronal muy básica (regresión lineal) usando TensorFlow / Keras. Está pensada como ejemplo didáctico para quienes comienzan a aprender redes neuronales con TensorFlow.

## Contenido del repositorio
- `regresion_lineal_keras.py` — Script Python con un ejemplo mínimo de una capa Dense (1 neurona). El script actualmente muestra cómo crear y usar un modelo Keras, y realiza una predicción simple.
- `requirements.txt` — Dependencias recomendadas (TensorFlow, numpy, matplotlib, pandas, scikit-learn).

## Requisitos
- Python 3.10+ (recomendado)
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar
Desde el directorio del proyecto:

```bash
python regresion_lineal_keras.py
```

El script imprimirá la predicción del modelo para el valor 10.0 (nota: en el estado actual el modelo no ha sido entrenado con etiquetas, por lo que la salida es el estado inicial de la red).

## Qué hace el script
- Crea un modelo secuencial con una sola capa densa de 1 unidad y `input_shape=[1]`.
- Compila el modelo con el optimizador `sgd` y la pérdida `mean_squared_error`.
- Llama a `modelo.predict(np.array([10.0]))` y muestra el resultado.

Observación: el archivo es un ejemplo mínimo y no incluye entrenamiento (no hay llamadas a `modelo.fit(...)` con datos de entrada/etiqueta). Además hay variables de ejemplo en el script que sobrescriben valores; revisa y ajusta los datos antes de entrenar.

## Próximos pasos sugeridos
- Corregir la inicialización/uso de datos en `regresion_lineal_keras.py` y agregar un bloque de entrenamiento (`fit`) con etiquetas.
- Añadir ejemplos de visualización (matplotlib) para mostrar ajuste de la recta.
- Agregar tests o notebooks explicativos para uso educativo.

## Contacto
Autor del repositorio: LeoBringasAtLife
