states of the system:

```ruby
- `defUNINITIALIZED` - UNINITIALIZED is defined as `getStateById(meetindId)` is 0.
- `defPENDING` - PENDING is defined as `getStateById(meetindId)` is 1.
- `defSTARTED` - STARTED is defined as `getStateById(meetindId)` is 2.
- `defENDED` - ENDED is defined as `getStateById(meetindId)` is 3.
- `defCANCELLED` - CANCELLED is defined as `getStateById(meetindId)` is 4.
```

1. **Valid state** - `defUNINITIALIZED` => `getStartTimeById(meetingId) == 0 && getEndTimeById(meetingId) == 0 && getNumOfParticipents(meetingId) == 0 && getStateById(meetingId) == 0 && getOrganizer(meetingId) == 0`

2. **Valid state** - `defPENDING` => `getStateById(meetingId) == 1 && getNumOfParticipents(meetingId) == 0 && getStartTimeById(meetingId) != 0 && getEndTimeById(meetingId) != 0 && getOrganizer(meetingId) != 0`

3. **Valid state** - `defSTARTED` => `getStateById(meetingId) == 2 && getStartTimeById(meetingId) != 0 && getEndTimeById(meetingId) != 0`

4. **Valid state** - `defENDED` => `getStateById(meetingId) == 3 && getStartTimeById(meetingId) != 0 && getEndTimeById(meetingId) != 0`

5. **Valid state** - `meetingCancelled` => `getStateById(meetingId) == 4 && getStartTimeById(meetingId) != 0 && getEndTimeById(meetingId) != 0`

6. **States transition** - `defUNINITIALIZED` -> `defUNINITIALIZED` and `defUNINITIALIZED` -> `defPENDING` are valid. `defUNINITIALIZED` -> `defPENDING` only by `scheduleMeeting`

7. **States transition** - `defPENDING` -> `defSTARTED` and `defPENDING` -> `defCANCELLED` are valid. `defPENDING` -> `defSTARTED` only by `startMeeting`. `defPENDING` -> `defCANCELLED` only by `cancelMeeting`

8. **States transition** - `defSTARTED` -> `defENDED` is valid. `defSTARTED` -> `defENDED` only by `endMeeting` and `getEndTimeById(meetingId) <= e.block.timestamp`

9. **Variable transition** - `numOfParticipents` increase only and only when `joinMeeting` was called.

10. **Variable transition** - `startTime` and `endTime` increase only and only when `scheduleMeeting` was called.

11. **Unit tests** - `joinMeeting` should increase `numOfParticipents` correctly.

## Prioritizing


### High Priority:

- Property 1, 2, 3, 4, 5, 6, 7, 8 are high priority because these states are critical to the system and should not behave wrongly.
- Property 10 is high priority because if they fail then attacker can change the startTime and endTime to invalid value.

### Medium Priority:

- Property 9 and 11 are medium priority because violation of this rule means that attacker can decrease the numOfParticipents or join without increase numOfParticipents.