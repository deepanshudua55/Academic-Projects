
-- Table: faculty
CREATE TABLE faculty ( 
    fid       INTEGER         PRIMARY KEY AUTOINCREMENT,
    lastname  VARCHAR( 100 ),
    firstname VARCHAR( 100 ),
    phone     INTEGER( 20 ),
    email     VARCHAR( 50 ),
    office    INTEGER( 10 ) 
);


-- Table: staff
CREATE TABLE staff ( 
    sid       INTEGER         PRIMARY KEY AUTOINCREMENT,
    lastname  VARCHAR( 100 ),
    firstname VARCHAR( 100 ),
    phone     INTEGER( 20 ),
    email     VARCHAR( 50 ),
    office    INTEGER( 10 ) 
);


-- Table: gradstudents
CREATE TABLE gradstudents ( 
    gid       INTEGER         PRIMARY KEY AUTOINCREMENT,
    lastname  VARCHAR( 100 ),
    firstname VARCHAR( 100 ),
    phone     INTEGER( 20 ),
    email     VARCHAR( 50 ),
    city      VARCHAR( 50 ),
    state     VARCHAR( 10 ),
    zip       VARCHAR( 10 ),
    office    INTEGER( 10 ),
    url       VARCHAR( 50 ),
    gpa       VARCHAR( 10 ) 
);


-- Table: undergradstudent
CREATE TABLE undergradstudent ( 
    uid       INTEGER         PRIMARY KEY AUTOINCREMENT,
    lastname  VARCHAR( 100 ),
    firstname VARCHAR( 100 ),
    phone     INTEGER( 20 ),
    email     VARCHAR( 50 ),
    city      VARCHAR( 50 ),
    state     VARCHAR( 10 ),
    zip       VARCHAR( 10 ),
    gpa       VARCHAR( 10 ) 
);


-- Table: deptname
CREATE TABLE deptname ( 
    did      INTEGER        PRIMARY KEY AUTOINCREMENT,
    deptname VARCHAR( 20 ) 
);

