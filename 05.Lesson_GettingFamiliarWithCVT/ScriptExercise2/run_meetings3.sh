#! /usr/bin/env sh
solc-select use 0.8.7&&
certoraRun ../../02.Lesson_InvestigateViolations/MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
--verify MeetingScheduler:../../02.Lesson_InvestigateViolations/MeetingScheduler/meetings.spec \
--solc solc \
--rule monotonousIncreasingNumOfParticipants \
--send_only \
--msg "$1"