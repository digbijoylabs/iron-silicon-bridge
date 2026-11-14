def analyze_db2_timings(smf_record):
    class1_el = smf_record['QWACESC']
    class2_el = smf_record['QWACAJCE']
    class3_wt = smf_record['QWACAWTI']
    
    network_wait = class1_el - class2_el
    
    # If wait time inside Db2 exceeds 50% of processing time
    if class3_wt > class2_el * 0.5:
        return "CRITICAL: Severe Db2 Engine Suspension"
    # If application/network delay accounts for 80% of total time
    elif network_wait > class1_el * 0.8:
        return "WARNING: High Client or Network Latency"
    
    return "HEALTHY"
