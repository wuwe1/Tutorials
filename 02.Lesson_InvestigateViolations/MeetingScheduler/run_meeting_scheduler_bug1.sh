#! /usr/bin/env sh
solc-select use 0.8.7&&
certoraRun MeetingSchedulerBug1.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc solc \
--msg "$1"