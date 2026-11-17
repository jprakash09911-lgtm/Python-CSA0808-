import time
import cProfile
import logging

logging.basicConfig(level=logging.INFO)

def cleaning():
    data = [48, 95, -5, 121, 60]

    clean = []

    for x in data:
        assert isinstance(x, (int, float))

        if 0 <= x <= 999:
            clean.append(x)

    logging.info("Cleaning completed")
    return clean

start = time.perf_counter()

print(cleaning())

end = time.perf_counter()

print("Execution time:", end - start)

cProfile.run("cleaning()")