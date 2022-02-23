#! /usr/bin/env sh
solc-select use 0.7.6
certoraRun BordaBug1.sol:Borda --verify Borda:Borda.spec \
--rule correctPointsIncreaseToContenders \
--solc solc \
--msg "$1"
