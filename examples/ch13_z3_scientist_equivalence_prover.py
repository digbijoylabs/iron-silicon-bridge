# Reference Blueprint: Scientist Pattern Parity Kernel
def run_semantic_experiment(
    experiment_name: str, legacy_func, new_func, *args
):
    legacy_result = legacy_func(*args)  #
    ign_keys = ['timestamp', 'uuid']
    try:
        new_result = new_func(*args)
        if not semantic_compare(
            legacy_result, new_result, ignore_keys=ign_keys
        ):  #
            publish_telemetry(
                "semantic_mismatch",
                exp=experiment_name, args=args
            )
    except Exception as exc:
        publish_telemetry(
            "logic_exception",
            exp=experiment_name, err=str(exc)
        )  #
    return legacy_result  #
