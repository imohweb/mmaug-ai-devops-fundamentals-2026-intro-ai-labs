"""Lab 05: simulate an agent choosing tools without calling any external service."""

from dataclasses import dataclass


@dataclass
class ToolResult:
    tool_name: str
    result: str


def search_policy(query: str) -> ToolResult:
    return ToolResult(
        "search_policy",
        "KB003: Abnormal equipment readings require qualified technician review.",
    )


def create_draft_response(asset_id: str, message: str) -> ToolResult:
    return ToolResult("create_draft_response", f"Draft created for {asset_id}: {message}")


def simple_agent(user_request: str) -> str:
    print("User request:", user_request)
    print("\nPLAN")
    print("1) Search approved policy")
    print("2) Create a draft response")
    print("3) Stop for human approval before anything is sent")

    policy = search_policy("abnormal equipment readings maintenance")
    print("\nTOOL CALL 1:", policy.tool_name)
    print("RESULT:", policy.result)

    draft = create_draft_response(
        "EQ-001",
        "Please arrange inspection by a qualified technician before continued operation.",
    )
    print("\nTOOL CALL 2:", draft.tool_name)
    print("RESULT:", draft.result)

    return "Final state: draft created only; qualified human approval is required before sending."


def main() -> None:
    print("=== LAB 05: TOOLS AND AGENTS ===")
    final = simple_agent("Handle EQ-001. The motor has rising vibration and a metallic sound.")
    print("\n", final)
    print("\nSECURITY IDEA: Once an AI system can act, permissions and approval boundaries matter as much as prompt quality.")


if __name__ == "__main__":
    main()
