#! /usr/bin/env sh
solc-select use 0.8.7&&
certoraRun MeetingSchedulerBug4.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--solc solc \
--rule checkStartedToStateTransition \
--msg "$1"