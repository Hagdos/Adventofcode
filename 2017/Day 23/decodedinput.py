set b 79
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000

    # Biggest loop; from eof
    set f 1
    set d 2
    
        # Loop 2: while d - b > 0: d += 1
        set e 2 
        
            # Smallest loop -> if b%d == 0 and b != d, f = 0
            set g d
            mul g e
            sub g b
            jnz g 2 
            set f 0
            sub e -1
            set g e
            sub g b
            jnz g -8
        
        sub d -1
        set g d
        sub g b
        jnz g -13
    
    jnz f 2
    sub h -1
    set g b
    sub g c
    jnz g 2
    jnz 1 3
    sub b -17
    jnz 1 -23
