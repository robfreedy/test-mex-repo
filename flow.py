from prefect import flow, get_run_logger

@flow(log_prints=True)
def simple_test_flow():
    logger = get_run_logger()
    logger.info("This is a simple test flow.")
    from requests import get

    ip = get('https://api.ipify.org').content.decode('utf8')
    print('My public IP address is: {}'.format(ip))

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/robfreedy/test-mex-repo.git",
        entrypoint="flow.py:simple_test_flow",
    ).deploy(
        name="test-managed-flow",
        work_pool_name="test-mex-pool",
    )
