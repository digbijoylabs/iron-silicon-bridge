def handle_message_bus_event(event: AgentMessage):
    if event.requires_legacy_execution():
        # 1. Natural language intent intercepted from bus
        reasoning = event.natural_language_context    #
        # 2. Translated to rigid RPC schema via MCP Client
        cust_id = extract_exact_id(reasoning)         #
        req = mcp_client.format_rpc_request(          #
            target_subsystem="DB2_PROD_01",
            procedure="SP_GET_CUST_V1",
            parameters={"CUST_ID": cust_id}
        )

        # 3. Deterministic execution against mainframe middleware
        resp = execute_mainframe_rpc(req)             #
        return resp                                   #