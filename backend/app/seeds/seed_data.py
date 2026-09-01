
TOPICS_DATA = [
    {"name": "Python Programming", "slug": "python", "description": "Core Python syntax, data structures, OOP, async programming, and standard library internals.", "icon": "Terminal", "color": "#3b82f6", "order": 1},
    {"name": "Computer Science & Programming", "slug": "programming", "description": "Core programming paradigms, compilers, memory management, and software design principles.", "icon": "Code", "color": "#10b981", "order": 2},
    {"name": "SQL & Relational Databases", "slug": "sql", "description": "Relational schema design, SQL joins, indexing, ACID transactions, and query optimization.", "icon": "Database", "color": "#f59e0b", "order": 3},
    {"name": "Modern Web Development", "slug": "web-dev", "description": "Frontend frameworks, DOM mechanics, HTTP/REST APIs, CSS Flexbox/Grid, and modern browser APIs.", "icon": "Globe", "color": "#ec4899", "order": 4},
    {"name": "Cybersecurity & Cryptography", "slug": "cybersecurity", "description": "Threat analysis, network defenses, cryptography, OWASP Top 10, and ethical hacking.", "icon": "ShieldCheck", "color": "#ef4444", "order": 5},
    {"name": "Mathematics & Discrete Math", "slug": "mathematics", "description": "Probability, combinatorics, linear algebra, graph theory, and mathematical problem-solving.", "icon": "Binary", "color": "#8b5cf6", "order": 6},
    {"name": "Natural Sciences", "slug": "science", "description": "Physics, chemistry, biology, astronomy, and fundamental scientific principles.", "icon": "Atom", "color": "#06b6d4", "order": 7},
    {"name": "General Knowledge & Trivia", "slug": "general-knowledge", "description": "Trivia spanning world events, cultural milestones, arts, and global phenomena.", "icon": "HelpCircle", "color": "#64748b", "order": 8},
    {"name": "Logical Reasoning & Puzzles", "slug": "logical-reasoning", "description": "Deductive logic, pattern recognition, spatial reasoning, and brain teasers.", "icon": "Cpu", "color": "#14b8a6", "order": 9},
    {"name": "Data Analytics & Statistics", "slug": "data-analytics", "description": "Data wrangling, statistical distributions, hypothesis testing, and BI visual storytelling.", "icon": "BarChart3", "color": "#f97316", "order": 10},
    {"name": "Artificial Intelligence & ML", "slug": "ai-ml", "description": "Neural networks, deep learning, NLP, transformers, reinforcement learning, and AI ethics.", "icon": "Bot", "color": "#6366f1", "order": 11},
    {"name": "Networking & Cloud Infrastructure", "slug": "networking", "description": "TCP/IP suite, DNS, routing protocols, distributed cloud architecture, and CDN edge delivery.", "icon": "Network", "color": "#0284c7", "order": 12},
    {"name": "Data Structures & Algorithms", "slug": "algorithms", "description": "Big-O complexity, binary search trees, dynamic programming, sorting, and graph traversals.", "icon": "GitBranch", "color": "#d946ef", "order": 13},
    {"name": "World History", "slug": "history", "description": "Ancient civilizations, global revolutions, empires, treaties, and turning points in human history.", "icon": "Landmark", "color": "#a855f7", "order": 14},
    {"name": "World Geography", "slug": "geography", "description": "Continents, capital cities, geopolitical borders, topographical features, and world landmarks.", "icon": "Compass", "color": "#84cc16", "order": 15}
]

