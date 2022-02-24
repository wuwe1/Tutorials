#! /usr/bin/env sh
solc-select use 0.8.7&&
certoraRun MeetingSchedulerBug2.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--rule checkPendingToCancelledOrStarted \
--solc solc \
--msg "$1"