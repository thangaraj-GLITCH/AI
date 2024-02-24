teaches(john, math).
teaches(lisa, english).
teaches(ali, physics).

enrolled(bob, math).
enrolled(bob, english).
enrolled(sara, physics).

course_code(math, 101).
course_code(english, 102).
course_code(physics, 103).

/* Rules */
student_teacher_course(Student) :-
    enrolled(Student, Course),
    teaches(Teacher, Course),
    course_code(Course, Code),
    format('~w is enrolled in ~w taught by ~w. Course code: ~w~n', [Student, Course, Teacher, Code]).
