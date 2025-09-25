"""Este módulo guarda todas as funções do MCP visíveis para o Agente usar"""

from os import getenv
from typing import Literal, Sequence

import aiohttp
import ujson
from siga_mcp import memory
from siga_mcp._types import (
    CategoriasInfraestruturaType,
    EquipeInfraestruturaType,
    EquipeSistemasType,
    FiltrosOSType,
    OrigemAtendimentoAvulsoSistemasType,
    ProjetoType,
    SistemasType,
    TipoAtendimentoAvulsoInfraestruturaType,
    TipoAtendimentoAvulsoSistemasType,
    TipoAtendimentosOSType,
    TiposAtendimentosOSType,
)
from siga_mcp.constants import (
    CATEGORIA_TO_NUMBER,
    COLABORADORES_PROMPT,
    EQUIPE_INFRAESTRUTURA_TO_NUMBER,
    EQUIPE_TO_NUMBER,
    ORIGEM_TO_NUMBER,
    PROJETO_TO_NUMBER,
    SISTEMA_TO_NUMBER,
    SYSTEM_INSTRUCTIONS,
    TIPO_TO_NUMBER_ATENDIMENTO_AVULSO,
    TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA,
    TYPE_TO_NUMBER,
)
from siga_mcp.decorators import controlar_acesso_matricula
from siga_mcp.domain import HoraMinuto, MeioPeriodo
from siga_mcp.utils import converter_data_siga, get_package_version
from siga_mcp.xml_builder import XMLBuilder


async def BUSCAR_INSTRUCOES_DE_USO_SIGA() -> str:
    return SYSTEM_INSTRUCTIONS


async def colaboradores_ativos_siga() -> str:
    return COLABORADORES_PROMPT


