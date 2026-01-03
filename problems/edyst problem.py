small_bricks=2
big_bricks=5
target=3
if target<=small_bricks:
    print ("possible")
elif target/5==big_bricks:
    print ("possible")
elif(target%5<big_bricks) and (target%5<small_bricks):
    print ("Possible")
else:
    print ("Impossible")
if(target%5<big_bricks):
    print("Possible")
elif(target%2<small_bricks):
    print("impossible")
else:
    print("impossible")
     
