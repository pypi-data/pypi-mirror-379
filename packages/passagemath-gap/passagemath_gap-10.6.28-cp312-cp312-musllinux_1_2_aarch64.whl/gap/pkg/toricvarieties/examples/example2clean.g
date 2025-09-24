LoadPackage( "ToricVariety" );

## We create the Hirzebruch surface H5.

H5 := Fan( [[-1,5],[0,1],[1,0],[0,-1]],[[1,2],[2,3],[3,4],[4,1]] );

H5 := ToricVariety( H5 );