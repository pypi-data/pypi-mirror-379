LoadPackage( "ToricVarieties" );

## We create a complicated 2-dimensional projective toric variety T.
P := Polytope( [ [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1], [-2,1], [-1,2] ] );

T := ToricVariety( P );

## It is complete and projective variety
IsComplete( T );

IsProjective( T );

