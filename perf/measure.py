import timeit
import statistics
from pathlib import Path


REPEAT = 20000
REPEAT_FULL = 100

nano = 0.000_000_001

perf_dir = Path(__file__).parent

for perf_file in perf_dir.glob("perf_*.py"):
    with open(perf_file) as file:
        data = file.read()
    if "#?" not in data:
        raise RuntimeError(
            "Magic '#?' not found in %s." \
            "'#?' used to divide setup and measure." \
            % perf_file
        )
    setup, measure = data.split("#?")
    result = timeit.repeat(
        measure,
        setup=setup,
        number=REPEAT,
        repeat=max(100, REPEAT_FULL)
    )
    quantiles = statistics.quantiles(result, n=10)
    quantiles = [round(q / max(result), 1) * 10 for q in quantiles]
    graph = [
        f"  {n*10}% " + ("-" * int(q))
        for n, q in enumerate(quantiles, start=1)
    ]
    print(
        perf_file,
        " min is %.2fns" % ((min(result) / (REPEAT * REPEAT_FULL)) / nano),
        " max is %.2fns" % ((max(result) / (REPEAT * REPEAT_FULL)) / nano),
        " mean is %.2fns" % ((statistics.mean(result) / (REPEAT * REPEAT_FULL)) / nano),
        "      0--------9",
        *graph,
        sep="\n",
        end="\n===\n\n"
    )
