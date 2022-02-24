#! /usr/bin/env sh
solc-select use 0.8.0 &&
certoraRun ERC20Bug3.sol:ERC20 --verify ERC20:ERC20.spec \
--solc solc \
--rule balanceChangesFromCertainFunctions \
--optimistic_loop \
--msg "$1"
