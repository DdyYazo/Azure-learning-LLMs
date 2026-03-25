<div align="center">

# **Descubrimiento Analisis y Planeación con Claude Code**

<p align="center">
  <img src="https://i.postimg.cc/MKztbJts/imagen-2026-02-03-115640734.png" alt="Aquí va el texto del enlace" width="500">
</p>

</div>

# **Tabla de contenido**
- [**Descubrimiento Analisis y Planeación con Claude Code**](#descubrimiento-analisis-y-planeación-con-claude-code)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Introducción a MCP**](#1-introducción-a-mcp)
  - [1.1. **¿Qué es el Model Context Protocol y por qué es importante?**](#11-qué-es-el-model-context-protocol-y-por-qué-es-importante)
  - [1.2. **¿Cómo implementar MCP en tus proyectos?**](#12-cómo-implementar-mcp-en-tus-proyectos)
  - [1.3. **Funcionalidades avanzadas del protocolo**](#13-funcionalidades-avanzadas-del-protocolo)
  - [1.4. **¿Por qué aprender MCP cambia tu rol como desarrollador?**](#14-por-qué-aprender-mcp-cambia-tu-rol-como-desarrollador)
- [2. **Componentes esenciales del protocolo MCP: servidor, cliente y host**](#2-componentes-esenciales-del-protocolo-mcp-servidor-cliente-y-host)
  - [2.1. **¿Qué es un servidor `"El cerebro del sistema"` y cuál es su función en MCP?**](#21-qué-es-un-servidor-el-cerebro-del-sistema-y-cuál-es-su-función-en-mcp)
    - [2.1.1. **Elementos clave del servidor en MCP**](#211-elementos-clave-del-servidor-en-mcp)
  - [2.2. **¿Cómo interactúan cliente `"El traductor intermedio"` y host `"La pantalla donde ves todo"` con el servidor en MCP?**](#22-cómo-interactúan-cliente-el-traductor-intermedio-y-host-la-pantalla-donde-ves-todo-con-el-servidor-en-mcp)
  - [2.3. **¿Cuál es el flujo detallado de información dentro del MCP?**](#23-cuál-es-el-flujo-detallado-de-información-dentro-del-mcp)
  - [2.4. **Explicacion puntual de los conceptos**](#24-explicacion-puntual-de-los-conceptos)
- [3. **Preparación del entorno de desarrollo para MCP con Python**](#3-preparación-del-entorno-de-desarrollo-para-mcp-con-python)
  - [3.1. **¿Qué herramientas instalar para MCP con Python?**](#31-qué-herramientas-instalar-para-mcp-con-python)
  - [3.2. **¿Qué versiones y comandos comprobar?**](#32-qué-versiones-y-comandos-comprobar)
    - [3.2.1. *Versiones de referencia del entorno*](#321-versiones-de-referencia-del-entorno)
  - [3.3. **¿Por qué usar WSL o Linux en el entorno?**](#33-por-qué-usar-wsl-o-linux-en-el-entorno)
  - [3.4. **¿Qué conocimientos previos recomienda el instructor?**](#34-qué-conocimientos-previos-recomienda-el-instructor)
    - [3.4.1. *Conocimientos de LLM e IA sugeridos*](#341-conocimientos-de-llm-e-ia-sugeridos)
    - [3.4.2. *Nivel de programación requerido*](#342-nivel-de-programación-requerido)
  - [3.5. **¿Se necesita suscripción de Azure para MCP?**](#35-se-necesita-suscripción-de-azure-para-mcp)
- [4. **Configuración de entorno de trabajo para desarrollo MCP**](#4-configuración-de-entorno-de-trabajo-para-desarrollo-mcp)
  - [4.1. **¿Qué opciones existen para configurar un entorno de trabajo MCP?**](#41-qué-opciones-existen-para-configurar-un-entorno-de-trabajo-mcp)
  - [4.2. **¿Cómo instalar y preparar MCP usando Python?**](#42-cómo-instalar-y-preparar-mcp-usando-python)
  - [4.3. **¿Cuál es el flujo básico para correr un servidor MCP?**](#43-cuál-es-el-flujo-básico-para-correr-un-servidor-mcp)
  - [4.4. **¿Cómo usar el MCP Inspector para revisar recursos y herramientas?**](#44-cómo-usar-el-mcp-inspector-para-revisar-recursos-y-herramientas)
  - [4.5. **¿Qué ejercicios prácticos ayudan a reforzar el aprendizaje?**](#45-qué-ejercicios-prácticos-ayudan-a-reforzar-el-aprendizaje)

# 1. **Introducción a MCP**

La revolución de la inteligencia artificial no está en los modelos más grandes, sino en la forma en que nos comunicamos con ellos. El **Model Context Protocol (MCP)** representa un cambio de paradigma en cómo interactuamos con sistemas de **IA**, transformando desarrolladores en arquitectos de sistemas inteligentes. Este protocolo establece el puente crucial entre nuestro código y los modelos de lenguaje avanzados, abriendo posibilidades que van mucho más allá de simples consultas a **ChatGPT**.

## 1.1. **¿Qué es el Model Context Protocol y por qué es importante?**

El **Model Context Protocol (MCP)** es el estándar que permite que el software se comunique con sistemas de inteligencia artificial de manera integrada y eficiente. Similar a lo que representó **HTTP** para la web en los años noventa, **MCP** está posicionándose como el protocolo fundamental que dominarán los líderes en el desarrollo de **IA**.

Este protocolo no es simplemente una herramienta más, sino la base para construir productos inteligentes, escalables y conversacionales. A diferencia de enfoques tradicionales, **MCP** reconoce que el futuro de la inteligencia artificial no depende de un modelo aislado, sino de un ecosistema completo e interconectado.

La importancia de **MCP** radica en su capacidad para crear una **arquitectura cliente-servidor** específica para **IA**:

- **Cliente**: puede ser un editor de código, un navegador web o incluso un bot de voz.
- **Servidor**: actúa como orquestador de inteligencia artificial, definiendo contextos y controlando respuestas.

<p align="center">
  <img src="https://i.postimg.cc/GpN8VcXP/Screenshot-2026-03-02-214104.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Arquitectura cliente-servidor de MCP</strong></span>
</p>
</br>


> [!IMPORTANT]
>
> **MCP** no es una API más. Es el protocolo que define cómo el software y los modelos de lenguaje **LLMs** se integran en un ecosistema cognitivo completo e interconectado.

## 1.2. **¿Cómo implementar MCP en tus proyectos?**

La implementación de **MCP** es sorprendentemente accesible, incluso para desarrolladores que apenas comienzan a explorar el campo de la inteligencia artificial. El proceso puede dividirse en etapas concretas y manejables:

- **En 10 minutos**: configurar tu primer servidor **MCP** funcionando.
- **En 20 minutos**: lograr integración con un modelo de lenguaje.
- **En menos de una hora**: desplegar a producción utilizando **Server Send Events (SSE)**.

Herramientas como **VS Code** se transforman en clientes inteligentes dentro de este ecosistema, mientras que servicios como **Azure OpenAI** se convierten en proveedores de la capacidad computacional necesaria. Lo verdaderamente revolucionario es que tú mantienes el control sobre aspectos críticos:

- Qué contexto se almacena.
- Cómo se optimizan las respuestas.
- De qué manera se enrutan las solicitudes.

> [!TIP]
>
> Usa **VS Code** como cliente y **Azure OpenAI** como proveedor para tener un entorno **MCP** completamente funcional en menos de una hora, sin configuraciones complejas.

## 1.3. **Funcionalidades avanzadas del protocolo**

**MCP** ofrece capacidades sofisticadas que transforman completamente la manera en que desarrollamos aplicaciones basadas en **IA**:

- **[RootContext]**: permite mantener conversaciones persistentes, conservando el historial y contexto de interacciones previas.
- **Enrutamiento inteligente**: facilita la distribución de tareas entre diversos agentes de **IA** según su especialización.
- **Arquitectura cliente-servidor**: separa claramente las responsabilidades entre la interfaz de usuario y el procesamiento de la inteligencia artificial.

## 1.4. **¿Por qué aprender MCP cambia tu rol como desarrollador?**

Dominar **MCP** representa un cambio fundamental en tu relación con la inteligencia artificial. Ya no serás simplemente un usuario de **IA**, sino un arquitecto de sistemas inteligentes. Esta transformación tiene implicaciones profundas:

- Tu código deja de ejecutarse de manera aislada para integrarse en un sistema cognitivo completo.
- Se adquiere control sobre cómo los modelos de lenguaje interpretan y responden a las solicitudes.
- Se pueden desarrollar aplicaciones con conversaciones persistentes y contextualmente ricas.

Los productos más innovadores de los próximos años no se construirán únicamente con **APIs** tradicionales. El futuro pertenece a quienes dominen:

- Protocolos de control de mensajes como **MCP**.
- Arquitecturas persistentes para mantener el contexto conversacional.
- Herramientas de integración multimodal que combinen diferentes formas de procesamiento de información.

---

# 2. **Componentes esenciales del protocolo MCP: servidor, cliente y host**

El protocolo **MCP** comprende varios conceptos imprescindibles que, al dominarlos, facilitan enormemente la programación en cualquier lenguaje deseado. Conocer estos principios permite gestionar sin dificultad cualquier implementación relacionada con **MCP**.

<p align="center">
  <img src="https://i.postimg.cc/3RtKV98z/Screenshot-2026-03-02-220745.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Componentes del protocolo MCP: cliente, servidor y host</strong></span>
</p>
</br>

## 2.1. **¿Qué es un servidor `"El cerebro del sistema"` y cuál es su función en MCP?**

El **servidor** es un componente fundamental en el protocolo **MCP**. Su rol principal es integrar todas las piezas que se quieran gestionar en **MCP**. Funciona recibiendo solicitudes y generando respuestas usando diferentes fuentes de información:

### 2.1.1. **Elementos clave del servidor en MCP**

- **Información contextual**: obtenida mediante conversaciones o interacción con algún **LLM**.
- **Fuentes de conocimiento externas**: documentos y enlaces externos.
- **Archivos locales**: interacciones específicas con archivos almacenados localmente.
- **APIs o servicios web**: comunicación con servicios externos para extraer información.

<p align="center">
  <img src="https://i.postimg.cc/Znqq52sr/imagen-2026-03-02-221103195.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Elementos clave del servidor en MCP</strong></span>
</p>
</br>

> [!NOTE]
>
> El **servidor** actúa como el núcleo inteligente del protocolo: centraliza y coordina las cuatro fuentes de información para generar respuestas contextualizadas.

## 2.2. **¿Cómo interactúan cliente `"El traductor intermedio"` y host `"La pantalla donde ves todo"` con el servidor en MCP?**

1. El **cliente** recibe y estructura las respuestas del **servidor** para presentarlas de forma clara y comprensible. Primero recibe la pregunta del usuario, la procesa y realiza una petición apropiada al **servidor**. Luego recibe su respuesta y la transforma a un formato amigable.

2. El **host** es la interfaz que permite la interacción directa de los usuarios con **MCP**. Es el elemento final donde el **cliente** presenta la información procesada. Ejemplos comunes de **host** incluyen aplicaciones y entornos de desarrollo integrados como **VS Code**, **Visual Studio** o **Eclipse**.


## 2.3. **¿Cuál es el flujo detallado de información dentro del MCP?**

El flujo de información inicia con una pregunta del usuario específica al contexto del **MCP** activo. 
- El **cliente** procesa la pregunta, 
- Transfiere la solicitud al **servidor**
- Este utiliza de manera autónoma las cuatro fuentes de información para generar una respuesta adecuada. 
- Luego el **cliente** estructura la respuesta y la transfiere al **host** para su presentación final.

<p align="center">
  <img src="https://i.postimg.cc/J03SSz5Q/imagen-2026-03-02-221955799.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Representacion del flujo de información dentro del protocolo MCP</strong></span>
</p>
</br>

Este flujo se resume en los siguientes pasos:

1. El usuario formula la pregunta en función del contexto del **MCP**.
2. El **cliente** interpreta la pregunta y solicita información al **servidor**.
3. El **servidor** analiza las fuentes de información disponibles y genera una respuesta.
4. El **cliente** reorganiza esa respuesta de manera organizada y clara.
5. El **host** presenta la información procesada al usuario.

## 2.4. **Explicacion puntual de los conceptos**


<p align="center">
  <img src="https://i.postimg.cc/xCvg3Jcj/imagen-2026-03-24-212216677.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Definicion puntual de los conceptos del protocolo MCP</strong></span>
</p>
</br>

---


# 3. **Preparación del entorno de desarrollo para MCP con Python**

Contar con las herramientas correctas evita errores y pérdidas de tiempo. El enfoque es trabajar con **Python**, **pip**, **UV** para entornos virtuales, **Uvicorn** como servidor web ligero y **npx** de **npm** para usar el inspector de **MCP** con interfaz gráfica.

## 3.1. **¿Qué herramientas instalar para MCP con Python?**

El entorno de desarrollo requiere cinco herramientas fundamentales. Cada una cumple un rol específico dentro del ecosistema **MCP**:

- **Python**: lenguaje elegido para el desarrollo en el curso.
- **pip**: instalación de dependencias puntuales cuando haga falta.
- **UV**: creación de entornos virtuales para aislar paquetes y evitar conflictos.
- **Uvicorn**: ejecución de servicios web de prueba, común con **FastAPI**.
- **npx**: ejecución del inspector de **MCP** sin instalaciones globales.

## 3.2. **¿Qué versiones y comandos comprobar?**

Antes de iniciar el desarrollo, verificar que cada herramienta esté disponible en el sistema. Ejecutar los siguientes comandos en la terminal:

- Verificar **Python 3** instalado:

```bash
python3 --version
```

- Confirmar **pip** activo:

```bash
pip3 --version
```

- Instalar **Uvicorn** desde **pip**:

```bash
pip3 install uvicorn
```

> [!IMPORTANT]
>
> Instalar el script de **UV** de Astral **antes** de instalar **Uvicorn** facilita la gestión de entornos virtuales y evita conflictos de dependencias. Ejecutar: `curl -LsSf https://astral.sh/uv/install.sh | sh`

- Comprobar **npx** para el inspector de **MCP**:

```bash
npx --version
```

### 3.2.1. *Versiones de referencia del entorno*

- **Python 3**: base del desarrollo. Versión de referencia: `3.13.7`.
- **pip**: gestor de paquetes de **Python**. Versión de referencia: `25.x`.
- **Uvicorn**: mini servidor web útil con **FastAPI** para pruebas locales.
- **npx** (**npm/Node**): necesario para ejecutar el inspector gráfico de **MCP**.

## 3.3. **¿Por qué usar WSL o Linux en el entorno?**

El trabajo se realiza en una terminal de **Ubuntu** usando **WSL** en **Windows**. Esto facilita una experiencia similar a Linux incluso en equipos Windows. En **macOS** o **Linux** puede haber variaciones menores, pero la lógica es la misma: terminal y herramientas al día.

## 3.4. **¿Qué conocimientos previos recomienda el instructor?**

**MCP** se ubica dentro de la especialidad de **AI Engineer**. Para aprovechar mejor el curso, se sugiere haber completado los fundamentos de **LLM** e inteligencia artificial, además de programar con soltura en el lenguaje elegido.

### 3.4.1. *Conocimientos de LLM e IA sugeridos*

- Conceptos base de modelos de lenguaje.
- Fundamentos de inteligencia artificial aplicados.
- Vocabulario y práctica mínima para entender la terminología del curso.

### 3.4.2. *Nivel de programación requerido*

- Manejo de sintaxis y módulos del lenguaje que usarás.
- Capacidad para instalar paquetes y entender errores.
- Confort con terminal y comandos básicos.

## 3.5. **¿Se necesita suscripción de Azure para MCP?**

**No es obligatoria**, pero **es altamente deseable para desplegar el servidor de MCP en la nube y usar recursos asociados**. Puedes crear una suscripción gratuita con cerca de 200 dólares de crédito. El consumo estimado para el curso es de 3 a 4 dólares bien administrados.

---

# 4. **Configuración de entorno de trabajo para desarrollo MCP**

Al iniciar en el desarrollo con **MCP**, es clave entender cómo preparar un entorno de trabajo funcional y adaptable. Este proceso no tiene que ser complicado y permite elegir entre diferentes herramientas según tus preferencias. El ejemplo usa **Python** y **VS Code**, aunque existen opciones alternativas para distintos entornos y lenguajes.

## 4.1. **¿Qué opciones existen para configurar un entorno de trabajo MCP?**

Puedes trabajar con **VS Code**, **Eclipse**, **IntelliJ**, **Visual Studio** o incluso soluciones en la nube como **Claude.ai** de Anthropic. Todas estas opciones son válidas y la decisión depende de lo que más te acomode.

Aunque el ejemplo se realiza en **Python**, existen **SDKs** para otros lenguajes:

- **TypeScript**
- **C#**
- **Java**
- **Node**

> [!NOTE]
>
> La flexibilidad de **MCP** para adaptarse a múltiples lenguajes y entornos es una de sus ventajas clave. No estás limitado a **Python**.

## 4.2. **¿Cómo instalar y preparar MCP usando Python?**

1. Preparar un repositorio vacío. Crear el directorio de trabajo y acceder a él:

```bash
mkdir carpeta_base
cd carpeta_base
```

2. Instalar el paquete de **pip** para **MCP**. Esto proporciona una herramienta de línea de comandos para gestionar todos los proyectos **MCP**:

```bash
pip install "[mcp-cli]"
```

3. Crear un archivo `server.py`

## 4.3. **¿Cuál es el flujo básico para correr un servidor MCP?**

En `server.py` incluir el import de la librería **MCP** y la creación de un servidor:

```python
import fastmcp

mcpfastdemo = fastmcp.Server()
```

Puedes agregar recursos y herramientas personalizadas. Luego, desde la terminal, ejecutar el servidor en modo desarrollo:

```bash
mcp dev server.py
```

El servidor responde mostrando un token de sesión y la entrada al **MCP Inspector**. 

> [!NOTE]
>
> El mcp inspector es una herramienta gráfica que permite revisar los recursos y herramientas definidos en el servidor **MCP**. Es fundamental para validar la implementación antes de conectar un cliente real.

<p align="center">
  <img src="https://i.postimg.cc/G359jcsF/Screenshot-2026-03-24-221528.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Inspector de MCP mostrando el token de sesión</strong></span>
</p>
</br>

> [!TIP]
> 
> Si surge algún problema de conectividad al intentar conectar, si se cuenta con **npx** en el sistema la alternativa es ejecutar:



> [!WARNING]
>
> Si surge algún problema de conectividad en el inspector como se puede visualizar en la anterior imagen, detener el proceso con `Ctrl+C`, limpiar la terminal y usar `mcp run server.py` en lugar de `mcp dev server.py`. Esto suele solucionar el inconveniente. Adicionalmente si se cuenta con **npx** en el sistema, la alternativa es ejecutar el siguiente comando para iniciar el inspector de **MCP** y que permita conectarse al servidor sin problemas de conectividad:

```bash
npx @modelcontextprotocol/inspector mcp run server.py
```

<p align="center">
  <img src="https://i.postimg.cc/SNtQWqJF/imagen-2026-03-24-222754182.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Inspector de MCP conectado al servidor sin problemas de conectividad</strong></span>
</p>
</br>


## 4.4. **¿Cómo usar el MCP Inspector para revisar recursos y herramientas?**

El **Inspector** permite listar recursos y herramientas del servidor. Desde su interfaz puedes ver:

- **Recursos definidos**: por ejemplo, `greeting` con el parámetro `name`.

<p align="center">
  <img src="https://i.postimg.cc/BZKRh0hR/Screenshot-2026-03-24-223124.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Seccion de recursos definidos en el inspector de MCP</strong></span>
</p>
</br>

- **Herramientas disponibles**: por ejemplo, sumar dos números, accesibles desde el inspector.

<p align="center">
  <img src="https://i.postimg.cc/W3JYfG73/Screenshot-2026-03-24-223158.png" alt="" width="450">
</p>
<p align="center">
  <span align="center"><strong>Seccion de herramientas disponibles en el inspector de MCP</strong></span>
</p>
</br>

> [!TIP]
>
> Usa el **MCP Inspector** para validar la implementación antes de conectar un cliente real. Facilita rastrear todos los componentes, visualizar su estructura y verificar lo que un cliente podría consumir.

## 4.5. **¿Qué ejercicios prácticos ayudan a reforzar el aprendizaje?**

Para consolidar lo aprendido, practicar con estas extensiones al servidor:

1. Agregar métodos como **restar**, **multiplicar** y **dividir**.
2. Crear recursos que permitan respuestas personalizadas, por ejemplo: `«Tu nombre completo es...»`, usando parámetros.
3. Experimentar con combinaciones de herramientas y recursos para ampliar las funcionalidades del servidor **MCP**.

---