states of the system

```ruby
- `defEventNonCreated` - is defined as `eventsMap[eventID]` returns all 0
- `defEventCreated` - is defined as `eventsMap[eventID].owner` is not 0
- `defTicketNonOffered` - is defined as `offerings[offerID]` returns all 0
- `defTicketOffered` - is defined as `offerings[offerID]` returns all not 0
```

1. **Valid state** - `defEventNonCreated` => `eventsMap[eventID]` returns all 0. 
2. **Valid state** - `defEventCreated` => `eventsMap[eventID].owner` is not 0. If owner is 0, `transacationFee` can not be retrieved. 
3. **Valid state** - `defTicketNonOffered` => `offerings[offerID]` returns all 0. 
4. **Valid state** - `defTicketOffered` => `offerings[offerID]` returns all not 0. 
5. **State transition** - `defEventNonCreated` => `defEventCreated` only by `createEvent`
6. **State transition** - `defTicketNonOffered` => `defTicketOffered` only by `offerTicket`
7. **State transition** - `defTicketOffered` => `defTicketNonOffered` only by `buyOfferedTicket`
8. **Variable transition** - `numEvents` increase only and only when `createEvent` is called. Otherwise, user can overwrite existing events.
9. **High-level** - Can not buy ticket when `eventsMap[eventID].ticketsRemaining` is 0.

## Prioritizing

### High Priority:
- Property 1,2,3,4,5,6,7 are high priority, because these states are critical to the system
- Property 8 is high priority, violation of this rule will lead to overwrite on existing events.
- Property 9 is high priority because if they fail the user can buy more tickets than expected.