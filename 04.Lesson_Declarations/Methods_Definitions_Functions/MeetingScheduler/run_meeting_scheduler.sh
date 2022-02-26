#! /usr/bin/env sh
solc-select use 0.8.0 &&
certoraRun MeetingSchedulerFixed.sol:MeetingScheduler \
 --verify MeetingScheduler:meetings.spec \
 --solc solc \
 --typecheck_only