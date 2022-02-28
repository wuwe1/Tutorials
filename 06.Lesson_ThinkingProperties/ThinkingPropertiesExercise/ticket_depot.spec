methods {
    ticketDepot(uint64)
    createEvent(uint64,uint16) returns(uint16)
    buyNewTicket(uint16,address) returns(uint16)
    offerTicket(uint16,uint16,uint64,address,uint16)
    buyOfferedTicket(uint16,uint16,address)

    getOwnerById(uint16) returns(address) envfree
    getTicketPriceById(uint16) returns(uint64) envfree
    getTicketsRemainingById(uint16) returns(uint16) envfree
    getBuyerById(uint16,uint16) returns (address) envfree
    getPriceById(uint16,uint16) returns (uint64) envfree
    getDeadlineById(uint16,uint16) returns (uint256) envfree
    getNumEvents() returns (uint16) envfree
}

definition eventNonCreated(uint16 eventID) returns bool =
    getOwnerById(eventID) == 0 &&
    getTicketPriceById(eventID) == 0 &&
    getTicketsRemainingById(eventID) == 0;

definition eventCreated(uint16 eventID) returns bool =
    getOwnerById(eventID) != 0;

definition ticketNonOffered(uint16 eventID, uint16 ticketID) returns bool =
    getBuyerById(eventID, ticketID) == 0 &&
    getPriceById(eventID, ticketID) == 0 &&
    getDeadlineById(eventID, ticketID) == 0;

definition ticketOffered(uint16 eventID, uint16 ticketID) returns bool =
    getBuyerById(eventID, ticketID) != 0 && 
    getPriceById(eventID, ticketID) != 0 && 
    getDeadlineById(eventID, ticketID) != 0;

// Checks that state transition from defEventNonCreated to defEventCreated can only happen if eventCreated() was called
rule checkEventNonCreatedToCreated(method f, uint16 eventID) {
    env e;
    calldataarg args;
    require eventNonCreated(eventID);
    f(e, args);
    assert eventNonCreated(eventID) || eventCreated(eventID), "the status of event changed from NonCreated to an invalid state";
    assert (eventCreated(eventID) => f.selector == createEvent(uint64, uint16).selector), "the status of the event changed from NonCreated to Created through a function other then createEvent(uint64, uint16)";
}

rule checkTicketOfferedToNonOffered(method f, uint16 eventID, uint16 ticketID) {
    env e;
    calldataarg args;
    require ticketNonOffered(eventID, ticketID);
    f(e, args);
    assert ticketNonOffered(eventID, ticketID) || ticketOffered(eventID, ticketID), "the status of ticket changed from NonOffered to an invalid state";
    assert (ticketOffered(eventID, ticketID) => f.selector == offerTicket(uint16,uint16,uint64,address,uint16).selector), "the status of the event changed from NonCreated to Created through a function other then offerTicket(uint16,uint16,uint64,address,uint16)";
}

rule checkTicketNonOfferedToOffered(method f, uint16 eventID, uint16 ticketID) {
    env e;
    calldataarg args;
    require ticketOffered(eventID, ticketID);
    f(e, args);
    assert ticketOffered(eventID, ticketID) || ticketNonOffered(eventID, ticketID), "the status of ticket changed from Offered to an invalid state";
    assert (ticketNonOffered(eventID, ticketID) => f.selector == buyOfferedTicket(uint16,uint16,address).selector), "the status of the event changed from NonCreated to Created through a function other then buyOfferedTicket(uint16,uint16,address)";
}

rule monotonousIncreasingNumEvents(method f) {
    env e;
    calldataarg args;
    uint16 numEventsBefore = getNumEvents();
    f(e, args);
    uint16 numEventsAfter = getNumEvents();

    assert numEventsBefore <= numEventsAfter, "the number of events decreased as a result of a function call";
    assert ((numEventsBefore < numEventsAfter) => f.selector == createEvent(uint64, uint16).selector), "the numEvents is increased through a function call other then createEvent(uint64, uint16)";
}

rule canNotBuyTicketWhenRemainingIsZero(method f, uint16 eventID) {
    env e;
    calldataarg args;
    require getTicketsRemainingById(eventID) == 0;
    f(e, args);

    assert getTicketsRemainingById(eventID) == 0, "Ticket is bought when remaining ticket is zero";
}