#! /usr/bin/env sh

solc-select use 0.7.0
certoraRun ../BankLesson1/Bank.sol:Bank \
  --verify Bank:../BankLesson1/Parametric.spec \
  --solc solc \
  --rule validityOfTotalFundsWithVars \
  --msg "validity of total funds with vars"