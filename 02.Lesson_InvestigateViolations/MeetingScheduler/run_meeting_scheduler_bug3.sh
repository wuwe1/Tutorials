#! /usr/bin/env sh
solc-select use 0.8.7&&
certoraRun MeetingSchedulerBug3.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc solc \
--rule startBeforeEnd \
--msg "$1"