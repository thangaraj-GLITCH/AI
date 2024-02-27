planet(mercury,1).
planet(venus,2).
planet(earth,3).

moon(earth,moon).
moon(venus,z102).

getdetail(NAME):-
    planet(NAME,X),
    moon(NAME,Y),
    format('~w is the ~w~n in the solar system and its moon is ~w',[NAME,X,Y]).