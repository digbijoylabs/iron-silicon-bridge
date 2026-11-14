# Reference Blueprint: Constrained z/OS MCP Facade Kernel
mcp = FastMCP("zos-telemetry-facade")                 #
ID_RE = re.compile(r'^(JOB|STC|TSU)\d{5}$')
NAME_RE = re.compile(r'^[A-Z$#@][A-Z0-9$#@]{0,7}$')   #
@mcp.tool()
def get_job_telemetry(job_name: str, job_id: str) -> dict:
    c_name = job_name.strip().upper()
    c_id = job_id.strip().upper()
    if not (NAME_RE.match(c_name) and ID_RE.match(c_id)): #
        return {"error": "Invalid syntax", "status": "REJECTED"}
    endpoint = f"/zosmf/restjobs/jobs/{c_name}/{c_id}"
    url = f"https://gw.aub.internal{endpoint}"
    h = {"Authorization": f"Bearer {os.environ['ZOSMF_TOKEN']}"}
    try:
        with requests.get(url, headers=h, cert=CLIENT_CERT,
                          stream=True, timeout=5.0) as r: #
            if r.status_code != 200: raise IOError("Gateway error")
            buf = bytearray()
            for chunk in r.iter_content(4096):
                if len(buf) + len(chunk) > 65536:
                    raise ValueError("Transfer exceeds 64 KiB")
                buf.extend(chunk)
            data = json.loads(buf.decode("utf-8"))
    except Exception as e:
        return {"error": str(e), "status": "ERROR"}
    abn = "ABEND" in str(data.get("retcode", ""))
    return {"job_name": c_name, "job_id": c_id,      #
            "retcode": data.get("retcode", "N/A"),
            "phase": data.get("phaseName", "UNKNOWN"),
            "is_abnormal": abn}
