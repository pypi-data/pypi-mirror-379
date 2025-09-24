## CompleteNonProjective.g

## gapcolor ##
gap> LoadPackage( "ToricVarieties" );
true
gap> ## Lets have a look at the toric variety
gap> ## that is complete but not projective
gap> rays := [ [1,0,0], [-1,0,0], [0,1,0],
gap> [0,-1,0], [0,0,1], [0,0,-1],
gap>   [2,1,1], [1,2,1], [1,1,2], [1,1,1] ];
[ [ 1, 0, 0 ], [ -1, 0, 0 ], [ 0, 1, 0 ], [ 0, -1, 0 ],
  [ 0, 0, 1 ], [ 0, 0, -1 ], [ 2, 1, 1 ], [ 1, 2, 1 ],
  [ 1, 1, 2 ], [ 1, 1, 1 ] ]
gap> cones := [ [1,3,6], [1,4,6], [1,4,5], [2,3,6],
gap>  [2,4,6], [2,3,5], [2,4,5],
gap>   [1,5,9], [3,5,8], [1,3,7], [1,7,9], [5,8,9], [3,7,8], 
gap> [7,9,10], [8,9,10], [7,8,10] ];
[ [ 1, 3, 6 ], [ 1, 4, 6 ], [ 1, 4, 5 ], [ 2, 3, 6 ],
  [ 2, 4, 6 ], [ 2, 3, 5 ], [ 2, 4, 5 ], [ 1, 5, 9 ],
  [ 3, 5, 8 ], [ 1, 3, 7 ], 
  [ 1, 7, 9 ], [ 5, 8, 9 ], [ 3, 7, 8 ],
  [ 7, 9, 10 ], [ 8, 9, 10 ], [ 7, 8, 10 ] ]
gap> F := Fan( rays, cones );
<A fan in |R^3>
gap> T := ToricVariety( F );
<A toric variety of dimension 3>
gap> IsComplete( T );
true
gap> IsAffine( T );
false
gap> SetIsProjective( T, false );
gap> Dimension( T );
3
gap> HasTorusfactor( T );
false
gap> IsSmooth( T );
true
gap> ClassGroup( T );
<A non-torsion left module presented by 3 relations
for 10 generators>
gap> PicardGroup( T );
<A non-torsion left submodule given by 10 generators>
gap> CoxRing( T, "x" );
Q[x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10]
(weights: [ [ 0, 0, 0, 0, 0, 1, -1, -1, -2, -1 ]
, [ 0, 0, 0, 1, 0, 0, -1, -2, -1, -1 ],
  [ 0, 0, 0, 0, 1, 0, 2, 1, 1, 1 ],
  [ 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ], 
  [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ], 
  [ 0, 0, 0, 0, 0, 0, 0, 0, 1, 0 ], 
  [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ] ])
gap> Display( ClassGroup ( T ) );
[ [   1,   0,   0,   0,   0,  -1,   1,   1,   2,   1 ],
  [   0,   1,   0,  -1,   0,   0,   1,   2,   1,   1 ],
  [   0,   0,  -1,   0,   1,   0,   2,   1,   1,   1 ] ]

Cokernel of the map

Z^(1x3) --> Z^(1x10),

currently represented by the above matrix
gap> Display( ByASmallerPresentation( ClassGroup( T ) ) );
Z^(1 x 7)
gap> CoxRing( T );
Q[x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,x_10]
(weights: [ [ 0, 0, 1, -1, -1, -2, -1 ],
 [ 1, 0, 0, -1, -2, -1, -1 ],
 [ 0, 1, 0, 2, 1, 1, 1 ],
 [ 1, 0, 0, 0, 0, 0, 0 ],
 [ 0, 1, 0, 0, 0, 0, 0 ], 
 [ 0, 0, 1, 0, 0, 0, 0 ],
 [ 0, 0, 0, 1, 0, 0, 0 ],
 [ 0, 0, 0, 0, 1, 0, 0 ],
 [ 0, 0, 0, 0, 0, 1, 0 ],
 [ 0, 0, 0, 0, 0, 0, 1 ] ])
## endgapcolor ##