ACHIEVEMENTS_DATA = [
    {"code": "FIRST_GAME", "title": "First Step", "description": "Play and finish your very first game session in GameVerse.", "icon": "Footprints", "category": "general", "requirement_type": "games_played", "requirement_value": 1, "xp_reward": 50, "badge_color": "#3b82f6"},
    {"code": "GAMES_10", "title": "Regular Challenger", "description": "Complete 10 game sessions across any mode.", "icon": "Medal", "category": "general", "requirement_type": "games_played", "requirement_value": 10, "xp_reward": 150, "badge_color": "#10b981"},
    {"code": "GAMES_50", "title": "Veteran Gamer", "description": "Complete 50 game sessions across any mode.", "icon": "Trophy", "category": "general", "requirement_type": "games_played", "requirement_value": 50, "xp_reward": 500, "badge_color": "#f59e0b"},
    {"code": "PERFECT_ROUND", "title": "Flawless Execution", "description": "Finish a challenge round with 100% accuracy.", "icon": "Sparkles", "category": "skill", "requirement_type": "perfect_game", "requirement_value": 1, "xp_reward": 200, "badge_color": "#ec4899"},
    {"code": "STREAK_5", "title": "On Fire", "description": "Reach a combo streak of 5 consecutive correct answers.", "icon": "Flame", "category": "skill", "requirement_type": "streak", "requirement_value": 5, "xp_reward": 100, "badge_color": "#ef4444"},
    {"code": "STREAK_10", "title": "Unstoppable", "description": "Reach a combo streak of 10 consecutive correct answers.", "icon": "Zap", "category": "skill", "requirement_type": "streak", "requirement_value": 10, "xp_reward": 300, "badge_color": "#8b5cf6"},
    {"code": "SCORE_1000", "title": "High Roller", "description": "Score over 1,000 points in a single match.", "icon": "Target", "category": "score", "requirement_type": "high_score", "requirement_value": 1000, "xp_reward": 250, "badge_color": "#f97316"},
    {"code": "MP_CHAMPION", "title": "Arena Victor", "description": "Win your first real-time multiplayer battle.", "icon": "Crown", "category": "multiplayer", "requirement_type": "win_multiplayer", "requirement_value": 1, "xp_reward": 300, "badge_color": "#eab308"}
]

