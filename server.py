
# Crear server.py para import de MPC

from mcp.server.fastmcp import FastMCP

# Crear una instancia de FastMCP con el nombre "Demo"
mcp = FastMCP("Demo")

# Agregar una tool al servidor MCP
@mcp.tool()
def add(a: int, b: int) -> int:
    """Agrega dos números enteros."""
    return a + b

# Agregar dinamicamente un recurso al servidor MCP
@mcp.resource("gretting/{name}")
def get_greeting(name: str) -> str:
    """Obtiene un saludo personalizado."""
    return f"Hola, {name}!"