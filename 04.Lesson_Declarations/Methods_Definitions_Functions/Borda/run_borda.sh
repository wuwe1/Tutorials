#! /usr/bin/env sh
solc-select use 0.7.0 &&
certoraRun BordaFixed.sol:Borda --verify Borda:Borda.spec \
 --solc solc \
 --typecheck_only