import random

from netqasm.logging.glob import get_netqasm_logger
from netqasm.runtime.application import default_app_instance
from netqasm.sdk import Qubit
from netqasm.sdk.external import NetQASMConnection, simulate_application

logger = get_netqasm_logger()


def run_alice():
    with NetQASMConnection("Alice") as alice:
        num = 10

        outcomes = alice.new_array(num)
        rand_nums = alice.new_array(
            num, init_values=[random.randint(0, 1) for _ in range(num)]
        )

        with rand_nums.enumerate() as (i, r):
            q = Qubit(alice)
            with r.if_eq(1):
                q.X()
            q.measure(future=outcomes.get_future_index(i))

        alice.flush()
        assert len(outcomes) == num
        print(f"rand_nums = {list(rand_nums)}")
        print(f"outcomes = {list(outcomes)}")
        assert list(rand_nums) == list(outcomes)


def test_enumerate():
    app_instance = default_app_instance(
        [
            ("Alice", run_alice),
        ]
    )
    simulate_application(app_instance, use_app_config=False, enable_logging=False)


if __name__ == "__main__":
    test_enumerate()