TASKS_DATA = [
    {
        "topic_slug": "python",
        "title": "List vs Tuple Mutability",
        "question": "Which statement accurately describes the difference between a Python list and a Python tuple?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Lists are mutable and can be changed in-place, while tuples are immutable.",
        "tags": "python,data-structures",
        "answers": [
            {
                "text": "Lists are mutable and can be changed in-place, while tuples are immutable.",
                "is_correct": True
            },
            {
                "text": "Tuples are mutable, while lists are strictly immutable.",
                "is_correct": False
            },
            {
                "text": "Lists can only store numbers, while tuples store any type.",
                "is_correct": False
            },
            {
                "text": "Tuples cannot be indexed or sliced.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "CPython Global Interpreter Lock",
        "question": "What is the primary function of the GIL in CPython?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "The GIL prevents multiple native threads from executing Python bytecodes simultaneously to protect CPython's memory management.",
        "tags": "python,concurrency,gil",
        "answers": [
            {
                "text": "It prevents multiple threads from executing CPython bytecode simultaneously to protect memory integrity.",
                "is_correct": True
            },
            {
                "text": "It accelerates CPU-bound multi-threaded loops automatically.",
                "is_correct": False
            },
            {
                "text": "It prevents garbage collection from freeing memory.",
                "is_correct": False
            },
            {
                "text": "It forces all asynchronous coroutines to run on a single CPU core.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Generator Memory Efficiency",
        "question": "Why is `(x*x for x in range(10**7))` more memory-efficient than `[x*x for x in range(10**7)]`?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Generators evaluate lazily on-demand rather than allocating all elements in RAM upfront.",
        "tags": "python,generators,memory",
        "answers": [
            {
                "text": "Generators evaluate lazily on-demand rather than allocating memory for all elements upfront.",
                "is_correct": True
            },
            {
                "text": "Generators store elements on disk cache instead of RAM.",
                "is_correct": False
            },
            {
                "text": "List comprehensions convert numbers to strings.",
                "is_correct": False
            },
            {
                "text": "Generators execute directly in GPU registers.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Dictionary Key Insertion Order",
        "question": "Since Python 3.7+, what guarantee exists for standard `dict` keys?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Dictionaries are officially guaranteed to preserve insertion order.",
        "tags": "python,dict,language-spec",
        "answers": [
            {
                "text": "Dictionaries are guaranteed to preserve insertion order.",
                "is_correct": True
            },
            {
                "text": "Dictionaries sort keys alphabetically automatically.",
                "is_correct": False
            },
            {
                "text": "Dictionaries randomize order for security.",
                "is_correct": False
            },
            {
                "text": "Dictionaries only retain order if using OrderedDict.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Python __slots__ Optimization",
        "question": "What is the primary benefit of defining `__slots__` inside a class?",
        "difficulty": "EXPERT",
        "points": 50,
        "time_limit_seconds": 30,
        "explanation": "It eliminates the default instance __dict__, saving significant RAM when creating millions of objects.",
        "tags": "python,oop,optimization",
        "answers": [
            {
                "text": "It eliminates the default `__dict__` per instance, drastically saving memory overhead.",
                "is_correct": True
            },
            {
                "text": "It enables multithreaded lock-free execution for class methods.",
                "is_correct": False
            },
            {
                "text": "It compiles the class into C machine code.",
                "is_correct": False
            },
            {
                "text": "It automatically serializes class instances to binary SQLite records.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Decorators with Arguments",
        "question": "How many nested functions are typically required to implement a Python decorator that accepts custom configuration arguments?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "A decorator accepting arguments requires an outer factory function, an inner decorator function, and a wrapper function (3 levels).",
        "tags": "python,decorators,functions",
        "answers": [
            {
                "text": "Three levels of nested functions (factory, decorator, and wrapper).",
                "is_correct": True
            },
            {
                "text": "Only one single flat function.",
                "is_correct": False
            },
            {
                "text": "Exactly two functions.",
                "is_correct": False
            },
            {
                "text": "Four recursive functions.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Python Metaclasses",
        "question": "In Python, which built-in class is the default metaclass of all standard classes?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "`type` is the metaclass responsible for constructing class objects in Python.",
        "tags": "python,metaprogramming,oop",
        "answers": [
            {
                "text": "type",
                "is_correct": True
            },
            {
                "text": "object",
                "is_correct": False
            },
            {
                "text": "ClassType",
                "is_correct": False
            },
            {
                "text": "BaseMeta",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "python",
        "title": "Context Managers and __enter__/__exit__",
        "question": "Which method of a Python context manager is invoked when an unhandled exception occurs inside a `with` block?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "`__exit__(exc_type, exc_val, exc_tb)` receives exception details and can suppress the exception if it returns True.",
        "tags": "python,context-manager,exceptions",
        "answers": [
            {
                "text": "__exit__",
                "is_correct": True
            },
            {
                "text": "__enter__",
                "is_correct": False
            },
            {
                "text": "__close__",
                "is_correct": False
            },
            {
                "text": "__catch__",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "programming",
        "title": "Pure Function Definition",
        "question": "What characterizes a function as 'pure' in functional programming?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "A pure function has no side effects and always returns identical output for identical inputs.",
        "tags": "cs,functional,paradigms",
        "answers": [
            {
                "text": "It produces no side effects and always returns the same result for the same arguments.",
                "is_correct": True
            },
            {
                "text": "It only accepts integers as parameters.",
                "is_correct": False
            },
            {
                "text": "It is written in assembly or pure C.",
                "is_correct": False
            },
            {
                "text": "It executes in O(1) constant time.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "programming",
        "title": "Stack vs Heap Allocation",
        "question": "How does stack memory allocation differ from heap memory allocation?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Stack allocation is fast and strictly follows LIFO call frames, whereas heap allocation is dynamic and managed manually or via garbage collection.",
        "tags": "cs,memory,architecture",
        "answers": [
            {
                "text": "Stack allocation is LIFO and managed automatically, while heap allocation is dynamic.",
                "is_correct": True
            },
            {
                "text": "Heap memory is allocated at compile time, while stack is dynamic.",
                "is_correct": False
            },
            {
                "text": "Stack memory cannot overflow.",
                "is_correct": False
            },
            {
                "text": "Heap memory is faster than CPU cache registers.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "programming",
        "title": "Dependency Inversion Principle",
        "question": "What is the core directive of the Dependency Inversion Principle (SOLID)?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "High-level modules should depend upon abstractions rather than low-level concrete implementations.",
        "tags": "cs,solid,architecture",
        "answers": [
            {
                "text": "High-level modules should depend on abstractions rather than concrete low-level implementations.",
                "is_correct": True
            },
            {
                "text": "A class should have only one reason to change.",
                "is_correct": False
            },
            {
                "text": "Classes should be open for modification and closed for extension.",
                "is_correct": False
            },
            {
                "text": "Interfaces must contain at least ten methods.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "programming",
        "title": "Idempotency in API Design",
        "question": "What does it mean for an API operation to be idempotent?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Executing the operation multiple times leaves the system in the same state as executing it once.",
        "tags": "cs,api,architecture",
        "answers": [
            {
                "text": "Executing the operation multiple times produces the exact same system state as executing it once.",
                "is_correct": True
            },
            {
                "text": "The API returns encrypted data on every request.",
                "is_correct": False
            },
            {
                "text": "The request is processed asynchronously in under 1ms.",
                "is_correct": False
            },
            {
                "text": "The endpoint requires two-factor authentication.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "programming",
        "title": "Deadlock Coffman Conditions",
        "question": "Which of the following is NOT one of Coffman's four conditions for a system deadlock to occur?",
        "difficulty": "EXPERT",
        "points": 50,
        "time_limit_seconds": 30,
        "explanation": "The 4 Coffman conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Preemptive Allocation prevents deadlock.",
        "tags": "cs,concurrency,deadlock",
        "answers": [
            {
                "text": "Preemptive Resource Reallocation",
                "is_correct": True
            },
            {
                "text": "Mutual Exclusion",
                "is_correct": False
            },
            {
                "text": "Hold and Wait",
                "is_correct": False
            },
            {
                "text": "Circular Wait",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "sql",
        "title": "INNER JOIN vs LEFT JOIN",
        "question": "What is the core difference between INNER JOIN and LEFT JOIN in SQL?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "LEFT JOIN retains all rows from the left table with NULLs for unmatched right rows, while INNER JOIN drops unmatched rows.",
        "tags": "sql,joins,relational",
        "answers": [
            {
                "text": "LEFT JOIN keeps all rows from the left table, filling unmatched right columns with NULL.",
                "is_correct": True
            },
            {
                "text": "INNER JOIN keeps all unmatched rows and drops matching rows.",
                "is_correct": False
            },
            {
                "text": "LEFT JOIN sorts results ascending by default.",
                "is_correct": False
            },
            {
                "text": "INNER JOIN only works on numeric primary keys.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "sql",
        "title": "B-Tree Index Search Complexity",
        "question": "What is the standard time complexity for searching a key in a database B-Tree index?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "A balanced B-Tree index has O(log N) search complexity.",
        "tags": "sql,indexing,performance",
        "answers": [
            {
                "text": "O(log N)",
                "is_correct": True
            },
            {
                "text": "O(1)",
                "is_correct": False
            },
            {
                "text": "O(N)",
                "is_correct": False
            },
            {
                "text": "O(N log N)",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "sql",
        "title": "ACID Isolation - Phantom Reads",
        "question": "Which ANSI SQL transaction isolation level completely prevents Phantom Reads?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "SERIALIZABLE prevents dirty reads, non-repeatable reads, and phantom reads through range locking or snapshot isolation.",
        "tags": "sql,transactions,acid",
        "answers": [
            {
                "text": "SERIALIZABLE",
                "is_correct": True
            },
            {
                "text": "READ COMMITTED",
                "is_correct": False
            },
            {
                "text": "READ UNCOMMITTED",
                "is_correct": False
            },
            {
                "text": "REPEATABLE READ",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "sql",
        "title": "SQL Window Functions",
        "question": "Which SQL clause partitions rows for calculation without collapsing them like GROUP BY does?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "OVER(PARTITION BY ...) calculates aggregate values across a window without collapsing individual rows.",
        "tags": "sql,window-functions,analytics",
        "answers": [
            {
                "text": "OVER (PARTITION BY ...)",
                "is_correct": True
            },
            {
                "text": "GROUP BY ROLLUP",
                "is_correct": False
            },
            {
                "text": "HAVING COUNT(*)",
                "is_correct": False
            },
            {
                "text": "CROSS APPLY",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "sql",
        "title": "Database Normalization - 3NF",
        "question": "What is required for a database table to be in Third Normal Form (3NF)?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "3NF requires the table to be in 2NF and have no transitive functional dependencies on non-key attributes.",
        "tags": "sql,database-design,normalization",
        "answers": [
            {
                "text": "It must be in 2NF and contain no transitive dependencies for non-key attributes.",
                "is_correct": True
            },
            {
                "text": "Every column must be an encrypted binary string.",
                "is_correct": False
            },
            {
                "text": "It must contain at least three foreign key relationships.",
                "is_correct": False
            },
            {
                "text": "All columns must have unique indexes.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "web-dev",
        "title": "React Virtual DOM Reconciliation",
        "question": "What is the purpose of reconciliation in React?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Reconciliation compares new and old virtual trees to apply minimal real DOM patches.",
        "tags": "react,frontend,virtual-dom",
        "answers": [
            {
                "text": "Diffing Virtual DOM trees to compute the minimal set of real DOM mutations.",
                "is_correct": True
            },
            {
                "text": "Transpiling JSX directly into browser assembly code.",
                "is_correct": False
            },
            {
                "text": "Managing session authentication tokens automatically.",
                "is_correct": False
            },
            {
                "text": "Optimizing network roundtrips via WebRTC.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "web-dev",
        "title": "CSS Flexbox Axis Alignment",
        "question": "Which CSS property aligns items along the cross axis in a row flex container?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "align-items aligns items on the cross axis, while justify-content aligns on the main axis.",
        "tags": "css,flexbox,layout",
        "answers": [
            {
                "text": "align-items",
                "is_correct": True
            },
            {
                "text": "justify-content",
                "is_correct": False
            },
            {
                "text": "flex-direction",
                "is_correct": False
            },
            {
                "text": "align-content",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "web-dev",
        "title": "CORS Preflight Request",
        "question": "Which HTTP method is sent by web browsers for a CORS preflight check?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Browsers automatically send an HTTP OPTIONS request to verify CORS headers prior to sending complex requests.",
        "tags": "http,cors,security",
        "answers": [
            {
                "text": "OPTIONS",
                "is_correct": True
            },
            {
                "text": "HEAD",
                "is_correct": False
            },
            {
                "text": "GET",
                "is_correct": False
            },
            {
                "text": "PATCH",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "web-dev",
        "title": "React useCallback Purpose",
        "question": "What problem does the `useCallback` hook solve in React?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "useCallback memoizes callback function instances across renders to prevent unnecessary re-rendering of child components.",
        "tags": "react,hooks,performance",
        "answers": [
            {
                "text": "It memoizes function instances between renders to prevent unnecessary child re-renders.",
                "is_correct": True
            },
            {
                "text": "It replaces all asynchronous Promises with synchronous operations.",
                "is_correct": False
            },
            {
                "text": "It prevents component state from persisting in memory.",
                "is_correct": False
            },
            {
                "text": "It forces immediate DOM repainting.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "cybersecurity",
        "title": "SQL Injection Primary Defense",
        "question": "What is the most effective defense against SQL injection attacks?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Parameterized queries (prepared statements) ensure user input is treated as data parameters rather than executable SQL code.",
        "tags": "security,sqli,owasp",
        "answers": [
            {
                "text": "Using parameterized queries / prepared statements with database drivers or ORMs.",
                "is_correct": True
            },
            {
                "text": "Client-side regex validation on input boxes.",
                "is_correct": False
            },
            {
                "text": "Base64 encoding all user input strings.",
                "is_correct": False
            },
            {
                "text": "Enabling SSL certificates on the load balancer.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "cybersecurity",
        "title": "Symmetric vs Asymmetric Encryption",
        "question": "Which of the following is a symmetric key encryption standard?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "AES is a symmetric block cipher, while RSA and ECC are asymmetric public-key systems.",
        "tags": "security,cryptography,aes",
        "answers": [
            {
                "text": "AES (Advanced Encryption Standard)",
                "is_correct": True
            },
            {
                "text": "RSA",
                "is_correct": False
            },
            {
                "text": "Elliptic Curve Cryptography (ECC)",
                "is_correct": False
            },
            {
                "text": "Diffie-Hellman",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "cybersecurity",
        "title": "Content Security Policy (CSP)",
        "question": "How does the `Content-Security-Policy` HTTP header mitigate Cross-Site Scripting (XSS)?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "CSP restricts the origins from which scripts, styles, and other assets can be loaded and executed by the browser.",
        "tags": "security,xss,csp,headers",
        "answers": [
            {
                "text": "By restricting the allowed sources and execution domains for executable scripts and media.",
                "is_correct": True
            },
            {
                "text": "By encrypting the user's password in browser memory.",
                "is_correct": False
            },
            {
                "text": "By banning all JavaScript from running on the page.",
                "is_correct": False
            },
            {
                "text": "By converting all cookies into HTTP-only session headers.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "mathematics",
        "title": "Combinatorics Factorial",
        "question": "How many distinct permutations exist for arranging 5 books on a shelf?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "5! = 5 * 4 * 3 * 2 * 1 = 120.",
        "tags": "math,combinatorics,factorial",
        "answers": [
            {
                "text": "120",
                "is_correct": True
            },
            {
                "text": "60",
                "is_correct": False
            },
            {
                "text": "25",
                "is_correct": False
            },
            {
                "text": "720",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "mathematics",
        "title": "Matrix Multiplication Determinant",
        "question": "For square matrices A and B of identical size, what is det(A * B)?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "det(AB) = det(A) * det(B).",
        "tags": "math,linear-algebra,matrices",
        "answers": [
            {
                "text": "det(A) * det(B)",
                "is_correct": True
            },
            {
                "text": "det(A) + det(B)",
                "is_correct": False
            },
            {
                "text": "det(A) / det(B)",
                "is_correct": False
            },
            {
                "text": "det(A + B)",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "mathematics",
        "title": "Eulerian Path Condition",
        "question": "A connected graph has an Eulerian path if and only if it has how many vertices of odd degree?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "Euler proved a graph has an Eulerian path if and only if exactly 0 or 2 vertices have odd degree.",
        "tags": "math,graph-theory,euler",
        "answers": [
            {
                "text": "Exactly 0 or 2 vertices with odd degree",
                "is_correct": True
            },
            {
                "text": "All vertices must have odd degree",
                "is_correct": False
            },
            {
                "text": "Exactly 1 vertex with odd degree",
                "is_correct": False
            },
            {
                "text": "Every vertex must have even degree with prime index",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "science",
        "title": "Speed of Light in Vacuum",
        "question": "What is the approximate speed of light in a vacuum ($c$)?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "The speed of light in a vacuum is 299,792,458 m/s (approx 3 x 10^8 m/s).",
        "tags": "science,physics,constants",
        "answers": [
            {
                "text": "300,000 km/s (3 x 10^8 m/s)",
                "is_correct": True
            },
            {
                "text": "150,000 km/s (1.5 x 10^8 m/s)",
                "is_correct": False
            },
            {
                "text": "3,000,000 km/s (3 x 10^9 m/s)",
                "is_correct": False
            },
            {
                "text": "30,000 km/s (3 x 10^7 m/s)",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "science",
        "title": "Cellular Energy Production",
        "question": "Which molecule is the primary chemical energy currency generated in mitochondria?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Mitochondria produce ATP (Adenosine Triphosphate) through oxidative phosphorylation.",
        "tags": "science,biology,energy",
        "answers": [
            {
                "text": "ATP (Adenosine Triphosphate)",
                "is_correct": True
            },
            {
                "text": "DNA",
                "is_correct": False
            },
            {
                "text": "Hemoglobin",
                "is_correct": False
            },
            {
                "text": "Sucrose",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "general-knowledge",
        "title": "Apollo 11 Moon Landing Year",
        "question": "In which year did the Apollo 11 mission land humans on the Moon?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Apollo 11 landed on the Moon on July 20, 1969.",
        "tags": "trivia,history,space",
        "answers": [
            {
                "text": "1969",
                "is_correct": True
            },
            {
                "text": "1965",
                "is_correct": False
            },
            {
                "text": "1971",
                "is_correct": False
            },
            {
                "text": "1958",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "general-knowledge",
        "title": "Most Electrically Conductive Metal",
        "question": "Which chemical element is the most electrically conductive metal at standard temperature?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Silver (Ag) has the highest electrical and thermal conductivity of any known metal.",
        "tags": "trivia,science,elements",
        "answers": [
            {
                "text": "Silver (Ag)",
                "is_correct": True
            },
            {
                "text": "Copper (Cu)",
                "is_correct": False
            },
            {
                "text": "Gold (Au)",
                "is_correct": False
            },
            {
                "text": "Platinum (Pt)",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "logical-reasoning",
        "title": "Contrapositive Equivalence",
        "question": "What is the contrapositive of the statement 'If P, then Q'?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "The contrapositive of 'P -> Q' is 'not Q -> not P', which is strictly logically equivalent.",
        "tags": "logic,reasoning,deduction",
        "answers": [
            {
                "text": "If not Q, then not P",
                "is_correct": True
            },
            {
                "text": "If not P, then not Q",
                "is_correct": False
            },
            {
                "text": "If Q, then P",
                "is_correct": False
            },
            {
                "text": "P and not Q",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "logical-reasoning",
        "title": "Sequence Pattern",
        "question": "What is the next number in the pattern: 2, 6, 12, 20, 30, 42, __?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Differences are +4, +6, +8, +10, +12, so next is +14 => 42 + 14 = 56.",
        "tags": "logic,sequences,patterns",
        "answers": [
            {
                "text": "56",
                "is_correct": True
            },
            {
                "text": "54",
                "is_correct": False
            },
            {
                "text": "60",
                "is_correct": False
            },
            {
                "text": "48",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "data-analytics",
        "title": "Variance and Standard Deviation",
        "question": "What is the mathematical connection between standard deviation and variance?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Standard deviation is the square root of variance.",
        "tags": "statistics,analytics,variance",
        "answers": [
            {
                "text": "Standard deviation is the square root of variance.",
                "is_correct": True
            },
            {
                "text": "Variance is the square root of standard deviation.",
                "is_correct": False
            },
            {
                "text": "Standard deviation equals variance times sample size.",
                "is_correct": False
            },
            {
                "text": "They are unrelated measures.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "data-analytics",
        "title": "Type I Error in Statistics",
        "question": "What constitutes a Type I error in statistical hypothesis testing?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "A Type I error is rejecting a true null hypothesis (false positive).",
        "tags": "statistics,hypothesis-testing,errors",
        "answers": [
            {
                "text": "Rejecting a true null hypothesis (false positive).",
                "is_correct": True
            },
            {
                "text": "Failing to reject a false null hypothesis (false negative).",
                "is_correct": False
            },
            {
                "text": "Collecting an unrepresentative sample size.",
                "is_correct": False
            },
            {
                "text": "Using the wrong regression formula.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "ai-ml",
        "title": "Transformer Self-Attention",
        "question": "What formula calculates Scaled Dot-Product Attention in Transformers?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "Attention(Q, K, V) = softmax(Q*K^T / sqrt(d_k)) * V.",
        "tags": "ai,transformers,deep-learning",
        "answers": [
            {
                "text": "softmax((Q * K^T) / sqrt(d_k)) * V",
                "is_correct": True
            },
            {
                "text": "sigmoid(Q * K) * V^T",
                "is_correct": False
            },
            {
                "text": "ReLU(Q + K) * V",
                "is_correct": False
            },
            {
                "text": "tanh(Q * V^T) * K",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "ai-ml",
        "title": "Neural Network Dropout",
        "question": "What is the purpose of Dropout in neural networks?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Dropout randomly deactivates neurons during training to prevent co-adaptation and overfitting.",
        "tags": "ai,regularization,dropout",
        "answers": [
            {
                "text": "Randomly disabling neuron activations during training to combat overfitting.",
                "is_correct": True
            },
            {
                "text": "Increasing learning rates exponentially during backpropagation.",
                "is_correct": False
            },
            {
                "text": "Compressing weights into 8-bit integers for deployment.",
                "is_correct": False
            },
            {
                "text": "Converting continuous loss values to discrete integers.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "networking",
        "title": "TCP 3-Way Handshake",
        "question": "What is the correct order of packets for establishing a TCP handshake?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "SYN -> SYN-ACK -> ACK.",
        "tags": "networking,tcp,protocols",
        "answers": [
            {
                "text": "SYN -> SYN-ACK -> ACK",
                "is_correct": True
            },
            {
                "text": "ACK -> SYN -> FIN",
                "is_correct": False
            },
            {
                "text": "HELLO -> READY -> CONNECT",
                "is_correct": False
            },
            {
                "text": "PING -> PONG -> ACK",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "networking",
        "title": "DNS AAAA Record",
        "question": "What address type does a DNS AAAA record point to?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "AAAA records map a domain name to an IPv6 address.",
        "tags": "networking,dns,ipv6",
        "answers": [
            {
                "text": "IPv6 address",
                "is_correct": True
            },
            {
                "text": "IPv4 address",
                "is_correct": False
            },
            {
                "text": "Mail server hostname",
                "is_correct": False
            },
            {
                "text": "Canonical alias",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "algorithms",
        "title": "Binary Search Complexity",
        "question": "What is the worst-case time complexity of Binary Search on a sorted array?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "Binary search divides search space by half at each step, yielding O(log N).",
        "tags": "algorithms,binary-search,complexity",
        "answers": [
            {
                "text": "O(log N)",
                "is_correct": True
            },
            {
                "text": "O(N)",
                "is_correct": False
            },
            {
                "text": "O(1)",
                "is_correct": False
            },
            {
                "text": "O(N^2)",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "algorithms",
        "title": "Dijkstra Algorithm Constraint",
        "question": "What fundamental requirement must graph edge weights satisfy in Dijkstra's algorithm?",
        "difficulty": "HARD",
        "points": 35,
        "time_limit_seconds": 25,
        "explanation": "All edge weights must be non-negative (>= 0). If negative weights exist, Bellman-Ford must be used.",
        "tags": "algorithms,graphs,dijkstra",
        "answers": [
            {
                "text": "All edge weights must be non-negative (>= 0).",
                "is_correct": True
            },
            {
                "text": "The graph must be a Directed Acyclic Graph (DAG).",
                "is_correct": False
            },
            {
                "text": "The graph must contain no cycles.",
                "is_correct": False
            },
            {
                "text": "Edge weights must be powers of 2.",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "history",
        "title": "Magna Carta Year",
        "question": "In which year was the Magna Carta signed by King John of England?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "The Magna Carta was signed in 1215 at Runnymede.",
        "tags": "history,medieval,england",
        "answers": [
            {
                "text": "1215",
                "is_correct": True
            },
            {
                "text": "1066",
                "is_correct": False
            },
            {
                "text": "1492",
                "is_correct": False
            },
            {
                "text": "1776",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "geography",
        "title": "Longest River in the World",
        "question": "Which river is traditionally recognized as the longest in the world?",
        "difficulty": "EASY",
        "points": 10,
        "time_limit_seconds": 20,
        "explanation": "The Nile River in Africa flows approximately 6,650 km.",
        "tags": "geography,rivers,africa",
        "answers": [
            {
                "text": "Nile River",
                "is_correct": True
            },
            {
                "text": "Amazon River",
                "is_correct": False
            },
            {
                "text": "Yangtze River",
                "is_correct": False
            },
            {
                "text": "Mississippi River",
                "is_correct": False
            }
        ]
    },
    {
        "topic_slug": "geography",
        "title": "Deepest Oceanic Point",
        "question": "What is the deepest known location in Earth's oceans?",
        "difficulty": "MEDIUM",
        "points": 20,
        "time_limit_seconds": 20,
        "explanation": "Challenger Deep in the Mariana Trench descends to approximately 10,994 meters.",
        "tags": "geography,oceans,earth",
        "answers": [
            {
                "text": "Challenger Deep",
                "is_correct": True
            },
            {
                "text": "Java Trench",
                "is_correct": False
            },
            {
                "text": "Puerto Rico Trench",
                "is_correct": False
            },
            {
                "text": "Milwaukee Deep",
                "is_correct": False
            }
        ]
    }
]
