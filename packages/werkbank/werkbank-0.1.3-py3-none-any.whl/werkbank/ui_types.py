import dataclasses
import typing as t

@dataclasses.dataclass(frozen=True)
class Port:
    id: str
    type: str  # "source" | "target"
    category: str  # "dep" | "param" | "out"
    name: str
    annotation: str

@dataclasses.dataclass(frozen=True)
class XYNodeData:
    label: str
    docs: str
    deprecated: bool
    path: str
    ports: list[Port]

@dataclasses.dataclass(frozen=True)
class XYGroupData:
    label: str

class XYNode(t.TypedDict):
    id: str
    data: XYNodeData | XYGroupData
    parentId: str | None
    type: t.Literal["Node", "Group"]

@dataclasses.dataclass(frozen=True)
class XYEdge:
    id: str
    source: str
    sourceHandle: str
    target: str
    targetHandle: str
