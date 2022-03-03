
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4()
	ballAt() != 4 && ballAt() != 3
		
		
rule neverReachP4(method f) {
	env e;
	calldataarg args;
	uint256 atBefore = ballAt();
	require(atBefore != 3 && atBefore != 4);
	f(e, args);
	uint256 atAfter = ballAt();
	assert atBefore != 4, "ball reach player 4";
}