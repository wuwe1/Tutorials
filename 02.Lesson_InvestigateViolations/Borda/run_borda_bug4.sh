#! /usr/bin/env sh
solc-select use 0.7.6
certoraRun BordaBug4.sol:Borda --verify Borda:Borda.spec \
--solc solc \
--msg "$1"
