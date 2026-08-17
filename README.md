# 🎯 IPFramework

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Plataforma](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/status-Active-success)
![License](https://img.shields.io/badge/license-MIT-green)

IPFramework es una plataforma de software científico orientada a la simulación, control y experimentación con un sistema de péndulo invertido sobre carro. El software integra estrategias de control clásico y técnicas de aprendizaje por refuerzo dentro de una misma interfaz de operación.
La plataforma permite seleccionar y ejecutar los controladores LQR, SAC y DDPG para el control de un sistema físico de péndulo invertido sobre carro, mediante la comunicación con un microcontrolador Arduino. Durante la ejecución, IPFramework adquiere y procesa las variables del sistema, genera las acciones de control correspondientes y proporciona herramientas para la visualización, supervisión y registro de la telemetría.
Asimismo, el software incorpora funciones para el entrenamiento de agentes de aprendizaje por refuerzo, la configuración de sus parámetros, el almacenamiento de modelos entrenados y la exportación de resultados experimentales.


## ✨ Características principales

- **🎛️ Cambio de controlador:** Cambie fácilmente entre los controladores **LQR, SAC y DDPG** en tiempo real.
- **📈 Telemetría y visualización en tiempo real:** Visualice dinámicamente las variables de estado (ángulo, posición, velocidades y recompensas) mediante **PyQtGraph**.
- **🧠 Entrenamiento de RL integrado en la interfaz gráfica:** Inicie, supervise y gestione el entrenamiento de agentes **SAC y DDPG** directamente desde la interfaz.
- **⚙️ Ajuste dinámico de parámetros:** Modifique los valores de las ganancias **K** del controlador LQR durante la ejecución.
- **💾 Exportación de telemetría a CSV:** Exporte los datos operativos en tiempo real para su posterior análisis e investigación.

---

## 🎥 Ejemplos del sistema

A continuación se presentan demostraciones del sistema funcionando con diferentes controladores:

### Control LQR+Swing-up

https://github.com/user-attachments/assets/67b9c8fa-9cf9-4b68-b97f-80f71a330034

### Soft Actor-Critic (SAC) Control

https://github.com/user-attachments/assets/48dc87b7-8e3e-41b1-96c2-5b272821629d

### Deep Deterministic Policy Gradient (DDPG) Control

https://github.com/user-attachments/assets/c9809c6d-f873-4e72-b827-2b89e02e6914

---

## 🚀 Guía de uso de la interfaz gráfica

La interfaz de usuario está diseñada para ser intuitiva, al tiempo que proporciona acceso a parámetros avanzados de control.

1. **Selección del controlador:** Utilice el menú desplegable del panel principal para seleccionar el controlador activo (`LQR`, `SAC` o `DDPG`).
2. **Ejecución del sistema:**
   - Asegúrese de que el Arduino esté conectado (si utiliza el modo hardware) y seleccione el puerto COM correspondiente en el menú desplegable.
   - Haga clic en el botón **Start** para iniciar el lazo de control.
3. **Detención de la ejecución:** Haga clic en el botón **Stop** o **Emergency Stop** para detener el péndulo de forma segura y desactivar las salidas del motor.
4. **Edición de las ganancias LQR:** Cuando se seleccione LQR, utilice los campos de entrada dinámicos para ajustar las matrices de ponderación $K$ y observar los cambios en la estabilidad del sistema.
5. **Visualización de telemetría y gráficas:** El panel de control muestra en tiempo real los valores numéricos de la telemetría. Cambie a las pestañas de visualización para observar gráficas en tiempo real del ángulo del péndulo, la posición del carro y la acción de control.
6. **Entrenamiento de agentes:** Acceda a la pestaña de entrenamiento de RL, configure los hiperparámetros (número de episodios, tamaño del lote) y haga clic en **Train**. El progreso y las recompensas se registran directamente en la interfaz.

---

### Instalación

Clone el repositorio y configure el entorno:

```bash
git clone https://github.com/primbiolab/IP_Framework
cd IPFramework
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Ejecución del sistema

Para iniciar el panel de control desarrollado en PyQt5 y comenzar a interactuar con el sistema:

```bash
python main_GUI.py
```

---

## 🔌 Requisitos de hardware

Para ejecutar este sistema con hardware físico, se requiere:

- Un microcontrolador **Arduino** programado con `inverted_pendulum_arduino.ino`.
- Controladores de motor y encoders conectados de acuerdo con las especificaciones esperadas por el firmware de Arduino.
- Una conexión USB Serial estable con el computador.

---

## 🏗️ Arquitectura del sistema

El software está diseñado para ofrecer un funcionamiento estricto en tiempo real mediante una arquitectura de múltiples capas:

- **GUI (PyQt5):** Gestiona todas las interacciones con el usuario, la actualización dinámica de parámetros y la visualización de gráficas en tiempo real mediante `pyqtgraph`. Opera en el hilo principal para mantener la interfaz responsiva.
- **Motor de multiprocesamiento:** Para evitar que la interfaz gráfica interfiera con la ejecución del control, el sistema utiliza el módulo `multiprocessing` de Python. Los lazos de control y la comunicación serial se ejecutan en procesos independientes y de alta prioridad.
- **Cola de telemetría:** Un sistema de colas seguro para la comunicación entre hilos y procesos transporta los vectores de estado y las recompensas desde el proceso de control hacia la GUI para su visualización y registro.
- **Lógica de control:** Está diseñada de forma modular para permitir el cambio dinámico entre el solucionador algebraico LQR y los motores de inferencia basados en redes neuronales (SAC/DDPG).
- **Simulación del entorno:** Un envoltorio personalizado que imita la API serial del hardware permite una transición fluida entre la simulación de la dinámica mediante Pygame y la actuación sobre el hardware físico.

---

## 📁 Estructura del proyecto

```text
Files/
├── agent_ddpg.py          # Implementación del algoritmo DDPG y lógica del actor/crítico
├── agent_sac.py           # Implementación del algoritmo SAC con ajuste de entropía
├── buffer.py              # Búfer de repetición para el entrenamiento RL off-policy
├── controller_runner.py   # Envoltorio de multiprocesamiento para la ejecución del control en tiempo real
├── environment.py         # Simulación de la dinámica e interacción con el hardware
├── LQR.py                 # Solucionadores matriciales y lógica del regulador LQR
├── main_ddpg.py           # Script independiente para entrenar el agente DDPG
├── main_sac.py            # Script independiente para entrenar el agente SAC
├── networks.py            # Arquitecturas de redes neuronales PyTorch para los agentes RL
├── plotting.py            # Utilidades para la visualización en tiempo real mediante PyQtGraph
├── test_ddpg.py           # Script para evaluar modelos DDPG previamente entrenados
├── test_sac.py            # Script para evaluar modelos SAC previamente entrenados
│
├── Models_agents/         # Directorio que contiene los pesos de los modelos PyTorch entrenados (.pth)
│   ├── ddpg/
│   ├── Modelo_con_entropia_final/
│   └── Pendulo_Entrenamiento_Nuevo/
│
├── videos/                # Videos demostrativos de los controladores en funcionamiento
│   ├── DDPG.mp4
│   ├── lqr_pendulum.mp4
│   └── SAC.mp4
│
├── inverted_pendulum_arduino.ino # Firmware en C++ para el microcontrolador Arduino
├── main_GUI.py            # Punto de entrada principal que inicia el panel de control PyQt5
└── requirements.txt       # Dependencias de paquetes de Python
```
---

## 🏋️ Entrenamiento de agentes de RL

El framework permite realizar el entrenamiento completo de modelos de aprendizaje por refuerzo:

- **Modos de entrenamiento:** Ejecute los scripts independientes (`main_sac.py` / `main_ddpg.py`) para realizar el entrenamiento sin interfaz gráfica, o inicie el entrenamiento directamente desde la pestaña **RL Training** de la GUI.
- **Límite de episodios:** Cada episodio se reinicia automáticamente después de 400 pasos (aproximadamente 15 segundos).
- **Puntos de control de los modelos:** Los pesos de las políticas se guardan periódicamente y se exportan al directorio `Models_agents/`, lo que permite seleccionarlos inmediatamente desde la GUI.

---

## ⚠️ Notas y solución de problemas

- **Problemas con el puerto serial:** Si el sistema no logra conectarse al hardware, verifique que el puerto COM correcto esté seleccionado en la GUI y asegúrese de que el Monitor Serial del Arduino IDE esté cerrado.
- **Modelos faltantes:** Si aparece un error al seleccionar SAC o DDPG en la GUI, asegúrese de que los pesos preentrenados estén ubicados correctamente en los subdirectorios de `Models_agents/`.

---


## 📜 Créditos y Contexto

Desarrollado en la Universidad Nacional de Colombia, Sede La Paz, en el marco de las actividades académicas de sus autores.

---
## Afiliación institucional

Escuela de Pregrado, Dirección Académica, Vicerrectoría de Sede, Universidad Nacional de Colombia, Sede La Paz, Cesar, Colombia.
