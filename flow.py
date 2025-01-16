from prefect import flow, get_run_logger

@flow(log_prints=True)
def simple_test_flow():
    logger = get_run_logger()
    logger.info("This is a simple test flow.")
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    return "Test flow executed successfully."

if __name__ == "__main__":
    flow.from_source(
        source="s3://test-mex-storage",
        entrypoint="flow.py:simple_test_flow",
    ).deploy(
        name="test-managed-flow",
        work_pool_name="test-mex-pool",
    )
