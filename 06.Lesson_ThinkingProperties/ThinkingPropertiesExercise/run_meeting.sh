#! /usr/bin/env sh
solc-select use 0.8.7 &&
certoraRun MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
--verify MeetingScheduler:meetings.spec \
--solc solc \
--send_only
