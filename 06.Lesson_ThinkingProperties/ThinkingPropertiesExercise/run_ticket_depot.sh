#! /usr/bin/env sh
solc-select use 0.6.0 &&
certoraRun TicketDepot/TicketDepot.sol:TicketDepot \
--verify TicketDepot:ticket_depot.spec \
--solc solc \
--rule monotonousIncreasingNumEvents \
--send_only
