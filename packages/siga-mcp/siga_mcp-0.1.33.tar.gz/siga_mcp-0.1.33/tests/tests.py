import asyncio
from siga_mcp.tools import listar_atendimentos_os


async def main() -> str:
    return await listar_atendimentos_os(
        **{
            "matricula": "24142",
            "codigo_os": None,
            "data_inicio": "25/09/2025",
            "data_fim": "25/09/2025",
        }
    )


if __name__ == "__main__":
    resultado = asyncio.run(main())
    print(resultado)
