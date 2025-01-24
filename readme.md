# Proyecto de Ajedrez

Este proyecto es un juego de ajedrez desarrollado en Python y Vue.js. A continuación se detalla la estructura del proyecto y su contenido.

## Estructura del Proyecto

# Project Structure

```plaintext
/project-root
│
├── desktop
│   ├── board.py
│   ├── game.py
│   ├── img
│   │   ├── util
│   │   │   ├── baner.svg
│   │   │   └── blits.svg
│   ├── main.py
│   ├── pices.py
│   ├── player.py
│   └── utils
│       ├── imports.py
│       └── variables.py
│
├── backend
│   ├── main.py
│   └── models.py
│
├── frontend
│   ├── .gitignore
│   ├── babel.config.js
│   ├── jsconfig.json
│   ├── package.json
│   ├── public
│   │   └── index.html
│   └── src
│       ├── App.vue
│       ├── components
│       │   └── HelloWorld.vue
│       └── main.js
└── vue.config.js
```

## Descripción de Directorios

### `desktop`

Este directorio contiene la lógica del juego de ajedrez, incluyendo la representación del tablero, las piezas y la lógica de movimiento.

- **board.py**: Define la clase `Board` que representa el tablero de ajedrez.
- **game.py**: Contiene la lógica del juego, incluyendo el cambio de turnos y la visualización del tablero.
- **img**: Contiene imágenes y gráficos utilizados en el juego.
- **main.py**: Punto de entrada para ejecutar el juego.
- **pices.py**: Define las clases para las piezas del ajedrez.
- **player.py**: Maneja la lógica de los jugadores.
- **utils/imports.py**: Maneja la carga de recursos gráficos.
- **varibales.py**: Define las variables y enumeraciones utilizadas en el juego.

### `backend`

Este directorio contiene la API del juego, que permite la interacción con el juego a través de solicitudes HTTP.

- **main.py**: Configura la aplicación FastAPI y define las rutas.
- **models.py**: Define los modelos de datos y la conexión a la base de datos.

### `frontend`

Este directorio contiene la interfaz de usuario del juego, desarrollada con Vue.js.

- **.gitignore**: Archivos y directorios que deben ser ignorados por Git.
- **babel.config.js**: Configuración de Babel para la transpilación de JavaScript.
- **jsconfig.json**: Configuración del compilador para JavaScript.
- **package.json**: Dependencias y scripts del proyecto.
- **public/index.html**: Archivo HTML principal de la aplicación.
- **src**: Contiene los componentes de Vue.js y el archivo principal de la aplicación.
- **vue.config.js**: Configuración de Vue CLI.

## Contribuidores

- **Tu Nombre** - [Juan Diaz](https://github.com/juanjh1)


## Cómo Ejecutar el Proyecto

1. **Backend**: Navega al directorio `backend` y ejecuta el siguiente comando:
   ```bash
   uvicorn main:app --reload
   ```

2. **Frontend**: Navega al directorio `frontend` y ejecuta:
   ```bash
   npm install
   npm run serve
   ```

3. **Desktop**: Navega al directorio `desktop` y ejecuta:
   ```bash
   python main.py
   ```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
