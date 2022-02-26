#! /usr/bin/env sh
solc-select use 0.8.0 &&
certoraRun ERC20Fixed.sol:ERC20 --verify ERC20:ERC20.spec \
 --solc solc \
 --typecheck_only