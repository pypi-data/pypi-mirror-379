from typing import Optional
from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph
from langgraph.typing import StateT, ContextT, InputT, OutputT
from langchain_dev_utils.graph_pipeline.types import SubGraph


def sequential_pipeline(
    sub_graphs: list[SubGraph],
    state_schema: type[StateT],
    graph_name: Optional[str] = None,
    context_schema: type[ContextT] | None = None,
    input_schema: type[InputT] | None = None,
    output_schema: type[OutputT] | None = None,
) -> CompiledStateGraph[StateT, ContextT, InputT, OutputT]:
    """
    Create a sequential pipeline from a list of subgraphs.

    Args:
        sub_graphs (list[SubGraph]): List of subgraphs to be executed sequentially.
        state_schema (type[StateT]): State schema for the pipeline.
        graph_name (Optional[str], optional): Name for the pipeline. Defaults to None.
        context_schema (type[ContextT] | None, optional): Context schema for the pipeline. Defaults to None.
        input_schema (type[InputT] | None, optional): Input schema for the pipeline. Defaults to None.
        output_schema (type[OutputT] | None, optional): Output schema for the pipeline. Defaults to None.

    Returns:
        CompiledStateGraph[StateT, ContextT, InputT, OutputT]: Compiled state graph of the pipeline.
    """
    graph = StateGraph(
        state_schema=state_schema,
        context_schema=context_schema,
        input_schema=input_schema,
        output_schema=output_schema,
    )

    subgraphs_names = set()

    compiled_subgraphs: list[CompiledStateGraph] = []
    for subgraph in sub_graphs:
        if isinstance(subgraph, StateGraph):
            subgraph = subgraph.compile()

        compiled_subgraphs.append(subgraph)
        if subgraph.name is None or subgraph.name == "LangGraph":
            raise ValueError(
                "Please specify a name when you create your agent, either via `create_react_agent(..., name=agent_name)` "
                "or via `graph.compile(name=name)`."
            )

        if subgraph.name in subgraphs_names:
            raise ValueError(
                f"Subgraph with name '{subgraph.name}' already exists. Subgraph names must be unique."
            )

        subgraphs_names.add(subgraph.name)

    for sub_graph in compiled_subgraphs:
        graph.add_node(sub_graph.name, sub_graph)

    for i in range(len(compiled_subgraphs) - 1):
        graph.add_edge(compiled_subgraphs[i].name, compiled_subgraphs[i + 1].name)
    graph.add_edge("__start__", compiled_subgraphs[0].name)
    return graph.compile(name=graph_name or "sequential graph")
