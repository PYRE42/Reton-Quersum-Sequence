# Reton-Quersum-Sequence

This is a very fun math trick

1. pick any n.
2. calculate the quersum (sum of digits) of n.
3. concatenate n with itself (this is oyur new n).
4. repeat with the new n.

it will always loop at some point

it will always go into 1 of 3 loops:
1. 1818 (1+8+1+8 = 18 = 1818) 1818
2. 10 11 22 44 88 1616 1414 1010 22 
3. 1212 (1+2+1+2 = 6 = 66) 66 (6+6 = 12 = 1212) 1212


I used my terrible coding skills to make a basic demo for this.

unsuprisingly it all depends on mod:
1. mod 3 = 0 → loop 1
2. mod 3 = 1 → loop 2
3. mod 3 = 2 → loop 3