async def buscar_informacoes_atendimentos_os(
    codigo_atendimento: int,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosOs/buscarInfoAtendimentosOsSigaIA/",
            json={
                "apiKey": getenv("AVA_API_KEY"),
                "atendimento": codigo_atendimento,
                "analista": codigo_analista,
            },
        ) as response:
            try:
                json = await response.json(content_type=None)
                retorno = XMLBuilder().build_xml(
                    data=json["result"],
                    root_element_name="info_atendimentos_os",
                    item_element_name="info_atendimentos_os",
                    root_attributes={
                        "atendimento": str(codigo_atendimento),
                        "analista": str(codigo_analista),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                return "Erro ao buscar as informações do atendimento."


@controlar_acesso_matricula
async def buscar_pendencias_lancamentos_atendimentos(
    *,
    matricula: str | int | Literal["CURRENT_USER"] = "CURRENT_USER",
    dataIni: str,
    dataFim: str,
) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosAvulsos/buscarPendenciasRegistroAtendimentosSigaIA/",
            json={
                "matricula": matricula,
                "dataIni": converter_data_siga(dataIni),
                "dataFim": converter_data_siga(dataFim),
                "apiKey": getenv("AVA_API_KEY"),
            },
        ) as response:
            try:
                # Verifica se a requisição HTTP foi bem-sucedida (status 2xx)
                response.raise_for_status()

                # Converte a resposta para JSON, permitindo qualquer content-type
                data = await response.json(content_type=None)

                retorno = XMLBuilder().build_xml(
                    # Usa [] se 'result' não existir ou for None
                    data=data.get("result", []),
                    root_element_name="pendencias_lançamentos",
                    item_element_name="pendencias_lançamentos",
                    root_attributes={"matricula": str(matricula)},
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                # Captura qualquer outro erro não previsto
                return "Erro ao consultar todas as pendências de registros SIGA do usuário."


async def buscar_todas_os_usuario(
    *,
    matricula: str | Sequence[str] | Literal["CURRENT_USER"] | None = "CURRENT_USER",
    os: str | Sequence[str] | None = None,
    filtrar_por: Sequence[FiltrosOSType]
    | Literal["Todas OS em Aberto"]
    | str
    | None = None,
    data_inicio: str | None = None,
    data_fim: str | None = None,
) -> str:
    if not matricula and not os:
        return "Erro: É necessário informar pelo menos a matrícula ou o código da OS para realizar a consulta."

    if filtrar_por == "Todas OS em Aberto":
        filtrar_por = [
            "Pendente-Atendimento",
            "Em Teste",
            "Pendente-Teste",
            "Em Atendimento",
            "Em Implantação",
            "Pendente-Liberação",
            "Não Planejada",
            "Pendente-Sist. Administrativos",
            "Pendente-AVA",
            "Pendente-Consultoria",
            "Solicitação em Aprovação",
            "Pendente-Aprovação",
            "Pendente-Sist. Acadêmicos",
            "Pendente-Marketing",
            "Pendente-Equipe Manutenção",
            "Pendente-Equipe Infraestrutura",
            "Pendente-Atualização de Versão",
            "Pendente-Help-Desk",
            "Pendente-Fornecedor",
            "Pendente-Usuário",
        ]

    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/os/buscarTodasOsPorMatriculaSigaIA/",
            json={
                "descricaoStatusOs": filtrar_por or "",  # Array ou string puro
                "matricula": matricula or "",  # Array ou string puro
                "codOs": os or "",  # Array ou string puro
                "dataIni": converter_data_siga(data_inicio) if data_inicio else "",
                "dataFim": converter_data_siga(data_fim) if data_fim else "",
                "apiKey": getenv("AVA_API_KEY"),
            },
        ) as response:
            try:
                # Verifica se a requisição HTTP foi bem-sucedida (status 2xx)
                # response.raise_for_status()

                data = await response.json(content_type=None)
                retorno = XMLBuilder().build_xml(
                    data=data["result"],
                    root_element_name="ordens_servico",
                    item_element_name="ordem_servico",
                    root_attributes={"matricula": str(matricula)},
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception as e:
                # Captura qualquer outro erro não previsto
                return f"Erro ao consultar dados da(s) OS. {e} Matrícula: {matricula}"


async def editar_atendimentos_os(
    codigo_atendimento: int,
    codigo_os: int,
    data_inicio: str,
    codigo_analista: int,
    descricao_atendimento: str,
    tipo_atendimento: TiposAtendimentosOSType = "Implementação",
    data_fim: str | None = None,
    primeiro_atendimento: bool = False,
    apresenta_solucao: bool = False,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # Busca o tipo correto na constante TYPE_TO_NUMBER ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TYPE_TO_NUMBER
        (
            key
            for key in TYPE_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo_atendimento).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo_atendimento,
                    "mensagem": f"Tipo '{tipo_atendimento}' não encontrado na constante TYPE_TO_NUMBER",
                    "tipos_validos": list(TYPE_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={"sistema": "SIGA", "funcao": "editar_atendimentos_os"},
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TYPE_TO_NUMBER[tipo_normalizado]

    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosOs/updateAtendimentosOsSigaIA/",
                json={
                    "atendimento": codigo_atendimento,
                    "os": codigo_os,
                    "dataIni": data_inicio,
                    "analista": codigo_analista,
                    "descricao": descricao_atendimento,
                    "tipo": tipo_final,
                    "dataFim": data_fim,
                    "primeiroAtendimento": primeiro_atendimento,
                    "apresentaSolucao": apresenta_solucao,
                    "apiKey": getenv("AVA_API_KEY"),
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Atendimento não encontrado em OS. Tente buscar nas funções editar_atendimento_avulso_sistemas ou editar_atendimento_avulso_infraestrutura.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento editado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao editar o atendimento. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="ordens_servico",
                    item_element_name="ordem_servico",
                    root_attributes={
                        "os": str(codigo_os),
                        "dataIni": str(data_inicio),
                        "analista": str(codigo_analista),
                        "descricao": str(descricao_atendimento),
                        "tipo": str(tipo_normalizado),
                        "dataFim": str(data_fim),
                        "primeiroAtendimento": str(primeiro_atendimento),
                        "apresentaSolucao": str(apresenta_solucao),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


async def excluir_atendimentos_os(
    codigo_atendimento: int,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
) -> str:
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosOs/excluiAtendimentosOsSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "atendimento": codigo_atendimento,
                    "analista": codigo_analista,
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Atendimento não encontrado em OS. Tente buscar na função excluir_atendimento_avulso.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento excluído com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao excluir o atendimento. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="exclusões_atendimento_os",
                    item_element_name="exclusão",
                    root_attributes={
                        "atendimento": str(codigo_atendimento),
                        "analista": str(codigo_analista),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


async def inserir_atendimentos_os(
    codigo_os: int,
    data_inicio: str,
    codigo_analista: int,
    descricao_atendimento: str,
    tipo: TipoAtendimentosOSType = "Implementação",
    data_fim: str | None = None,
    primeiro_atendimento: bool = False,
    apresenta_solucao: bool = False,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # Busca o tipo correto na constante TYPE_TO_NUMBER ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TYPE_TO_NUMBER
        (
            key
            for key in TYPE_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo,
                    "mensagem": f"Tipo '{tipo}' não encontrado na constante TYPE_TO_NUMBER",
                    "tipos_validos": list(TYPE_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={"sistema": "SIGA", "funcao": "inserir_atendimentos_os"},
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TYPE_TO_NUMBER[tipo_normalizado]

    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosOs/inserirAtendimentosOsSigaIA/",
                json={
                    "os": codigo_os,
                    "dataIni": data_inicio,
                    "analista": codigo_analista,
                    "descricao": descricao_atendimento,
                    "tipo": tipo_final,
                    "dataFim": data_fim,
                    "primeiroAtendimento": primeiro_atendimento,
                    "apresentaSolucao": apresenta_solucao,
                    "apiKey": getenv("AVA_API_KEY"),
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Não foi possível salvar o atendimento. Verifique as informações digitadas.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento cadastrado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao gravar o atendimento. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="ordens_servico",
                    item_element_name="ordem_servico",
                    root_attributes={
                        "os": str(codigo_os),
                        "dataIni": str(data_inicio),
                        "analista": str(codigo_analista),
                        "descricao": str(descricao_atendimento),
                        "tipo": str(tipo_normalizado),
                        "dataFim": str(data_fim),
                        "primeiroAtendimento": str(primeiro_atendimento),
                        "apresentaSolucao": str(apresenta_solucao),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


async def listar_atendimentos_avulsos(
    *,
    matricula: str | int | Literal["CURRENT_USER"] = "CURRENT_USER",
    data_inicio: str,
    data_fim: str,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio)

    if data_fim:
        data_fim = converter_data_siga(data_fim)

    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosAvulsos/buscarAtendimentosAvulsosSigaIA/",
            json={
                "matricula": matricula,
                "dataIni": data_inicio,
                "dataFim": data_fim,
                "apiKey": getenv("AVA_API_KEY"),
            },
        ) as response:
            try:
                json = await response.json(content_type=None)
                retorno = XMLBuilder().build_xml(
                    data=json["result"],
                    root_element_name="atendimentos_avulsos",
                    item_element_name="atendimentos_avulsos",
                    root_attributes={
                        "matricula": str(matricula),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                return "Erro ao listar atendimentos avulsos."


@controlar_acesso_matricula
async def listar_atendimentos_os(
    matricula: str | int | Literal["CURRENT_USER"] = "CURRENT_USER",
    codigo_os: str | int | None = None,
    data_inicio: str | None = None,
    data_fim: str | None = None,
) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosOs/buscarAtendimentosOsSigaIA/",
            json={
                "matricula": str(matricula),
                "os": str(codigo_os) if codigo_os else "",
                "dataIni": converter_data_siga(data_inicio) if data_inicio else "",
                "dataFim": converter_data_siga(data_fim) if data_fim else "",
                "apiKey": getenv("AVA_API_KEY"),
            },
        ) as response:
            try:
                json = await response.json(content_type=None)
                retorno = XMLBuilder().build_xml(
                    data=json["result"],
                    root_element_name="atendimentos_os",
                    item_element_name="atendimentos_os",
                    root_attributes={
                        "matricula": str(matricula),
                        "os": str(codigo_os) if codigo_os else "",
                        "dataIni": str(data_inicio) if data_inicio else "",
                        "dataFim": str(data_fim) if data_fim else "",
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                return "Erro ao listar atendimentos OS."


@controlar_acesso_matricula
async def listar_horas_trabalhadas(
    *,
    matricula: str | int | Literal["CURRENT_USER"] = "CURRENT_USER",
    data_inicio: str,
    data_fim: str,
) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosAvulsos/buscarTotalHorasTrabalhadasSigaIA/",
            json={
                "matricula": matricula,
                "dataIni": converter_data_siga(data_inicio) if data_inicio else "",
                "dataFim": converter_data_siga(data_fim) if data_fim else "",
                "apiKey": getenv("AVA_API_KEY"),
            },
        ) as response:
            try:
                json = await response.json(content_type=None)
                resultado = json["result"]

                retorno = XMLBuilder().build_xml(
                    data=resultado,
                    root_element_name="atendimentos_avulsos",
                    item_element_name="atendimentos_avulsos",
                    root_attributes={
                        "matricula": str(matricula),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                return "Erro ao listar horas trabalhadas."


@controlar_acesso_matricula
async def inserir_atendimento_avulso_sistemas(
    data_inicio: str,
    data_fim: str,
    matricula_solicitante: str | Literal["CURRENT_USER"],
    descricao_atendimento: str,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
    tipo: TipoAtendimentoAvulsoSistemasType = "Atividade Interna",
    origem: OrigemAtendimentoAvulsoSistemasType = "Teams",
    sistema: SistemasType = "Sistemas AVA",
    equipe: EquipeSistemasType = "Equipe AVA",
    projeto: ProjetoType = "Operação AVA",
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # CRIANDO NORMALIZAÇÃO DAS LITERAIS

    # NORMALIZANDO LITERAL "TIPO"

    # Busca o tipo correto na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TIPO_TO_NUMBER_ATENDIMENTO_AVULSO
        (
            key
            for key in TIPO_TO_NUMBER_ATENDIMENTO_AVULSO.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo,
                    "mensagem": f"Tipo '{tipo}' não encontrado na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO",
                    "tipos_validos": list(TIPO_TO_NUMBER_ATENDIMENTO_AVULSO.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TIPO_TO_NUMBER_ATENDIMENTO_AVULSO[tipo_normalizado]

    # Busca a origem correta na constante ORIGEM_TO_NUMBER ignorando maiúsculas/minúsculas
    origem_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário ORIGEM_TO_NUMBER
        (
            key
            for key in ORIGEM_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a origem recebida em minúsculas
            if str(key).lower() == str(origem).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma origem válida após a busca case-insensitive
    if origem_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "origem_invalida",
                    "origem_informada": origem,
                    "mensagem": f"Origem '{origem}' não encontrada na constante ORIGEM_TO_NUMBER",
                    "origens_validas": list(ORIGEM_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    origem_final = ORIGEM_TO_NUMBER[origem_normalizada]

    # Busca o sistema correto na constante SISTEMA_TO_NUMBER ignorando maiúsculas/minúsculas
    sistema_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário SISTEMA_TO_NUMBER
        (
            key
            for key in SISTEMA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o sistema recebido em minúsculas
            if str(key).lower() == str(sistema).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um sistema válido após a busca case-insensitive
    if sistema_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "sistema_invalido",
                    "sistema_informado": sistema,
                    "mensagem": f"Sistema '{sistema}' não encontrado na constante SISTEMA_TO_NUMBER",
                    "sistemas_validos": list(SISTEMA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    sistema_final = SISTEMA_TO_NUMBER[sistema_normalizado]

    # Busca a equipe correta na constante EQUIPE_TO_NUMBER ignorando maiúsculas/minúsculas
    equipe_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário EQUIPE_TO_NUMBER
        (
            key
            for key in EQUIPE_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a equipe recebida em minúsculas
            if str(key).lower() == str(equipe).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma equipe válida após a busca case-insensitive
    if equipe_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "equipe_invalida",
                    "equipe_informada": equipe,
                    "mensagem": f"Equipe '{equipe}' não encontrada na constante EQUIPE_TO_NUMBER",
                    "equipes_validas": list(EQUIPE_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    equipe_final = EQUIPE_TO_NUMBER[equipe_normalizada]

    # Busca o projeto correto na constante PROJETO_TO_NUMBER ignorando maiúsculas/minúsculas
    projeto_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário PROJETO_TO_NUMBER
        (
            key
            for key in PROJETO_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o projeto recebido em minúsculas
            if str(key).lower() == str(projeto).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um projeto válido após a busca case-insensitive
    if projeto_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "projeto_invalido",
                    "projeto_informado": projeto,
                    "mensagem": f"Projeto '{projeto}' não encontrado na constante PROJETO_TO_NUMBER",
                    "projetos_validos": list(PROJETO_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    projeto_final = PROJETO_TO_NUMBER[projeto_normalizado]

    # FUNÇÃO PARA GRAVAR INFORMAÇÕES
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosAvulsos/inserirAtendimentoAvulsoSigaIA/",
                # "https://9f7a79af77d0.ngrok-free.app/ava/api/atendimentosAvulsos/inserirAtendimentoAvulsoSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "dataIni": data_inicio,
                    "dataFim": data_fim,
                    "matSolicitante": matricula_solicitante,
                    "tipo": tipo_final,
                    "descricao": descricao_atendimento,
                    "origem": origem_final,
                    "area": 1,
                    "equipe": equipe_final,
                    "analista": codigo_analista,
                    "projeto": projeto_final,
                    "sistema": sistema_final,
                    "nomeSolicitante": "",
                    "centroCusto": "",
                    "setor": "",
                    "matGestor": "",
                    "tempoGasto": "",
                    "campus": "",
                    "categoria": "",
                    "plaqueta": "",
                    "ramal": "",
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Não foi possível salvar o atendimento avulso. Verifique as informações digitadas.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento avulso cadastrado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao gravar o atendimento avulso. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="atendimentos_avulsos",
                    item_element_name="atendimento_avulso",
                    root_attributes={
                        "dataIni": str(data_inicio),
                        "dataFim": str(data_fim),
                        "matSolicitante": str(matricula_solicitante),
                        "tipo": str(tipo_final),
                        "descricao": str(descricao_atendimento),
                        "origem": str(origem_final),
                        "equipe": str(equipe_final),
                        "analista": str(codigo_analista),
                        "projeto": str(projeto_final),
                        "sistema": str(sistema_final),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


async def buscar_informacoes_atendimento_avulso(
    codigo_atendimento: int,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
) -> str:
    async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
        async with session.post(
            "https://ava3.uniube.br/ava/api/atendimentosAvulsos/buscarInfoAtendimentoAvulsoSigaIA/",
            json={
                "apiKey": getenv("AVA_API_KEY"),
                "atendimento": codigo_atendimento,
                "analista": codigo_analista,
            },
        ) as response:
            try:
                json = await response.json(content_type=None)
                retorno = XMLBuilder().build_xml(
                    data=json["result"],
                    root_element_name="info_atendimentos_avulsos",
                    item_element_name="info_atendimento_avulso",
                    root_attributes={
                        "atendimento": str(codigo_atendimento),
                        "analista": str(codigo_analista),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

                return retorno

            except Exception:
                return "Erro ao buscar as informações do atendimento avulso."


@controlar_acesso_matricula
async def editar_atendimento_avulso_sistemas(
    codigo_atendimento: int,
    data_inicio: str,
    data_fim: str,
    matricula_solicitante: str | Literal["CURRENT_USER"],
    descricao_atendimento: str,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
    tipo: TipoAtendimentoAvulsoSistemasType = "Atividade Interna",
    origem: OrigemAtendimentoAvulsoSistemasType = "Teams",
    sistema: SistemasType = "Sistemas AVA",
    equipe: EquipeSistemasType = "Equipe AVA",
    projeto: ProjetoType = "Operação AVA",
    area: int = 1,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # VALIDAÇÃO DA ÁREA (SISTEMAS DEVE SER 1)
    if area != 1:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "area_invalida",
                    "area_informada": area,
                    "mensagem": f"Não é possível alterar a área para {area}. Esta função é específica para área Sistemas (1). Para alterar para Infraestrutura, exclua este atendimento e crie um novo na função editar_atendimento_avulso_infraestrutura. Sugestão: peça à IA para replicar este lançamento e solicite a exclusão do atendimento incorreto.",
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    # CRIANDO NORMALIZAÇÃO DAS LITERAIS

    # NORMALIZANDO LITERAL "TIPO"

    # Busca o tipo correto na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TIPO_TO_NUMBER_ATENDIMENTO_AVULSO
        (
            key
            for key in TIPO_TO_NUMBER_ATENDIMENTO_AVULSO.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo,
                    "mensagem": f"Tipo '{tipo}' não encontrado na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO",
                    "tipos_validos": list(TIPO_TO_NUMBER_ATENDIMENTO_AVULSO.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TIPO_TO_NUMBER_ATENDIMENTO_AVULSO[tipo_normalizado]

    # Busca a origem correta na constante ORIGEM_TO_NUMBER ignorando maiúsculas/minúsculas
    origem_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário ORIGEM_TO_NUMBER
        (
            key
            for key in ORIGEM_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a origem recebida em minúsculas
            if str(key).lower() == str(origem).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma origem válida após a busca case-insensitive
    if origem_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "origem_invalida",
                    "origem_informada": origem,
                    "mensagem": f"Origem '{origem}' não encontrada na constante ORIGEM_TO_NUMBER",
                    "origens_validas": list(ORIGEM_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    origem_final = ORIGEM_TO_NUMBER[origem_normalizada]

    # Busca o sistema correto na constante SISTEMA_TO_NUMBER ignorando maiúsculas/minúsculas
    sistema_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário SISTEMA_TO_NUMBER
        (
            key
            for key in SISTEMA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o sistema recebido em minúsculas
            if str(key).lower() == str(sistema).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um sistema válido após a busca case-insensitive
    if sistema_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "sistema_invalido",
                    "sistema_informado": sistema,
                    "mensagem": f"Sistema '{sistema}' não encontrado na constante SISTEMA_TO_NUMBER",
                    "sistemas_validos": list(SISTEMA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    sistema_final = SISTEMA_TO_NUMBER[sistema_normalizado]

    # Busca a equipe correta na constante EQUIPE_TO_NUMBER ignorando maiúsculas/minúsculas
    equipe_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário EQUIPE_TO_NUMBER
        (
            key
            for key in EQUIPE_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a equipe recebida em minúsculas
            if str(key).lower() == str(equipe).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma equipe válida após a busca case-insensitive
    if equipe_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "equipe_invalida",
                    "equipe_informada": equipe,
                    "mensagem": f"Equipe '{equipe}' não encontrada na constante EQUIPE_TO_NUMBER",
                    "equipes_validas": list(EQUIPE_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    equipe_final = EQUIPE_TO_NUMBER[equipe_normalizada]

    # Busca o projeto correto na constante PROJETO_TO_NUMBER ignorando maiúsculas/minúsculas
    projeto_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário PROJETO_TO_NUMBER
        (
            key
            for key in PROJETO_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o projeto recebido em minúsculas
            if str(key).lower() == str(projeto).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um projeto válido após a busca case-insensitive
    if projeto_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "projeto_invalido",
                    "projeto_informado": projeto,
                    "mensagem": f"Projeto '{projeto}' não encontrado na constante PROJETO_TO_NUMBER",
                    "projetos_validos": list(PROJETO_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_sistemas",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    projeto_final = PROJETO_TO_NUMBER[projeto_normalizado]

    # FUNÇÃO PARA GRAVAR INFORMAÇÕES
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosAvulsos/atualizarAtendimentoAvulsoSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "atendimento": codigo_atendimento,
                    "dataIni": data_inicio,
                    "dataFim": data_fim,
                    "matSolicitante": matricula_solicitante,
                    "tipo": tipo_final,
                    "descricao": descricao_atendimento,
                    "origem": origem_final,
                    "area": area,
                    "equipe": equipe_final,
                    "analista": codigo_analista,
                    "projeto": projeto_final,
                    "sistema": sistema_final,
                    "nomeSolicitante": "",
                    "centroCusto": "",
                    "setor": "",
                    "matGestor": "",
                    "tempoGasto": "",
                    "campus": "",
                    "categoria": "",
                    "plaqueta": "",
                    "ramal": "",
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Atendimento não encontrado em Avulso Sistemas. Tente buscar nas funções editar_atendimentos_os ou editar_atendimento_avulso_infraestrutura.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento avulso editado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao gravar o atendimento avulso. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="atendimentos_avulsos",
                    item_element_name="atendimento_avulso",
                    root_attributes={
                        "codigo_atendimento": str(codigo_atendimento),
                        "dataIni": str(data_inicio),
                        "dataFim": str(data_fim),
                        "matSolicitante": str(matricula_solicitante),
                        "tipo": str(tipo_final),
                        "descricao": str(descricao_atendimento),
                        "origem": str(origem_final),
                        "equipe": str(equipe_final),
                        "analista": str(codigo_analista),
                        "projeto": str(projeto_final),
                        "sistema": str(sistema_final),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


async def excluir_atendimento_avulso(
    codigo_atendimento: int,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
) -> str:
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosAvulsos/excluiAtendimentoAvulsoSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "atendimento": codigo_atendimento,
                    "analista": codigo_analista,
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Atendimento não encontrado em Avulso. Tente buscar na função excluir_atendimentos_os.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento avulso excluído com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao excluir o atendimento avulso. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="exclusões_atendimento_avulso",
                    item_element_name="exclusão",
                    root_attributes={
                        "atendimento": str(codigo_atendimento),
                        "analista": str(codigo_analista),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


@controlar_acesso_matricula
async def inserir_atendimento_avulso_infraestrutura(
    data_inicio: str,
    data_fim: str,
    matricula_solicitante: str | Literal["CURRENT_USER"],
    descricao_atendimento: str,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
    tipo: TipoAtendimentoAvulsoInfraestruturaType = "Suporte",
    origem: OrigemAtendimentoAvulsoSistemasType = "E-mail",
    categoria: CategoriasInfraestruturaType = "Suporte/Dúvidas/Outros",
    equipe: EquipeInfraestruturaType = "Help-Desk - Aeroporto",
    projeto: ProjetoType = "Operação Help Desk",
    plaqueta: str | None = None,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # CRIANDO NORMALIZAÇÃO DAS LITERAIS

    # NORMALIZANDO LITERAL "TIPO"

    # Busca o tipo correto na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA
        (
            key
            for key in TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo,
                    "mensagem": f"Tipo '{tipo}' não encontrado na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA",
                    "tipos_validos": list(
                        TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA.keys()
                    ),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA[tipo_normalizado]

    # Busca a origem correta na constante ORIGEM_TO_NUMBER ignorando maiúsculas/minúsculas
    origem_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário ORIGEM_TO_NUMBER
        (
            key
            for key in ORIGEM_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a origem recebida em minúsculas
            if str(key).lower() == str(origem).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma origem válida após a busca case-insensitive
    if origem_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "origem_invalida",
                    "origem_informada": origem,
                    "mensagem": f"Origem '{origem}' não encontrada na constante ORIGEM_TO_NUMBER",
                    "origens_validas": list(ORIGEM_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    origem_final = ORIGEM_TO_NUMBER[origem_normalizada]

    # Busca a categoria correta na constante CATEGORIA_TO_NUMBER ignorando maiúsculas/minúsculas
    categoria_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário CATEGORIA_TO_NUMBER
        (
            key
            for key in CATEGORIA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a categoria recebida em minúsculas
            if str(key).lower() == str(categoria).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado uma categoria válida após a busca case-insensitive
    if categoria_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "categoria_invalida",
                    "categoria_informada": categoria,
                    "mensagem": f"Categoria '{categoria}' não encontrada na constante CATEGORIA_TO_NUMBER",
                    "sistemas_validos": list(CATEGORIA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    categoria_final = CATEGORIA_TO_NUMBER[categoria_normalizada]

    # Busca a equipe correta na constante EQUIPE_INFRAESTRUTURA_TO_NUMBER ignorando maiúsculas/minúsculas
    equipe_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário EQUIPE_INFRAESTRUTURA_TO_NUMBER
        (
            key
            for key in EQUIPE_INFRAESTRUTURA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a equipe recebida em minúsculas
            if str(key).lower() == str(equipe).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma equipe válida após a busca case-insensitive
    if equipe_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "equipe_invalida",
                    "equipe_informada": equipe,
                    "mensagem": f"Equipe '{equipe}' não encontrada na constante EQUIPE_INFRAESTRUTURA_TO_NUMBER",
                    "equipes_validas": list(EQUIPE_INFRAESTRUTURA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    equipe_final = EQUIPE_INFRAESTRUTURA_TO_NUMBER[equipe_normalizada]

    # Busca o projeto correto na constante PROJETO_TO_NUMBER ignorando maiúsculas/minúsculas
    projeto_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário PROJETO_TO_NUMBER
        (
            key
            for key in PROJETO_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o projeto recebido em minúsculas
            if str(key).lower() == str(projeto).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um projeto válido após a busca case-insensitive
    if projeto_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "projeto_invalido",
                    "projeto_informado": projeto,
                    "mensagem": f"Projeto '{projeto}' não encontrado na constante PROJETO_TO_NUMBER",
                    "projetos_validos": list(PROJETO_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "inserir_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    projeto_final = PROJETO_TO_NUMBER[projeto_normalizado]

    # FUNÇÃO PARA GRAVAR INFORMAÇÕES
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosAvulsos/inserirAtendimentoAvulsoSigaIA/",
                # "https://9f7a79af77d0.ngrok-free.app/ava/api/atendimentosAvulsos/inserirAtendimentoAvulsoSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "dataIni": data_inicio,
                    "dataFim": data_fim,
                    "matSolicitante": matricula_solicitante,
                    "tipo": tipo_final,
                    "descricao": descricao_atendimento,
                    "origem": origem_final,
                    "area": 2,
                    "equipe": equipe_final,
                    "analista": codigo_analista,
                    "projeto": projeto_final,
                    "sistema": "",
                    "nomeSolicitante": "",
                    "centroCusto": "",
                    "setor": "",
                    "matGestor": "",
                    "tempoGasto": "",
                    "campus": "",
                    "categoria": categoria_final,
                    "plaqueta": plaqueta if plaqueta else "",
                    "ramal": "",
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Não foi possível salvar o atendimento avulso. Verifique as informações digitadas.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento avulso cadastrado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao gravar o atendimento avulso. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="atendimentos_avulsos_infra",
                    item_element_name="atendimento_avulso_infra",
                    root_attributes={
                        "dataIni": str(data_inicio),
                        "dataFim": str(data_fim),
                        "matSolicitante": str(matricula_solicitante),
                        "tipo": str(tipo_final),
                        "descricao": str(descricao_atendimento),
                        "origem": str(origem_final),
                        "equipe": str(equipe_final),
                        "analista": str(codigo_analista),
                        "projeto": str(projeto_final),
                        "categoria": str(categoria_final),
                        "plaqueta": str(plaqueta if plaqueta else ""),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


# VERIFICAR ESSE CÓDIGO


@controlar_acesso_matricula
async def editar_atendimento_avulso_infraestrutura(
    codigo_atendimento: int,
    data_inicio: str,
    data_fim: str,
    matricula_solicitante: str | Literal["CURRENT_USER"],
    descricao_atendimento: str,
    codigo_analista: str | Literal["CURRENT_USER"] = "CURRENT_USER",
    tipo: TipoAtendimentoAvulsoInfraestruturaType = "Suporte",
    origem: OrigemAtendimentoAvulsoSistemasType = "E-mail",
    categoria: CategoriasInfraestruturaType = "Suporte/Dúvidas/Outros",
    equipe: EquipeInfraestruturaType = "Help-Desk - Aeroporto",
    projeto: ProjetoType = "Operação Help Desk",
    plaqueta: str | None = None,
    area: int = 2,
) -> str:
    if data_inicio:
        data_inicio = converter_data_siga(data_inicio, manter_horas=True)

    if data_fim:
        data_fim = converter_data_siga(data_fim, manter_horas=True)

    # VALIDAÇÃO DA ÁREA (INFRAESTRUTURA DEVE SER 2)
    if area != 2:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "area_invalida",
                    "area_informada": area,
                    "mensagem": f"Não é possível alterar a área para {area}. Esta função é específica para área Infraestrutura (2). Para alterar para Sistemas, exclua este atendimento e crie um novo na função editar_atendimento_avulso_sistemas. Sugestão: peça à IA para replicar este lançamento e solicite a exclusão do atendimento incorreto.",
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    # CRIANDO NORMALIZAÇÃO DAS LITERAIS

    # NORMALIZANDO LITERAL "TIPO"

    # Busca o tipo correto na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA ignorando maiúsculas/minúsculas
    tipo_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA
        (
            key
            for key in TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA.keys()
            # Compara a chave atual em minúsculas com o tipo recebido em minúsculas
            if str(key).lower() == str(tipo).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um tipo válido após a busca case-insensitive
    if tipo_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "tipo_invalido",
                    "tipo_informado": tipo,
                    "mensagem": f"Tipo '{tipo}' não encontrado na constante TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA",
                    "tipos_validos": list(
                        TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA.keys()
                    ),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    tipo_final = TIPO_TO_NUMBER_ATENDIMENTO_AVULSO_INFRAESTRUTURA[tipo_normalizado]

    # Busca a origem correta na constante ORIGEM_TO_NUMBER ignorando maiúsculas/minúsculas
    origem_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário ORIGEM_TO_NUMBER
        (
            key
            for key in ORIGEM_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a origem recebida em minúsculas
            if str(key).lower() == str(origem).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma origem válida após a busca case-insensitive
    if origem_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "origem_invalida",
                    "origem_informada": origem,
                    "mensagem": f"Origem '{origem}' não encontrada na constante ORIGEM_TO_NUMBER",
                    "origens_validas": list(ORIGEM_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    origem_final = ORIGEM_TO_NUMBER[origem_normalizada]

    # Busca a categoria correta na constante CATEGORIA_TO_NUMBER ignorando maiúsculas/minúsculas
    categoria_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário CATEGORIA_TO_NUMBER
        (
            key
            for key in CATEGORIA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a categoria recebida em minúsculas
            if str(key).lower() == str(categoria).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado uma categoria válida após a busca case-insensitive
    if categoria_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "categoria_invalida",
                    "categoria_informada": categoria,
                    "mensagem": f"Categoria '{categoria}' não encontrada na constante CATEGORIA_TO_NUMBER",
                    "categorias_validas": list(CATEGORIA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    categoria_final = CATEGORIA_TO_NUMBER[categoria_normalizada]

    # Busca a equipe correta na constante EQUIPE_INFRAESTRUTURA_TO_NUMBER ignorando maiúsculas/minúsculas
    equipe_normalizada = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário EQUIPE_INFRAESTRUTURA_TO_NUMBER
        (
            key
            for key in EQUIPE_INFRAESTRUTURA_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com a equipe recebida em minúsculas
            if str(key).lower() == str(equipe).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrada uma equipe válida após a busca case-insensitive
    if equipe_normalizada is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "equipe_invalida",
                    "equipe_informada": equipe,
                    "mensagem": f"Equipe '{equipe}' não encontrada na constante EQUIPE_INFRAESTRUTURA_TO_NUMBER",
                    "equipes_validas": list(EQUIPE_INFRAESTRUTURA_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    equipe_final = EQUIPE_INFRAESTRUTURA_TO_NUMBER[equipe_normalizada]

    # Busca o projeto correto na constante PROJETO_TO_NUMBER ignorando maiúsculas/minúsculas
    projeto_normalizado = next(
        # Expressão geradora que itera sobre todas as chaves do dicionário PROJETO_TO_NUMBER
        (
            key
            for key in PROJETO_TO_NUMBER.keys()
            # Compara a chave atual em minúsculas com o projeto recebido em minúsculas
            if str(key).lower() == str(projeto).lower()
        ),
        # Se nenhuma correspondência for encontrada, retorna None como valor padrão
        None,
    )

    # Verifica se foi encontrado um projeto válido após a busca case-insensitive
    if projeto_normalizado is None:
        # Retorna XML de erro em vez de levantar exceção
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "tipo_erro": "projeto_invalido",
                    "projeto_informado": projeto,
                    "mensagem": f"Projeto '{projeto}' não encontrado na constante PROJETO_TO_NUMBER",
                    "projetos_validos": list(PROJETO_TO_NUMBER.keys()),
                }
            ],
            root_element_name="erro_validacao",
            item_element_name="erro",
            root_attributes={
                "sistema": "SIGA",
                "funcao": "editar_atendimento_avulso_infraestrutura",
            },
            custom_attributes={"sistema": "SIGA"},
        )

    projeto_final = PROJETO_TO_NUMBER[projeto_normalizado]

    # FUNÇÃO PARA GRAVAR INFORMAÇÕES
    try:
        async with aiohttp.ClientSession(json_serialize=ujson.dumps) as session:
            async with session.post(
                "https://ava3.uniube.br/ava/api/atendimentosAvulsos/atualizarAtendimentoAvulsoSigaIA/",
                json={
                    "apiKey": getenv("AVA_API_KEY"),
                    "atendimento": codigo_atendimento,
                    "dataIni": data_inicio,
                    "dataFim": data_fim,
                    "matSolicitante": matricula_solicitante,
                    "tipo": tipo_final,
                    "descricao": descricao_atendimento,
                    "origem": origem_final,
                    "area": area,
                    "equipe": equipe_final,
                    "analista": codigo_analista,
                    "projeto": projeto_final,
                    "sistema": "",
                    "nomeSolicitante": "",
                    "centroCusto": "",
                    "setor": "",
                    "matGestor": "",
                    "tempoGasto": "",
                    "campus": "",
                    "categoria": categoria_final,
                    "plaqueta": plaqueta if plaqueta else "",
                    "ramal": "",
                },
            ) as response:
                json_response = await response.json(content_type=None)
                result_data = json_response.get("result")

                # Trata a resposta
                if result_data is None:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Atendimento não encontrado em Avulso Infraestrutura. Tente buscar nas funções editar_atendimentos_os ou editar_atendimento_avulso_sistemas.",
                        }
                    ]
                elif result_data == 1:
                    data_final = [
                        {
                            "status": "sucesso",
                            "mensagem": "Atendimento avulso editado com sucesso!",
                        }
                    ]
                else:
                    data_final = [
                        {
                            "status": "erro",
                            "mensagem": "Erro ao gravar o atendimento avulso. Tente novamente.",
                        }
                    ]

                # Adiciona os root_attributes
                return XMLBuilder().build_xml(
                    data=data_final,
                    root_element_name="atendimentos_avulsos_infra",
                    item_element_name="atendimento_avulso_infra",
                    root_attributes={
                        "codigo_atendimento": str(codigo_atendimento),
                        "dataIni": str(data_inicio),
                        "dataFim": str(data_fim),
                        "matSolicitante": str(matricula_solicitante),
                        "tipo": str(tipo_final),
                        "descricao": str(descricao_atendimento),
                        "origem": str(origem_final),
                        "equipe": str(equipe_final),
                        "analista": str(codigo_analista),
                        "projeto": str(projeto_final),
                        "categoria": str(categoria_final),
                        "plaqueta": str(plaqueta if plaqueta else ""),
                    },
                    custom_attributes={"sistema": "SIGA"},
                )

    except Exception as e:
        return XMLBuilder().build_xml(
            data=[
                {
                    "status": "erro",
                    "mensagem": f"Erro interno: {str(e)}. Tente novamente mais tarde.",
                }
            ],
            root_element_name="resultado",
            item_element_name="item",
            custom_attributes={"sistema": "SIGA"},
        )


# @controlar_acesso_matricula
# async def cadastrar_todos_dias_pendentes(
#     colaborador: str | Literal["CURRENT_USER"] = "CURRENT_USER",
#     codigo_os: str | None = None,
#     descricao: str = "debugando codigo",
#     cadastrar_como_atendimento_avulso: bool = True,
# ) -> str:
#     if codigo_os is not None and cadastrar_como_atendimento_avulso:
#         raise ValueError(
#             "Os parâmetros 'codigo_os' e 'cadastrar_como_atendimento_avulso' são mutuamente exclusivos. "
#             "Informe apenas um deles."
#         )

#     pendencias = await buscar_pendencias_lancamentos_atendimentos()

#     raise NotImplementedError("Função ainda não implementada.")


async def atualizar_horarios_colaborador(
    entrada_1: str | None = None,
    saida_1: str | None = None,
    entrada_2: str | None = None,
    saida_2: str | None = None,
) -> str:
    _entrada_1 = memory.periodo.periodos[0].entrada
    if entrada_1:
        _entrada_1 = HoraMinuto.from_string(entrada_1)

    _saida_1 = memory.periodo.periodos[0].saida
    if saida_1:
        _saida_1 = HoraMinuto.from_string(saida_1)

    _entrada_2 = memory.periodo.periodos[1].entrada
    if entrada_2:
        _entrada_2 = HoraMinuto.from_string(entrada_2)

    _saida_2 = memory.periodo.periodos[1].saida
    if saida_2:
        _saida_2 = HoraMinuto.from_string(saida_2)

    primeiro_periodo = MeioPeriodo(
        entrada=_entrada_1 if entrada_1 else memory.periodo.periodos[0].entrada,
        saida=_saida_1 if saida_1 else memory.periodo.periodos[0].saida,
    )

    segundo_periodo = MeioPeriodo(
        entrada=_entrada_2 if entrada_2 else memory.periodo.periodos[1].entrada,
        saida=_saida_2 if saida_2 else memory.periodo.periodos[1].saida,
    )

    memory.periodo.alterar_periodos(novos_periodos=[primeiro_periodo, segundo_periodo])

    return "Horários atualizados com sucesso."


async def __version__() -> str:
    return get_package_version()
