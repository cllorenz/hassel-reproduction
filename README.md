# NetPlumber Reproduction

This repository offers a scripted reproduction of the Internet2 and Stanford
benchmarks for NetPlumber.
It is based on the original repo as offered by Peyman Kazemian with minor
changes to enable reproduction: https://bitbucket.org/peymank/hassel-public/wiki/Home

Changes include unnecessary inter-rule-dependency calculations (which is later
done by NetPlumber), a missing library for the linker, and a fix for the TF
handling of the Juniper parser.

The benchmark workloads stem from the ATPG repository: https://github.com/eastzone/atpg/tree/master/atpg/data


## How to reproduce the NetPlumber results

You can reproduce the benchmark results using a Docker container. First, build the container with

    cd hassel-reproduction
    sudo docker build -t "repro:latest" .

Then, you can run the benchmark with a prepared script (values may be `stanford` or `i2`):

    sudo docker run -t "repro:latest" bash run_benchmarks.sh stanford
